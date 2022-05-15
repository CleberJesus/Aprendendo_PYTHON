# a = int(input("digite o primeiro valor: "))
# b = int(input("digite o segundo valor: "))
# c = int(input("digite o terceiro valor: "))
#
# if(a > b and a > c):
#     print(f"o maior numero é {a}")
# elif(b > a and b > c):
#     print(f"o maior numero é {b}")
# else:
#     print(f"o maior numero é {c}")
#
# d = int(input("digite o quarto valor: "))
# e = int(input("digite o quinto valor: "))
# resto_d = d % 2
# resto_e = e % 2
# if(resto_d == 0 or resto_e == 0):
#     print("foi digitado um numero par")
#     if(resto_d == 0):
#         print(f"o numero {d} é par")
#     if(resto_e == 0):
#         print(f"o numero {e} é par")
# else:
#     print("nenhum numero par foi digitado")

#calcular media
nota_1 = int(input("Digite a primeira nota: "))
if(nota_1 > 10):
    nota_1 = int(input("Nota inválida! digite novamente: "))
nota_2 = int(input("Digite a segunda nota: "))
if(nota_2 > 10):
    nota_2 = int(input("Nota inválida! digite novamente: "))

media = (nota_1 + nota_2) / 2
if( media < 6):
    print("Aluno reprovado! ")
else:
    print("Aluno Aprovado!")



