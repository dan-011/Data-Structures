import unittest
import random
from DeckOfCards import DeckOfCards

class TestDeckOfCards(unittest.TestCase):

    def test_init(self):
        card_list = []
        suits = ['hearts', 'diamonds', 'clubs', 'spades']
        values = ['two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten','jack', 'queen', 'king', 'ace']
        for suit in suits:
            for value in values:
                card_list.append(value + ' of ' + suit)
        random.shuffle(card_list)

        d1 = DeckOfCards(card_list)

        # test that full list of cards is in the deck
        self.assertEqual(len(d1.cards), 52)

        # test that the bottom card is card_list[0]
        self.assertEqual(d1.cards.head._item, card_list[0])

        # test that the top card is card_list[-1]
        self.assertEqual(d1.cards.tail._item, card_list[-1])
    
    def test_deal_top(self):
        card_list = []
        suits = ['hearts', 'diamonds', 'clubs', 'spades']
        values = ['two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten','jack', 'queen', 'king', 'ace']
        for suit in suits:
            for value in values:
                card_list.append(value + ' of ' + suit)
        random.shuffle(card_list)

        # test main functionality
        d1 = DeckOfCards(card_list)
        top_card = card_list[-1]
        self.assertEqual(d1.deal_top(), top_card)
        self.assertEqual(len(d1.cards), 51)

        # test exception
        with self.assertRaises(RuntimeError):
            for i in range(54):
                d1.deal_top()

    def test_deal_bottom(self):
        card_list = []
        suits = ['hearts', 'diamonds', 'clubs', 'spades']
        values = ['two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten','jack', 'queen', 'king', 'ace']
        for suit in suits:
            for value in values:
                card_list.append(value + ' of ' + suit)
        random.shuffle(card_list)
        
        # test main functionality
        d1 = DeckOfCards(card_list)
        bottom_card = card_list[0]
        self.assertEqual(d1.deal_bottom(), bottom_card)
        self.assertEqual(len(d1.cards), 51)

        # test exception
        with self.assertRaises(RuntimeError):
            for i in range(54):
                d1.deal_bottom()

    def test_is_cheating(self):
        card_list = []
        suits = ['hearts', 'diamonds', 'clubs', 'spades']
        values = ['two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten','jack', 'queen', 'king', 'ace']
        for suit in suits:
            for value in values:
                card_list.append(value + ' of ' + suit)
        random.shuffle(card_list)
        
        d1 = DeckOfCards(card_list)
        dealt_card = d1.deal_top()

        # test True scenario
        self.assertEqual(d1.is_cheating(dealt_card), True)

        # test False scenario
        self.assertEqual(d1.is_cheating(d1.cards.head), False)

unittest.main()