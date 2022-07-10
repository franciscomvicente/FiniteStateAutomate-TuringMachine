from .models import AFD

def verificar_automato(sequencia, afd_id):
    Objeto = AFD.objects.get(id=afd_id)
    estadoInicial = Objeto.estadoinicial
    estadosDeAceitacao = set(Objeto.estadosdeaceitacao)
    dicionarioTransicao = {}
    for elemento in Objeto.tabeladetransicoes.split():
        estadoAtual = elemento[0]
        simbolo = elemento[1]
        estadoSeguinte = elemento[2]
        dicionarioTransicao[(estadoAtual, simbolo)] = estadoSeguinte

    estadoAtual = estadoInicial
    for n in sequencia:
        for state in dicionarioTransicao.keys():
            if str(estadoAtual) == str(state[0]) and str(n) == str(state[1]):
                estadoAtual = dicionarioTransicao.get(state)
                break

    for a in list(estadosDeAceitacao):
        if estadoAtual == str(a):
            return ('A sequência é aceite')
    if estadoAtual != str(a):
        return ('A sequência não é aceite')
