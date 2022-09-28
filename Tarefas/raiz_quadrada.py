i=0
t=1000
for j in range(0,t+1):   # range from 1 to t
    while(i<=((j//2)+1)):
        if(i**2==j):
            print(j)
        i+=1    
    i=0
