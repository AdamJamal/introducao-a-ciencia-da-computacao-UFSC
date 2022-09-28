#Faça um programa em Python que leia 3 valores correspondentes aos lados de um triângulo e escreva True se o triângulo 
##formado por esses 3 lados é equilátero; False caso contrário. Note que o programa não deve escrever nada além disso.
###Na leitura, também não deverá ser escrito textos pedindo para o usuário digitar os lados, tipo "Entre com o lado 1".

lado1 = float(input(""))
lado2 = float(input(""))
lado3 = float(input(""))

if lado1 == lado2 == lado3:
    print("True")
else:
    print("False")
