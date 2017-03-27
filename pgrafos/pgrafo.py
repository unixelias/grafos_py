#!/usr/bin/env python
# Author: Elias Alves (elias.alves@ufvjm.edu.br)

#    All rights reserved.
#    GLPv3 license.

import networkx as nx

def grafo_dist():
    # Retorna as cidades registradas em miles_dat.txt
    # do arquivo Stanford GraphBase.
    
    # abre o arquivo miles_dat.txt.gz
    import gzip
    arquivo = gzip.open('knuth_miles.txt.gz','r')

    G=nx.Graph()
    G.posicao={}
    G.populacao={}

    cidades=[]
    for linha in arquivo.readlines(): #para cada linha do arquivo
        linha = linha.decode() # cria o objeto para tratar linhas
        if linha.startswith("*"): # Pula a linha comentada com *
            continue

        linhanumeral=re.compile("^\d+") # recebe uma sequencia de digitos Regex

        if linhanumeral.match(linha):  # se a linha for uma sequencia de digitos linhas de distancias
            distancias=linha.split() # converte os numeros da a linha em um vetor
            for d in distancias:
                # um vertice x,y com a distancia como peso
                # cidade = eixo y (linha)
                # cidades[i] eixo x (coluna)
                G.add_edge(cidade,cidades[i],weight=int(d))
                i=i+1
        else: # linha com cidade, posicao, populacao
            i=1
            # cidade = "nome da cidade, ES"
            # restante = o resto da linha
            (cidade,restante)=linha.split("[")
            cidades.insert(0,cidade)
            (coordenadas,qhabitantes)=restante.split("]")
            # x = primeiro numero
            # y - segundo numero
            (y,x)=coordenadas.split(",")

            # adiciona um no para a cidade
            G.add_node(cidade)
            # assign posicao - flip x axis for matplotlib, shift origin
            G.posicao[cidade]=(-int(x)+7500,int(y)-3000)
            G.populacao[cidade]=float(qhabitantes)/1000.0
    return G

if __name__ == '__main__':
    import networkx as nx
    import re
    import sys

    G=grafo_dist()
    
    

    print("Arquivo miles_dat.txt contendo 128 cidades carregado!")
    print("esse grafo contem %d vertices com %d arestas"\
          %(nx.number_of_nodes(G),nx.number_of_edges(G)))


    # make new graph of cites, edge if less then 300 miles between them
    H=nx.Graph()
    for v in G:
        H.add_node(v)
    for (u,v,d) in G.edges(data=True):
            
            H.add_edge(u,v)

