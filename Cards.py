"""
Exercises from chapter 18 on Inheritence
Building classes for playing cards and decks
"""

import random

class Card:
    """represents a standard playing card"""

    suit_names = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
    # using none so ranks map to indexes
    rank_names = [None, 'Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']

    def __init__(self, suit=0, rank=2):
        self.suit  = suit
        self.rank = rank

    def __str__(self):
        return f'{Card.rank_names[self.rank]} of {Card.suit_names[self.suit]}'
    
    def __lt__(self, other):
        # arbitrarily ranking suits
        card1 = self.suit, self.rank
        card2 = other.suit, other.rank
        return card1 < card2
    
class Deck:
    """represents a collection of cards"""

    # populate cards with a standard card deck
    def __init__(self) -> None:
        self.cards = []
        for suit in range(4):
            for rank in range(1,14):
                card = Card(suit, rank)
                self.cards.append(card)
    
    def __str__(self) -> str:
        res = []
        for card in self.cards:
            res.append(str(card))
        return '\n'.join(res)
    
    def pop_card(self):
        return self.cards.pop()
    
    def add_card(self, card):
        return self.cards.append(card)
    
    def shuffle(self):
        return random.shuffle(self.cards)
    
    def sort(self):
        return self.cards.sort()
    
    def move_cards(self, hand, num):
        for i in range(num):
            hand.add_card(self.pop_card())

    def deal_hands(self, n_hands, cards_per_hand):
        hands = []
        for i in range(n_hands):
            hand = Hand('hand' + str(i))
            self.move_cards(hand, cards_per_hand)
            hands.append(hand)
        return hands
    
class Hand(Deck):
    """Represents a hand of playing cards"""

    def __init__(self, label='') -> None:
        self.cards = []
        self.label = label
    
if __name__ == '__main__':
    queen_of_diamonds = Card(1,12)
    print(queen_of_diamonds)

    print('create a deck')
    deck = Deck()
    print(deck)

    print('after a shuffle')
    deck.shuffle()
    print(deck)

    print('deal 4 hands of 5 cards')
    hands = deck.deal_hands(4, 5)
    for hand in hands:
        print(f'contents of {hand.label}')
        print(hand)
        print('\n')

    print(deck)

