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
            return "Está na sequência\n"

        else:
            return "Não está na sequência\n"
        
    except ValueError:
        return "Entrada Inválida\n"
    
def verificar_palavra():
    palavra = input('Digite uma palavra:')

    if 'a' in palavra.lower():
        quantidade = palavra.count('a')
        return f"\nA letra a existe na palavra {palavra}\nQuantidade de vezes que a letra a se repete: {palavra.count('a')}"
       
    else:
        return f"\nA letra a não aparece na palavra {palavra}"
    
    
print("Questão 1 - Fibonacci")
print(Fibonacci())

print("Questão 2 - Teste String")
print(verificar_palavra())



