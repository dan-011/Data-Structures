class Node:
    def __init__(self, _item, _next=None):
        self._item = _item
        self._next = _next


class LinkedList:
    def __init__(self):
        self._head = None
        self._len = 0

    def add_first(self, item):
        # note the ternary (three-parameter) if:
        #    x = a if (boolean) else b
        # equiv to
        #    if (boolean): x = a
        #    else: x = b
        self._head = Node(item) if (len(self) == 0) else Node(item, self._head)

        self._len += 1

    def remove_first(self):
        if len(self) == 0:
            raise RuntimeError("attempt to remove_first from empty LL")

        item = self._head._item  # extract item
        self._head = self._head._next  # cut off head
        self._len -= 1  # decrease length
        return item  # return item

    def __len__(self):
        return self._len

    def __str__(self):
        if len(self) == 0:
            return ""  # edge case - just return an empty string

        list_of_strings = []  # empty list to hold strings of each item
        self._str(self._head, list_of_strings)  # call helper function _str w/ head node
        return "".join(
            list_of_strings
        )  # join all items in list_of_strings into one string

    # leading underscore - this is private!
    # attributes within this class, like __str__, can call it, but users should not
    # this is called a "helper" function
    def _str(self, node, list_of_strings):
        # base case: tail node
        if node._next is None:
            list_of_strings.append(
                str(node._item)
            )  # add this item to the list of strings
            return  # start bouncing back up chain of recursive calls

        # non-base case: recursively call on next node
        else:
            self._str(node._next, list_of_strings)  # recursively call on next node

        # we have hit the tail, and are bouncing back up.
        # add this item to "list_of_strings", then return
        list_of_strings.insert(
            0, str(node._item) + "-"
        )  # pre-pend "item-" to list of strings

    def __contains__(self, other):
        return self._in(self._head, other)

    def _in(self, node, other):
        if node is None:
            return False
        elif other == node._item:
            return True
        else:
            return self._in(node._next, other)

    def add_last(self, item):
        self._add_last(self._head, item)

    def _add_last(self, node, item):
        if node is None:
            self.add_first(item)
        elif node._next is None:
            node._next = Node(item)
            self._len += 1
        else:
            self._add_last(node._next, item)


if __name__ == "__main__":
    # Test Node
    n = Node(1)
    assert n._item == 1
    assert n._next is None
    print("Node tests pass")

    # Test LL - add_first/len/remove_first
    LL = LinkedList()

    for i in range(4):
        assert len(LL) == i
        LL.add_first(i)

    for i in range(4):
        assert LL.remove_first() == 3 - i
        assert len(LL) == 3 - i

    # Test LL - str
    for i in range(4):
        LL.add_first(i)
    assert str(LL) == "3-2-1-0"
    print("starter LL tests pass!")

    #   * test in
    ll = LinkedList()
    for i in range(10):
        ll.add_first(i)
    assert 7 in ll
    assert 10 not in ll

    #   * test add_last
    ll = LinkedList()
    for i in range(20, 31):
        ll.add_last(i)
    for i in range(20, 31):
        assert ll.remove_first() == i