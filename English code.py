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