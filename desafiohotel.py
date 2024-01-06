# loop crescente com for

for numero in range(1, 21):
    if numero != 13:
        print(numero, end=" ")

# loop crescente com while

numero = 1
while numero <= 20:
    if numero != 13:
        print(numero, end=" ")
    numero += 1


# loop decrescente com for

for numero in range(20, 0, -1):
    if numero != 13:
        print(numero, end=" ")

# loop decrescente com while

numero = 20
while numero >= 1:
    if numero != 13:
        print(numero, end=" ")
    numero -= 1
