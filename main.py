import pandas as pd
import grafoPonderado as gp

#criando o grafo ponderado
g = gp.GrafoPonderado()

#pegando o arquivo com os dados dos votos
caminho = input("Digite o caminho do arquivo com .xlsx: ")
df = pd.read_excel(caminho)

#criando os nós
dicDeputados = {}
for i in range(len(df)):
    dicDeputados[df['deputado_id'][i]] = df['deputado_nome'][i]
g.adiciona_nos(dicDeputados.keys())

#separando as votações
votacoes = []
for i in range(len(df)):
    votacoes.append(df['idVotacao'][i])
votacoes = list(set(votacoes))

#agrupando os votos por votação
dicVotacoes = {}
for i in range(len(votacoes)):
    dicVotacoes[votacoes[i]] = {}
for i in range(len(df)):
    dicVotacoes[df['idVotacao'][i]][df['deputado_id'][i]] = df['voto'][i]


#criando as arestas
for votacaoId in dicVotacoes:
    for deputadoId1 in dicVotacoes[votacaoId]:
        for deputadoId2 in dicVotacoes[votacaoId]:
            if deputadoId1 != deputadoId2:
                if dicVotacoes[votacaoId][deputadoId1] == dicVotacoes[votacaoId][deputadoId2]:
                    if(g.verifica_aresta(deputadoId1, deputadoId2)):
                        g.soma_um_peso(deputadoId1, deputadoId2)
                    else:
                        g.adicionar_aresta(deputadoId1, deputadoId2, 1)


#criando o arquivo de saída com a relação de votos com deputados
relacaoVotos = open("relacaoVotos.txt", "w")
relacaoVotos.write(f"{g.num_nos} {g.num_arestas / 2}\n")
relacaoDeputadosVotos = {}
for no in g.lista_adj:
    for adj in g.lista_adj[no]:
        if (adj, no) not in relacaoDeputadosVotos:
            relacaoDeputadosVotos[(no, adj)] = g.lista_adj[no][adj]
            relacaoVotos.write(f"{dicDeputados[no]} {dicDeputados[adj]} {g.lista_adj[no][adj]}\n")
relacaoVotos.close()

#criando o arquivo de saída com participação de cada deputado em votações
votacoesParticipacao = {}
for votacao in dicVotacoes:
    for deputado in dicVotacoes[votacao]:
        if deputado not in votacoesParticipacao:
            votacoesParticipacao[deputado] = 1
        else:
            votacoesParticipacao[deputado] += 1

participacao = open("participacao.txt", "w")
for deputado in votacoesParticipacao:
    participacao.write(f"{dicDeputados[deputado]} {votacoesParticipacao[deputado]}\n")
participacao.close()

#mostrar ao usuário os arquivos gerados
print("Arquivos gerados:")
print("relacaoVotos.txt")
print("participacao.txt")


        




