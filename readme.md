# Blackjack

A very simple Blackjack game program in the console/terminal. Uses a random module to generate numbers.

## Breakdown

I used a "while True" statement for the main game, and defined some variables above. I also appeneded values to an array to find the average statistic.

```python
while True:
        menuChoice = int(input("Choose an option: "))
        print()
        if menuChoice == 4:
            break
        elif menuChoice == 1:
            if hand < 21:
                cardToAdd = rng.next_int(13) + 1 # using the random module
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
# menu choice two
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
                # etc for each choice
# menu choice three
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
```

On selection three, I used the array values to help calculate the wins and percentage statistic.

```python
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

winsTotal = 0
dealerWIns = 0
tied = 0
gamesFinal = 0

# calculations

 print("Number of Player wins:", winsTotal)
            print("Number of Dealer wins:", dealerWIns)
            print("Number of tie games:", tied)
            print("Total # of games played is:", gamesFinal)
            if gamesFinal > 0:
                print(
                    "Percentage of Player wins:",
                    f"{round((winsTotal / gamesFinal) * 100, 2)}%",

```

Sample Output

```python
START GAME #1

Your card is a 5!
Your hand is: 5

1. Get another card
2. Hold hand
3. Print statistics
4. Exit

Choose an option: 1

Your card is a 8!
Your hand is: 13

1. Get another card
2. Hold hand
3. Print statistics
4. Exit

Choose an option: 1

Your card is a 2!
Your hand is: 15

1. Get another card
2. Hold hand
3. Print statistics
4. Exit

Choose an option: 1

Your card is a ACE!
Your hand is: 16

1. Get another card
2. Hold hand
3. Print statistics
4. Exit

Choose an option: 2

Dealer's hand: 24
Your hand is: 16

You win!
```
