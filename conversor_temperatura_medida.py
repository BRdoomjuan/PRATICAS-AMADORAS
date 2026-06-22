# função para converter valores numéricamente
def converter_temperatura (valor, origem, destino):
    if origem == 1 and destino == 2:
        return valor * 1.8 + 32
    elif origem == 1 and destino == 3:
        return valor + 273.15
    elif origem == 2 and destino == 1:
        return (valor - 32) / 1.8
    elif origem == 2 and destino == 3:
        return ((valor - 32) / 1.8) + 273.15
    elif origem == 3 and destino == 1:
        return valor - 273.15
    elif origem == 3 and destino == 2:
        return (valor - 273.15) * 1.8 + 32
    else:
        return valor

# loop do código principal
while True:

    print("Olá!\nBem vindo ao Conversor de Temperaturas\n")

    # menu e inserção de valor e tratamento de erros
    try:
        # menu de opções
        medida_origem = int(input("Qual medida você tem em mãos? 1-Celsius | 2-Fahrenheit | 3-Kelvin:\n"))
        medida_destino = int(input("Qual medida você deseja obter? 1-Celsius | 2-Fahrenheit | 3-Kelvin:\n"))

        # inserção de valor
        valor_user = float(input("Qual o valor numérico de sua temperatura?\n"))

        # tratamento de erros
    except ValueError:
        print("Digite uma opção válida!\n")
        continue # volta para o início

    # exibição da resposta após a filtragem da função
    resposta = converter_temperatura(valor_user, medida_origem, medida_destino) # atribuição de valores nos parâmetros da função
    print(f"resposta: {resposta:.2f}")

    # continuação do loop
    continuar = input("deseja continuar?\n").strip().lower()
    if continuar in ["não", "nao", "n", "negativo", "não quero", "parar", "sair"]: # lista com possíveis respostas negativas
        print("Obrigado pelo uso!")
        break # fecha o loop