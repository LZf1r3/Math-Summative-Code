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
    print("O valor do ticket unico com cartao de credito ou debito no periodo de um mes sera de $\n{}".format(preco_mensal_ticket_unico_cartao))
    print("O valor do ticket unico com o cartao compass no periodo de um mes sera de ${}\n".format(preco_mensal_ticket_unico_compass))
    print("O valor do ticket 'All Day' no periodo de um mes sera de ${}\n".format(preco_mensal_ticket_dia_todas_as_zonas))
    print("O valor do ticket mensal das duas zonas no periodo de um mes sera de ${}\n".format(preco_mensal_ticket_mes))
    print("Obrigado por usar o sistema LZ! Volte sempre.")