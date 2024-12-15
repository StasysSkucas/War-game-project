import random

class Card:
    def __init__(self,  rank: int, suit: int):
        self.rank = rank
        self.suit = suit

    def __str__(self):
        face_cards = {11: "🤴", 12: "👸", 13: "🫅 ", 14: "🅰️ "}
        suits = {0:" ♠", 1:" ♥", 2:" ♦", 3:" ♣"}
        if self.rank in face_cards:
            return face_cards[self.rank] + suits[self.suit]
        return str(self.rank) + suits[self.suit]
    
    def __gt__(self, other):
        return self.rank > other.rank
    
    def __eq__(self, other):
        return self.rank == other.rank


def create_deck():
    deck = []
    for suit in range(4):
        for rank in range(2, 15):
            deck.append(Card(rank, suit))
    return deck
            
    
def draw_card(deck):
    return deck.pop()


def add_cards_to_winner(winner_deck, p1Card, p2Card):
    winner_deck.append(p1Card)
    winner_deck.append(p2Card)


def main():
    deck = create_deck()
    random.shuffle(deck)
    player_1_deck = deck[:26]
    player_2_deck = deck[26:]
    while True:
        input("Press Enter to draw cards...") 
        
        player_1_card =draw_card(player_1_deck)
        player_2_card =draw_card(player_2_deck)
        print( str(len(player_1_deck))+"🟥  "+str(player_1_card) + " vs " + (str(player_2_card)) +"  "+str(len(player_2_deck))+"🟦")
        
        if player_1_card > player_2_card:
            print("      hand won by 🟥")
            add_cards_to_winner(player_1_deck, player_1_card, player_2_card)
        elif player_1_card < player_2_card:
            print("      hand won by 🟦")
            add_cards_to_winner(player_2_deck,  player_1_card, player_2_card)
        else:
            print("            TIE")           
            # implement tie logic
                          
        
        if (len(player_1_deck)==0):
            print("Player 2 wins the game!")
            break
        elif (len(player_2_deck)==0):
            print("Player 1 wins the game!")
            break
        
        

  
    

main()


