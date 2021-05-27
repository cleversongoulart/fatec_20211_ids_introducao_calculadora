a=int(input("Digite o primeiro inteiro: "))
b=int(input("Digite o segundo inteiro: "))
operacao=input("Escolha a operação:\n (+) soma\n (-) subtração\n (*) multiplicação\n (/) divisão\n (**) exponenciação \n Digite o símbolo da operação escolhida:  ")
if(operacao=='+'):
    resultado=a+b
elif(operacao=='-'):
    resultado=a-b
elif(operacao=='*'):
    resultado=a*b
elif(operacao=='/'):
    resultado=a//b
elif(operacao=='**'):
    resultado=a**b
else:
    print("Operação inválida")
print(resultado) 