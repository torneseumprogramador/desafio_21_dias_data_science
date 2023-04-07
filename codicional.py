idade = int(input("Digite aqui sua idade:\n"))

if idade > 63:
    print("Parabéns você foi um guerreiro(a) e merece ter sua aposentadoria")
elif (idade >= 41) and (idade <= 63):
    print("Você está entre a idade final da cadeia produtiva")
elif idade >= 31 and idade <= 40:
    print("Você é um adulto")
elif idade >= 18 and idade <= 30:
    print("Você é maior de idade.")
elif idade >= 16:
    print("Você é adolescente.")
elif idade == 13:
    print("Você está mudando de fase.")
else:
    print("Você é criança.")

"""

>= # maior igual
<= # menor igual
> # maior
< # menor
== # igual

or # ou
and # e
not # negar

"""