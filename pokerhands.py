"""
Adapted PokerHand for exercise 18-3

Think Python, 2nd Edition
by Allen Downey
http://thinkpython2.com

Copyright 2015 Allen Downey

License: http://creativecommons.org/licenses/by/4.0/
"""

from __future__ import print_function, division

from Cards import Hand, Deck

class PokerHand(Hand):
    """Represents a poker hand."""

    all_labels = ['straight_flush', 'four_of_a_kind', 'full_house', 'flush', 'straight',
                  'three_of_a_kind', 'two_pair', 'pair']

    def suit_hist(self):
        """Builds a histogram of the suits that appear in the hand.
        Stores the result in attribute suits.
        """
        self.suits = {}
        for card in self.cards:
            self.suits[card.suit] = self.suits.get(card.suit, 0) + 1
    
    def rank_hist(self):
        """Builds a histogram of the ranks that appear in the hand.
        Stores the result in attribute suits.
        """
        self.ranks = {}
        for card in self.cards:
            self.ranks[card.rank] = self.ranks.get(card.rank, 0) + 1
    
    def check_ranks(self, *need):
        """
        Checks the occurence of different ranks against requirement for a hand
        need: list of ints
        """
        self.rank_hist()
        rank_set = list(self.ranks.values())
        for need, have in zip(need, sorted(rank_set, reverse=True)):
            if need > have:
                return False
        return True

    def has_flush(self):
        """Returns True if the hand has a flush, False otherwise.
        """
        self.suit_hist()
        for val in self.suits.values():
            if val >= 5:
                return True
        return False

    def has_pair(self):
        """returns true of there are 2 cards of the same rank"""
        return self.check_ranks(2)

    def has_two_pair(self):
        """returns true of there are 2 pairs of cards of the same rank"""
        return self.check_ranks(2, 2)
    
    def has_three_of_a_kind(self):
        return self.check_ranks(3)
    
    def has_straight(self):
        ranks = []
        for card in self.cards:
            ranks.append(card.rank)
        # if there's an ace with rank 1, we also need to add rank 14
        if 1 in ranks:
            ranks.append(14)
        ranks.sort()
        for i in range(len(ranks)-4):
            slice = ranks[i:i+5]
            if slice == list(range(min(slice), max(slice) + 1)):
                return True
        return False

    def has_full_house(self):
        return self.check_ranks(3, 2)
    
    def has_four_of_a_kind(self):
        return self.check_ranks(4)
    
    def has_straight_flush(self):
        # divide cards into suits
        d = {}
        for c in self.cards:
            d.setdefault(c.suit, PokerHand()).add_card(c)
    
        for h in d.values():
            if len(h.cards) < 5:
                continue
            if h.has_straight():
                return True
        return False

    def classify(self):
        for label in PokerHand.all_labels:
            # get the bound method for the label
            f = getattr(self, 'has_' + label)
            if f():
                self.label = label
                return
        self.label = 'high_card'

def hand_probabilities(n=10000):
    results = []
    n = 10000
    for i in range(n):

        # show progress
        if i % 1000 == 0:
            print(i)

        # make a deck
        deck = Deck()
        deck.shuffle()

        # deal the cards and classify the hands
        for i in range(7):
            hand = PokerHand()
            deck.move_cards(hand, 7)
            hand.classify()
            results.append(hand.label)

    for label in PokerHand.all_labels:
        print(f'{label} appears {results.count(label)} time out of {n*7}, {results.count(label)/(n*7)*100:.03}%')
    
    return results


if __name__ == '__main__':
    hand_probabilities()
