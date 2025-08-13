# informações iniciais 

print("Caculadora MD")
print("Vou te ajudar, vamos começar")

nome = input("Qual o seu nome? ")
print("Olá ", nome)

# Solicita os números e o operador

n1 = input("Digite o primeiro número: ")
operador = input("Digite o símbolo de operação (+, -, *, /, %): ")
n2 = input("Digite o segundo número: ")

# Converter strings em inteiros

num1 = float(n1)
num2 = float(n2)

# Executa a operação com base no operador

if operador == '+':
  resultado = num1 + num2
elif operador == '-':
  resultado = num1 - num2
elif operador == '*':
  resultado = num1 * num2
elif operador == '/':
  if num2 != 0:
    resultado = num1 / num2
  else:
    resultado = "Erro: Divisão por zero!"
elif operador == '%':
  if num2 != 0:
    resultado1 = num1 * num2
    resultado = resultado1  / 100
  else:
    resultado = "Erro: Módulo por zero!"
else:
    resultado = "Erro: Operador inválido!"

# Executa de resultado final 

print(nome,"Resultado:", resultado)
