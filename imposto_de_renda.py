def imposto_renda(n, h, f):
    ir = (((n*h)- (189.59*f))*A - VD)
n = int (input())
h = float (input())
f = int (input())
if(n*h <= 1903.98):
  ir = 0
elif (1903.99 <= (n*h)-(189.59*f) <= 2826.65):
  ir = (((n*h)-(189.59*f))*0.075 - 142.80)
elif (2826.66 <= (n*h)-(189.59*f) <= 3751.05):
  ir = (((n*h)-(189.59*f))*0.15 - 354.80)
elif (3751.06 <= (n*h)-(189.59*f) <= 4664.68):
  ir = (((n*h)-(189.59*f))*0.225 - 636.13)
else:
  ir = (((n*h)-(189.59*f))*0.275 - 869.36)
ir_formatado = "{:.2f}".format(ir) 
print(ir_formatado)
