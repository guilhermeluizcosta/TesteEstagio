def Fibonacci():
    num = input('Digite um numero:')
    try:
        num = int(num)
        a = 0
        b = 1
        fib = b

        while fib < num:
            fib = a + b
            a = b
            b = fib


        if fib == num:
            return "Está na sequência"

        else:
            return "Não está na sequência"
        
    except ValueError:
        print("Entrada Inválida")
    

print("Questão 1 - Fibonacci")
print(Fibonacci())

