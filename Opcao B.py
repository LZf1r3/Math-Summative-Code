#Codigo da opcao B
def Opcao_B():

#importando bibliotecas 
    import random

#variaveis de preco 
    dias_sem_ms_melnicky = random.randint(1,10)
#precos do ticket unico com cartao de credito/debito
    tickets_unicos_cartao_zona_1 = 3.10

#precos do ticket unico com cartao compass
    tickets_unicos_compass_zona_1 = 2.50

#precos dia todo
    tickets_dia_todas_as_zonas = 11

#precos passe mensal
    tickets_mes_zona_1 = 102.55

###############################################################################################################################

#comeco do codigo
    print("Bem vindo aos sistemas LZ, port gentileza responda as proximas questoes com precisao")

#Feriados / finais de semana 
    dias = 31
    feriados = int(input("Por gentileza digite apenas o numero de dias que serao feriados e finais de semana: "))
    dias_doente = int(input("Digite quantos dias da semana voce podera ficar doente: "))
    dias_sem_aula = feriados + dias_doente + dias_sem_ms_melnicky
    dias = dias - dias_sem_aula 

#variaveis de precos mensais
    preco_mensal_ticket_cartao = (tickets_unicos_cartao_zona_1 * dias)*2
    preco_mensal_ticket_compass = (tickets_unicos_compass_zona_1 * dias)*2
    preco_mensal_todo_o_dia = tickets_dia_todas_as_zonas * dias
    preco_mensal_mes = tickets_mes_zona_1 

#problema com ms melnicky
    
    #calculo ms melnicky
    preco_mensal_final_cartao = preco_mensal_ticket_cartao + (15.1 * dias_sem_ms_melnicky)
    preco_mensal_final_compass = preco_mensal_ticket_compass + (15.1 * dias_sem_ms_melnicky)
    preco_mensal_final_dia_todo = preco_mensal_todo_o_dia + (8.9 * dias_sem_ms_melnicky)
    preco_mensal_final_mes = preco_mensal_mes + (8.9 * dias_sem_ms_melnicky)
#final do codigo
    
    print("Dias sem carona = {}".format(dias_sem_ms_melnicky))
    print("preco da primeira opcao e de ${:.2f}".format(preco_mensal_final_cartao))
    print("preco da segunda opcao e de ${:.2f}".format(preco_mensal_final_compass))
    print("preco da terceira opcao e de ${:.2f}".format(preco_mensal_final_dia_todo))
    print("preco da quarta opcao e de ${:.2f}".format(preco_mensal_final_mes))

Opcao_B()