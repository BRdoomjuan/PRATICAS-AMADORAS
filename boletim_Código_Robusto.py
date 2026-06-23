def ler_notas (mensagem):
    while True:
        try:
            return float(input(mensagem))
        except ValueError:
            print("ERRO: Digite uma nota válida!")

def media_parcial(ap1, ap2):

    media_calculada = ap1 + ap2

    if media_calculada < 8:
        return "Aluno reprovado!"
    elif media_calculada < 16:
        return "P.F. necessária."
    else:
        return "Aluno aprovado!" 

while True:
    print("-" * 30)
    print("Boletim Digital")

    print("-" * 30)
    aluno = input("Digite o nome do aluno: ").upper()

    nota_ap1 = ler_notas(f"\nAP1 de {aluno}: ")
    nota_ap2 = ler_notas(f"AP2 de {aluno}: ")

    media = (media_parcial(nota_ap1, nota_ap2))
    situacao_aluno = print(f"\n{media}")

    nota_pf_necesssaria = 18 - (nota_ap1+nota_ap2)
    
    if media == "P.F. necessária.":
        print(f"Precisa de {nota_pf_necesssaria:.2f} na P.F.")
    else:
        print("Sem P.F.")

    with open("BOLETIM_DA_TURMA.txt","a", encoding="utf-8") as arquivo:
        arquivo.write(f"{aluno} | AP1: {nota_ap1} | AP2: {nota_ap2} | {media} | Precisa de: {nota_pf_necesssaria}\n")
    
    print("-" * 30)
    continuar = input("Continuar? (S/N): ").strip().lower()
    if continuar in ["não", "n", "negativo", "parar", "fechar", "encerrar"]:
        print("-" * 30)
        print("Obrigado pelo uso!")
        break