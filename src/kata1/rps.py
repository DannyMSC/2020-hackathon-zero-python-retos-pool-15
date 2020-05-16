from random import randint

options = ["Piedra", "Papel", "Tijeras"]

# El resultado de salida son las siguientes String
#'Empate!'
#'Ganaste!'
#'Perdiste!'
def quienGana(player, ai):

    player = player.lower()
    ai=ai.lower()

    if ai == player:
        result = "Empate!"
    elif player == options[0].lower() and ai == options[2].lower():
        result = "Ganaste!"
    elif player == options[0].lower() and ai == options[1].lower():
        result = "Perdiste!"
    elif player == options[1].lower() and ai == options[0].lower():
        result = "Ganaste!"
    elif player == options[1].lower() and ai == options[2].lower():
        result = "Perdiste!"
    elif player == options[2].lower() and ai == options[1].lower():
        result = "Ganaste!"
    elif player == options[2].lower() and ai == options[0].lower():
        result = "Perdiste!"
    

    return result

# Entry Point
def Game():
    #
    #
    
    #
    #
    
    winner = quienGana(player, ai)

    print(winner)

