#DESAFIO DE CODIGO DIO FEITO POR: EDERSON CASSIANO WERMEIER
#PROXIMA ETAPA IREI ABSTRAIR ALGUNS CÓDIGOS REPETIDOS E CRIAR UMA SESSAO ONDE O 
#USUARIO NÃO PRECISE DIGITAR O CPF PARA CADA OPERACAO APENAS NA PRIMEIRA
#E PODERA SAIR DA SESSÃO QUANDO QUISER NAVEGAR PELA CONTA DE OUTRO CPF

#numero de saques permitidos
SAQUES_DIARIOS = 3

#Limite de saque permitido
LIMITE_SAQUE = 500

#Lista de clientes com os dados em dicionarios conforme abaixo
#{CPF: {NOME, ESTADO, CIDADE, RUA, NUMERO}]
clientes = []

#{cpf:{'Conta': numero_conta, 'Agencia': agencia, 'Saldo': 0, 'Saques_efetuados': 0, 'Limite': 500 ,'Extrato': ''}}
contas = []

def menu():
    while True:
        #menu bancario
        menu = input('''
        ###################################
        #   [1] - Cadastro de usuario     #
        #   [2] - Cadastro de conta       #
        #   [3] - Deposito bancário       #
        #   [4] - Saque de valor          #
        #   [5] - Extrato Bancário        #
        #   [6] - Informações da Conta    #
        #   [7] - Editar Dados da conta   #
        #   [8] - SAIR                    #
        ###################################
                     
                DIGITE AQUI: ''')
        #se o valor digitado for digito
        if menu.isdigit():
            #converte para inteiro
            menu = int(menu)

            #Verifica se o numero está nalista de acoes do menu
            if menu in range(1,9):
                return menu
                
            else:
                print(f'''
        {menu} não está na Lista | Tente novamente!''')
            
        else:
            print(f'''\n
            {menu} não é número | Tente novamente!\n''')



#funcao é reutilizada para verificar cpf no cadastro do cliente e na busca do mesmo
def verificar_cpf(cpf):

    if cpf.isdigit():
            
        if len(cpf) == 11:

            #verificando se o cpf esta em algum dicionario da lista de clientes
            if any(cpf in cliente for cliente in clientes):
                return True
            else:
                return False

        else:
            return print("\nCPF precisa ter 11 digitos!\n")
            
    else:
        return print("\nApenas numeros são permitidos!\n")



def cadastrar_cliente():

    while True:
        cpf = input("Digite o CPF com 11 dígitos: ")

        #caso o retorno da funcao verifica cpf é True indica que o CPF já esta na lista
        if verificar_cpf(cpf) is True:
            print("CPF JÁ ESTA CADASTRADO")
            iniciar()
        elif verificar_cpf(cpf) is None:
            print("\nSiga as instruções\n")
        else:
            break
        
    nome = input('Seu nome completo: ')
    idade = input("Sua idade: ")
    estado = input("Estado: ")
    cidade = input("Cidade: ")
    rua = input("Rua: ")
    numero = input("Numero da casa: ")

    

    dicionario = {
                    cpf: {'Nome':nome.title(), 'Idade':idade, 'Estado':estado.upper(), 'Cidade':cidade.title(), 'Rua':rua.title(), 'Numero':numero}
                    }

    clientes.append(dicionario)
    print("\nCliente adicionado com sucesso!\n")

    iniciar()




def buscar_cliente(cpf_procurado, lista=clientes):

    for cliente in lista:
        for cpf, info in cliente.items():
            if cpf == cpf_procurado:

                nome = info.get('Nome')
                idade = info.get('Idade')
                estado = info.get('Estado')
                cidade = info.get('Cidade')
                rua = info.get('Rua')
                numero = info.get('Numero')

                #retorna uma tupla
                return nome, idade, estado, cidade, rua, numero
                
    return None  # Retorna None se o CPF não for encontrado



def buscar_conta(cpf_procurado, lista=contas):

    for conta in lista:
        for cpf, info in conta.items():

            #se o cpf é igual cpf procurado
            if cpf == cpf_procurado:

                #buscar dados da lista contas
                conta = info.get('Conta')
                agencia = info.get('Agencia')
                saldo = info.get('Saldo')
                saques = info.get('Saques_efetuados')
                limite = info.get('Limite')
                extrato = info.get('Extrato')

                #retorna tupla com os dados da conta
                return conta, agencia, saldo, saques, limite, extrato
            
        return None
               


#realizar Saque
def saque(cpf_procurado = '', saque = '', lista=contas):

    for dicionario in lista:
        for cpf, conta in dicionario.items():
            if cpf == cpf_procurado:
        
                conta.get(cpf_procurado)

                saques = conta['Saques_efetuados']
                if saques < SAQUES_DIARIOS:

                    limite = conta['Limite']
                    if saque <= LIMITE_SAQUE: #se valor do saque menor que o limite de saque diario

                        saldo = conta.get('Saldo')
                        if saque <= saldo:

                            #subtraindo valor do saque
                            conta['Saldo'] -= saque

                            #formatação do extrato e o valor do deposito
                            extrato = f'Saque de R$:{saque}\n'

                            #adicionando operacao ao extrato
                            conta['Extrato'] += extrato

                            #aumentando a contagem de saques
                            conta['Saques_efetuados'] += 1

                            #diminuindo o limite diario de valor saque
                            conta['Limite'] -= saque
                            print("Saque finalizado com sucesso!")

                            #voltando ao menu
                            iniciar()

                        else:
                            print(f"Saldo insuficiente para essa operação!\nSaldo R$:{saldo}\n")
                            iniciar()

                    else:
                        print(f"Você está tentando sacar um valor acima do seu limite!\nLimite R$:{limite}\n")
                        iniciar()

                else:
                    print("Você atingiu o numero máximo de saques por dia!\n")
                    iniciar()

            else:
                print("Erro ao procurar o cpf na lista das contas")
                iniciar()



#realizar deposito
def deposito(cpf_procurado,deposito, lista=contas):
    #buscar conta
    #ja foi verificado anteriormente se a conta existe entao nao tem verificação d erro aqui
    for dicionario in lista:
        for cpf, conta in dicionario.items():
            if cpf == cpf_procurado:
               
                conta.get(cpf_procurado)

                #colocar valor do deposito na conta
                conta['Saldo'] += deposito

                #formatação do extrato e o valor do deposito
                extrato = f'Deposito de R$:{deposito}\n'

                #adicionando operacao ao extrato
                conta['Extrato'] += extrato
                iniciar()

            else:
                print("Erro ao procurar o cpf na lista das contas")

                iniciar()


#cadastrar a conta com base no CPF filtrado
def cadastrar_conta(lista_contas = contas):

    cpf = input("Informe o CPF do responsável pela conta: ")
    if verificar_cpf(cpf) is True:
        print("Cliente encontrado | Dados abaixo:\n")

        #envia o cpf e retorna os dados em uma tupla
        cliente, idade, estado, cidade, rua, numero = buscar_cliente(cpf)
        
        #pegamos apenas os dados nome e cidade da tupla para exibir na tela
        print(f"Olá {cliente} adoramos {cidade}! :-)\nVamos abrir sua conta? ")

        continuar = input('sim | nao \nDigite aqui: ')

        if continuar.lower() == 'sim' or continuar.lower() == 's':

            print(f"Estamos abrindo sua conta")
            print("Aguarde...")

            #metodo padrao para criar numero da conta
            #como nao tem funcao excluir conta nao havera problemas com numeros de conta repetidos
            numero_conta = len(lista_contas) + 1
            agencia = '0001'
            limite = 500
            
            #formato que sera enviado a lista
            dados = {cpf:{'Conta': numero_conta, 'Agencia': agencia, 'Saldo': 0, 'Saques_efetuados': 0, 'Limite': limite ,'Extrato': ''}}
            lista_contas.append(dados)

            print(f'''
        Sua conta foi criada {cliente}
        Conta: {numero_conta}
        Agencia: {agencia}
        Limite: R${limite}
''')   
            iniciar()

    #retorna falso se nao encontra o cpf
    elif verificar_cpf(cpf) is False:
        print('Você precisa cadastrar o usuario primeiro ou conferir se digitou o CPF correto!\n')
        iniciar()
    else:
        print("\nTente novamente!\n")
        iniciar()



#se a funcao iniciar recebe algum parametro ele pula o menu e entra na condicional
def iniciar():
    
    opcao = menu()

    if opcao == 1:
        #CADASTRO DE USUARIO
        cadastrar_cliente()

    elif opcao == 2:
        #CADASTRO DE CONTA
        cadastrar_conta()


    elif opcao == 3:
        #DEPOSITO BANCARIO
        while True:
            cpf = input("Qual o CPF do responsável pela conta: ")

            verificar = verificar_cpf(cpf)

            if verificar:
                #buscar os dados do cliente
                cliente, idade, estado, cidade, rua, numero = buscar_cliente(cpf)
                #buscar os dados da conta do cliente
                conta, agencia, saldo, saques, limite, extrato = buscar_conta(cpf)

                #a tupla deve estar trazendo a agencia 0001 e a conta maior que zero
                #se esses dados foram recebidos significa que podemo seguir pois numero da agencia sempre e 0001 e conta sempre maior q zero
                #só uma garantia que os valores retornaram da funcao
                if agencia == '0001' and conta > 0:

                    valor = input(f'''
            Olá {cliente}
            Conta: {conta}
            Agencia: {agencia}

            Seu saldo é de R$:{saldo}
            Quanto deseja depositar?
            R$: ''')
                    if valor.isdigit():
                        valor = int(valor)
                        #chama funcao deposito e envia o cpf e valor a ser depositado
                        deposito(cpf,valor)
                    else:
                        print("Deposito interrompido!\nErro com o valor digitado {valor}")

                    #buscar os dados atualizados do dict
                    conta, agencia, saldo, saques, limite, extrato = buscar_conta(cpf)
                    print(f'''
            Seu saldo atualizado é R$: {saldo}''')

                    iniciar()
                else:
                    print("Esse CPF não está vinculado a nenhuma conta")
                    iniciar()
            else:
                print("Não encontramos o CPF em nossa base de dados")
                iniciar()
            


    elif opcao == 4:
        #SAQUE
        while True:
            cpf = input("Qual o CPF do responsável pela conta: ")

            verificar = verificar_cpf(cpf)

            if verificar:
                #buscar os dados do cliente
                cliente, idade, estado, cidade, rua, numero = buscar_cliente(cpf)
                #buscar os dados da conta do cliente
                conta, agencia, saldo, saques, limite, extrato = buscar_conta(cpf)

                #a tupla deve estar trazendo a agencia 0001 e a conta maior que zero
                #se esses dados foram recebidos significa que podemo seguir pois numero da agencia sempre e 0001 e conta sempre maior q zero
                #só uma garantia que os valores retornaram da funcao
                if agencia == '0001' and conta > 0:

                    valor = input(f'''
            Olá {cliente}
            Conta: {conta}
            Agencia: {agencia}

            Seu saldo é de R$:{saldo}
            Saques hoje: {saques}
            Quanto deseja sacar?
            R$: ''')
                    if valor.isdigit():
                        valor = int(valor)
                        #chama funcao deposito e envia o cpf e valor a ser depositado
                        saque(cpf,valor)
                    else:
                        print("Saque interrompido!\nErro com o valor digitado {valor}")

                    #buscar os dados atualizados do dict
                    conta, agencia, saldo, saques, limite, extrato = buscar_conta(cpf)
                    print(f'''
            Seu saldo atualizado é R$: {saldo}''')

                    iniciar()
                else:
                    print("Esse CPF não está vinculado a nenhuma conta")
                    iniciar()
            else:
                print("Não encontramos o CPF em nossa base de dados")
                iniciar()


    elif opcao == 5:
        cpf = input("Qual o CPF do responsável pela conta: ")

        verificar = verificar_cpf(cpf)

        if verificar:
            #buscar os dados do cliente
            cliente, idade, estado, cidade, rua, numero = buscar_cliente(cpf)
            #buscar os dados da conta do cliente
            conta, agencia, saldo, saques, limite, extrato = buscar_conta(cpf)

            #a tupla deve estar trazendo a agencia 0001 e a conta maior que zero
            #se esses dados foram recebidos significa que podemo seguir
            if agencia == '0001' and conta > 0:

                print(f'''
    EXTRATO DO CLIENTE {cliente}
    Conta: {conta}  Agencia: {agencia}        
    Saldo disponível: R$:{saldo}
    OPERAÇÕES REALIZADAS
    {extrato}
''')

                iniciar()
            else:
                print("Esse CPF não está vinculado a nenhuma conta")
                iniciar()
        else:
            print("Não encontramos o CPF em nossa base de dados")
            iniciar()


    elif opcao == 6:
        #INFORMAÇÕES SOBRE A CONTA

        cpf = input("Qual o CPF do responsável pela conta: ")

        verificar = verificar_cpf(cpf)

        if verificar:
            #buscar os dados do cliente
            cliente, idade, estado, cidade, rua, numero = buscar_cliente(cpf)
            #buscar os dados da conta do cliente
            conta, agencia, saldo, saques, limite, extrato = buscar_conta(cpf)

            #a tupla deve estar trazendo a agencia 0001 e a conta maior que zero
            #se esses dados foram recebidos significa que podemo seguir
            if agencia == '0001' and conta > 0:

                print(f'''
            INFORMAÇÕE DO CLIENTE
            Nome: {cliente}
            CPF: {cpf}
            Idade: {idade}
            Endereço: {estado} - {cidade} - {rua} - {numero}

            INFORMAÇÕES SOBRE CONTAS
            Conta: {conta}
            Agencia: {agencia}
            Saldo: R$:{saldo}
            Limite DI: R$:{limite}''')

                iniciar()
            else:
                print("Esse CPF não está vinculado a nenhuma conta")
                iniciar()
        else:
            print("Não encontramos o CPF em nossa base de dados")
            iniciar()

    elif opcao == 7:
        #EDITAR DADO DA CONTA
        #PODERÁ EDITAR ENDEREÇO
        #PODERÁ SOLICITAR AUMENTO DE LIMITE E O CODIGO IRÁ ANALISAR ALGUNS FATORES PARA LIBERAR OU NAO
        #SERÁ IMPLEMENTADO MAIS A FRENTE
        print("INDISPONÍVEL  |  CONTATE O ADMINISTRADOR")
        pass


    elif opcao == 8:
        #SAIR
        print("Você saiu")



################################################################################################

#Chama a funcao 
iniciar()