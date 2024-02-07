import p1_random as p1

rng = p1.P1Random()

cardNames = {
    1: "ACE",
    11: "JACK",
    12: "QUEEN",
    13: "KING",
    2: "2",
    3: "3",
    4: "4",
    5: "5",
    6: "6",
    7: "7",
    8: "8",
    9: "9",
    10: "10",
}

print("START GAME #1\n")

winsTotal = 0
dealerWIns = 0
tied = 0
gamesFinal = 0

while True:
    cardValue = rng.next_int(13) + 1
    if cardValue >= 11:
        hand = 10
    else:
        hand = cardValue

    print(f"Your card is a {cardNames[cardValue]}!")
    print(f"Your hand is: {hand}\n")
    print("1. Get another card")
    print("2. Hold hand")
    print("3. Print statistics")
    print("4. Exit\n")

    while True:
        menuChoice = int(input("Choose an option: "))
        print()
        if menuChoice == 4:
            break
        elif menuChoice == 1:
            if hand < 21:
                cardToAdd = rng.next_int(13) + 1
                if cardToAdd >= 11:
                    hand += 10
                else:
                    hand += cardToAdd
                print(f"Your card is a {cardNames[cardToAdd]}!")
                print("Your hand is:", hand)
                print()
                if hand > 21:
                    print("You exceeded 21! You lose.")
                    print()
                    print("START GAME #6")
                    dealerWIns += 1
                    gamesFinal += 1
                    break
                if hand == 21:
                    print("BLACKJACK! You win!")
                    winsTotal += 1
                    gamesFinal += 1
                    print()
                    print("START GAME #3")
                    break
        elif menuChoice == 2:
            dealerHand = rng.next_int(11) + 16
            if dealerHand > hand and dealerHand > 21:
                print(f"Dealer's hand: {dealerHand}")
                print(f"Your hand is: {hand}")
                print()
                print("You win!")
                print()
                winsTotal += 1
                gamesFinal += 1
                print("START GAME #2")
                break
            if hand > dealerHand:
                print(f"Dealer's hand: {dealerHand}")
                print(f"Your hand is: {hand}\n")
                print("You Win!")
                winsTotal += 1
                gamesFinal += 1
            if dealerHand > hand:
                print(f"Dealer's hand: {dealerHand}")
                print(f"Your hand is: {hand}\n")
                print("Dealer wins!")
                print()
                dealerWIns += 1
                gamesFinal += 1
                print("START GAME #5")
                print()
                cardValue = rng.next_int(13) + 1
                if cardValue >= 11:
                    hand = 10
                else:
                    hand = cardValue
                print(f"Your card is a {cardNames[cardValue]}!")
                print(f"Your hand is: {hand}\n")
            if hand == dealerHand:
                print(f"Dealer's hand: {dealerHand}")
                print(f"Your hand is: {hand}\n")
                print("It's a tie! No one wins!")
                print()
                tied += 1
                gamesFinal += 1
                print("START GAME #4")
                print()
                cardValue = rng.next_int(13) + 1
                if cardValue >= 11:
                    hand = 10
                else:
                    hand = cardValue
                print(f"Your card is a {cardNames[cardValue]}!")
                print(f"Your hand is: {hand}\n")
        elif menuChoice == 3:
            print("Number of Player wins:", winsTotal)
            print("Number of Dealer wins:", dealerWIns)
            print("Number of tie games:", tied)
            print("Total # of games played is:", gamesFinal)
            if gamesFinal > 0:
                print(
                    "Percentage of Player wins:",
                    f"{round((winsTotal / gamesFinal) * 100, 2)}%",
                )
                print()
        else:
            print("Invalid input!\nPlease enter an integer value between 1 and 4.")
            print()

        print("1. Get another card")
        print("2. Hold hand")
        print("3. Print statistics")
        print("4. Exit\n")

    if menuChoice == 4:
        break

    print()
