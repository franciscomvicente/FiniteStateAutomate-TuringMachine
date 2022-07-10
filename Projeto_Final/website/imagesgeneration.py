from graphviz import Digraph

def desenha_automato(descricao, estados, estadoInicial, estadosdeaceitacao, tabeladetransicoes):
    try:
        estadosDeAceitacao = set(estadosdeaceitacao)
        dicionarioTransicao = {}
        for elemento in tabeladetransicoes.split():
            estadoAtual = elemento[0]
            simbolo = elemento[1]
            estadoSeguinte = elemento[2]
            dicionarioTransicao[(estadoAtual, simbolo)] = estadoSeguinte

        d = Digraph(name=descricao)

        # configurações gerais
        d.graph_attr['rankdir'] = 'LR'
        d.edge_attr.update(arrowhead='vee', arrowsize='1')
        # d.edge_attr['color'] = 'blue'
        d.node_attr['shape'] = 'circle'
        # d.node_attr['color'] = 'blue'

        # Estado inicial
        d.node('Start', label='', shape='none')

        # Estados de transição
        estadosDeTransicao = set(estados) - set(estadosDeAceitacao)
        for estado in estadosDeTransicao:
            d.node(estado)

        # Estado aceitação
        for estado in estadosDeAceitacao:
            d.node(estado, shape='doublecircle')

        # Transicoes
        d.edge('Start', estadoInicial)

        for tuplo, estadoSeguinte in dicionarioTransicao.items():
            d.edge(tuplo[0], estadoSeguinte, label=tuplo[1])

        # print(d.source)
        d.format = 'svg'
        d.render('website/static/website/images/' + descricao)

    except IOError:
        print("O ficheiro não existe")

def desenha_turing(descricao, estados, estadoInicial, estadodeaceitacao, tabeladetransicoes):
    try:
        estadosDeAceitacao = set(estadodeaceitacao)
        dicionarioTransicao = {}
        for elemento in tabeladetransicoes.split():
            estadoAtual = elemento[0]
            simbolo = elemento[1]
            substitui = elemento[2]
            andar = elemento[3]
            estadoSeguinte = elemento[4]
            dicionarioTransicao[(estadoAtual, simbolo)] = (substitui, andar, estadoSeguinte)

        d = Digraph(name=descricao)

        # configurações gerais
        d.graph_attr['rankdir'] = 'LR'
        d.edge_attr.update(arrowhead='vee', arrowsize='1')
        # d.edge_attr['color'] = 'blue'
        d.node_attr['shape'] = 'circle'
        # d.node_attr['color'] = 'blue'

        # Estado inicial
        d.node('Start', label='', shape='none')

        # Estados de transição
        estadosDeTransicao = set(estados) - set(estadosDeAceitacao)
        for estado in estadosDeTransicao:
            d.node(estado)

        # Estado aceitação
        for estado in estadosDeAceitacao:
            d.node(estado, shape='doublecircle')

        # Transicoes
        d.edge('Start', estadoInicial)

        for tuplo1, tuplo2 in dicionarioTransicao.items():
            d.edge(tuplo1[0], tuplo2[2], label=tuplo1[1]+tuplo2[0]+tuplo2[1])

        # print(d.source)
        d.format = 'svg'
        d.render('website/static/website/images/' + descricao)

    except IOError:
        print("O ficheiro não existe")