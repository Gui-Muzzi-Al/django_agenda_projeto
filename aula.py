name = input("Qual é o seu nome? ")
idade = int(input("Qual é a sua idade? "))
peso = float(input("Qual é o seu peso? "))
altura = float(input("Qual é a sua altura? "))
ano_nascimento = 2023 - idade
print(f"Olá {name}, você tem {idade} anos, pesa {peso} kg e mede {altura} m.")
print(f"Seu ano de nascimento é {ano_nascimento}.")
print(f"Seu IMC é {peso / (altura ** 2):.2f}.")
