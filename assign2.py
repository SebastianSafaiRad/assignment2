from lists import UnorderedList
import unittest

class QueueLL:
    """ ADD DOCUMENTATION HERE, REMOVING/REPLACING COMMENTS IN ALL CAPS """

    def __init__(self):
        """ Create the one field/attribute needed for our QueueLL class """
        self.queue = UnorderedList()

    def __str__(self):
        return self.queue.__str__()

    def isEmpty(self):
        return self.queue.isEmpty()

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        return self.queue.pop(0)

    def peek(self):
        return self.queue.head

    def size(self):
        return self.queue.size()


    # ADD ALL REQUIRED METHODS HERE - SEE PART 1 DIRECTIONS IN Canvas
    # (REMOVE/REPLACE THIS AND ANY OTHER COMMENTS IN CAPS)


class TestQueueLL(unittest.TestCase):
    """ ADD DOCUMENTATION HERE, REMOVING/REPLACING COMMENTS IN ALL CAPS """

    # ADD AT LEAST TWO UNIT TESTS HERE TO TEST THAT QUEUELL METHODS WORK AS EXPECTED
    # (REMOVE/REPLACE THIS AND ANY OTHER COMMENTS IN CAPS)

# SEE PART 2 BELOW FOR THE CONTINUATION OF THIS FILE