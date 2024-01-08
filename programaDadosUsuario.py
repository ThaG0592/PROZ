from datetime import datetime

def calcular_idade(ano_nascimento):
    ano_atual = datetime.now().year
    return ano_atual - ano_nascimento

def obter_ano_nascimento():
    while True:
        try:
            ano = int(input("Digite o ano de nascimento (entre 1922 e 2021): "))
            if 1922 <= ano <= 2021:
                return ano
            else:
                print("Por favor, digite um ano válido entre 1922 e 2021.")
        except ValueError:
            print("Por favor, digite um número válido.")

nome = input("Digite seu nome completo: ")

ano_nascimento = obter_ano_nascimento()
idade = calcular_idade(ano_nascimento)

print(f"Olá, {nome}! Você completou ou completará {idade} anos em 2024.")
