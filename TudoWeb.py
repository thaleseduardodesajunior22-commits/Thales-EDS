excelente = 0
bom = 0
ruim = 0

for i in range(1, 11):
    print(f"\nEntrevistado {i}")
    
    nome = input("Digite o nome: ")
    escolha_idade = True
    while escolha_idade:
        idade = input("Digite a idade: ")
        try:
            idade = int(idade)
            if idade <= 0:
                print("Por favor, insira um valor válido")
                continue
            if idade > 130:
                print("Por favor, insira um valor válido")
                continue
            break
        except ValueError:
            print("Por favor, insira um valor válido")
            continue
    
    print("Opinião sobre o atendimento:")
    print("1 - EXCELENTE")
    print("2 - BOM")
    print("3 - RUIM")
    
    opiniao = int(input("Digite a opção (1/2/3): "))
    
    
    if opiniao == 1:
        excelente += 1
    elif opiniao == 2:
        bom += 1
    elif opiniao == 3:
        ruim += 1
    else:
        print("Por favor, insira um valor válido")

print("\nRESULTADO DA PESQUISA")
print(f"Quantidade de respostas EXCELENTE: {excelente}")
print(f"Quantidade de respostas BOAS: {bom}")
print(f"Quantidade de respostas RUIM: {ruim}")