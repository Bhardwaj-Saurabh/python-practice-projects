import random 

cards = [11, 10, 10, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(cards)

result = False

dealer_cards = list()
player_cards = list()

pick_dealer_card = random.choice(cards)
pick_player_card = random.choice(cards)

print(f"Dealer's Card is {pick_dealer_card}")
print(f"Player's Card is {pick_player_card}")

dealer_cards.append(pick_dealer_card)
player_cards.append(pick_player_card)

while not result:
    user_choice = input("'Hit' or 'Show': ").lower()

    if user_choice == 'show':
        total_dealer_card =  sum(dealer_cards) 
        if total_dealer_card <= 16:
            pick_dealer_card = random.choice(cards)
            dealer_cards.append(pick_dealer_card)
        
        if 11 in dealer_cards and total_dealer_card > 21:
            total_dealer_card -= 10

        total_player_card = sum(player_cards)
        if  total_player_card > total_dealer_card:
            print('Player win')
        elif total_player_card == total_dealer_card:
            print('Draw')
        else:
            print('Dealer Win')
        result = True
    
    if user_choice == 'hit':
        pick_dealer_card = random.choice(cards)
        pick_player_card = random.choice(cards)
        print(f"Player's Card is {pick_player_card}")
        dealer_cards.append(pick_dealer_card)
        player_cards.append(pick_player_card)

        total_player_card =  sum(player_cards) 
        if 11 in player_cards and total_player_card > 21:
            total_player_card -= 10
        
        if total_player_card > 21:            
            print('Opps! You are Busted.') 
            result = True



        








