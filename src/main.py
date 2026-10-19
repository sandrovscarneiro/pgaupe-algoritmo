from data import *
from classes import *

n_horas_dia, n_dias, n_horarios, n_turmas_curso, matriz_disciplinas, lista_professores, turno = gerar_cenario_semestre_1()

problem = TimetablingProblem(matriz_disciplinas, n_horas_dia, n_dias, lista_professores, turno)
algorithm = GA(pop_size = 100, sampling = MatrixPermutationSampling(), crossover = MatrixPointCrossover(), mutation = SwapMutation())
termination = get_termination("n_gen", 200)
res = minimize(problem, algorithm, termination, return_least_infeasible=True, save_history = True)


matriz_horarios = res.X.reshape(problem.n_periodos, problem.n_horarios)

print(res.X)
print(res.F)
print(res.CV)
print(res.G)
