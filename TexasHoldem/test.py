import random
from combinations import  find_pairs, find_three_of_a_kind, find_poker, find_color, find_straight

PICAS = "\u2660"   # ♠
HEARTS = "\u2665" # ♥
DIAMONDS = "\u2666" # ♦
CLOVERS = "\u2663" # ♣

PALOS = [PICAS, HEARTS, DIAMONDS, CLOVERS]


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



deck = create_deck()
hand_1, hand_2, deck = deal_cards(deck)
table_cards = random.sample(deck, 3)

print(["K\u2663","Q\u2663"])
print(["J\u2665","9\u2665","8\u2665"])



points = check_hand(["K\u2663","Q\u2663"], ["J\u2665","9\u2665","8\u2665"])

print("Puntos:" + str(points))




