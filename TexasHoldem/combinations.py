def find_pairs(cards):
    pairs = []
    numbers_list = []

    for card in cards:
        try:
            numbers_list.append(int(card[0]))

        except ValueError:
            if card[0] == "A":
                numbers_list.append(1)
            elif card[0] == "J":
                numbers_list.append(10)
            elif card[0] == "Q":
                numbers_list.append(11)
            elif card[0] == "K":
                numbers_list.append(12)

    for num in numbers_list:
        amount = numbers_list.count(num)

        if amount == 2 and num not in pairs:
            pairs.append(num)

    hand_combination = []

    for card in cards:
        try:
            if int(card[0]) in pairs:
                hand_combination.append(card)

        except ValueError:
            if card[0] == "A":
                if 1 in pairs:
                    hand_combination.append(card)

            elif card[0] == "J":
                if 10 in pairs:
                    hand_combination.append(card)

            elif card[0] == "Q":
                if 11 in pairs:
                    hand_combination.append(card)

            elif card[0] == "K":
                if 12 in pairs:
                    hand_combination.append(card)

    if 0 < len(hand_combination) < 3:
        return True, False

    elif len(hand_combination) > 2:
        return False, True

    else:
        return False, False


def find_three_of_a_kind(cards):
    triplets = []

    numbers_list = []

    for card in cards:
        try:
            numbers_list.append(int(card[0]))

        except ValueError:
            if card[0] == "A":
                numbers_list.append(1)
            elif card[0] == "J":
                numbers_list.append(10)
            elif card[0] == "Q":
                numbers_list.append(11)
            elif card[0] == "K":
                numbers_list.append(12)

    for num in numbers_list:
        amount = numbers_list.count(num)

        if amount == 3 and num not in triplets:
            return  True

    return  False


def find_poker(cards):
    poker = []

    numbers_list = []

    for card in cards:
        try:
            numbers_list.append(int(card[0]))

        except ValueError:
            if card[0] == "A":
                numbers_list.append(1)
            elif card[0] == "J":
                numbers_list.append(10)
            elif card[0] == "Q":
                numbers_list.append(11)
            elif card[0] == "K":
                numbers_list.append(12)

    for num in numbers_list:
        amount = numbers_list.count(num)

        if amount == 4 and num not in poker:
            return True

    return False


def find_color(cards):
    cards_color= []
    colors = []

    for card in cards:
        cards_color.append(card[1])

    for color in cards_color:
        if cards_color.count(color) == 5 and color not in colors:
            return True

    return False


def check_straight_color(straight_list, cards):
    hand_combination = []

    royal_flush = False

    for card in cards:
        try:
            if int(card[0]) in straight_list:
                hand_combination.append(card)

        except ValueError:
            if card[0] == "A":
                if 1 in straight_list:
                    hand_combination.append(card)

            elif card[0] == "J":
                if 10 in straight_list:
                    hand_combination.append(card)

            elif card[0] == "Q":
                if 11 in straight_list:
                    hand_combination.append(card)

            elif card[0] == "K":
                royal_flush = True

                if 12 in straight_list:
                    hand_combination.append(card)

    cards_color= []
    colors = []

    print(hand_combination)

    for card in hand_combination:
        cards_color.append(card[1])

    for color in cards_color:
        if cards_color.count(color) == 5 and color not in colors:
            return True, royal_flush

    return False, False



def find_straight(cards):

    numbers_list = []
    straight = False
    straight_color = False
    royal_flush = False

    for card in cards:
        try:
            numbers_list.append(int(card[0]))

        except ValueError:
            if card[0] == "A":
                numbers_list.append(1)
            elif card[0] == "J":
                numbers_list.append(10)
            elif card[0] == "Q":
                numbers_list.append(11)
            elif card[0] == "K":
                numbers_list.append(12)

    numbers_list = sorted(numbers_list)
    contador = 1

    straight_list = [numbers_list[0]]

    for i in range(1, len(numbers_list)):
        if numbers_list[i] == numbers_list[i - 1] + 1:
            contador += 1

            straight_list.append(numbers_list[i])

            if contador >= 5:
                straight = True
        else:
            contador = 1



    if straight:
        straight_color, royal_flush = check_straight_color(straight_list, cards)

        print(royal_flush)

        return straight, straight_color, royal_flush


    return straight, straight_color, royal_flush
