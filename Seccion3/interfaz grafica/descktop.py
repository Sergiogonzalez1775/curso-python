import PySimpleGUI as sg

PLAYER_ONE = "X"
PLAYER_TWO = "O"


def gen_layout(button_size):
    layout = [[sg.Button("", key = "-0-", size = button_size),
               sg.Button("", key = "-1-", size = button_size),
               sg.Button("", key = "-2-", size = button_size)],

              [sg.Button("", key = "-3-", size = button_size),
               sg.Button("", key = "-4-", size = button_size),
               sg.Button("", key = "-5-", size = button_size)],

              [sg.Button("", key = "-6-", size = button_size),
               sg.Button("", key = "-7-", size = button_size),
               sg.Button("", key = "-8-", size = button_size)],

              [sg.Text("", key = "-WINNER-")],

              [sg.Button("Exit", key = "-OK-"),
               sg.Button("Restar", key = "-RESTART-")]]

    return layout


def restart_game(window):
    deck = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    for i in range(0, 9):
        element = "-"+str(i)+"-"
        window.Element(element).Update(text="")
    window.Element("-WINNER-").Update(value="")
    return deck


def update_button(current_player, event, window):
    window.Element(event).Update(text=current_player)


def change_player(current_player):
    if current_player == PLAYER_ONE:
        current_player = PLAYER_TWO
    else:
        current_player = PLAYER_ONE
    return current_player


def check_end_game(deck, window):
    if 0 not in deck:
        window.Element("-WINNER-").Update(value="El juego ha terminado en empate!!!")
        return True


def check_winner(winner_plays, deck, window):
    for winner_play in winner_plays:
        if deck[winner_play[0]] == deck[winner_play[1]] == deck[winner_play[2]] != 0:
            if deck[winner_play[0]] == PLAYER_ONE:
                window.Element("-WINNER-").Update(value="Ha ganado el jugador 1!!!")
                return True
            else:
                window.Element("-WINNER-").Update(value="Ha ganado el jugador 2!!!")
                return True


def main():
    current_player = PLAYER_ONE
    game_end = False
    winner = False

    button_size = (7, 3)

    winner_plays = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
    deck = [0, 0, 0, 0, 0, 0, 0, 0, 0]

    layout = gen_layout(button_size)
    window = sg.Window("Demo", layout)

    while True:
        event, value = window.read()

        if event == "-RESTART-":
            deck = restart_game(window)
            game_end = False
            winner = False

        if event == sg.WIN_CLOSED or event == "-OK-":
            break

        if window.Element(event).ButtonText == "" and not game_end and not winner:
            index = int(event.replace("-", ""))
            deck[index] = current_player
            update_button(current_player, event, window)
            winner = check_winner(winner_plays, deck, window)
            game_end = check_end_game(deck, window)
            current_player = change_player(current_player)

    window.close()

if __name__ == "__main__":
    main()

