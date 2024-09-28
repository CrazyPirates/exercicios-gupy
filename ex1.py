numero = int(input("Digite um número e veja se ele está na sequência de Fibonacci: "))

t1, t2 = 0, 1
retorno = 0

while t1 <= numero:
    if t1 == numero:
        retorno = 1
    t1, t2 = t2, t1 + t2    

if retorno == 1:
    print(f"O número {numero} ESTÁ na sequência!") 
else:
    print(f"O número {numero} NÃO ESTÁ na sequência...")           