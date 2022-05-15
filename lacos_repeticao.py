# #iniciando laco do zero
# for x in range(10):
#     print(x)
#
# #iniciando do 2 até o 10
# for x in range(2,11):
#     print(x)


#verificando numero primo
# div = 0
# a = int(input("Digite um numero: "))
# for x in range(1, a+1):
#     resto = a % x
#     if(resto == 0):
#         div = div + 1
#
# if(div == 2):
#     print(f"o numero {a} é primo")
# else:
#     print(f"o numero {a} não é primo")

# for num in range(1,101):
#     div = 0
#     for x in range(1, num + 1):
#         resto = num % x
#         if(resto == 0):
#             div += 1
#     if(div == 2):
#         print(num)

# a = 0
# while(a <= 10):
#     print(a)
#     a += 1

nota = int(input("entre com a nota: "))
while(nota > 10):
    nota = int(input("entre com a nota: "))
print(nota)