# verificador_idade.py

# Verificador de Idade 🧓👦👨

Este é um programa simples feito em Python que classifica uma pessoa de acordo com a idade informada.

## 🚀 Funcionalidades

- Pede o nome e a idade do usuário
- Valida se a idade é um número positivo
- Classifica o usuário como:
  - Criança (menos de 12 anos)
  - Adolescente (12 a 17 anos)
  - Adulto (18 a 59 anos)
  - Idoso (60 anos ou mais)
- Identifica e informa se a idade for negativa

## 🧠 Conceitos aplicados

- Funções com parâmetros (`def`)
- Estruturas condicionais (`if`, `elif`, `else`)
- Validação com laço `while` e `.isdigit()`
- Formatação de strings com `f-strings`
- Entrada de dados com `input()`

## 🖥️ Como executar o projeto

1. Certifique-se de ter o [Python](https://www.python.org/) instalado.
2. Baixe ou clone o repositório:

```bash
git clone https://github.com/danns006/verificador_idade.git
cd verificador_idade
python verificador_idade.py
```

```bash
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

if __name__ == "__main__":
    main()
```
