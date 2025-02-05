def fibonacci(num):
    fibonacciA = []
    fibonacciA.append(0)
    for i in range(num+1):
        if(i == 1 or i == 2):
            fibonacciA.append(1)
        elif(i != 0):
            auxNum = fibonacciA[i-2] + fibonacciA[i-1]
            fibonacciA.append(auxNum)
    return fibonacciA[num]

fator = int(input("Digite o fator desejado da sequencia de fibonacci: "))
print(fibonacci(fator))
#shoutout pro meu amigo vitor(VitorF aqui no github) que me deu esse desafiozinho :)
