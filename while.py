# crie um programa que receba 5 numeros, realize a soma mas caso um numero for negativo ele deve ser desconsiderado  
soma_num = 0
numeros_lidos = 0

while (numeros_lidos < 5):
  num_lido = float(input("digite um numero: "))
  if num_lido >= 0:   # não permite que numeros  negativos entre na operação
    soma_num += num_lido
  numeros_lidos += 1
  
print("a soma é %.2f" % (soma_num))
