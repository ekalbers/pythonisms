import pytest
from linked_list_dunders import LinkedList, Node


def test_eq():
    node5 = Node(5)
    node4 = Node(4, node5)
    node3 = Node(3, node4)
    node2 = Node(2, node3)
    node1 = Node(1, node2)
    ll1 = LinkedList(node1)
    node10 = Node(5)
    node9 = Node(4, node10)
    node8 = Node(3, node9)
    node7 = Node(2, node8)
    node6 = Node(1, node7)
    ll2 = LinkedList(node6)
    assert ll1 == ll2


def test_eq_false():
    node5 = Node(5)
    node4 = Node(4, node5)
    node3 = Node(3, node4)
    node2 = Node(2, node3)
    node1 = Node(1, node2)
    ll1 = LinkedList(node1)
    node10 = Node(5)
    node9 = Node(4, node10)
    node8 = Node(3, node9)
    node7 = Node(1, node8)
    node6 = Node(1, node7)
    ll2 = LinkedList(node6)
    assert not ll1 == ll2


def test_eq_false_length():
    node11 = Node(11)
    node5 = Node(5, node11)
    node4 = Node(4, node5)
    node3 = Node(3, node4)
    node2 = Node(2, node3)
    node1 = Node(1, node2)
    ll1 = LinkedList(node1)
    node10 = Node(5)
    node9 = Node(4, node10)
    node8 = Node(3, node9)
    node7 = Node(1, node8)
    node6 = Node(1, node7)
    ll2 = LinkedList(node6)
    assert not ll1 == ll2


def test_get_set():
    node5 = Node(5)
    node4 = Node(4, node5)
    node3 = Node(3, node4)
    node2 = Node(2, node3)
    node1 = Node(1, node2)
    ll1 = LinkedList(node1)
    ll1[2] = 10
    assert ll1[2] == 10
    assert ll1[0] == 1


def test_get_error():
    ll1 = LinkedList(Node(1))
    with pytest.raises(IndexError):
        ll1[1]


def test_set_error():
    ll1 = LinkedList(Node(1))
    with pytest.raises(IndexError):
        ll1[1] = 2


def test_length():
    node5 = Node(5)
    node4 = Node(4, node5)
    node3 = Node(3, node4)
    node2 = Node(2, node3)
    node1 = Node(1, node2)
    ll1 = LinkedList(node1)
    assert len(ll1) == 5


def test_contains():
    node5 = Node(5)
    node4 = Node(4, node5)
    node3 = Node(3, node4)
    node2 = Node(2, node3)
    node1 = Node(1, node2)
    ll1 = LinkedList(node1)
    assert 2 in ll1


def test_contains_false():
    node5 = Node(5)
    node4 = Node(4, node5)
    node3 = Node(3, node4)
    node2 = Node(2, node3)
    node1 = Node(1, node2)
    ll1 = LinkedList(node1)
    assert 6 not in ll1


def test_iter():
    node5 = Node(5)
    node4 = Node(4, node5)
    node3 = Node(3, node4)
    node2 = Node(2, node3)
    node1 = Node(1, node2)
    ll1 = LinkedList(node1)
    test_str = ''
    for x in ll1:
        test_str = test_str + str(x)
    assert test_str == '12345'
