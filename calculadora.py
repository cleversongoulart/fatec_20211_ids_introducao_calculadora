a=int(input("Digite o primeiro inteiro: "))
b=int(input("Digite o segundo inteiro: "))
operacao=input("Escolha a operação: (+) soma ou (-) subtração. Digite o símbolo da operação escolhida: ")
if(operacao=='+'):
    resultado=a+b
elif(operacao=='-'):
    resultado=a-b
else:
    print("Operação inválida")
print(resultado) 