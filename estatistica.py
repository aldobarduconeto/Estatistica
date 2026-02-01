# estatistica.py
# Função para achar o menor valor em uma lista
def acharMenor(valores):
    menor = min(valores)
    return menor
# Função para achar o maior valor em uma lista
def acharMaior(a):
    maior = max(a)
    return maior
# Função para calcular a média dos valores em uma lista: Feito usando um laço 
# para contabilizar todos valores e somando o valor atual com os outros. Depois 
# que se tem a soma de todos os valores do array, é dividido pelo total de valores.
def calcularMedia(valores):
    soma = sum(valores)
    media = soma / len(valores)
    return media
# Função para calcular a mediana dos valores em uma lista: Esse metodo primeiro verifica
# se o tamanho do array é par ou impar usando um if. Depois de identificado se é par ou 
# impar, o metodo pega o(s) valor(es) no meio do array.
def calcularMediana(valores):
    n = len(valores)
    meio = n // 2
    if n % 2 == 0:
        mediana = (valores[meio - 1] + valores[meio]) / 2
    else:
        mediana = valores[meio]
    return mediana
# Função para calcular o desvio padrão dos valores em uma lista: Feito usando
# um for para passar por todos os valores do array, subtraindo ele com a media,
# depois elevando o resultado da subtração ao quadrado com a função pow da lib
# Math. Depois adciona os valores em uma variavel chamada 'soma'. No fim, é calculado
# de todos os valores do array, é dividido a soma dos valores calculados no for e é 
# dividido pelo tamanho do array e então é tirado a raiz quadrada com a função sqrt da lib Math.
def calcularDesvioPadrao(valores):
    media = calcularMedia(valores)
    soma = 0
    tamanho = len(valores)
    for valor in valores:
        im = valor - media
        a = im ** 2
        soma += a
    d = soma/tamanho
    desvio_padrao = d ** 0.5
    return desvio_padrao