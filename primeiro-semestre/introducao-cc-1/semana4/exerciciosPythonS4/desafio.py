x = int(input("Digite um numero: "))
soma = 0
i = 0

while x != 0: 
    i = x % 10
    soma = soma + i
    x = x // 10

print("Soma dos digitos eh: ", soma)
