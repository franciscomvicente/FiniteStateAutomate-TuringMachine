from .models import TM

def listToString(s):
    str1 = ""

    for ele in s:
        str1 += ele

    return str1


def turing_machine(seq, tm_id):
    Objeto = TM.objects.get(id=tm_id)
    estadoinicial = Objeto.estadoinicial
    estadodeaceitacao = Objeto.estadodeaceitacao
    dicionariotransições = {}
    for elemento in Objeto.tabeladetransicoes.split():
        estadoAtual = elemento[0]
        simbolo = elemento[1]
        substitui = elemento[2]
        andar = elemento[3]
        estadoSeguinte = elemento[4]
        dicionariotransições[(estadoAtual, simbolo)] = (substitui,andar,estadoSeguinte)


    estadoatual = estadoinicial
    deltas = ['¬'] * 30
    sequencia = list(seq)
    fita = deltas + sequencia + deltas
    cabeca = fita.index(sequencia[0])
    dicionariotransições.update(({'exit': 1}))
    erro = False

    while estadoatual != estadodeaceitacao and erro != True:
            for tuplo1, tuplo2 in dicionariotransições.items():
                if tuplo1[0] == estadoatual and tuplo1[1] == fita[cabeca]:
                    fita[cabeca] = tuplo2[0]
                    estadoatual = tuplo2[2]
                    if tuplo2[1] == 'R':
                        cabeca = cabeca + 1
                    if tuplo2[1] == 'L':
                        cabeca = cabeca - 1
                    break
                if tuplo1 == 'exit':
                    erro = True

    ListaFinal = [s for s in fita if s != '¬']
    if estadoatual == estadodeaceitacao:
        return ('Sequência Válida: ' + listToString(ListaFinal))
    if erro == True:
        return ('Sequência Inválida')