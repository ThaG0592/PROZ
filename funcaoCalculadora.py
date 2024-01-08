import unittest


def calculadora(num1, num2, operacao):
    if operacao == 1:
        return num1 + num2
    elif operacao == 2:
        return num1 - num2
    elif operacao == 3:
        return num1 * num2
    elif operacao == 4:
        if num2 != 0:  # Verifica se o segundo número não é zero para evitar divisão por zero
            return num1 / num2
        else:
            return "Não é possível dividir por zero."
    else:
        return 0  # Se a operação não for reconhecida, retorna 0

# Exemplo de uso:
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
op = int(input("Escolha a operação (1: Soma, 2: Subtração, 3: Multiplicação, 4: Divisão): "))

resultado = calculadora(num1, num2, op)
print("O resultado é:", resultado)
