Calculadora Simples em Python com Script de Execução
Este repositório contém um script Python para uma calculadora básica e um script de shell (.sh) 
para automatizar a instalação de dependências e a execução do programa.

Passo a Passo da Criação e Execução
Abaixo estão os comandos utilizados no terminal para criar e executar os arquivos.

1. Criação do Script de Execução (etapa.sh)

  O comando 
  nano etapa.sh foi usado para abrir o editor de texto nano e criar o arquivo de script.
  
  Bash:
  #!/bin/bash
  echo "inciado o Script"
  sudo apt update
  sudo apt install python3
  python3 /home/felipe/modulo1/python/calculadora.py

  CTRL + X e depois Y foram usados para salvar e fechar o arquivo. 

2. Concessão de Permissão de Execução para o Script O comando 
  chmod 355 etapa.sh foi utilizado para dar permissão de execução ao arquivo. 

4. Execução do Script Principal
  Para rodar o script, o comando ./etapa.sh foi executado.

5. Concessão de Permissão de Execução para a Calculadora
  O comando chmod 355 calculadora.py foi utilizado para dar permissão de execução ao arquivo.

6. Execução Direta do Script Python
Por fim, o comando python3 calculadora.py foi usado para executar o programa da calculadora diretamente. 

Como Executar o Arquivo .sh
Para executar o script etapa.sh, que automatiza todo o processo, siga os passos abaixo:

1. Abra o seu terminal.

2. Navegue até o diretório onde o arquivo etapa.sh está salvo.

3. Dê a permissão de execução para o arquivo. Você só precisa fazer isso uma vez.

   Bash: chmod 355 etapa.sh

4. Execute o script:
   Bash: ./etapa.sh

5. O script irá solicitar a sua senha de administrador (
   [sudo] password:) para poder atualizar os pacotes do sistema e instalar o Python 3.
   Após a instalação, ele executará o script da calculadora automaticamente.


Explicação do Código Python (calculadora.py)
O script calculadora.py é um programa simples que realiza operações matemáticas básicas 
com base na entrada do usuário.

1. Informações Iniciais e Saudação

  O programa começa imprimindo uma mensagem de boas-vindas e em seguida solicita o nome do usuário. 

  Python:
  print("Caculadora MD")
  print("Vou te ajudar, vamos começar")
  nome = input("Qual o seu nome? ")
  print("Olá ", nome)


2. Solicitação dos Números e Operador

  O programa pede ao usuário para digitar dois números e o símbolo da operação desejada (+, -, *, /, %). 

  Python:
  n1 = input("Digite o primeiro número: ")
  operador = input("Digite o símbolo de operação (+, -, *, /, %): ") [cite: 2]
  n2 = input("Digite o segundo número: ") [cite: 2]

3. Conversão de Tipos de Dados
  Os números recebidos pela função input() são do tipo texto (string).
  Para realizar cálculos, eles são convertidos para o tipo numérico 

  float (números com casas decimais). 

  Python:
  num1 = float(n1)
  num2 = float(n2)

4. Lógica das Operações
   O programa utiliza uma estrutura de 
   if/elif/else para verificar qual operador foi digitado pelo usuário e realizar a operação correspondente.

   Soma (+), Subtração (-) e Multiplicação (*): Realiza o cálculo diretamente.

   Divisão (/): Antes de dividir, o código verifica se o segundo número (num2) é diferente de zero
   para evitar um erro.Se for zero, armazena uma mensagem de erro.

   Porcentagem (%): O cálculo (num1 * num2) / 100 é realizado para encontrar a porcentagem. Também
   inclui uma verificação para evitar o módulo por zero.

   Operador Inválido: Se o símbolo digitado não corresponder a nenhum dos operadores válidos,
   uma mensagem de erro é definida.

   Python:
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
    resultado = "Erro: Divisão por zero!" [cite: 3]
elif operador == '%':
  if num2 != 0:
    resultado1 = num1 * num2
    resultado = resultado1  / 100
  else:
    resultado = "Erro: Módulo por zero!" [cite: 3]
else:
    resultado = "Erro: Operador inválido!" [cite: 4]

6. Exibição do Resultado Final

  Ao final, o programa exibe o nome do usuário junto com o resultado da operação ou a mensagem de erro correspondente.
  
  Python:
  print(nome,"Resultado:", resultado)

  

