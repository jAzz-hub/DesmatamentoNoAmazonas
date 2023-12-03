

def ProcurarTodosOsCliques(grafo):
  CliquesEncontrados = []

  for vertice in grafo.vertices():
    cliqueMaximoPresente = VizinhosVermelhos(vertice)

    for verticeDeClique in cliqueMaximoPresente:
      conjunto_de_vizinhos = VizinhosVermelhos(verticeDeClique)

    cliqueMaximoPresente = cliqueMaximoPresente | conjunto_de_vizinhos  # União
    cliqueMaximoPresente = cliqueMaximoPresente & conjunto_de_vizinhos  # Intersecção

    for vertice_candidato in grafo.vertices:    # !cliqueMaximoPresente - grafo.vertices()
      if vertice_candidato not in conjunto_de_vizinhos:
        cliqueMaximoPresente.remove(vertice_candidato)

    if cliqueMaximoPresente not in CliquesEncontrados:
      CliquesEncontrados.append(cliqueMaximoPresente)

  return CliquesEncontrados


def VizinhosVermelhos(vertice):
  return [v for v in vertice.vizinhos if v.desmatamento_elevado]



# % \begin{algorithm}
# % \caption{Algoritmo de busca por todos os cliques em um grafo qualquer}
# % \begin{algorithmic}[1]
# %     \Procedure{ProcurarTodosOsCliques}{$Grafo$}]
# %     \State $Cliques$ \gets [\empty]
    
# %         \FOREACH{$verticeInicial$ no $Grafo$} \do
# %             $cliqueMáximoAtual$ \gets $vizinhosDesmatamentoElevado$($verticeInicial$)
        
# %             \FOR{$verticeClique$ no $cliqueMáximoAtual$}
# %                 $conjuntoDeVizinhos$ \gets $vizinhosDesmatamentoElevado$($verticeClique$)
    
# %             \ENDFOR
# %             $cliqueMaxAtual$ \gets $cliqueMaxAtual$ \cup $conjuntoDeVizinhos$  
# %             $cliqueMaxAtual$ \gets $cliqueMaxAtual$ \cap $conjuntoDeVizinhos$ 
        
# %             \FOR{cada $verticeCandidato$ em $Grafo$ }
# %                 \If{$verticeCandidato$ \notin $conjuntoDeVizinhos$}
# %                     cliqueMaxAtual.remove($verticeCandidato$)
# %                 \EndIf
# %             \ENDFOR
# %         \If{$cliqueMaxAtual$ \not\subset $Cliques$}
# %             $Cliques$.adicionar($cliqueMaxAtual$)
        
# %         \EndIf
# %     % \ENDFOR
# %     \EndProcedure
# % \end{algorithmic}
# % \end{algorithm}