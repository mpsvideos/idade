"""
Desenvolvimento 6 #100177
INSTRUÇÕES DO PROJETO:

Desenvolva um programa que recebe do usuário nome completo e ano de nascimento que seja entre 1922 e 2021.
A partir dessas informações, o sistema mostrará o nome do usuário e a idade que completou, ou completará, no ano atual (2022).
Caso o usuário não digite um número ou apareça um inválido no campo do ano, o sistema informará o erro e
continuará perguntando até que um valor correto seja preenchido.
"""

valor_valido = False

while valor_valido == False:
    nome = str(input('Digite seu nome completo: '))
    ano_nascimento = input('Digite seu ano de nascimento [1922 até 2021: ')
    ano_atual = 2022
    try:
        if int(ano_nascimento) >= 1922 and int(ano_nascimento) <= 2021:
            idade = ano_atual - int(ano_nascimento)
            print(f'{nome}, você tem {idade} ano(s).')
            valor_valido = True
        else:
            print('Ano de nascimento inválido, digite o ano de nascimento entre 1922 a 2021.')
    except:
        print('Dado inválido, digite o ano de nascimento entre 1922 a 2021.')
