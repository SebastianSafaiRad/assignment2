from lists import UnorderedList
from lists import Node
import unittest


class QueueLL:
    """ ADD DOCUMENTATION HERE, REMOVING/REPLACING COMMENTS IN ALL CAPS """

    def __init__(self):
        """ Create the one field/attribute needed for our QueueLL class """
        self.queue = UnorderedList()

    def __str__(self):
        '''override Python str function/method to facilitate printing of the entire queue,
        this should print the contents of the queue with front of the queue on left,
        and back of the queue on the right'''
        return self.queue.__str__()

    def isEmpty(self):
        '''return True if the queue has zero items, and False if has one or more items'''
        return self.queue.isEmpty()

    def enqueue(self, item):
        '''add new item to back or queue, don’t return anything'''
        self.queue.append(item)

    def deQueue(self):
        '''return and remove item at the front of the queue'''
        return self.queue.pop(0)

    def peek(self):
        '''return item at the front of the queue, but don’t remove it'''
        return Node(self.queue.convert2List()[0]).getData()

    def size(self):
        '''return the number of items currently in the queue'''
        return self.queue.size()


class TestQueueLL(unittest.TestCase):
    """ ADD DOCUMENTATION HERE, REMOVING/REPLACING COMMENTS IN ALL CAPS """

    # Creating a QueueLL object and populating its fields
    ll = QueueLL()
    ll.enqueue("a")
    ll.enqueue("b")
    ll.enqueue("c")
    ll.enqueue("d")
    print("List of nodes", ll.__str__())
    print("This is a peek: ", ll.peek())

    def testSize(self):
        '''Tests to make sure that the size() method is working'''
        self.assertEqual(self.ll.size(), 4)

    def testPeek(self):
        '''Tests to make sure that the peek() method is working'''
        self.assertEqual(self.ll.peek(), "a")

# SEE PART 2 BELOW FOR THE CONTINUATION OF THIS FILE


