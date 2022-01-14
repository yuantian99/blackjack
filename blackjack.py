#simple blackjack game
#rules
#draw cards until you get as close to 21 as possible
#dealer draws cards if their score is 16 or under
#17 and above, the dealer must stand
#if player has a higher score than dealer, the player wins
#if player gets over 21, the player loses

import random
score = 0
dealer_score = 0
aces = 0

draw = input("Draw another card? (enter 'y' to continue): ")

while draw == 'y' or draw == "Y":
    card = random.randint(1, 10)
    print("You drew a", card)
    score += card
    if card == 1:
        while True:
            ace = input("You drew an Ace (enter 1 or 11): ")
            try:
                ace = int(ace)
            except ValueError:
                print("Enter a valid number")
                continue
            if ace == 1 or ace == 11:
                score += ace
                break
    print("Your current score is", score)
    draw = input("Draw another card? (enter 'y' to continue): ")

while dealer_score <= 16 and score <= 21:

    dealer_card = random.randint(1, 10)

    if dealer_card == 1:
        print("Dealer drew an Ace")
        aces += 1
        dealer_score += 1
    else:
        print("Dealer drew a", dealer_card)
        dealer_score += dealer_card

    if aces > 0 and dealer_score <= 11:
        dealer_score += 10

    if dealer_score > 16:
        break

    print("Dealer's current score is", dealer_score)

print("Dealer's final score is", dealer_score)
print("Your final score is", score)

if score < dealer_score and dealer_score <= 21:
    print("You lose")
elif score > 21:
    print("You lose")
elif score == dealer_score:
    print("Tie game")
else:
    print("You win!")
