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


    

# f = open("new_file.txt", "x")

# f = open("new_file.txt", "a")
# f.write("Now the file has more content!")
# f.close()

