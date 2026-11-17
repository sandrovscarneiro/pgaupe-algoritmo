import pandas as pd
def gerar_timetable(matriz_horarios, matriz_disciplinas, lista_professores, turno):
    if turno == "noite":
                # 1. Usamos 'dados_grade' para o dicionário inicial de dados
        dados_grade = {'Seg': [], 'Ter': [], 'Qua': [], 'Qui': [], 'Sex': []}

        for i in range(len(matriz_horarios)):
            contador = 0
            sorted_periodo = sorted(zip(matriz_horarios[i], matriz_disciplinas[i]))

            for horario in sorted_periodo:
                info_disc = horario[1]
                nome_disciplina = info_disc["disciplina"]

                if info_disc.get("professores") and len(info_disc["professores"]) > 0:
                    idx_professor = info_disc["professores"][0]
                    nome_professor = lista_professores[idx_professor]["nome"]
                    texto_celula = f"{nome_disciplina} ({nome_professor})"
                else:
                    texto_celula = f"{nome_disciplina} (Sem Prof.)"

                # Adiciona na lista do dia correspondente no dicionário
                list(dados_grade.values())[contador].append(texto_celula)

                if horario[0] % 2 == 0:
                    contador += 1

        # 2. Montagem do MultiIndex (todas as 3 listas com tamanho 8)
        cursos = ['Matemática'] * 8

        periodos = (
            ['Primeiro Período'] * 2
            + ['Terceiro Período'] * 2
            + ['Quinto Período'] * 2
            + ['Sétimo Período'] * 2
        )

        horarios = ['19h00-20h30', '20h30-22h00'] * 4

        midx = pd.MultiIndex.from_arrays(
            [cursos, periodos, horarios], names=['curso', 'periodo', 'horario']
        )

        # 3. Criação do DataFrame final passando o dicionário 'dados_grade'
        df = pd.DataFrame(dados_grade, index=midx)

        print(df)
    else:
        primeiro_periodo = sorted(zip(matriz_horarios[0], matriz_disciplinas[0]))
        df = {'Seg':[], 'Ter':[], 'Qua':[], 'Qui':[], 'Sex':[]}

        for i in range(len(matriz_horarios)):
            contador = 0
            sorted_periodo = sorted(zip(matriz_horarios[i], matriz_disciplinas[i]))

        for horario in sorted_periodo:
            list(df.values())[contador].append(f'{horario[1]["disciplina"]}')
            if horario[0]%5 == 0:
                contador+=1


        cursos = ['Licenciatura em Computação']*20 + ['Engenharia de Software']*20
        periodos = ['Primeiro Período']*5+['Terceiro Período']*5+['Quinto Período']*5+['Sétimo Período']*5+['Primeiro Período']*5+['Terceiro Período']*5+['Quinto Período']*5+['Sétimo Período']*5
        horarios = ['07h30-09h10', '09h10-11h00', '11h00-12h30', '13h30-15h10', '15h10-16h50']*8

        midx = pd.MultiIndex.from_arrays([cursos, periodos, horarios], None, ['curso', 'periodo', 'horario'])
        df = pd.DataFrame(df, index = midx)
    df.to_excel('results/timetable.xlsx', index=True)
    return df