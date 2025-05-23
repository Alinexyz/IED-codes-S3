usuarios = []
pessoa = {}
dadostransporte = {}

def mostrarusuarios    ():
    for item in usuarios:
        i = 0
        i = i + 1
        print(f"{i}.   {usuarios[i - 1]}")

def adicionarusuario():
    pessoa["nome"] = input("Digite o seu nome: ").capitalize()
    pessoa["idade"] = int(input("Digite a sua idade: "))
    pessoa["cidade"] = input("Digite a sua cidade: ").capitalize() 
    pessoa["possuiTransporte"] = input("Você possui um meio de transporte? (Sim / Não) ").lower()
      
    if pessoa["possuiTransporte"] == "sim":
          dadostransporte["Tipo"] = input("Qual o tipo de transporte? ").capitalize()
          dadostransporte["Propriedade"] = input("Você possui, aluga ou é cedido? "). capitalize()
          dadostransporte["Modelo"] = input("Por favor, digite o modelo do seu transporte: "). capitalize()
          dadostransporte["Placa"] = input("Por favor, digite a placa do seu transporte: "). capitalize()
          dadostransporte["Cor"] = input("Por favor, digite a cor do seu transporte: "). capitalize()
          
          pessoa["dadostransporte"] = dadostransporte

          usuarios.append(f'Nome: {pessoa["nome"]}, Idade: {pessoa["idade"]}, Cidade: {pessoa["cidade"]}, Tem transporte: {pessoa["possuiTransporte"]}, Sobre o transporte: {pessoa ["dadostransporte"]}')
          print("Informações de usuário salvas com sucesso!")

    else:
        usuarios.append(f'Nome: {pessoa["nome"]}, Idade: {pessoa["idade"]} Cidade: {pessoa["cidade"]}, Tem transporte: {pessoa["possuiTransporte"]}')

        print("Informações de usuário salvas com sucesso!")
   
   
while True:  
    print('---------------------------')
    print('🎀༘⋆      Menu       🎀༘⋆')
    print()
    print('   1. Adicionar usuário    ')
    print('   2. Deletar usuário      ')
    print('   3. Ver usuários         ')
    print('   4. Sair do programa     ')
    print('---------------------------')

    option = int(input("Selecione uma opção acima: "))

    match option:
        case 1:
            adicionarusuario()
        
        case 2:

            mostrarusuarios()

            index = int(input("Qual dos acima deseja deletar?(Escolha por índice)"))
            usuarios.pop(index - 1)

            
            print("Processo concluído!")
            
            
        case 3:
            mostrarusuarios()

        case 4:
            print("Saindo...")
            break

        case _:
            print("Opção inválida")
