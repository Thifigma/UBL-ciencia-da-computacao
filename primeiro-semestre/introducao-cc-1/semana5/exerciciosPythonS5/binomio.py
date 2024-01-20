def fat(n):
    i = 1
    fat = 1
    while  i <= n:
        fat = fat * i
        i = i + 1
    return fat

def numBinomial(n, k):
    return fat(n) / (fat(k) * fat(n - k))

n = int(input("N: "))
k = int(input("K: "))

print(numBinomial(n, k))
