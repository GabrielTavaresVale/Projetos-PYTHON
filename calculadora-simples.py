n1= int(input("Digite o primeiro valor"))
n2= int(input("Digite o Segundo Valor"))

operacao= input("Informe a Operação desejada + Soma - Subtracao *- Multiplicacao /- Divisao")
if(operacao=='+'):
    soma= n1+n2
    print("O Resultado e", soma)

elif (operacao== '-'):
    subtracao= n1-n2
    print("O resultado e", subtracao)
elif (operacao== '*'):
    multiplicaao= n1*n2
    print("O resultado e ", multiplicaao)
elif (operacao== '/'):
    divisao= n1/n2
    print("O resultado e", divisao)

