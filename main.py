#Python básico

#usuario entra com os numeros
a = int(input("digite o primeiro numero: "))
b = int(input("digite o segundo numero: "))

#operações
soma = a + b
subtracao = a - b
multiplicacao = a * b
divisao = a / b
resto = a % b

#tipos das variáveis / convertendo variáveis
print(type(soma))
soma = str(soma)
print(type(soma))
print(soma)

x = '1'
soma2 = int(x) + 1
print(soma2)

#imprimindo
print(soma, subtracao, multiplicacao, divisao, resto)
print('\n')
print("soma: {}\nmultiplicacao: {}\nsubtracao: {}\ndivisao: {}\nresto: {} \n"
      .format(soma, multiplicacao, subtracao, divisao, resto))
print("soma: {soma}".format(soma=soma))
print(f'soma: {soma}')


