import csv

tabela = {}

def converteTemperatura(unidade, valor):
    if unidade == 2: 
        # Converte Celsius para Kelvin
        valor = valor + 273
    elif unidade == 3:
        #Converte Fahrenheit para Kelvin
        valor = valor + 457.87
    return valor

def convertePressao(unidade, valor):
    if unidade == 2: 
        # Converte bar para Pascal
        valor = valor / 100000
    elif unidade == 3:
        #Converte atm para Pascal
        valor = valor / 101325
    return valor

def leTabela():
    with open('steam-table-l.csv') as csvfile: #'steam-table-g.csv'
        spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
        for row in spamreader:
            tabela[row[0]] = row[1:]

def procuraTabela(a, b, c, d):
    resposta = {}
    for r in range(len(tabela[c])):
        if tabela[c][r] == a:
            if tabela[d][r] == b:
                resposta['P'] = tabela['P'][r]
                resposta['T'] = tabela['T'][r]
                resposta['H'] = tabela['H'][r]
                resposta['V'] = tabela['V'][r]
                resposta['S'] = tabela['S'][r]
                resposta['E'] = tabela['E'][r]
                resposta['X'] = tabela['X'][r]
    return resposta

def leParametro(parametro):
    if parametro == 'P':
        unidade = input("Qual a unidade de pressão: \n 1: Pa \n 2: bar \n 3: atm \n")
        valor = input("Digite o valor de pressão: ")
        valor = convertePressao(unidade, valor)
    elif parametro == 'T':
        unidade = input("Qual a unidade de temperatura: \n 1: Kelvin \n 2: Celsius \n 3: Fahrenheit \n")
        valor = input("Digite o valor de temperatura: ")
        valor = converteTemperatura(unidade, valor)
    elif parametro == 'H':
        valor = input("Digite o valor de entalpia: ")
    elif parametro == 'V':
        valor = input("Digite o valor de volume específico: ")
    elif parametro == 'S':
        valor = input("Digite o valor de entropia: ")
    elif parametro == 'E':
        valor = input("Digite o valor de energia interna: ")
    elif parametro == 'X':
        valor = input("Digite o valor de qualidade: ")
    return valor

def tabelaVapor():
    tipo_parametro_1 = input("Qual o primeiro parâmetro? \n P: Pressão \n T: Temperatura \n H: Entalpia \n V: Volume específico \n S: Entropia \n E: Energia interna \n X: Qualidade \n")
    valor_parametro_1 = leParametro(tipo_parametro_1)
    tipo_parametro_2 = input("Qual o segundo parâmetro? \n P: Pressão \n T: Temperatura \n H: Entalpia \n V: Volume específico \n S: Entropia \n E: Energia interna \n X: Qualidade \n")
    valor_parametro_2 = leParametro(tipo_parametro_2)
    leTabela()
    resultado = procuraTabela(valor_parametro_1, valor_parametro_2, tipo_parametro_1, tipo_parametro_2)
    print(resultado)

tabelaVapor()