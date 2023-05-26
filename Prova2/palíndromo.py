testa_palavra = str(input(""))

res = str(testa_palavra) == str(testa_palavra)[::-1]
if res==True: 
    print ("Palíndroma") 
if res==False:
    print ("Não palíndroma") 
