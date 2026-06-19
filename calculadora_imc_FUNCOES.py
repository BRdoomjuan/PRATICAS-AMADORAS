# função para classificar meus diferentes resultados de IMC e devolver para o código principal
def classificacao(imc_classificar):
    if imc_classificar <= 18.4:
        return "abaixo do peso"
    elif 18.4 <= imc_classificar <= 24.4:
        return "peso ideal"
    else:
        return "sobrepeso"

# código principal usando while
while True:
    peso = float(input("digite seu peso: "))
    altura = float(input("digite sua altura: "))

    denominador = altura**2
    imc = peso/denominador

    print(f"seu imc é: {imc:.3f}")

    classificado = classificacao(imc) # ponte de retorno da função inicial com o bloco principak
    print(f"sua situação: {classificado}") # exibição dos resultados depois da inserção de valores e filtragem da função
    
    continuar = input("deseja continuar?\n").strip().lower()

    if continuar in ["não", "nao", "n", "negativo", "não quero", "parar", "sair"]: # lista de possíveis respostas negativas
        print("Obrigado pelo uso!")
        break # fim do loop caso uma das respostas listadas seja inserida