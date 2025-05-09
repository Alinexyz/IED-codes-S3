import os # Importa o módulo "os" para verificar a existência de arquivos no sistema

tarefas = []            # Lista principal de tarefas (espaço para armazenar as tarefas)
historico = []          # Pilha para desfazer tarefas (onde elas irão ser armazazenadas)
fila_execucao = []      # Fila para executar tarefas (a ordem em que as tarefas serão mostradas)
ARQUIVO = "tarefas.txt" # Nome do arquivo onde as tarefas serão salvas e carregadas

def salvar_em_arquivo():     # Salva todas as tarefas da lista 'tarefas' no arquivo .txt
    with open(ARQUIVO, "w") as f:   # Abre o arquivo no modo escrita ("w"), apagando o conteúdo anterior
        for t in tarefas:   # Percorre cada tarefa
            linha = f"{t['titulo']}|{t['prioridade']}|{t['data']}\n"    # Monta uma linha com os dados da tarefa
            f.write(linha)  # Escreve a linha no arquivo

def carregar_do_arquivo():      # Carrega tarefas do arquivo para a lista e fila
    if os.path.exists(ARQUIVO): # Verifica se o arquivo existe
        with open(ARQUIVO, "ler") as f:    # Abre o arquivo no modo leitura ("ler")
            for linha in f: # Lê o arquivo linha por linha
                partes = linha.strip().split("|")    # Remove espaços/quebra de linha e separa os dados
                if len(partes) == 3:     # Garante que há 3 partes: título, prioridade e data
                    tarefa = {"titulo": partes[0], "prioridade": partes[1], "data": partes[2]}   # Cria a tarefa
                    tarefas.append(tarefa)  # Adiciona à lista principal
                    fila_execucao.append(tarefa)     # Adiciona à fila de execução


def adicionar_tarefa(titulo, prioridade, data): # Cria uma tarefa com título, prioridade e data
    tarefa = {
        "titulo": titulo, # Título da tarefa
        "prioridade": prioridade,  # Prioridade da tarefa (Alta, Média, Baixa)
        "data": data # Data de vencimento da tarefa
    }
    tarefas.append(tarefa)   # Adiciona a tarefa à lista principal
    tarefas.append(tarefa)  # Adiciona a tarefa ao histórico (para desfazer)
    historico.append(tarefa)    # Adiciona a tarefa à fila de execução
    fila_execucao.append(tarefa)    # Adiciona a tarefa à fila de execução
    salvar_em_arquivo()    # Salva as alterações no arquivo
    print(f"Tarefa '{titulo}' adicionada com prioridade {prioridade} e data {data}!\n")  # Confirmação ao usuário

def desfazer_ultima_tarefa():   # Função para desfazer a última tarefa adicionada
    if historico:   # Verifica se há alguma tarefa no histórico
        ultima = historico.pop()    # Remove a última tarefa adicionada ao histórico (estilo pilha)
        tarefas.remove(ultima)  # Remove essa tarefa da lista principal
        fila_execucao.remove(ultima)    # Remove essa tarefa da fila de execução
        salvar_em_arquivo() # Atualiza o arquivo
        print(f"Tarefa '{ultima}' desfeita!\n")  # Informa que a tarefa foi desfeita
    else:
        print("Nenhuma tarefa para desfazer.\n")

def atender_tarefa():   # Função para atender a tarefa (remoção da fila de execução)
    if fila_execucao:   # Se o histórico estiver vazio
        feita = fila_execucao.pop(0)    # Remove a primeira tarefa da fila (modo FIFO)
        tarefas.remove(feita)    # Remove a tarefa da lista principal
        salvar_em_arquivo() # Atualiza o arquivo
        print(f"Tarefa '{feita}' atendida!\n")  # Informa qual tarefa foi atendida
    else:
        print("Nenhuma tarefa para atender.\n") # Se a fila estiver vazia

def mostrar_tarefas():  # Função para mostrar todas as tarefas
    print("\n📋 Lista de Tarefas:") # Título da listagem
    if not tarefas: # Se a lista de tarefas estiver vazia
        print("Nenhuma tarefa cadastrada.\n")     # Informa que não há tarefas
    else:
        for i, t in enumerate(tarefas):  # Percorre todas as tarefas com índice
            print(f"{i + 1}. Tarefa: {t['titulo']}, Prioridade: {t['prioridade']}, Data: {t['data']}")  # Mostra os dados de cada tarefa
    print() # Linha em branco para melhorar a leitura

carregar_do_arquivo()   # Carrega tarefas do arquivo no início

while True:  # Laço principal que mantém o programa rodando até que o usuário escolha sair
    print("1. Adicionar Tarefa")  # Mostra a opção 1 no menu
    print("2. Desfazer Última Tarefa")  # Mostra a opção 2 no menu
    print("3. Atender Tarefa (modo fila)")  # Mostra a opção 3 no menu
    print("4. Mostrar Tarefas")  # Mostra a opção 4 no menu
    print("5. Sair")  # Mostra a opção 5 no menu


    opcao = input("Escolha uma opção: ")    # Lê a opção escolhida pelo usuário

    if opcao == '1':  # Se a opção for 1, adiciona uma nova tarefa
        titulo = input("Digite o título da tarefa: ")  # Lê o título da tarefa
        prioridade = input("Prioridade (Alta, Média, Baixa): ")  # Lê a prioridade
        data = input("Data de vencimento (DD/MM/AAAA): ")  # Lê a data de vencimento
        adicionar_tarefa(titulo, prioridade, data)  # Chama a função para adicionar a tarefa
    elif opcao == '2':  # Se a opção for 2, desfaz a última tarefa
        desfazer_ultima_tarefa()  # Chama a função de desfazer
    elif opcao == '3':  # Se a opção for 3, atende (remove) a próxima tarefa da fila
        atender_tarefa()  # Chama a função de atender tarefa
    elif opcao == '4':  # Se a opção for 4, mostra todas as tarefas
        mostrar_tarefas()  # Chama a função de mostrar tarefas
    elif opcao == '5':  # Se a opção for 5, sai do programa
        print("Saindo do programa...")  # Informa que o programa vai encerrar
        break  # Interrompe o laço infinito e encerra o programa
    else:  # Se a opção não for válida (não está entre 1 e 5)
        print("Opção inválida!\n")  # Informa que a opção é inválida