"""
CÓDIGO PARA PASSE DE ÔNIBUS
"""
import time
def verifica_onibus(ent):
    lista = ['1', '2', '3', '4']
    while ent not in lista:
        ent = input(f' ENTRADA INVÁLIDA \n(como que tu pega {int(ent)*2} onibus misera)\n')
    ent = int(ent)
    return ent

def verifica_dia(ent):
    dia = ['1', '2', '3', '4','5','6','7']
    while ent not in dia:
        ent = input(f' ENTRADA INVÁLIDA \n')
    ent = int(ent)
    return ent


saldo = float(input('Digite o valor restante no seu passe:(ex: 50.20 ; 17.50)\n'))
valor_passagem = float(input('Digite o valor de uma passagem:\n'))
viagens_total = int(saldo/valor_passagem)
print(f'Número de viagens restantes: {viagens_total}')
time.sleep(1.5)
n_onibus = verifica_onibus(input('''Digite o número de ônibus que são necessários para ir para seu destino(ou voltar)\n'''))
valor_diario = valor_passagem*n_onibus

print('Valor gasto em um dia: R${:.2f}'.format(valor_diario))
dias_restantes = viagens_total/n_onibus
time.sleep(1.5)
print(f'Você pode viajar por {dias_restantes} dias\n')
time.sleep(1)
if dias_restantes > 7:
    dia_semana = verifica_dia(input('Qual o dia da semana de hoje?(ex: 2 para segunda, 7 para sábado)\n'))
    dia_fim = (dia_semana + dias_restantes)%7
    if dia_fim == 1:
        print('Seu crédito acabará em um domingo')
    elif dia_fim == 2:
        print('Seu crédito acabará em uma segunda')
    elif dia_fim == 3:
        print('Seu crédito acabará em uma terça')
    elif dia_fim == 4:
        print('Seu crédito acabará em uma quarta')
    elif dia_fim == 5:
        print('Seu crédito acabará em uma quinta')
    elif dia_fim == 6:
        print('Seu crédito acabará em uma sexta')
    elif dia_fim == 7:
        print('Seu crédito acabará em um sábado')


