def gerar_cenario_semestre_1():
  
  n_horas_dia = 5
  n_dias = 5
  n_horarios = n_horas_dia*n_dias
  n_turmas_curso = 4
  turno = 'manhã'

  matriz_disciplinas = [
  [   {'disciplina': 'COMPUTAÇÃO, ÉTICA E SOCIEDADE', 'carga': 30, 'partes': False, 'penalidade_tarde':3, 'professores' : [3], 'compartilhada': {4:0}, 'lab':False},
      {'disciplina': 'EMPREENDEDORISMO E INOVAÇÃO', 'carga': 60, 'partes': True, 'penalidade_tarde':5, 'professores' : [10], 'compartilhada': {4:1}, 'lab': False},
      {'disciplina': 'EMPREENDEDORISMO E INOVAÇÃO', 'carga': 60, 'partes': True, 'penalidade_tarde':5, 'professores' : [10], 'compartilhada': {4:2}, 'lab': False},
      {'disciplina': 'AÇÃO CURRICULAR DE EXTENSÃO I', 'carga': 30, 'partes': False, 'penalidade_tarde':1, 'professores' : [2], 'compartilhada': False, 'lab':False},
      {'disciplina': 'INTRODUÇÃO A COMPUTAÇÃO', 'carga': 60, 'partes': True, 'penalidade_tarde':5, 'professores' : [2], 'compartilhada': False, 'lab':False},
      {'disciplina': 'INTRODUÇÃO A COMPUTAÇÃO', 'carga': 60, 'partes': True, 'penalidade_tarde':5, 'professores' : [2], 'compartilhada': False, 'lab':False},
      {'disciplina': 'PROGRAMAÇÃO I', 'carga': 90, 'partes': True, 'penalidade_tarde':10, 'professores' : [1], 'compartilhada': False, 'lab':True},
      {'disciplina': 'PROGRAMAÇÃO I', 'carga': 90, 'partes': True, 'penalidade_tarde':10, 'professores' : [1], 'compartilhada': False, 'lab':True},
      {'disciplina': 'PROGRAMAÇÃO I', 'carga': 90, 'partes': True, 'penalidade_tarde':10, 'professores' : [1], 'compartilhada': False, 'lab':True},
      {'disciplina': 'MATEMÁTICA ELEMENTAR', 'carga': 60, 'partes': True,'penalidade_tarde':5, 'professores' : [19], 'compartilhada': False, 'lab':False},
      {'disciplina': 'MATEMÁTICA ELEMENTAR', 'carga': 60, 'partes': True, 'penalidade_tarde':5, 'professores' : [19], 'compartilhada': False, 'lab':False},
      {'disciplina': 'FUNDAMENTOS FILOSÓFICOS DA EDUCAÇÃO', 'carga': 60, 'partes': True,'penalidade_tarde':3, 'professores' : [23], 'compartilhada': False, 'lab':False},
      {'disciplina': 'FUNDAMENTOS FILOSÓFICOS DA EDUCAÇÃO', 'carga': 60, 'partes': True, 'penalidade_tarde':3, 'professores' : [23], 'compartilhada': False, 'lab':False},
      {'disciplina': 'LÍNGUA PORTUGUESA NA PRODUÇÃO DO CONHECIMENTO', 'carga': 60, 'partes': True,'penalidade_tarde':2, 'professores' : [], 'compartilhada': False, 'lab':False},
      {'disciplina': 'LÍNGUA PORTUGUESA NA PRODUÇÃO DO CONHECIMENTO', 'carga': 60, 'partes': True, 'penalidade_tarde':2, 'professores' : [], 'compartilhada': False, 'lab':False},
  ],
  [   {'disciplina': 'BANCO DE DADOS', 'carga': 60, 'partes': True, 'penalidade_tarde':1, 'professores' : [11], 'compartilhada': {5:0}, 'lab':True},
      {'disciplina': 'BANCO DE DADOS', 'carga': 60, 'partes': True, 'penalidade_tarde':1, 'professores' : [11], 'compartilhada': {5:1}, 'lab':True},
      {'disciplina': 'ALGORITMOS E ESTRUTURAS DE DADOS', 'carga': 60, 'partes': True, 'penalidade_tarde':5, 'professores' : [7], 'compartilhada': False, 'lab':True},
      {'disciplina': 'ALGORITMOS E ESTRUTURAS DE DADOS', 'carga': 60, 'partes': True, 'penalidade_tarde':5, 'professores' : [7], 'compartilhada': False, 'lab':True},
      {'disciplina': 'ENSINO DE COMPUTAÇÃO II', 'carga': 60, 'partes': True, 'penalidade_tarde':5, 'professores' : [15], 'compartilhada': False, 'lab':False},
      {'disciplina': 'ENSINO DE COMPUTAÇÃO II', 'carga': 60, 'partes': True, 'penalidade_tarde':5, 'professores' : [15], 'compartilhada': False, 'lab':False},
      {'disciplina': 'CÁLCULO II', 'carga': 60, 'partes': True, 'penalidade_tarde':10, 'professores' : [19], 'compartilhada': False, 'lab':False},
      {'disciplina': 'CÁLCULO II', 'carga': 60, 'partes': True, 'penalidade_tarde':10, 'professores' : [19], 'compartilhada': False, 'lab':False},
      {'disciplina': 'AÇÃO CURRICULAR DE EXTENSÃO III', 'carga': 30, 'partes': False, 'penalidade_tarde':5, 'professores' : [16], 'compartilhada': False, 'lab':False},
      {'disciplina': 'ORGANIZAÇÃO DA EDUCAÇÃO NACIONAL', 'carga': 60, 'partes': True, 'penalidade_tarde':10, 'professores' : [24], 'compartilhada': False, 'lab':False},
      {'disciplina': 'ORGANIZAÇÃO DA EDUCAÇÃO NACIONAL', 'carga': 60, 'partes': True,'penalidade_tarde':10, 'professores' : [24], 'compartilhada': False, 'lab':False},
      {'disciplina': 'ÁLGEBRA LINEAR E GEOMETRIA ANALÍTICA', 'carga': 60, 'partes': True, 'penalidade_tarde':5, 'professores' : [25], 'compartilhada': False, 'lab':False},
      {'disciplina': 'ÁLGEBRA LINEAR E GEOMETRIA ANALÍTICA', 'carga': 60, 'partes': True,'penalidade_tarde':5, 'professores' : [25], 'compartilhada': False, 'lab':False},
  ],
  [
      {'disciplina': 'REDES DE COMPUTADORES', 'carga': 60, 'partes': True, 'penalidade_tarde':3, 'professores' : [4], 'compartilhada': {6:0}, 'lab':True},
      {'disciplina': 'REDES DE COMPUTADORES', 'carga': 60, 'partes': True, 'penalidade_tarde':3, 'professores' : [4], 'compartilhada': {6:1}, 'lab':True},
      {'disciplina': 'PARADIGMAS DE LINGUAGENS DE PROGRAMAÇÃO', 'carga': 60, 'partes': True, 'penalidade_tarde':5, 'professores' : [18], 'compartilhada': {6:2}, 'lab':True},
      {'disciplina': 'PARADIGMAS DE LINGUAGENS DE PROGRAMAÇÃO', 'carga': 60, 'partes': True, 'penalidade_tarde':5, 'professores' : [18], 'compartilhada': {6:3}, 'lab':True},
      {'disciplina': 'ENSINO DE COMPUTAÇÃO IV', 'carga': 60, 'partes': True, 'penalidade_tarde':5, 'professores' : [22], 'compartilhada': False, 'lab':False},
      {'disciplina': 'ENSINO DE COMPUTAÇÃO IV', 'carga': 60, 'partes': True, 'penalidade_tarde':5, 'professores' : [22], 'compartilhada': False, 'lab':False},
      {'disciplina': 'FUNDAMENTOS PSICOLÓGICOS DA EDUCAÇÃO', 'carga': 60, 'partes': True, 'penalidade_tarde':10, 'professores' : [26], 'compartilhada': False, 'lab':False},
      {'disciplina': 'FUNDAMENTOS PSICOLÓGICOS DA EDUCAÇÃO', 'carga': 60, 'partes': True, 'penalidade_tarde':10, 'professores' : [26], 'compartilhada': False, 'lab':False},
      {'disciplina': 'EDUCAÇÃO À DISTÂNCIA', 'carga': 60, 'partes': True, 'penalidade_tarde':5, 'professores' : [27], 'compartilhada': False, 'lab':False},
      {'disciplina': 'EDUCAÇÃO À DISTÂNCIA', 'carga': 60, 'partes': True,'penalidade_tarde':5, 'professores' : [27], 'compartilhada': False, 'lab':False},
      {'disciplina': 'AÇÃO CURRICULAR DE EXTENSÃO V', 'carga': 30, 'partes': False, 'penalidade_tarde':1, 'professores' : [15], 'compartilhada': False, 'lab':False},
      {'disciplina': 'ESTÁGIO SUPERVISIONADO I', 'carga': 30, 'partes': False,'penalidade_tarde':1, 'professores' : [22], 'compartilhada': False, 'lab':False},
      {'disciplina': 'EDUCAÇÃO INCLUSIVA', 'carga': 30, 'partes': False, 'penalidade_tarde':3, 'professores' : [28], 'compartilhada': False, 'lab':False},
  ],
  [
      {'disciplina': 'SEMINÁRIO DE COMPUTAÇÃO I', 'carga': 30, 'partes': False, 'penalidade_tarde':3, 'professores' : [17], 'compartilhada': {7:0}, 'lab':False},
      {'disciplina': 'SEMINÁRIO DE COMPUTAÇÃO II', 'carga': 30, 'partes': False, 'penalidade_tarde':3, 'professores' : [17], 'compartilhada': {7:1}, 'lab':False},
      {'disciplina': 'TÓPICOS AVANÇADOS EM ESW E SISTEMAS', 'carga': 60, 'partes': True, 'penalidade_tarde':5, 'professores' : [7], 'compartilhada': {7:2}, 'lab':True},
      {'disciplina': 'TÓPICOS AVANÇADOS EM ESW E SISTEMAS', 'carga': 60, 'partes': True, 'penalidade_tarde':5, 'professores' : [7], 'compartilhada': {7:3}, 'lab':True},
      {'disciplina': 'ENGENHARIA DE SOFTWARE EDUCATIVO', 'carga': 30, 'partes': False, 'penalidade_tarde':5, 'professores' : [2], 'compartilhada': {7:4}, 'lab':True},
      {'disciplina': 'AÇÃO CURRICULAR DE EXTENSÃO VII', 'carga': 30, 'partes': False, 'penalidade_tarde':1, 'professores' : [22], 'compartilhada': False, 'lab':False},
      {'disciplina': 'ESTÁGIO SUPERVISIONADO III', 'carga': 30, 'partes': False, 'penalidade_tarde':3, 'professores' : [2], 'compartilhada': False, 'lab':False},
      {'disciplina': 'PLANEJAMENTO E GERENCIAMENTO DE PROJETOS', 'carga': 30, 'partes': False, 'penalidade_tarde':3, 'professores' : [1], 'compartilhada': {6:4}, 'lab':False},
      {'disciplina': 'ENSINO DE COMPUTAÇÃO VI', 'carga': 60, 'partes': True, 'penalidade_tarde':5, 'professores' : [15], 'compartilhada': False, 'lab':False},
      {'disciplina': 'ENSINO DE COMPUTAÇÃO VI', 'carga': 60, 'partes': True, 'penalidade_tarde':5, 'professores' : [15], 'compartilhada': False, 'lab':False},
      {'disciplina': 'TECNOLOGIA E EDUCAÇÃO', 'carga': 60, 'partes': True, 'penalidade_tarde':5, 'professores' : [28], 'compartilhada': False, 'lab':False},
      {'disciplina': 'TECNOLOGIA E EDUCAÇÃO', 'carga': 60, 'partes': True,'penalidade_tarde':5, 'professores' : [28], 'compartilhada': False, 'lab':False},

  ],
  [   #1ES
      {'disciplina': 'COMPUTAÇÃO, ÉTICA E SOCIEDADE', 'carga': 30, 'partes': False, 'penalidade_tarde':3, 'professores' : [3], 'compartilhada': {0:0}, 'lab':False},
      {'disciplina': 'EMPREENDEDORISMO E INOVAÇÃO', 'carga': 60, 'partes': True, 'penalidade_tarde':5, 'professores' : [10], 'compartilhada': {0:1}, 'lab':False},
      {'disciplina': 'EMPREENDEDORISMO E INOVAÇÃO', 'carga': 60, 'partes': True, 'penalidade_tarde':5, 'professores' : [10], 'compartilhada': {0:2}, 'lab':False},
      {'disciplina': 'DCExt I', 'carga': 45, 'partes': False, 'penalidade_tarde':1, 'professores' : [3], 'compartilhada': False, 'lab':False},
      {'disciplina': 'INTRODUÇÃO A COMPUTAÇÃO', 'carga': 60, 'partes': True, 'penalidade_tarde':5, 'professores' : [3], 'compartilhada': False, 'lab':False},
      {'disciplina': 'INTRODUÇÃO A COMPUTAÇÃO', 'carga': 60, 'partes': True, 'penalidade_tarde':5, 'professores' : [3], 'compartilhada': False, 'lab':False},
      {'disciplina': 'PROGRAMAÇÃO I', 'carga': 90, 'partes': True, 'penalidade_tarde':10, 'professores' : [0], 'compartilhada': False, 'lab':True},
      {'disciplina': 'PROGRAMAÇÃO I', 'carga': 90, 'partes': True, 'penalidade_tarde':10, 'professores' : [0], 'compartilhada': False, 'lab':True},
      {'disciplina': 'PROGRAMAÇÃO I', 'carga': 90, 'partes': True, 'penalidade_tarde':10, 'professores' : [0], 'compartilhada': False, 'lab':True},
      {'disciplina': 'CALCULO I', 'carga': 60, 'partes': True,'penalidade_tarde':5, 'professores' : [13], 'compartilhada': False, 'lab':False},
      {'disciplina': 'CALCULO I', 'carga': 60, 'partes': True, 'penalidade_tarde':5, 'professores' : [13], 'compartilhada': False, 'lab':False},
      {'disciplina': 'GEOMETRIA ANALITICA', 'carga': 60, 'partes': True,'penalidade_tarde':3, 'professores' : [21], 'compartilhada': False, 'lab':False},
      {'disciplina': 'GEOMETRIA ANALITICA', 'carga': 60, 'partes': True, 'penalidade_tarde':3, 'professores' : [21], 'compartilhada': False, 'lab':False},
  ],
  [   #3ES
      {'disciplina': 'BANCO DE DADOS', 'carga': 60, 'partes': True, 'penalidade_tarde':1, 'professores' : [11], 'compartilhada': {1:0}, 'lab':True},
      {'disciplina': 'BANCO DE DADOS', 'carga': 60, 'partes': True, 'penalidade_tarde':1, 'professores' : [11], 'compartilhada': {1:1}, 'lab':True},
      {'disciplina': 'ALGORITMOS E ESTRUTURAS DE DADOS', 'carga': 60, 'partes': True, 'penalidade_tarde':5, 'professores' : [6], 'compartilhada': False, 'lab':True},
      {'disciplina': 'ALGORITMOS E ESTRUTURAS DE DADOS', 'carga': 60, 'partes': True, 'penalidade_tarde':5, 'professores' : [6], 'compartilhada': False, 'lab':True},
      {'disciplina': 'PROGRAMAÇÃO III', 'carga': 60, 'partes': True, 'penalidade_tarde':5, 'professores' : [6], 'compartilhada': False, 'lab':True},
      {'disciplina': 'PROGRAMAÇÃO III', 'carga': 60, 'partes': True, 'penalidade_tarde':5, 'professores' : [6], 'compartilhada': False, 'lab':True},
      {'disciplina': 'ENGENHARIA DE REQUISITOS', 'carga': 60, 'partes': True, 'penalidade_tarde':10, 'professores' : [20], 'compartilhada': False, 'lab':True},
      {'disciplina': 'ENGENHARIA DE REQUISITOS', 'carga': 60, 'partes': True, 'penalidade_tarde':10, 'professores' : [20], 'compartilhada': False, 'lab':True},
      {'disciplina': 'DCEXT III', 'carga': 30, 'partes': False, 'penalidade_tarde':5, 'professores' : [16], 'compartilhada': False, 'lab':False},
      {'disciplina': 'PROJETO DE SOFTWARE', 'carga': 60, 'partes': True, 'penalidade_tarde':10, 'professores' : [7], 'compartilhada': False, 'lab':True},
      {'disciplina': 'PROJETO DE SOFTWARE', 'carga': 60, 'partes': True,'penalidade_tarde':10, 'professores' : [7], 'compartilhada': False, 'lab':True},
      {'disciplina': 'ESTATÍSTICA I', 'carga': 60, 'partes': True, 'penalidade_tarde':5, 'professores' : [12], 'compartilhada': False, 'lab':False},
      {'disciplina': 'ESTATÍSTICA I', 'carga': 60, 'partes': True,'penalidade_tarde':5, 'professores' : [12], 'compartilhada': False, 'lab':False},
  ],
  [   #5ES
      {'disciplina': 'REDES DE COMPUTADORES', 'carga': 60, 'partes': True, 'penalidade_tarde':3, 'professores' : [4], 'compartilhada': {2:0}, 'lab':True},
      {'disciplina': 'REDES DE COMPUTADORES', 'carga': 60, 'partes': True, 'penalidade_tarde':3, 'professores' : [4], 'compartilhada': {2:1}, 'lab':True},
      {'disciplina': 'PARADIGMAS DE LINGUAGENS DE PROGRAMAÇÃO', 'carga': 60, 'partes': True, 'penalidade_tarde':5, 'professores' : [18], 'compartilhada': {2:2}, 'lab':True},
      {'disciplina': 'PARADIGMAS DE LINGUAGENS DE PROGRAMAÇÃO', 'carga': 60, 'partes': True, 'penalidade_tarde':5, 'professores' : [18], 'compartilhada': {2:3}, 'lab':True},
      {'disciplina': 'GERÊNCIA DE PROJETOS', 'carga': 60, 'partes': True, 'penalidade_tarde':5, 'professores' : [1], 'compartilhada': {3:7}, 'lab':False}, #{3:7}
      {'disciplina': 'GERÊNCIA DE PROJETOS', 'carga': 60, 'partes': True, 'penalidade_tarde':5, 'professores' : [1], 'compartilhada': False, 'lab':False},
      {'disciplina': 'VERIFICAÇÃO E VALIDAÇÃO DE SISTEMAS', 'carga': 60, 'partes': True, 'penalidade_tarde':10, 'professores' : [10], 'compartilhada': False, 'lab':True},
      {'disciplina': 'VERIFICAÇÃO E VALIDAÇÃO DE SISTEMAS', 'carga': 60, 'partes': True, 'penalidade_tarde':10, 'professores' : [10], 'compartilhada': False, 'lab':True},
      {'disciplina': 'PROJETO I', 'carga': 60, 'partes': True, 'penalidade_tarde':5, 'professores' : [18], 'compartilhada': False, 'lab':True},
      {'disciplina': 'PROJETO I', 'carga': 60, 'partes': True,'penalidade_tarde':5, 'professores' : [18], 'compartilhada': False, 'lab':True},
      {'disciplina': 'DCExt V', 'carga': 30, 'partes': False, 'penalidade_tarde':1, 'professores' : [11], 'compartilhada': False, 'lab':False},
      {'disciplina': 'PROGRAMAÇÃO PARA DISPOSITIVOS MÓVEIS', 'carga': 60, 'partes': True,'penalidade_tarde':10, 'professores' : [16], 'compartilhada': False, 'lab':True},
      {'disciplina': 'PROGRAMAÇÃO PARA DISPOSITIVOS MÓVEIS', 'carga': 60, 'partes': True,'penalidade_tarde':10, 'professores' : [16], 'compartilhada': False, 'lab':True},
  ],
  [   #7ES
      {'disciplina': 'SEMINÁRIO DE COMPUTAÇÃO I', 'carga': 30, 'partes': False, 'penalidade_tarde':3, 'professores' : [17], 'compartilhada': {3:0}, 'lab':False},
      {'disciplina': 'SEMINÁRIO DE COMPUTAÇÃO II', 'carga': 30, 'partes': False, 'penalidade_tarde':0, 'professores' : [17], 'compartilhada': {3:1}, 'lab':False},
      {'disciplina': 'TÓPICOS AVANÇADOS EM ESW E SISTEMAS', 'carga': 60, 'partes': True, 'penalidade_tarde':5, 'professores' : [7], 'compartilhada': {3:2}, 'lab':True},
      {'disciplina': 'TÓPICOS AVANÇADOS EM ESW E SISTEMAS', 'carga': 60, 'partes': True, 'penalidade_tarde':5, 'professores' : [7], 'compartilhada': {3:3}, 'lab':True},
      {'disciplina': 'ENGENHARIA DE SOFTWARE EDUCATIVO', 'carga': 60, 'partes': True, 'penalidade_tarde':5, 'professores' : [2], 'compartilhada': {3:4}, 'lab':True},
      {'disciplina': 'ENGENHARIA DE SOFTWARE EDUCATIVO', 'carga': 60, 'partes': True,'penalidade_tarde':5, 'professores' : [2], 'compartilhada': False, 'lab':True},
      {'disciplina': 'SEGURANÇA DE SISTEMAS', 'carga': 60, 'partes': True, 'penalidade_tarde':3, 'professores' : [4], 'compartilhada': False, 'lab':True},
      {'disciplina': 'SEGURANÇA DE SISTEMAS', 'carga': 60, 'partes': True, 'penalidade_tarde':3, 'professores' : [4], 'compartilhada': False, 'lab':True},
      {'disciplina': 'DCEXT VII', 'carga': 30, 'partes': False, 'penalidade_tarde':1, 'professores' : [17], 'compartilhada': False, 'lab':False},
      {'disciplina': 'PROJETO II', 'carga': 60, 'partes': True, 'penalidade_tarde':5, 'professores' : [20], 'compartilhada': False, 'lab':True},
      {'disciplina': 'PROJETO II', 'carga': 60, 'partes': True, 'penalidade_tarde':5, 'professores' : [20], 'compartilhada': False, 'lab':True},
  ]
  ]

  lista_professores = [
      {"nome": "Adauto Trigueiro", "disponibilidade": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], "seq": False}, #0 seg ter
      {"nome": "Aêda Monalliza", "disponibilidade": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], "seq": True}, #1 seg ter
      {"nome": "Ariane Nunes", "disponibilidade": [16, 17, 18, 19, 20, 21, 22, 23, 24, 25], "seq": False}, #2 qui sex
      {"nome": "Brunno Wagner", "disponibilidade": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15], "seq": False}, #3 seg ter qua
      {"nome": "Cleiton Martins", "disponibilidade": [6, 7, 8, 9, 10, 11, 12, 13, 14, 15], "seq": False}, #4 ter quar
      {"nome": "Cleverton Silva", "disponibilidade": [1, 2, 3, 6, 7, 8, 16, 17, 18], "seq": False}, #5 seg ter qui
      {"nome": "Emanoel Francisco", "disponibilidade": [11, 12, 13, 16, 17, 18, 21, 22, 23], "seq": False},#6 qua qui sex
      {"nome": "Ewerton Mendonça", "disponibilidade": [6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20], "seq": False},#7 ter qua qui
      {"nome": "Felipe Barreto", "disponibilidade": [6, 7, 14, 15, 19, 20], "seq": False},#8 ter qua qui
      {"nome": "Helaine Barreiro", "disponibilidade": [11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25], "seq": False},#9 qua qui sex
      {"nome": "Ivaldir Honório", "disponibilidade": [11, 12, 13, 14, 15, 16, 17, 18, 19, 20], "seq": False},#10 qua qui
      {"nome": "Victor Santos", "disponibilidade": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15], "seq": False},#11 seg ter qua
      {"nome": "Milton Perceus", "disponibilidade": [6, 7, 8, 9, 10, 11, 12, 13, 14, 15], "seq": False},#12 ter qua
      {"nome": "Geovany Fernandes", "disponibilidade": [6, 7,8,9,10,21, 22, 23, 24, 25], "seq": False},#13 ter sex
      {"nome": "Renato Silvestre", "disponibilidade": [11, 12, 16, 17], "seq": False},#14 qua qui
      {"nome": "Elvis Melo", "disponibilidade": [11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25], "seq": False},#15 qua qui sex
      {"nome": "Elisson Rocha", "disponibilidade": [6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20], "seq": False},#16 ter qua qui
      {"nome": "Marcello Mendonça", "disponibilidade": [6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20], "seq": False},#17 ter qua qui
      {"nome": "Eraylson Galdino", "disponibilidade": [16, 17, 18, 19, 20, 21, 22, 23, 24, 25], "seq": False},#18 qui sex
      {"nome": "Janaína Barros", "disponibilidade": [11,12,13,14,15,16,17,18,19, 20, 21, 22, 23, 24, 25], "seq": False},#19 qua qui sex
      {"nome": "Mariana Maia", "disponibilidade": [16, 17, 18, 19, 20, 21, 22, 23, 24, 25], "seq": False},#20 qui sex
      {"nome": "Felipe Fernando", "disponibilidade": [16, 17, 18, 19, 20, 21, 22, 23, 24, 25], "seq": False},#21 qui sex
      {"nome": "Fellipe Anchieta", "disponibilidade": [11,12,13,14,15,16, 17, 18, 19, 20], "seq": False},#22 qua qui
      {"nome": "Adjair", "disponibilidade": [6,7,8,9,10], "seq": False},#23 ter
      {"nome": "Clecia", "disponibilidade": [6,7,8,9,10], "seq": False},#24 ter
      {"nome": "Renato", "disponibilidade": [16, 17, 18, 19, 20, 21, 22, 23, 24, 25], "seq": False},#25  qui sex
      {"nome": "Roselma", "disponibilidade": [16, 17, 18, 19, 20], "seq": False},#26 qui
      {"nome": "Marcia Xavier", "disponibilidade": [21, 22, 23, 24, 25], "seq": False},#27 sex
      {"nome": "Jose Roniero", "disponibilidade": [16, 17, 18, 19, 20, 21, 22, 23, 24, 25], "seq": False},#28 qui sex
  ] #Lista contendo nomes de professores e seus horários disponíveis na representação do algoritmo

  # seg 5 ter 14 qua 15 qui 19 sex 12


  for turma in matriz_disciplinas:
    for i in range(len(turma), n_horarios):
      turma.append({'disciplina': 'Aula Vaga', 'carga': 0, 'partes': False, 'professores': [], 'compartilhada': False, 'lab':False})
  return n_horas_dia, n_dias, n_horarios, n_turmas_curso, matriz_disciplinas, lista_professores, turno

# Cenario Semestre 2 - 2025.2
def gerar_cenario_semestre_2():

  n_horas_dia = 5
  n_dias = 5
  n_horarios = n_horas_dia*n_dias
  n_turmas_curso = 4
  turno = 'manhã'

  matriz_disciplinas = [
  [   {'disciplina': 'AÇÃO CURRICULAR DE EXTENSÃO II', 'carga': 30, 'partes': False, 'penalidade_tarde':1, 'professores' : [14], 'compartilhada': {4:0}, 'lab':False},
      {'disciplina': 'LÍNGUA PORTUGUESA NA PRODUÇÃO DO CONHECIMENTO', 'carga': 60, 'partes': True, 'penalidade_tarde':5, 'professores' : [26], 'compartilhada': False, 'lab': False},
      {'disciplina': 'LÍNGUA PORTUGUESA NA PRODUÇÃO DO CONHECIMENTO', 'carga': 60, 'partes': True, 'penalidade_tarde':5, 'professores' : [26], 'compartilhada': False, 'lab': False},
      {'disciplina': 'PROGRAMAÇÃO II', 'carga': 90, 'partes': True, 'penalidade_tarde':10, 'professores' : [5], 'compartilhada': False, 'lab':True},
      {'disciplina': 'PROGRAMAÇÃO II', 'carga': 90, 'partes': True, 'penalidade_tarde':10, 'professores' : [5], 'compartilhada': False, 'lab':True},
      {'disciplina': 'PROGRAMAÇÃO II', 'carga': 90, 'partes': True, 'penalidade_tarde':10, 'professores' : [5], 'compartilhada': False, 'lab':True},
      {'disciplina': 'ENSINO DA COMPUTAÇÃO I', 'carga': 60, 'partes': True, 'penalidade_tarde':5, 'professores' : [7], 'compartilhada': False, 'lab':False},
      {'disciplina': 'ENSINO DA COMPUTAÇÃO I', 'carga': 60, 'partes': True, 'penalidade_tarde':5, 'professores' : [7], 'compartilhada': False, 'lab':False},
      {'disciplina': 'METODOLOGIA CIENTÍFICA', 'carga': 60, 'partes': True,'penalidade_tarde':5, 'professores' : [2], 'compartilhada': False, 'lab':False},
      {'disciplina': 'METODOLOGIA CIENTÍFICA', 'carga': 60, 'partes': True, 'penalidade_tarde':5, 'professores' : [2], 'compartilhada': False, 'lab':False},
      {'disciplina': 'CÁLCULO I', 'carga': 60, 'partes': True,'penalidade_tarde':10, 'professores' : [19], 'compartilhada': False, 'lab':False},
      {'disciplina': 'CÁLCULO I', 'carga': 60, 'partes': True, 'penalidade_tarde':10, 'professores' : [19], 'compartilhada': False, 'lab':False},
      {'disciplina': 'FUNDAMENTOS SOCIOLÓGICOS DA EDUCAÇÃO', 'carga': 60, 'partes': True,'penalidade_tarde':2, 'professores' : [20], 'compartilhada': False, 'lab':False},
      {'disciplina': 'FUNDAMENTOS SOCIOLÓGICOS DA EDUCAÇÃO', 'carga': 60, 'partes': True, 'penalidade_tarde':2, 'professores' : [20], 'compartilhada': False, 'lab':False},
      {'disciplina': 'MATEMÁTICA DISCRETA', 'carga': 60, 'partes': True,'penalidade_tarde':2, 'professores' : [25], 'compartilhada': {4:3}, 'lab':False},
      {'disciplina': 'MATEMÁTICA DISCRETA', 'carga': 60, 'partes': True, 'penalidade_tarde':2, 'professores' : [25], 'compartilhada': {4:4}, 'lab':False},
      {'disciplina': 'DIDÁTICA', 'carga': 60, 'partes': True,'penalidade_tarde':2, 'professores' : [27], 'compartilhada': False, 'lab':False},
      {'disciplina': 'DIDÁTICA', 'carga': 60, 'partes': True, 'penalidade_tarde':2, 'professores' : [27], 'compartilhada': False, 'lab':False},
  ],
  [   {'disciplina': 'FUNDAMENTOS ANTROPOLÓGICOS DA EDUCAÇÃO', 'carga': 60, 'partes': True, 'penalidade_tarde':1, 'professores' : [22], 'compartilhada': False, 'lab':False},
      {'disciplina': 'FUNDAMENTOS ANTROPOLÓGICOS DA EDUCAÇÃO', 'carga': 60, 'partes': True, 'penalidade_tarde':1, 'professores' : [22], 'compartilhada': False, 'lab':False},
      {'disciplina': 'TEORIA DA COMPUTAÇÃO', 'carga': 60, 'partes': True, 'penalidade_tarde':5, 'professores' : [3], 'compartilhada': {5:2}, 'lab':False},
      {'disciplina': 'TEORIA DA COMPUTAÇÃO', 'carga': 60, 'partes': True, 'penalidade_tarde':5, 'professores' : [3], 'compartilhada': {5:3}, 'lab':False},
      {'disciplina': 'ORGANIZAÇÃO E ARQUITETURA DE COMPUTADORES', 'carga': 60, 'partes': True, 'penalidade_tarde':5, 'professores' : [4], 'compartilhada': {5:4}, 'lab':False},
      {'disciplina': 'ORGANIZAÇÃO E ARQUITETURA DE COMPUTADORES', 'carga': 60, 'partes': True, 'penalidade_tarde':5, 'professores' : [4], 'compartilhada': {5:5}, 'lab':False},
      {'disciplina': 'ENSINO DE COMPUTAÇÃO III', 'carga': 60, 'partes': True, 'penalidade_tarde':5, 'professores' : [7], 'compartilhada': False, 'lab':False},
      {'disciplina': 'ENSINO DE COMPUTAÇÃO III', 'carga': 60, 'partes': True, 'penalidade_tarde':5, 'professores' : [7], 'compartilhada': False, 'lab':False},
      {'disciplina': 'AÇÃO CURRICULAR DE EXTENSÃO IV', 'carga': 30, 'partes': False, 'penalidade_tarde':1, 'professores' : [15], 'compartilhada': False, 'lab':False},
      {'disciplina': 'ENGENHARIA DE SOFTWARE', 'carga': 60, 'partes': True, 'penalidade_tarde':5, 'professores' : [13], 'compartilhada': False, 'lab':False},
      {'disciplina': 'ENGENHARIA DE SOFTWARE', 'carga': 60, 'partes': True,'penalidade_tarde':5, 'professores' : [13], 'compartilhada': False, 'lab':False},
      {'disciplina': 'PROBABILIDADE E ESTATÍSTICA', 'carga': 60, 'partes': True, 'penalidade_tarde':2, 'professores' : [18], 'compartilhada': False, 'lab':False},
      {'disciplina': 'PROBABILIDADE E ESTATÍSTICA', 'carga': 60, 'partes': True,'penalidade_tarde':2, 'professores' : [18], 'compartilhada': False, 'lab':False},
  ],
  [
      {'disciplina': 'INTELIGÊNCIA ARTIFICIAL', 'carga': 60, 'partes': True, 'penalidade_tarde':5, 'professores' : [10], 'compartilhada': {6:0}, 'lab':True}, #e aqui
      {'disciplina': 'INTELIGÊNCIA ARTIFICIAL', 'carga': 60, 'partes': True, 'penalidade_tarde':5, 'professores' : [10], 'compartilhada': {6:1}, 'lab':True},
      {'disciplina': 'AVALIAÇÃO DA APRENDIZAGEM', 'carga': 60, 'partes': True, 'penalidade_tarde':2, 'professores' : [21], 'compartilhada': False, 'lab':False},
      {'disciplina': 'AVALIAÇÃO DA APRENDIZAGEM', 'carga': 60, 'partes': True, 'penalidade_tarde':2, 'professores' : [21], 'compartilhada': False, 'lab':False},
      {'disciplina': 'COMPUTAÇÃO GRÁFICA E SISTEMAS MULTIMÍDIA', 'carga': 60, 'partes': True, 'penalidade_tarde':5, 'professores' : [6], 'compartilhada': {7:3}, 'lab':True}, #-O crossover ta com problema aqui
      {'disciplina': 'COMPUTAÇÃO GRÁFICA E SISTEMAS MULTIMÍDIA', 'carga': 60, 'partes': True, 'penalidade_tarde':5, 'professores' : [6], 'compartilhada': {7:4}, 'lab':True},
      {'disciplina': 'ENSINO DE COMPUTAÇÃO V', 'carga': 60, 'partes': True, 'penalidade_tarde':5, 'professores' : [15], 'compartilhada': False, 'lab':False},
      {'disciplina': 'ENSINO DE COMPUTAÇÃO V', 'carga': 60, 'partes': True, 'penalidade_tarde':5, 'professores' : [15], 'compartilhada': False, 'lab':False},
      {'disciplina': 'LIBRAS', 'carga': 60, 'partes': True, 'penalidade_tarde':1, 'professores' : [24], 'compartilhada': False, 'lab':False},
      {'disciplina': 'LIBRAS', 'carga': 60, 'partes': True,'penalidade_tarde':1, 'professores' : [24], 'compartilhada': False, 'lab':False},
      {'disciplina': 'AÇÃO CURRICULAR DE EXTENSÃO VI', 'carga': 30, 'partes': False, 'penalidade_tarde':1, 'professores' : [6], 'compartilhada': False, 'lab':False},
      {'disciplina': 'ESTÁGIO SUPERVISIONADO II', 'carga': 30, 'partes': False,'penalidade_tarde':3, 'professores' : [2], 'compartilhada': False, 'lab':False},
  ],
  [
      {'disciplina': 'SEMINÁRIO DE COMPUTAÇÃO II', 'carga': 30, 'partes': False, 'penalidade_tarde':5, 'professores' : [9], 'compartilhada': {7:0}, 'lab':False},
      {'disciplina': 'TÓPICOS AVANÇADOS EM REDES DE COMPUTADORES E SISTEMAS DISTRIBUÍDOS', 'carga': 60, 'partes': True, 'penalidade_tarde':5, 'professores' : [4], 'compartilhada': False, 'lab':False},
      {'disciplina': 'TÓPICOS AVANÇADOS EM REDES DE COMPUTADORES E SISTEMAS DISTRIBUÍDOS', 'carga': 60, 'partes': True, 'penalidade_tarde':5, 'professores' : [4], 'compartilhada': False, 'lab':False},
      {'disciplina': 'TÓPICOS AVANÇADOS EM ENSINO DE COMPUTAÇÃO', 'carga': 30, 'partes': False, 'penalidade_tarde':5, 'professores' : [9], 'compartilhada': False, 'lab':False},
      {'disciplina': 'AÇÃO CURRICULAR DE EXTENSÃO VIII', 'carga': 30, 'partes': False, 'penalidade_tarde':1, 'professores' : [15], 'compartilhada': False, 'lab':False},
      {'disciplina': 'ESTÁGIO SUPERVISIONADO IV', 'carga': 30, 'partes': False, 'penalidade_tarde':3, 'professores' : [15], 'compartilhada': False, 'lab':False},
      {'disciplina': 'EDUCAÇÃO E RELAÇÕES ÉTNICOS RACIAIS', 'carga': 30, 'partes': False, 'penalidade_tarde':3, 'professores' : [23], 'compartilhada': False, 'lab':False},
      {'disciplina': 'APRENDIZAGEM DE MÁQUINA E RECONHECIMENTO DE PADRÕES', 'carga': 60, 'partes': True, 'penalidade_tarde':5, 'professores' : [10], 'compartilhada': {7:5}, 'lab':True},
      {'disciplina': 'APRENDIZAGEM DE MÁQUINA E RECONHECIMENTO DE PADRÕES', 'carga': 60, 'partes': True, 'penalidade_tarde':5, 'professores' : [10], 'compartilhada': {7:6}, 'lab':True},
      {'disciplina': 'INTERAÇÃO HUMANO-COMPUTADOR', 'carga': 60, 'partes': True, 'penalidade_tarde':5, 'professores' : [2], 'compartilhada': {6:8}, 'lab':True},
      {'disciplina': 'INTERAÇÃO HUMANO-COMPUTADOR', 'carga': 60, 'partes': True,'penalidade_tarde':5, 'professores' : [2], 'compartilhada': {6:9}, 'lab':True},
      {'disciplina': 'ROBÓTICA EDUCACIONAL', 'carga': 30, 'partes': False,'penalidade_tarde':1, 'professores' : [7], 'compartilhada': False, 'lab':False},
  ],
  [   #1ES
      {'disciplina': 'DCext II', 'carga': 30, 'partes': False, 'penalidade_tarde':3, 'professores' : [14], 'compartilhada': {0:0}, 'lab':False},
      {'disciplina': 'Processo de Software', 'carga': 60, 'partes': True, 'penalidade_tarde':5, 'professores' : [3], 'compartilhada': False, 'lab':False},
      {'disciplina': 'Processo de Software', 'carga': 60, 'partes': True, 'penalidade_tarde':5, 'professores' : [3], 'compartilhada': False, 'lab':False},
      {'disciplina': 'Matemática Discreta', 'carga': 60, 'partes': True, 'penalidade_tarde':1, 'professores' : [25], 'compartilhada': {0:14}, 'lab':False},
      {'disciplina': 'Matemática Discreta', 'carga': 60, 'partes': True, 'penalidade_tarde':1, 'professores' : [25], 'compartilhada': {0:15}, 'lab':False},
      {'disciplina': 'Metodologia Científica', 'carga': 60, 'partes': True, 'penalidade_tarde':5, 'professores' : [12], 'compartilhada': False, 'lab':False},
      {'disciplina': 'Metodologia Científica', 'carga': 60, 'partes': True, 'penalidade_tarde':5, 'professores' : [12], 'compartilhada': False, 'lab':False},
      {'disciplina': 'Programação II', 'carga': 90, 'partes': True, 'penalidade_tarde':5, 'professores' : [1], 'compartilhada': False, 'lab':True},
      {'disciplina': 'Programação II', 'carga': 90, 'partes': True, 'penalidade_tarde':5, 'professores' : [1], 'compartilhada': False, 'lab':True},
      {'disciplina': 'Programação II', 'carga': 90, 'partes': True, 'penalidade_tarde':5, 'professores' : [1], 'compartilhada': False, 'lab':True},
      {'disciplina': 'Cálculo II', 'carga': 60, 'partes': True,'penalidade_tarde':5, 'professores' : [18], 'compartilhada': False, 'lab':False},
      {'disciplina': 'Cálculo II', 'carga': 60, 'partes': True, 'penalidade_tarde':5, 'professores' : [18], 'compartilhada': False, 'lab':False},
      {'disciplina': 'Álgebra Linear II', 'carga': 60, 'partes': True,'penalidade_tarde':3, 'professores' : [16], 'compartilhada': False, 'lab':False},
      {'disciplina': 'Álgebra Linear II', 'carga': 60, 'partes': True, 'penalidade_tarde':3, 'professores' : [16], 'compartilhada': False, 'lab':False},
  ],
  [   #3ES
      {'disciplina': 'Gerência de Configuração', 'carga': 60, 'partes': True, 'penalidade_tarde':5, 'professores' : [1], 'compartilhada': False, 'lab':False},
      {'disciplina': 'Gerência de Configuração', 'carga': 60, 'partes': True, 'penalidade_tarde':5, 'professores' : [1], 'compartilhada': False, 'lab':False},
      {'disciplina': 'Teoria da computação', 'carga': 60, 'partes': True, 'penalidade_tarde':5, 'professores' : [3], 'compartilhada': {1:2}, 'lab':False},
      {'disciplina': 'Teoria da computação', 'carga': 60, 'partes': True, 'penalidade_tarde':5, 'professores' : [3], 'compartilhada': {1:3}, 'lab':False},
      {'disciplina': 'ORGANIZAÇÃO E ARQUITETURA DE COMPUTADORES', 'carga': 60, 'partes': True, 'penalidade_tarde':5, 'professores' : [4], 'compartilhada': {1:4}, 'lab':False},
      {'disciplina': 'ORGANIZAÇÃO E ARQUITETURA DE COMPUTADORES', 'carga': 60, 'partes': True, 'penalidade_tarde':5, 'professores' : [4], 'compartilhada': {1:5}, 'lab':False},
      {'disciplina': 'Padrões de Projeto de Software', 'carga': 60, 'partes': True, 'penalidade_tarde':10, 'professores' : [6], 'compartilhada': False, 'lab':True},
      {'disciplina': 'Padrões de Projeto de Software', 'carga': 60, 'partes': True, 'penalidade_tarde':10, 'professores' : [6], 'compartilhada': False, 'lab':True},
      {'disciplina': 'DCExt IV', 'carga': 30, 'partes': False, 'penalidade_tarde':5, 'professores' : [10], 'compartilhada': False, 'lab':False},
      {'disciplina': 'Programação Web', 'carga': 60, 'partes': True, 'penalidade_tarde':10, 'professores' : [8], 'compartilhada': False, 'lab':True},
      {'disciplina': 'Programação Web', 'carga': 60, 'partes': True,'penalidade_tarde':10, 'professores' : [8], 'compartilhada': False, 'lab':True},
      {'disciplina': 'ESTATÍSTICA II', 'carga': 60, 'partes': True, 'penalidade_tarde':2, 'professores' : [17], 'compartilhada': False, 'lab':False},
      {'disciplina': 'ESTATÍSTICA II', 'carga': 60, 'partes': True,'penalidade_tarde':2, 'professores' : [17], 'compartilhada': False, 'lab':False},
  ],
  [   #5ES
      {'disciplina': 'Inteligência Artificial', 'carga': 60, 'partes': True, 'penalidade_tarde':3, 'professores' : [10], 'compartilhada': {2:0}, 'lab':True},
      {'disciplina': 'Inteligência Artificial', 'carga': 60, 'partes': True, 'penalidade_tarde':3, 'professores' : [10], 'compartilhada': {2:1}, 'lab':True},
      {'disciplina': 'Sistemas Operacionais', 'carga': 60, 'partes': True, 'penalidade_tarde':5, 'professores' : [4], 'compartilhada': False, 'lab':False},
      {'disciplina': 'Sistemas Operacionais', 'carga': 60, 'partes': True, 'penalidade_tarde':5, 'professores' : [4], 'compartilhada': False, 'lab':False},
      {'disciplina': 'Engenharia de Software Experimental', 'carga': 60, 'partes': True, 'penalidade_tarde':5, 'professores' : [0], 'compartilhada': False, 'lab':False},
      {'disciplina': 'Engenharia de Software Experimental', 'carga': 60, 'partes': True, 'penalidade_tarde':5, 'professores' : [0], 'compartilhada': False, 'lab':False},
      {'disciplina': 'Integração de Sistemas', 'carga': 60, 'partes': True, 'penalidade_tarde':5, 'professores' : [8], 'compartilhada': False, 'lab':True},
      {'disciplina': 'Integração de Sistemas', 'carga': 60, 'partes': True, 'penalidade_tarde':5, 'professores' : [8], 'compartilhada': False, 'lab':True},
      {'disciplina': 'Interação Humano Computador', 'carga': 60, 'partes': True, 'penalidade_tarde':5, 'professores' : [2], 'compartilhada': {3:9}, 'lab':True},
      {'disciplina': 'Interação Humano Computador', 'carga': 60, 'partes': True,'penalidade_tarde':5, 'professores' : [2], 'compartilhada': {3:10}, 'lab':True},
      {'disciplina': 'DCExt VI', 'carga': 30, 'partes': False, 'penalidade_tarde':1, 'professores' : [12], 'compartilhada': False, 'lab':False},
      {'disciplina': 'Arquitetura de Software', 'carga': 60, 'partes': True,'penalidade_tarde':3, 'professores' : [3], 'compartilhada': False, 'lab':False},
      {'disciplina': 'Arquitetura de Software', 'carga': 60, 'partes': True,'penalidade_tarde':3, 'professores' : [3], 'compartilhada': False, 'lab':False},
  ],
  [   #7ES
      {'disciplina': 'SEMINÁRIO DE COMPUTAÇÃO II', 'carga': 30, 'partes': False, 'penalidade_tarde':0, 'professores' : [9], 'compartilhada': {3:0}, 'lab':False},
      {'disciplina': 'Manutenção e evolução de Software', 'carga': 60, 'partes': True, 'penalidade_tarde':5, 'professores' : [14], 'compartilhada': False, 'lab':False},
      {'disciplina': 'Manutenção e evolução de Software', 'carga': 60, 'partes': True, 'penalidade_tarde':5, 'professores' : [14], 'compartilhada': False, 'lab':False},
      {'disciplina': 'Computação Gráfica e Sistemas Multimídia', 'carga': 60, 'partes': True, 'penalidade_tarde':5, 'professores' : [6], 'compartilhada': {2:4}, 'lab':True},
      {'disciplina': 'Computação Gráfica e Sistemas Multimídia', 'carga': 60, 'partes': True,'penalidade_tarde':5, 'professores' : [6], 'compartilhada': {2:5}, 'lab':True},
      {'disciplina': 'Aprendizagem de Máquina e Reconhecimento de Padrões', 'carga': 60, 'partes': True, 'penalidade_tarde':3, 'professores' : [10], 'compartilhada': {3:7}, 'lab':True},
      {'disciplina': 'Aprendizagem de Máquina e Reconhecimento de Padrões', 'carga': 60, 'partes': True, 'penalidade_tarde':3, 'professores' : [10], 'compartilhada': {3:8}, 'lab':True},
      {'disciplina': 'DCExt VIII', 'carga': 30, 'partes': False, 'penalidade_tarde':1, 'professores' : [9], 'compartilhada': False, 'lab':False},
      {'disciplina': 'Tópicos Avançados em Engenharia de Software e Sistemas IV', 'carga': 60, 'partes': True, 'penalidade_tarde':5, 'professores' : [13], 'compartilhada': False, 'lab':False},
      {'disciplina': 'Tópicos Avançados em Engenharia de Software e Sistemas IV', 'carga': 60, 'partes': True, 'penalidade_tarde':5, 'professores' : [13], 'compartilhada': False, 'lab':False},
  ]
  ]

  lista_professores = [
      {"nome": "Adauto Trigueiro", "disponibilidade": [1, 2, 3, 6, 7, 8, 11, 12, 13, 16, 17, 18, 21, 22, 23], "seq": False}, #0 seg ter qua qui sex
      {"nome": "Aêda Monalliza", "disponibilidade": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], "seq": True}, #1 seg ter
      {"nome": "Ariane Nunes", "disponibilidade": [16, 17, 18, 19, 20, 21, 22, 23, 24, 25], "seq": False}, #2 qui sex
      {"nome": "Brunno Wagner", "disponibilidade": [2, 3, 4, 5, 6, 7, 8, 9, 10], "seq": True}, #3 seg ter
      {"nome": "Cleiton Martins", "disponibilidade": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 13, 14, 15], "seq": False}, #4 seg ter quar
      {"nome": "Emanoel Francisco", "disponibilidade": [7, 8, 9, 10, 12, 13, 14, 15, 17, 18, 19, 20, 22, 23, 24, 25], "seq": False},#5 ter qua qui sex
      {"nome": "Ewerton Mendonça", "disponibilidade": [6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20], "seq": False},#6 ter qua qui
      {"nome": "Elvis Melo", "disponibilidade": [11, 12, 13, 14, 15, 16, 17, 18, 19, 20], "seq": False},#7 qua qui
      {"nome": "Elisson Rocha", "disponibilidade": [16, 17, 18, 19, 20, 21, 22, 23, 24, 25], "seq": False},#8 ter qua qui
      {"nome": "Marcello Mendonça", "disponibilidade": [6, 7, 8, 9, 10], "seq": False},#9 ter
      {"nome": "Eraylson Galdino", "disponibilidade": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25], "seq": False},#10 seg ter qua qui sex
      {"nome": "Helaine Barreiro", "disponibilidade": [], "seq": False},#11
      {"nome": "Ivaldir Honório", "disponibilidade": [11, 12, 13, 14, 15, 16, 17, 18], "seq": False},#12 qua qui
      {"nome": "Mariana Maia", "disponibilidade": [16, 17, 18, 19, 20, 21, 22, 23, 24, 25], "seq": False},#13 qui sex
      {"nome": "Victor Santos", "disponibilidade": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15], "seq": False},#14 seg ter qua
      {"nome": "Fellipe Anchieta", "disponibilidade": [11, 12, 13, 14, 15, 16, 17, 18, 19, 20], "seq": False},#15 qua qui
      {"nome": "Felipe Barreto", "disponibilidade": [16, 17, 18, 19, 20], "seq": False},#16 ter qua qui
      {"nome": "Milton Perceus", "disponibilidade": [6, 7, 8, 9, 10, 11, 12, 13, 14, 15], "seq": False},#17 ter qua
      {"nome": "Renato Silvestre", "disponibilidade": [6, 7, 8, 9, 10, 21, 22, 23, 24, 25], "seq": False},#18 ter sex
      {"nome": "Janaína Barros", "disponibilidade": [11, 12, 13, 16, 17, 18, 21, 22, 23], "seq": False},#19 qua qui sex
      {"nome": "Adjair", "disponibilidade": [9, 10, 19, 20], "seq": False},#20 ter
      {"nome": "Clecia", "disponibilidade": [6, 7, 8, 9, 10], "seq": False},#21 ter
      {"nome": "Roberto", "disponibilidade": [1, 2, 3, 4, 5], "seq": False},#22 qui
      {"nome": "Delma", "disponibilidade": [21, 22, 23, 24, 25], "seq": False},#23 sex
      {"nome": "Jose Roniero", "disponibilidade": [19, 20, 24, 25], "seq": False},#24 qui sex
      {"nome": "Junio Teles", "disponibilidade": [19, 20, 24, 25], "seq": False}, #25 qui sex
      {"nome": "Gitanna", "disponibilidade": [1, 2, 3, 4, 5], "seq": False}, #26 seg
      {"nome": "Diogenes", "disponibilidade": [21, 22, 23, 24, 25], "seq": False}, #27 sex
  ] #Lista contendo nomes de professores e seus horários disponíveis na representação do algoritmo

  # seg 5 ter 14 qua 15 qui 19 sex 12


  for turma in matriz_disciplinas:
    for i in range(len(turma), n_horarios):
      turma.append({'disciplina': 'Aula Vaga', 'carga': 0, 'partes': False, 'professores': [], 'compartilhada': False, 'lab':False})
  return n_horas_dia, n_dias, n_horarios, n_turmas_curso, matriz_disciplinas, lista_professores, turno

"""# Cenário 3 - Matemática"""

# Cenario Noite - Pedir a Paulo (Matemática)

def gerar_cenario_3_matematica():
  n_horas_dia = 2
  n_dias = 5
  n_horarios = n_horas_dia*n_dias
  n_turmas_curso = 4
  turno = 'noite'

  matriz_disciplinas = [
      [{'disciplina': 'DCExt I', 'carga': 30, 'partes': False, 'penalidade_tarde':1, 'professores' : [0], 'compartilhada': False, 'lab':False},
       {'disciplina': 'Fenômenos Didáticos I', 'carga': 30, 'partes': False, 'penalidade_tarde':1, 'professores' : [0], 'compartilhada': False, 'lab':False},
       {'disciplina': 'Fundamentos Filosóficos da Educação', 'carga': 60, 'partes': True, 'penalidade_tarde':1, 'professores' : [1], 'compartilhada': False, 'lab':False},
       {'disciplina': 'Fundamentos Filosóficos da Educação', 'carga': 60, 'partes': True, 'penalidade_tarde':1, 'professores' : [1], 'compartilhada': False, 'lab':False},
       {'disciplina': 'Geometria Euclidiana Básica', 'carga': 60, 'partes': True, 'penalidade_tarde':1, 'professores' : [2], 'compartilhada': False, 'lab':False},
       {'disciplina': 'Geometria Euclidiana Básica', 'carga': 60, 'partes': True, 'penalidade_tarde':1, 'professores' : [2], 'compartilhada': False, 'lab':False},
       {'disciplina': 'Fundamentos Socioantropológicos da Educação', 'carga': 60, 'partes': True, 'penalidade_tarde':1, 'professores' : [1], 'compartilhada': False, 'lab':False},
       {'disciplina': 'Fundamentos Socioantropológicos da Educação', 'carga': 60, 'partes': True, 'penalidade_tarde':1, 'professores' : [1], 'compartilhada': False, 'lab':False},
       {'disciplina': 'Matemática Básica II', 'carga': 60, 'partes': True, 'penalidade_tarde':1, 'professores' : [3], 'compartilhada': False, 'lab':False},
       {'disciplina': 'Matemática Básica II', 'carga': 60, 'partes': True, 'penalidade_tarde':1, 'professores' : [3], 'compartilhada': False, 'lab':False},

       ],
      [
          {'disciplina': 'Álgebra Linear II', 'carga': 60, 'partes': True, 'penalidade_tarde':1, 'professores' : [4], 'compartilhada': False, 'lab':False},
          {'disciplina': 'Álgebra Linear II', 'carga': 60, 'partes': True, 'penalidade_tarde':1, 'professores' : [4], 'compartilhada': False, 'lab':False},
          {'disciplina': 'Prática Profissional IV (Geometria e Grandezas e Medidas)', 'carga': 30, 'partes': False, 'penalidade_tarde':1, 'professores' : [0], 'compartilhada': False, 'lab':False},
          {'disciplina': 'Didática da Matemática', 'carga': 30, 'partes': False, 'penalidade_tarde':1, 'professores' : [0], 'compartilhada': False, 'lab':False},
          {'disciplina': 'Didática', 'carga': 60, 'partes': True, 'penalidade_tarde':1, 'professores' : [5], 'compartilhada': False, 'lab':False},
          {'disciplina': 'Didática', 'carga': 60, 'partes': True, 'penalidade_tarde':1, 'professores' : [5], 'compartilhada': False, 'lab':False},
          {'disciplina': 'Cálculo II', 'carga': 60, 'partes': True, 'penalidade_tarde':1, 'professores' : [6], 'compartilhada': False, 'lab':False},
          {'disciplina': 'Cálculo II', 'carga': 60, 'partes': True, 'penalidade_tarde':1, 'professores' : [6], 'compartilhada': False, 'lab':False},
          {'disciplina': 'Fundamentos Sociológicos da Educação', 'carga': 60, 'partes': True, 'penalidade_tarde':1, 'professores' : [1], 'compartilhada': False, 'lab':False},
          {'disciplina': 'Fundamentos Sociológicos da Educação', 'carga': 60, 'partes': True, 'penalidade_tarde':1, 'professores' : [1], 'compartilhada': False, 'lab':False},
      ],
      [
          {'disciplina': 'Introdução às Estruturas Algébricas', 'carga': 60, 'partes': True, 'penalidade_tarde':1, 'professores' : [7], 'compartilhada': False, 'lab':False},
          {'disciplina': 'Introdução às Estruturas Algébricas', 'carga': 60, 'partes': True, 'penalidade_tarde':1, 'professores' : [7], 'compartilhada': False, 'lab':False},
          {'disciplina': 'Metodologia Científica', 'carga': 60, 'partes': True, 'penalidade_tarde':1, 'professores' : [8], 'compartilhada': False, 'lab':False},
          {'disciplina': 'Metodologia Científica', 'carga': 60, 'partes': True, 'penalidade_tarde':1, 'professores' : [8], 'compartilhada': False, 'lab':False},
          {'disciplina': 'Estágio Supervisionado II', 'carga': 30, 'partes': False, 'penalidade_tarde':1, 'professores' : [9], 'compartilhada': False, 'lab':False},
          {'disciplina': 'Prática Profissional VI', 'carga': 30, 'partes': False, 'penalidade_tarde':1, 'professores' : [9], 'compartilhada': False, 'lab':False},
          {'disciplina': 'Fundamentos Filosóficos da Educação', 'carga': 60, 'partes': True, 'penalidade_tarde':1, 'professores' : [10], 'compartilhada': False, 'lab':False},
          {'disciplina': 'Fundamentos Filosóficos da Educação', 'carga': 60, 'partes': True, 'penalidade_tarde':1, 'professores' : [10], 'compartilhada': False, 'lab':False},
          {'disciplina': 'Eletiva I - Inferência Estatística', 'carga': 30, 'partes': False, 'penalidade_tarde':1, 'professores' : [6], 'compartilhada': False, 'lab':False},
          {'disciplina': 'Educação e Relações Étnico-Raciais', 'carga': 30, 'partes': False, 'penalidade_tarde':1, 'professores' : [], 'compartilhada': False, 'lab':False},

      ],
      [
          {'disciplina': 'Projeto de Pesquisa II', 'carga': 30, 'partes': False, 'penalidade_tarde':1, 'professores' : [11], 'compartilhada': False, 'lab':False},
          {'disciplina': 'Educação Inclusiva', 'carga': 30, 'partes': False, 'penalidade_tarde':1, 'professores' : [12], 'compartilhada': False, 'lab':False},
          {'disciplina': 'História da Matemática', 'carga': 60, 'partes': True, 'penalidade_tarde':1, 'professores' : [9], 'compartilhada': False, 'lab':False},
          {'disciplina': 'História da Matemática', 'carga': 60, 'partes': True, 'penalidade_tarde':1, 'professores' : [9], 'compartilhada': False, 'lab':False},
          {'disciplina': 'Libras', 'carga': 60, 'partes': True, 'penalidade_tarde':1, 'professores' : [13], 'compartilhada': False, 'lab':False},
          {'disciplina': 'Libras', 'carga': 60, 'partes': True, 'penalidade_tarde':1, 'professores' : [13], 'compartilhada': False, 'lab':False},
          {'disciplina': 'Análise Matemática II', 'carga': 60, 'partes': True, 'penalidade_tarde':1, 'professores' : [4], 'compartilhada': False, 'lab':False},
          {'disciplina': 'Análise Matemática II', 'carga': 60, 'partes': True, 'penalidade_tarde':1, 'professores' : [4], 'compartilhada': False, 'lab':False},
          {'disciplina': 'Estágio Supervisionado IV', 'carga': 30, 'partes': False, 'penalidade_tarde':1, 'professores' : [14], 'compartilhada': False, 'lab':False},
          {'disciplina': 'Eletiva III - Resolução de Problemas', 'carga': 30, 'partes': False, 'penalidade_tarde':1, 'professores' : [14], 'compartilhada': False, 'lab':False},
      ],
  ]
  lista_professores = [
      # * feito de forma aleatória
      {"nome":"Lucas H.", "disponibilidade": [1,2,3,4,5,6], "seq": True}, #ok
      {"nome":"Aldenor", "disponibilidade": [3,4,7,8,9,10], "seq": False}, #ok
      {"nome":"Felipe", "disponibilidade": [5,6,7,8,9,10], "seq": True}, #ok
      {"nome":"Janaína", "disponibilidade": [5,6,7,8,9,10], "seq": True}, #ok
      {"nome":"Elizângelo", "disponibilidade": [1,2,5,6,7,8], "seq": False}, #ok *
      {"nome":"Nayana", "disponibilidade": [3,4,5,6,9,10], "seq": False}, #ok *
      {"nome":"Lucas A.", "disponibilidade": [3,4,7,8,9,10], "seq": True}, #ok *
      {"nome":"Junio", "disponibilidade": [1,2,7,8,9,10], "seq": False}, # ok
      {"nome":"Roberto", "disponibilidade": [1,2,3,4,7,8], "seq": False}, #ok *
      {"nome":"Robson", "disponibilidade": [3,4,5,6,9,10], "seq": True}, #ok *
      {"nome":"Adjair", "disponibilidade": [3,4,7,8,9,10], "seq": False}, #ok *
      {"nome":"Paulo Jr.", "disponibilidade": [1,2,5,6,7,8], "seq": False}, #ok *
      {"nome":"Alena", "disponibilidade": [1,2,3,4,7,8], "seq": False}, #ok *
      {"nome":"Roniero", "disponibilidade": [5,6,7,8,9,10], "seq": False}, #ok
      {"nome":"Diógenes", "disponibilidade": [1,2,5,6,9,10], "seq": False}, #ok *
      {"nome":"Renato", "disponibilidade": [3,4,5,6,9,10], "seq": False}, #ok
  ]
  for turma in matriz_disciplinas:
    for i in range(len(turma), n_horarios):
      turma.append({'disciplina': 'Aula Vaga', 'carga': 0, 'partes': False, 'professores': [], 'compartilhada': False, 'lab':False})
  return n_horas_dia, n_dias, n_horarios, n_turmas_curso, matriz_disciplinas, lista_professores, turno
