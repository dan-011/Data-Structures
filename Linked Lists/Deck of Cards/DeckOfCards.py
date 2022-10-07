from DoublyLinkedList import DoublyLinkedList

class DeckOfCards:
    def __init__(self, cards):
        self.cards = DoublyLinkedList()
        for i in cards:
            self.cards.add_last(i)
        self._store = set()
        
    def deal_top(self):
        try:
            item = self.cards.remove_last()
            self._store.add(item)
            return item
        except RuntimeError:
            raise RuntimeError("Attempt to deal_top from empty DeckOfCards")

    def deal_bottom(self):
        try:
            item = self.cards.remove_first()
            self._store.add(item)
            return item
        except RuntimeError:
            raise RuntimeError("Attempt to deal_bottom from empty DeckOfCards")

    def is_cheating(self, card):
        return card in self._store