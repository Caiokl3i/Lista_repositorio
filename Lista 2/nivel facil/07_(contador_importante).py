n = int(input("Digite um numero: "))

counter = 0
for i in range(1, n + 1):
    if n % i == 0:
        counter += 1
div = counter
print(f"Esse numero tem {div} divisores")
