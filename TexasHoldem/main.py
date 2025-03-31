import os
import random
from combinations import find_pairs, find_straight, find_poker, find_color, find_three_of_a_kind

PICAS = "\u2660"   # ♠
HEARTS = "\u2665" # ♥
DIAMONDS = "\u2666" # ♦
CLOVERS = "\u2663" # ♣

PALOS = [PICAS, HEARTS, DIAMONDS, CLOVERS]

def clear_and_continue():
    input("Enter para continuar...\n\n")
    os.system("clear")

def create_deck():
    deck = []
    for palo in PALOS:
        for i in range(1, 13):
            if i == 1:
                deck.append("A" + palo)
                continue

            if i == 10:
                deck.append("J" + palo)
                continue

            if i == 11:
                deck.append("Q" + palo)
                continue

            if i == 12:
                deck.append("K" + palo)
                continue

            deck.append(str(i) + palo)

    return deck


def remove_cards(cards, deck):

    for card in cards:
        deck.remove(card)

    return deck


def deal_cards(deck):
    player_hand = random.sample(deck, 2)

    cpu_hand = random.sample(deck, 2)

    deck = remove_cards((player_hand + cpu_hand), deck)

    return player_hand, cpu_hand, deck


def deal_table_cards(cards, table_cards, deck):

    deck = remove_cards(cards, deck)

    for card in cards:
        table_cards.append(card)

    return deck, table_cards

def show_cards(player_hand, cpu_hand, table_cards):
    print("Player cards: {}".format(player_hand))
    print("CPU cards: {}".format(cpu_hand))
    print("table cards: {}".format(table_cards))

def cpu_ask():
    if random.sample(range(0, 4), 1) == 0:
        print("La maquina no quiere seguir jugando")
        clear_and_continue()
        raise SystemExit("Partida terminado...")

    else:
        print("La maquina quiere seguir jugando")
        clear_and_continue()


def player_ask():
    play = False

    while not play:
        request = input("¿Quieres seguir jugando? [S/N]")

        if request == "S":
            print("El jugador quiere continuar la partida")
            clear_and_continue()
            play = True

        elif request == "N":
            print("El jugador no quiere continuar la partida")
            raise SystemExit("Partida terminado...")
        else:
            continue


def game(deck, player_hand):

    round = 1

    table_cards = []

    while round < 4:
        print("------RONDA {}------".format(round))

        if round  == 1:
            cards = random.sample(deck, 3)
            deck, table_cards = deal_table_cards(cards, table_cards, deck)
            print("Player cards: {}".format(player_hand))
            print("table cards: {}".format(table_cards))
            clear_and_continue()

        elif round  == 2 or 3:
            cards = random.sample(deck, 1)
            deck, table_cards = deal_table_cards(cards, table_cards, deck)
            print("Player cards: {}".format(player_hand))
            print("table cards: {}".format(table_cards))
            clear_and_continue()

        cpu_ask()
        player_ask()

        round += 1

    return table_cards


def check_hand(hand, table_cards):
    cards = hand + table_cards
    one_pair, two_pair = find_pairs(cards)
    three_of_a_kind = find_three_of_a_kind(cards)
    poker = find_poker(cards)
    flush = find_color(cards)
    straight, straight_color, royal_flush = find_straight(cards)

    if royal_flush:
        return 9

    elif straight_color:
        return 8

    elif poker:
        return 7

    elif three_of_a_kind and one_pair:
        return 6

    elif flush:
        return 5

    elif straight:
        return 4

    elif three_of_a_kind:
        return 3

    elif two_pair:
        return 2

    elif one_pair:
        return 1

    else:
        return 0


def main():
    deck = create_deck()
    clear_and_continue()

    player_hand, cpu_hand, deck = deal_cards(deck)

    print("Player cards: {}".format(player_hand))
    clear_and_continue()

    table_cards = game(deck, player_hand)

    player_points = check_hand(player_hand, table_cards)
    cpu_points = check_hand(cpu_hand, table_cards)

    if player_points > cpu_points:
        print("Has ganado")
        show_cards(player_hand, cpu_hand, table_cards)


    elif player_points < cpu_points:
        print("has perdido")
        show_cards(player_hand, cpu_hand, table_cards)

    else:
        if player_hand[0][0] > player_hand[1][0]:
            player_high_card = player_hand[0]

        else:
            player_high_card = player_hand[1]


        if cpu_hand[0][0] > cpu_hand[1][0]:
            cpu_high_card = cpu_hand[0]

        else:
            cpu_high_card = cpu_hand[1]


        if player_high_card > cpu_high_card:
            print("Has ganado")
            show_cards(player_hand, cpu_hand, table_cards)

        elif player_high_card < cpu_high_card:
            print("Has perdido")
            show_cards(player_hand, cpu_hand, table_cards)


        else:
            print("Has empatado")
            show_cards(player_hand, cpu_hand, table_cards)

if __name__ == "__main__":
    main()
