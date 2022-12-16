#!/usr/bin/env python3

print("Cálculo da media das notas.")

Total = 0 #define uma variável "Total" e atribui o valor Zero a ela

Contador = 0  #define uma variável "Contador" e atribui o valor Zero a ela
    

while Contador <= 10:            # cria um loop em wile para um somador de notas
    num = int(input("Digite uma nota: "))  #recebe um imput das notas para as contas
    Total = num + Total
    Contador = Contador + 1
    
Nota = Total / 10    
print(Nota)
