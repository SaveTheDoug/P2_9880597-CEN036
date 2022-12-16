#!/usr/bin/env python3

print("Cálculo da media das notas.")

Total = 0 #define uma variável "Total" e atribui o valor Zero a ela

Contador = 0  #define uma variável "Contador" e atribui o valor Zero a ela
    

while Contador <= 10:            # cria um loop em wile para um somador de notas, PORÉM EXISTE UM ERRO, DEVIA SER APENAS "CONTADOR < 10" E NÃO "CONTADOR<=10"
    num = int(input("Digite uma nota: "))  #recebe um imput das notas para as contas
    Total = num + Total   #soma o número digitado a variável "total"
    Contador = Contador + 1  #adiciona um ao contador para continuar
    
Nota = Total / 10      #define a variável nota
print(Nota)        #exibe a nota

