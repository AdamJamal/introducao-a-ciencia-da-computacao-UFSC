test_number = int(input("digite o numero:"))

res = str(test_number) == str(test_number)[::-1]
if res==True: 
    print ("Palíndromo") 
if res==False:
    print ("Não palíndromo")    
