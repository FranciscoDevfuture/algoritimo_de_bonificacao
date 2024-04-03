salario = float(input('Qual seu salário?'))
ano_admissao = int(input('Qual seu ano de admissão na empresa?'))
ano_atual = float(input('Em que ano estamos?'))

tempo = ano_atual-ano_admissao
if (tempo > 10):
    bonus = salario * 0.3
else:
    if (tempo > 5):
        bonus = salario * 0.2
    else:
        bonus = salario * 0.1

print(f'Você tem {tempo} anos dentro da empresa.')
print(f'Seu salario é de {salario}')
print(f'E sua bonificação é de {bonus}')
print(f'Salario final: {salario + bonus}.')