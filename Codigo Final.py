def trabalho_de_matematica():
    #codigo do Math Summative work

    #comeco do codigo
    lingua = str(input("Write 'English' to set the language as English or 'Portuguese to set the language as Portuguese: (if you want to understand the code 'Help') "))

    #funcoes de repeticao de codigo
    def novamente_ou_nao():
        #perguntando se quer executar o codigo outra vez ou nao
        if lingua == "Portuguese" or lingua == "portuguese" or lingua == "portugues":
            outra_vez = str(input("Deseja reiniciar o codigo ou encerrar ele?\n"))

            if outra_vez == "reiniciar":
                trabalho_de_matematica()

            elif outra_vez == "encerrar":
                print("Servico encerrado!")

            else:
                print("Comando nao encontrado!")

    def novamente_ou_nao_ingles():
        #perguntando se quer executar o codigo outra vez ou nao (Ingles)
        if lingua == "English" or lingua == "english" or lingua =="ingles":
            outra_vez = str(input("Do you want to 'reset' the code or 'end' the code??\n"))

            if outra_vez == "reset":
                trabalho_de_matematica()

            elif outra_vez == "end":
                print("Service ended!")

            else:
                print("Command not found!")
    
    #codigo em portugues
    def Portuguese():
        #comecando o codigo
        print("Bem vindo ao programa de precos LZ! Por gentileza responda as seguintes perguntas com precisao: \n")

        #precos do ticket unico com cartao de credito/debito
        tickets_unicos_cartao_zona_1 = 3.10
        tickets_unicos_cartao_zona_2 = 4.45
        tickets_unicos_cartao_soma = tickets_unicos_cartao_zona_1 + tickets_unicos_cartao_zona_2

        #precos do ticket unico com cartao compass
        tickets_unicos_compass_zona_1 = 2.50
        tickets_unicos_compass_zona_2 = 3.65
        tickets_unicos_compass_soma = tickets_unicos_compass_zona_1 + tickets_unicos_compass_zona_2

        #precos dia todo
        tickets_dia_todas_as_zonas = 11

        #precos passe mensal
        tickets_mes_zona_1 = 102.55
        tickets_mes_zona_2 = 137.10
        tickets_mes_soma = tickets_mes_zona_1 + tickets_mes_zona_2

        #variaveis do codigo
        dias = 31
        feriados = 0
        dias_doente = 0

        #Feriados / finais de semana
        feriados = int(input("Por gentileza digite apenas o numero de dias que serao feriados e finais de semana: "))
        dias_doente = int(input("Digite quantos dias da semana voce podera ficar doente: "))
        dias_sem_aula = feriados + dias_doente
        dias = dias - dias_sem_aula

        #calculos de preco:
        preco_mensal_ticket_unico_cartao = "{:.2f}".format((tickets_unicos_cartao_soma * dias)*2)

        preco_mensal_ticket_unico_compass = "{:.2f}".format((tickets_unicos_compass_soma * dias)*2)

        preco_mensal_ticket_dia_todas_as_zonas = "{:.2f}".format(tickets_dia_todas_as_zonas * dias)

        preco_mensal_ticket_mes = "{:.2f}".format(tickets_mes_soma)

        #enviando os arquivos para a tela de resposta
        print("---------------------------------------------------------------")
        print("O valor do ticket unico com cartao de credito ou debito sera um total de ${} por mes \n".format(preco_mensal_ticket_unico_cartao))
        print("O valor do ticket unico com o cartao compass sera um total de ${}por mes \n".format(preco_mensal_ticket_unico_compass))
        print("O valor do ticket 'All Day' sera um total de ${} por mes \n".format(preco_mensal_ticket_dia_todas_as_zonas))
        print("O valor do ticket mensal das duas zonas no periodo de um mes sera de ${}\n".format(preco_mensal_ticket_mes))
        print("Obrigado por usar o sistema LZ! Volte sempre.")
        novamente_ou_nao()

    #codigo em ingles
    def English():

        #comecando o codigo
        print("Welcome to LZ's services! Please, answer the questions below with precision: \n")
        
        #precos do ticket unico com cartao de credito/debito
        tickets_unicos_cartao_zona_1 = 3.10
        tickets_unicos_cartao_zona_2 = 4.45
        tickets_unicos_cartao_soma = tickets_unicos_cartao_zona_1 + tickets_unicos_cartao_zona_2

        #precos do ticket unico com cartao compass
        tickets_unicos_compass_zona_1 = 2.50
        tickets_unicos_compass_zona_2 = 3.65
        tickets_unicos_compass_soma = tickets_unicos_compass_zona_1 + tickets_unicos_compass_zona_2

        #precos dia todo
        tickets_dia_todas_as_zonas = 11

        #precos passe mensal
        tickets_mes_zona_1 = 102.55
        tickets_mes_zona_2 = 137.10
        tickets_mes_soma = tickets_mes_zona_1 + tickets_mes_zona_2

        #variaveis do codigo
        dias = 31
        feriados = 0
        dias_doente = 0

        #Feriados / finais de semana
        feriados = int(input("Please, type the numbers of days that you won't use the transport: (It includes Weekends and Holidays only!) \n"))
        dias_doente = int(input("Please, type the numbers of days that you think are necessary for any problem:  \n"))
        dias_sem_aula = feriados + dias_doente
        dias = dias - dias_sem_aula

        #calculos de preco:
        preco_mensal_ticket_unico_cartao = "{:.2f}".format((tickets_unicos_cartao_soma * dias)*2)

        preco_mensal_ticket_unico_compass = "{:.2f}".format((tickets_unicos_compass_soma * dias)*2)

        preco_mensal_ticket_dia_todas_as_zonas = "{:.2f}".format(tickets_dia_todas_as_zonas * dias)

        preco_mensal_ticket_mes = "{:.2f}".format(tickets_mes_soma)

        #enviando os arquivos para a tela de resposta
        print("---------------------------------------------------------------")
        print("If you choose to buy the single ticket for zone '1' and '2', and pay with credit/debit card, the price per month would be ${}\n".format(preco_mensal_ticket_unico_cartao))
        print("If you choose to buy the single ticket for zone '1' and '2', and pay with the compass card, the price per month would be ${}\n".format(preco_mensal_ticket_unico_compass))
        print("If you choose to buy the 'All Day' ticket, the price per month would be {}\n".format(preco_mensal_ticket_dia_todas_as_zonas))
        print("If you choose to buy the whole month ticket, the price would be ${}\n".format(preco_mensal_ticket_mes))
        print("Thank you for using LZ's services. We'll wait for you!")
        novamente_ou_nao_ingles()


    #Variaveis de help
    help_portuguese=[
        "Este codigo foi criado com o intuito de responder as questoes do trabalho de matematica!"
        "O codigo basicamente tem os valores dos tickets armazenados e quando voce informa o numero de dias sem uso (Feriados/ doente/ etc..), ele executa os calculos e informa os valores"
    ]
    help_english=[
        "This code were created to answer the questions from Ms.Lee's problem"
        "The code basically already have the tickets' prices and when you inform the number of days that you won't use the transport (hollidays, sick, problems...), it only does some basic math calcs and shows the anser"
    ]


    #selecionando lingua
    if lingua == "Portuguese" or lingua == "portuguese" or lingua == "portugues":
        print("Idioma selecionado como 'Portugues'! \n \n \n")
        Portuguese()

    elif lingua == "English" or lingua == "english" or lingua =="ingles":
        print("Language setted 'English'!  \n \n \n")
        English()

    elif lingua == "Help":
        lingua_help = str(input("Choose between 'English' and 'Portuguese': "))

        if lingua_help == "portuguese" or lingua_help == "Portuguese":
            print(help_portuguese)
            help_reset = str(input("Voce deseja reiniciar o codigo? "))

            if help_reset == "sim" or help_reset == "Sim":
                trabalho_de_matematica()

            else:
                print("Programa encerrado!")

        else:
            print(help_english,"\n")
            help_reset = str(input("Do you want to restart the code? "))
            
            if help_reset == "yes" or help_reset == "Yes":
                trabalho_de_matematica()
            
            else:
                print("Service ended!")

    else:
        print("Comando nao encontrado! / Command not found!")
        trabalho_de_matematica()
            
trabalho_de_matematica()