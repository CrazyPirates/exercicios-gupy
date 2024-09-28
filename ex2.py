string = input("Digite uma palavra aqui: ")

string = string.lower()
qtde_de_a = 0


for a in string:
    if a == "a":
        qtde_de_a += 1

if qtde_de_a > 0:
    print(f"Sua palavra ou frase tem a letra A! Mais especificamente, ela tem {qtde_de_a} A(s).")
else:
    print(f"Sua palavra ou frase não tem nenhuma letra A...")    
