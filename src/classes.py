import numpy as np
import pandas as pd

from itertools import groupby
from pymoo.core.problem import ElementwiseProblem
from pymoo.core.sampling import Sampling
from pymoo.core.mutation import Mutation
from pymoo.core.crossover import Crossover



from pymoo.algorithms.soo.nonconvex.ga import GA
from pymoo.operators.selection.tournament import TournamentSelection

from pymoo.termination import get_termination
from pymoo.optimize import minimize

class TimetablingProblem(ElementwiseProblem):
  def __init__(self, disciplinas, n_horas_dia, n_dias, professores, turno: str):
    super().__init__(n_var = len(disciplinas) * n_horas_dia * n_dias, n_obj = 1, n_constr = 7, xl = 1, xu = n_horas_dia*n_dias, vtype=int)
    self.disciplinas = disciplinas
    self.disciplinas_flat = np.array(disciplinas).flatten()
    self.n_periodos = len(disciplinas)
    self.n_dias = n_dias
    self.n_horas_dia = n_horas_dia
    self.n_horarios = n_horas_dia * n_dias
    self.professores = professores
    self.uso_lab = np.zeros((self.n_periodos, self.n_horarios))
    self.turno = turno

    for i in range(self.n_periodos):
      for j in range(self.n_horarios):
        self.uso_lab[i][j] = True if disciplinas[i][j]['lab'] else False
    self.uso_lab_flat = self.uso_lab.flatten()


  def _evaluate(self, x, out, show = False):
    if self.turno == 'manhã':
      out['F']=self.calcular_penalidade_tarde(x, self.disciplinas)+self.calcular_dias_de_aula(x) + self.calcular_dias_professores(x, show)
    else:
      out['F'] = self.calcular_dias_de_aula(x) + self.calcular_dias_professores(x, show)
    out['G'] = np.column_stack([
        self.restricao_aula_sequencia(x, self.professores, show),
        self.restricao_laboratorio(x, show),
        self.restricao_aulas_vagas(x, show),
        self.restricao_disponibilidade(x, show),
        self.restricao_aulas_seguidas(x, show=show),
        self.restricao_compartilhada(x, show=show),
        self.restricao_prof_conflito(x, show=show)
        ])

  def iter_disciplinas(self, x):
    disciplinas = self.disciplinas_flat
    for i in range(len(x)):
      if len(disciplinas[i]["professores"]) >= 1:
        professor = self.professores[disciplinas[i]["professores"][0]]
      yield i, x[i], disciplinas[i], professor

  # Restrições flexíveis
  def calcular_dias_professores(self, x, show):
    penalidade = 0
    prof_dict = {}
    for i in range(0, len(self.professores)):
      prof_dict[i] = []
    for i, horario, disciplina, professor in self.iter_disciplinas(x):
      if disciplina["disciplina"] == "Aula Vaga" or len(disciplina["professores"]) == 0:
        continue
      id_prof = disciplina["professores"][0]
      dia_aula = (int(horario-1))//self.n_horas_dia
      if dia_aula not in prof_dict[id_prof]:
        prof_dict[id_prof].append(dia_aula)
    for prof, dias in prof_dict.items():
      if len(dias)>3:
        penalidade+=1



    return penalidade
  def calcular_penalidade_tarde(self, x, disciplinas):
    penalidade = 0
    disciplinas = np.array(disciplinas).flatten()
    for i, horario, disciplina, professor in self.iter_disciplinas(x):
      if disciplina["disciplina"] != "Aula Vaga":
        if (horario % 5 == 0) or ((horario + 1) % 5) == 0:
          penalidade += disciplina["penalidade_tarde"]
    return penalidade

  def calcular_dias_de_aula(self, x): # Somado ou subtraído, depende do curso
    dias_de_aula = 0
    valor_esperado = self.n_dias*self.n_periodos
    horarios = x.reshape(self.n_periodos, self.n_horarios)
    for i in range(self.n_periodos):
      dias_disponiveis = ['seg','ter',
'qua',
'qui',
'sex']
      for horario, aulas in zip(horarios[i], self.disciplinas[i]):
        if aulas['disciplina'] != 'Aula Vaga':
          if horario <= self.n_horas_dia and 'seg' in dias_disponiveis:
            dias_disponiveis.remove('seg')
            dias_de_aula += 1
          elif horario <= self.n_horas_dia*2 and 'ter' in dias_disponiveis:
            dias_disponiveis.remove('ter')
            dias_de_aula += 1
          elif horario <= self.n_horas_dia*3 and 'qua' in dias_disponiveis:
            dias_disponiveis.remove('qua')
            dias_de_aula += 1
          elif horario <= self.n_horas_dia*4 and 'qui' in dias_disponiveis:
            dias_disponiveis.remove('qui')
            dias_de_aula += 1
          elif horario <= self.n_horas_dia*5 and 'sex' in dias_disponiveis:
            dias_disponiveis.remove('sex')
            dias_de_aula += 1
    return valor_esperado - dias_de_aula

    # Restrições rígidas

  def restricao_aula_sequencia(self, x, professores, show):

    penalidade = 0
    dias_aula = []
    for i in range(len(professores)):
      dias_aula.append([0]*self.n_dias)
    for i, horario, disciplina, professor in self.iter_disciplinas(x):
      if disciplina['disciplina'] == 'Aula Vaga' or len(disciplina['professores']) == 0:
        continue
      id_professor = disciplina['professores'][0]
      dias_aula[id_professor][int((horario)-1)//self.n_horas_dia] = 1
    for i in range(len(dias_aula)):
      lista = dias_aula[i]
      grupos = [chave for chave, grupo in groupby(lista)]

      if grupos.count(1) > 1 and professores[i]['seq']:
        penalidade += 1
        if show:
          print(f"Restrição de aulas em dias seguidos")


    return penalidade
  def restricao_laboratorio(self, x, show):
    uso_lab = 0
    penalidade = 0
    for i in range(1, self.n_horarios+1):
      uso_lab = 0
      idxs = np.where(x == i)[0]
      for j in idxs:
        if np.array(self.disciplinas).flatten()[j]["lab"]:
          uso_lab +=1
      if uso_lab>3:
        penalidade+=1
        if show:
          print("Restrição de uso de laboratórios")
    return penalidade
  def restricao_aulas_vagas(self, x, show):
    penalidade = 0
    dias_aula = np.zeros((self.n_periodos, self.n_dias, self.n_horas_dia))

    for i, horario, disciplina, professor in self.iter_disciplinas(x):
      if disciplina['disciplina'] == "Aula Vaga":
        continue
      dias_aula[int(i//self.n_horarios)][int((horario-1)//self.n_horas_dia)][int((horario-1)%self.n_horas_dia)] = 1
    for semana_periodo in dias_aula:
      for dias in semana_periodo:
        grupos = [chave for chave, grupo in groupby(dias)]
        if grupos.count(1) > 1:
          penalidade += 1
          if show:
            print("Restrição de aulas vagas entre aulas")

    return penalidade
  def restricao_compartilhada(self, x, show): # Reestruturar
    restricao_compartilhada = 0
    for i, horario, disciplina, professor in self.iter_disciplinas(x):
      if i < len(x)//2 and disciplina['compartilhada']: #(alterar o i<100 pra um valor variável)
        periodo = next(iter(disciplina['compartilhada']))
        posicao = disciplina['compartilhada'][periodo]
        if x[self.n_horarios*periodo+posicao] != horario:
          if show:
            print(f'Restrição compartilhada, disciplina: {disciplina}, horario: {horario}')
          restricao_compartilhada += 1
    return restricao_compartilhada

  def restricao_aulas_seguidas(self, x, show):
    def verificar_sequencia(h1, h2):
      if (h1-1)//self.n_horas_dia == (h2-1)//self.n_horas_dia:
        if self.turno == 'noite':
          return True
        if (h1%self.n_horas_dia != 3):
          return True
        # if turno == 'noite' or (h1%self.n_horas_dia != 3): True
      return False
    penalidade = 0
    horarios = x.reshape(self.n_periodos, self.n_horarios)
    disciplinas = self.disciplinas

    for i in range(self.n_periodos):
      validadas_60 = set()
      validadas_90 = {}
      sorted_periodo = sorted(zip(horarios[i], disciplinas[i]), key=lambda x: x[0])

      for j in range(self.n_horarios):
        if j < self.n_horarios-1:
          h1, d1 = sorted_periodo[j]
          h2, d2 = sorted_periodo[j+1]

          if verificar_sequencia(h1, h2) and d1['carga'] == 60:
            if d1['disciplina'] not in validadas_60:
              validadas_60.add(d1['disciplina'])
              if d1['disciplina'] != d2['disciplina']:
                penalidade += 1
                if show:
                  print(f'penalidade de sequência (60) nos horários {h1} e {h2} do período {i}, disciplinas: {d1["disciplina"]} e {d2["disciplina"]}')
          elif verificar_sequencia(h1, h2) and d1['carga'] == 90:
            if d1['disciplina'] not in validadas_90:
              validadas_90[d1['disciplina']] = 0
            if d1['disciplina'] != d2['disciplina']:
              validadas_90[d1['disciplina']] += 1
            if validadas_90[d1['disciplina']] > 2:
              penalidade += 1
          elif not verificar_sequencia(h1, h2):
            if d1['carga'] == 60 and d1['disciplina'] not in validadas_60:
              penalidade += 1
            elif d1['carga'] == 90:
              if d1['disciplina'] not in validadas_90:
                validadas_90[d1['disciplina']] = 0
              validadas_90[d1['disciplina']] += 1
              if validadas_90[d1['disciplina']] > 2:
                penalidade += 1
    return penalidade

  def restricao_disponibilidade(self, x, show):
    restricao_disponibilidade = 0
    for i, horario, disciplina, professor in self.iter_disciplinas(x):
        if disciplina['disciplina'] == 'Aula Vaga':
            continue
        for id in disciplina['professores']:
          if horario not in self.professores[id]['disponibilidade']:
            restricao_disponibilidade += 1
            if show:
              print(f"Professor {self.professores[id]['nome']} não está disponível no horário {horario}")
    return restricao_disponibilidade
  def restricao_prof_conflito(self, x, show):
    restricao_prof_conflito = 0
    profs_por_horario = {}
    for i, horario, disciplina, professor in self.iter_disciplinas(x):
        if disciplina['disciplina'] == 'Aula Vaga':
            continue
        for id in disciplina['professores']:
          if horario not in profs_por_horario:
            profs_por_horario[horario] = {}
          if id not in profs_por_horario[horario]:
            profs_por_horario[horario][id] = []
            if not disciplina['compartilhada']:
              profs_por_horario[horario][id].append(i)
          else:
            profs_por_horario[horario][id].append(i)

  # após percorrer, verificar conflitos de professor
    for horario, profs in profs_por_horario.items():
      for prof, disciplinas in profs.items():
        if len(disciplinas) > 1:
          restricao_prof_conflito += 1
          if show:
            print(f"Conflito de professor no horário {horario}: {prof} : {disciplinas}")
    return restricao_prof_conflito
  def restricao_aula_isolada(self, x, show = False):
    restricao_aula_isolada = 0
    semana = []
    for i in range(self.n_periodos):
      semana.append({'seg':[], 'ter':[], 'qua':[], 'qui':[], 'sex':[]})
    for i, horario, disciplina, professor in self.iter_disciplinas(x):
      if disciplina['disciplina'] == 'Aula Vaga':
        continue
      if horario <= self.n_horas_dia:
        semana[i//self.n_horarios]['seg'].append(disciplina)
      elif horario <= self.n_horas_dia*2:
        semana[i//self.n_horarios]['ter'].append(disciplina)
      elif horario <= self.n_horas_dia*3:
        semana[i//self.n_horarios]['qua'].append(disciplina)
      elif horario <= self.n_horas_dia*4:
        semana[i//self.n_horarios]['qui'].append(disciplina)
      elif horario <= self.n_horas_dia*5:
        semana[i//self.n_horarios]['sex'].append(disciplina)
    for i in range(len(semana)):
      for dia in semana[i]:
        if len(semana[i][dia]) == 1 and semana[i][dia][0]['carga'] == 30:
          restricao_aula_isolada += 1
          if show:
            print(f"Restrição de aula isolada no dia {dia}")

    return restricao_aula_isolada

"""### Criando um crossover personalizado"""

class MatrixPointCrossover(Crossover):
  def __init__(self, **kwargs):
    super().__init__(n_parents = 2, n_offsprings = 2, **kwargs)
  def _do(self, problem, X, **kwargs):

    n_parents, n_matings, n_var = X.shape
    child = np.zeros((self.n_offsprings, n_matings, problem.n_var))
    point = np.random.randint(1, problem.n_periodos-1)



    for i in range(n_matings):

      compartilhadas = {}
      for j in range(problem.n_periodos):
        compartilhadas[j] = []

      p1, p2 = X[0, i].reshape(problem.n_periodos, problem.n_horarios), X[1, i].reshape(problem.n_periodos, problem.n_horarios)

      new_child_1, new_child_2 = np.zeros_like(p1), np.zeros_like(p1)
      new_child_1[:point] = p1[:point]
      new_child_1[point:] = p2[point:]
      new_child_2[:point] = p2[:point]
      new_child_2[point:] = p1[point:]

      for j in range(len(new_child_1) // 2):
          for k in range(len(new_child_1[j])):
              disciplina = problem.disciplinas[j][k]
              if disciplina['compartilhada']:
                  periodo = next(iter(disciplina['compartilhada']))
                  posicao = disciplina['compartilhada'][periodo]
                  val = new_child_1[j][k]            # valor a ser replicado
                  while val in compartilhadas[periodo]:
                    new_pos = np.random.randint(0, problem.n_horarios)
                    if problem.disciplinas[j][new_pos]['compartilhada'] or problem.disciplinas[periodo][new_pos]['compartilhada']:
                      continue
                    new_child_1[j][k], new_child_1[j][new_pos] = new_child_1[j][new_pos], new_child_1[j][k]
                    val = new_child_1[j][k]
                  pos_val = np.where(new_child_1[periodo] == val)[0]  # onde já existe esse valor
                  if pos_val.size > 0:  # se já existe, faz swap
                      pos_val = pos_val[0]
                      new_child_1[periodo][posicao], new_child_1[periodo][pos_val] = (
                          new_child_1[periodo][pos_val],
                          new_child_1[periodo][posicao],
                      )
                  else:
                      # se não existe, apenas coloca (fallback, raro)
                      new_child_1[periodo][posicao] = val
                  compartilhadas[j].append(val)
                  compartilhadas[periodo].append(val)

      for j in range(len(new_child_2) // 2):
          for k in range(len(new_child_2[j])):
              disciplina = problem.disciplinas[j][k]
              if disciplina['compartilhada']:
                  periodo = next(iter(disciplina['compartilhada']))
                  posicao = disciplina['compartilhada'][periodo]
                  val = new_child_2[j][k]
                  while val in compartilhadas[periodo]:
                    new_pos = np.random.randint(0, problem.n_horarios)
                    if problem.disciplinas[j][new_pos]['compartilhada'] or problem.disciplinas[periodo][new_pos]['compartilhada']:
                      continue
                    new_child_2[j][k], new_child_2[j][new_pos] = new_child_2[j][new_pos], new_child_2[j][k]
                    val = new_child_2[j][k]
                  pos_val = np.where(new_child_2[periodo] == val)[0]
                  if pos_val.size > 0:
                      pos_val = pos_val[0]
                      new_child_2[periodo][posicao], new_child_2[periodo][pos_val] = (
                          new_child_2[periodo][pos_val],
                          new_child_2[periodo][posicao],
                      )
                  else:
                      new_child_2[periodo][posicao] = val
                  compartilhadas[j].append(val)
                  compartilhadas[periodo].append(val)



      child[0, i, :] = new_child_1.flatten()
      child[1, i, :] = new_child_2.flatten()

    return child

"""### Criando um "Sampling" personalizado"""

class MatrixPermutationSampling(Sampling):
  def _do(self, problem, n_samples, **kwargs):
    samples = []

    for _ in range(n_samples):

      matriz = np.zeros((problem.n_periodos, problem.n_horarios))

      for i in range(problem.n_periodos//2):
        valores_validos = [v for v in range(1, problem.n_horarios+1)]
        for j in range(problem.n_horarios):
          horario = np.random.choice(valores_validos)
          disciplina = problem.disciplinas[i][j]
          if disciplina['compartilhada']:
            periodo = next(iter(disciplina['compartilhada']))
            posicao = disciplina['compartilhada'][periodo]
            while horario in matriz[periodo]:
              horario = np.random.choice(valores_validos)
        #if x[self.n_horarios*periodo+posicao] != horario:
            matriz[periodo][posicao] = horario
          matriz[i][j] = horario
          valores_validos.remove(horario)

      for i in range(problem.n_periodos//2, problem.n_periodos):
        valores_validos = [v for v in range(1, problem.n_horarios+1) if v not in matriz[i]]
        for j in range(problem.n_horarios):
          if matriz[i][j] == 0:
            horario = np.random.choice(valores_validos)
            valores_validos.remove(horario)
            matriz[i][j] = horario
      samples.append(np.array(matriz).flatten())
    return np.array(samples)

"""### Criando uma mutação personalizada"""

class SwapMutation(Mutation):
  def _do(self, problem, X, **kwargs):
    for i in range(len(X)):
      matrix = X[i].reshape(problem.n_periodos, problem.n_horarios)
      periodo = np.random.randint(0, problem.n_periodos)
      sorteio_2 = True
      while True:
        if sorteio_2:
          index1, index2 = np.random.randint(0, problem.n_horarios, size = 2)

        sorteio_2 = True

        if index1 == index2:
          continue

        disciplina1, disciplina2 = problem.disciplinas[periodo][index1], problem.disciplinas[periodo][index2]
        if disciplina1['compartilhada'] and disciplina2['compartilhada']:
          periodo_compartilhado_1 = next(iter(disciplina1['compartilhada']))
          periodo_compartilhado_2 = next(iter(disciplina2['compartilhada']))
          if periodo_compartilhado_1 != periodo_compartilhado_2:
            continue
        if disciplina1['compartilhada']:
          periodo_compartilhado_1 = next(iter(disciplina1['compartilhada']))
          posicao_compartilhada = disciplina1['compartilhada'][periodo_compartilhado_1]
          horario_troca = np.where(matrix[periodo_compartilhado_1] == matrix[periodo][index2])[0][0]
          if problem.disciplinas[periodo_compartilhado_1][horario_troca]['compartilhada']:
            index1 = np.random.randint(0, problem.n_horarios)
            sorteio_2 = False
            continue
        if disciplina2['compartilhada']:
          periodo_compartilhado_2 = next(iter(disciplina2['compartilhada']))
          posicao_compartilhada = disciplina2['compartilhada'][periodo_compartilhado_2]
          horario_troca = np.where(matrix[periodo_compartilhado_2] == matrix[periodo][index1])[0][0]
          if problem.disciplinas[periodo_compartilhado_2][horario_troca]['compartilhada']:
            index2 = np.random.randint(0, problem.n_horarios)
            sorteio_2 = False
            continue
        break

      matrix[periodo][index1], matrix[periodo][index2] = matrix[periodo][index2], matrix[periodo][index1]

      disciplina1, disciplina2 = problem.disciplinas[periodo][index1], problem.disciplinas[periodo][index2]

      if disciplina1['compartilhada']:
        periodo_compartilhado_1 = next(iter(disciplina1['compartilhada']))
        posicao_compartilhada = disciplina1['compartilhada'][periodo_compartilhado_1]
        horario_troca = np.where(matrix[periodo_compartilhado_1] == matrix[periodo][index1])[0][0]

        matrix[periodo_compartilhado_1][posicao_compartilhada], matrix[periodo_compartilhado_1][horario_troca] = matrix[periodo_compartilhado_1][horario_troca], matrix[periodo_compartilhado_1][posicao_compartilhada]

      if disciplina2['compartilhada']:
        periodo_compartilhado_2 = next(iter(disciplina2['compartilhada']))
        posicao_compartilhada = disciplina2['compartilhada'][periodo_compartilhado_2]
        horario_troca = np.where(matrix[periodo_compartilhado_2] == matrix[periodo][index2])[0][0]

        matrix[periodo_compartilhado_2][posicao_compartilhada], matrix[periodo_compartilhado_2][horario_troca] = matrix[periodo_compartilhado_2][horario_troca], matrix[periodo_compartilhado_2][posicao_compartilhada]

      X[i] = matrix.flatten()
    return X