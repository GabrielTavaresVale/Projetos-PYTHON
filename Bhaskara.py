##Biblioteca para raiz quadrada
import math

## O usuario do digita os valores de a,b,c
a= float(input('Informe o valor de a'))
print ("O valor de a=",a)

b= float(input('Informe o valor de b'))
print("O valor de b=",b)

c= float(input('Informe o valor de c'))
print("O valor de c",c)
## calculo do delta
delta= (b**2)-4*a*c
print("Delta=",delta)
if(delta<0):
    print("não existem raizes reais de delta")
else:##formula do calculo do x1 e x2
        x1= -b + math.sqrt(delta)/(2*a)
        
        x2= -b - math.sqrt(delta) /(2*a)
        ##resultado
        print("x1: {}, x2: {}".format(x1, x2))


        

