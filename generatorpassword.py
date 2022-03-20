#GERADOR DE SENHAS / PASSWORD GENERATOR
import random
minusculas = "abcdefghijklmnopqrstuvwxyz"
maiusculas = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numeros = "0123456789"
simbolos = "[]{}()*%#&/_-@"
tudo = minusculas + maiusculas + numeros + simbolos
tamanho = 16
senha = "".join(random.sample(tudo, tamanho))
print(senha)
