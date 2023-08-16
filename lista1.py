'''
Exercícios sobre os comandos básicos em python
'''

#1. Faça um programa que imprima o seu nome.
def q01():
    print('João Paulo Delgado Preti')

#2. Faça um programa que imprima o produto dos valores 30 e 27.

#3. Faça um programa que imprima a média aritmética entre os números 5, 8, 12.

#4. Faça um programa que leia e imprima um número inteiro.

#5. Faça um programa que leia dois números reais e os imprima.
def q05():
    num1 = float(input('Digite um número: '))
    num2 = float(input('Digite um outro número: '))
    print(f'Número 1: {num1}')
    print(f'Número 2: {num2}')

#6. Faça um programa que leia um número inteiro e imprima o seu
#   antecessor e o seu sucessor.
def q06():
    num = int(input('Digite um número: '))
    print(f'Sucessor de {num} = {num+1}')
    print(f'Antecessor de {num} = {num-1}')
  
#7. Faça um programa que leia o nome o endereço e o telefone de
#   um cliente e ao final, imprima esses dados.

#8. Faça um programa que leia dois números inteiros e imprima a
#   subtração deles.

#9. Faça um programa que leia um número real e imprima ¼ deste número.
def q09():
    num = float(input('Digite um número: '))
    print(f'Resultado: {num/4}')

#10. Faça um programa que leia três números reais e calcule a
#    média aritmética destes números. Ao final, o programa deve
#    imprimir o resultado do cálculo.
def q10():
    num1 = float(input('Digite o 1 número: '))
    num2 = float(input('Digite o 2 número: '))
    num3 = float(input('Digite o 3 número: '))
    media = (num1+num2+num3)/3
    print(f'Média: {media}')

#11. Faça um programa que leia dois números reais e calcule as
#    quatro operações básicas entre estes dois números, adição,
#    subtração,multiplicação e divisão. Ao final, o programa
#    deve imprimir os resultados dos cálculos.

#12. Faça um programa que leia um número real e calcule o
#    quadrado deste número. Ao final, o programa deve
#    imprimir o resultado do cálculo.

#13. Faça um programa que leia o saldo de uma conta poupança e
#    imprima o novo saldo, considerando um reajuste de 2%.
def q13():
    saldo = float(input('Saldo R$: '))
    print(f'Saldo com reajuste de 2% = R$ {saldo*1.02}')

#14. Faça um programa que leia a base e a altura de um retângulo
#    e imprima o perímetro (base + altura) e a área (base * altura).

#15. Faça um programa que leia o valor de um produto, o percentual
#    do desconto desejado e imprima o valor do desconto e o valor
#    do produto subtraindo o desconto.
def q15():
    valor_produto = float(input('Valor do Produto: R$ '))
    perc_desconto = float(input('% do desconto: '))
    valor_desconto = valor_produto * perc_desconto/100
    print(f'Desconto: R$ {valor_desconto}')
    print(f'Valor final do produto: R$ {valor_produto-valor_desconto}')

#16. Faça um programa que calcule o reajuste do salário de um
#    funcionário. Para isso, o programa deverá ler o salário atual
#    do funcionário e ler o percentual de reajuste. Ao final imprimir
#    o valor do novo salário.

#17. Faça um programa que calcule a conversão entre graus centígrados
#    e Fahrenheit. Para isso, leia o valor em centígrados e calcule
#    com base na fórmula a seguir. Após calcular o programa deve
#    imprimir o resultado da conversão.
#    F = (9 x C + 160) / 5

#18. Faça um programa que calcule a quantidade de litros de combustível
#    consumidos em uma viagem, sabendo-se que o carro tem autonomia de
#    12 km por litro de combustível. O programa deverá ler o tempo
#    decorrido na viagem e a velocidade média e aplicar as fórmulas:
#    D = T x V       L = D / 12
#    Em que:
#    • D = Distância percorrida em horas
#    • T = Tempo
#    • V = Velocidade média
#    • L = Litros de combustível consumidos
#    Ao final, o programa deverá imprimir a distância percorrida e a
#    quantidade de litros consumidos na viagem.

#19. Faça um programa que calcule o valor de uma prestação em atraso.
#    Para isso, o programa deve ler o valor da prestação vencida, a
#    taxa periódica de juros e o período de atraso. Ao final, o
#    programa deve imprimir o valor da prestação atrasada, o período
#    de atraso, os juros que serão cobrados pelo período de atraso, o
#    valor da prestação acrescido dos juros. Considere juros simples.

#20. Faça um programa que efetue a apresentação do valor da conversão
#    em real (R$) de um valor lido em dólar (US$). Para isso, será
#    necessário também ler o valor da cotação do dólar.

q15()
