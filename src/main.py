from data import *
from classes import *
from convert import *

value = 1
n_horas_dia, n_dias, n_horarios, n_turmas_curso, matriz_disciplinas, lista_professores, turno = gerar_cenario_3_matematica()

problem = TimetablingProblem(matriz_disciplinas, n_horas_dia, n_dias, lista_professores, turno)
algorithm = GA(pop_size = 500, sampling = MatrixPermutationSampling(), crossover = MatrixPointCrossover(), mutation = SwapMutation())
termination = get_termination("n_gen", 2000)
res = minimize(problem, algorithm, termination, return_least_infeasible=True, save_history = True, callback=ColabCallback())
value = res.CV
matriz_horarios = res.X.reshape(problem.n_periodos, problem.n_horarios)
gerar_timetable(matriz_horarios, matriz_disciplinas, lista_professores, turno)








