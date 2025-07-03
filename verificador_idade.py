# Verificador de idade 

def classificar_idade(nome, idade):
    if idade < 0:
        print("Idade inválida. Ainda não nasceu 😤")
    elif idade < 12:
        print(f"{nome} tem {idade} anos e é uma criança.")
    elif 12 <= idade <= 17:
        print(f"{nome} tem {idade} anos e é um adolescente.")
    elif 18 <= idade <= 59:
        print(f"{nome} tem {idade} anos e é um adulto.")
    else:
        print(f"{nome} tem {idade} anos e é um idoso.")


while True:
    nome = input("Digite seu nome: ")
    idade_input = input("Digite sua idade: ")

    if idade_input.isdigit():
        idade = int(idade_input)
        break
    else:
        print("Idade inválida. Digite apenas números positivos.")

classificar_idade(nome, idade)
