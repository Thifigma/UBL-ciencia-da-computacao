n = int(input("Digite um valor: "))
soma = 0

while n != 0:
    x = n % 10
    soma = soma + x
    n = n // 10

print(soma)
