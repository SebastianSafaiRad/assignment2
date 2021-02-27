import random

from lists import UnorderedList
from lists import Node
import unittest


class QueueLL:
    """ Implements a Linked List """

    def __init__(self):
        """ Create the one field/attribute needed for our QueueLL class """
        self.queue = UnorderedList()

    def __str__(self):
        """ override Python str function/method to facilitate printing of the entire queue,
        this should print the contents of the queue with front of the queue on left,
        and back of the queue on the right """
        return self.queue.__str__()

    def isEmpty(self):
        """ return True if the queue has zero items, and False if has one or more items """
        return self.queue.isEmpty()

    def enqueue(self, item):
        """ add new item to back or queue, don’t return anything """
        self.queue.append(item)

    def deQueue(self):
        """ return and remove item at the front of the queue """
        return self.queue.pop(0)

    def peek(self):
        """ return item at the front of the queue, but don’t remove it """
        return Node(self.queue.convert2List()[0]).getData()

    def size(self):
        """ return the number of items currently in the queue """
        return self.queue.size()


class TestQueueLL(unittest.TestCase):
    """ A Class to test the methods of QueueLL """

    # Creating a QueueLL object and populating its fields
    ll = QueueLL()
    ll.enqueue("a")
    ll.enqueue("b")
    ll.enqueue("c")
    ll.enqueue("d")
    print("List of nodes", ll.__str__())
    print("This is a peek: ", ll.peek())

    def testSize(self):
        """ Tests to make sure that the size() method is working """
        self.assertEqual(self.ll.size(), 4)

    def testPeek(self):
        """ Tests to make sure that the peek() method is working """
        self.assertEqual(self.ll.peek(), "a")


class TrafficSimulatorQueue(QueueLL):
    """
    A class to simulate traffic arriving and leaving an intersection with a stop
    light.  As with all simulations, time is discretized so that each loop
    iteration represents one (1) second of time.

    Fields:
      * queue [from inheritance] - the internal structure that holds the queue
      * traffic_light_state - current status of the traffic light, either 'red' or 'green'
      * time_steps_needed_for_1_car_to_exit - time steps (e.g. 'seconds') needed for front car to exit intersection
      * prob_arrival - probability that an automobile arrives on any given iteration/epoch
      * time_steps_light_is_red - number of time steps (e.g. 'seconds') the traffic light is red
      * time_steps_light_is_green - number of time steps (e.g. 'seconds') the traffic light is green

    Methods:
      * __init__() - constructor to initialize class fields/attributes
      * isEmpty() [from inheritance]
      * enqueue(new_item) [from inheritance]
      * dequeue() [from inheritance]
      * size() [from inheritance]
      * peek() [from inheritance]
      * setProbabilityArrival(prob_arrival) - modify the probablity that a car arrives at any given time step
      * setMinutesRed(min_red) - modify the number of minutes the traffic light is red for (and convert to seconds/time_steps)
      * setMinutesGreen(min_red) - modify the number of minutes the traffic light is red for (and convert to seconds/time_steps)
      * checkForArrivingAuto() - check to see if a car arrives (intended to be called at each time step)
      * simulateTraffic(n) - simulate traffic for n cycles of red and green lights, starting with red first and
                             printing status, queue, etc. as the simulation is carried out
    """

    def __init__(self):

        super(TrafficSimulatorQueue, self).__init__()
        self.traffic_light_state = "red"
        self.time_steps_needed_for_1_car_to_exit = 1
        self.prob_arrival = 0.5
        self.time_steps_light_is_red = 1
        self.time_steps_light_is_green = 1

    def setProbabilityArrival(self, prob_arrival):
        self.prob_arrival = prob_arrival

    def setMinutesRed(self, min_red):
        self.time_steps_light_is_red = min_red * 60

    def setMinutesGreen(self, min_green):
        self.time_steps_light_is_green = min_green * 60

    def checkForArrivingAuto(self):
        """
        Generate a random number between 0 and 1, then see if it less than
        self.prob_arrival. If it is, then add a new auto/car to the queue.
        """
        r = random.random()
        if r < self.prob_arrival:
            car_arriving = random.choice('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
            self.enqueue(car_arriving)

    def simulateTraffic(self, number_redgreen_cycles):
        """ Run the simulation where each iteration of the while loop represents 1 second. """
        print("Traffic light is red, current queue size = " + str(self.size()))

        i = number_redgreen_cycles * (self.time_steps_light_is_green + self.time_steps_light_is_red)
        i_light = self.time_steps_light_is_red

        while i > 0:
            # cars can arrive regardless of whether the light is red or green
            self.checkForArrivingAuto()

            # light is red, so just decrement the light counter, i_light
            # once i_light has counted down to 0, then set everything needed to
            # change it to greeen
            if self.traffic_light_state == "red":
                i_light -= 1
                if i_light == 0:
                    self.traffic_light_state = "green"
                    i_light = self.time_steps_light_is_green
                    print("Traffic light changing to green, current queue size = " + str(self.size()) + ", queue:")
                    print(" " * 2, self)

            # light is green, so just decrement light counter AND check to see if
            # time_steps_needed_for_1_car_to_exit iterations have passed (if so, removed a car from the queue)
            # once i_light has counted down to 0, then set everything needed to change the light to red
            else:
                i_light -= 1
                if i % self.time_steps_needed_for_1_car_to_exit == 0:
                    if self.queue.size() > 0:
                        car_leaving = Node(self.deQueue()).getData()
                        print(" " * 4, "car,", car_leaving, ", exiting intersection")
                    else:
                        print("No cars waiting")
                if i_light == 0:
                    self.traffic_light_state = "red"
                    i_light = self.time_steps_light_is_red
                    i_light = number_redgreen_cycles * self.time_steps_light_is_red
                    print("Traffic light changing to red, current queue size = " + str(self.size()) + ", queue:")
                    print(" " * 2, self)
            i -= 1


if __name__ == '__main__':
    print('=' * 30, 'Simulation 1:', '=' * 30)
    ts = TrafficSimulatorQueue()

    # set probability that a car arrives on any given second (i.e. loop # iteration) to 50%
    ts.setProbabilityArrival(0.8)

    # set the light to be red for 2 minutes (needs to be converted to seconds inside)
    ts.setMinutesRed(1)

    # set the light to be green for 1 minute (needs to be converted to seconds inside)
    ts.setMinutesGreen(1)

    # run simulation for two red-green cycles (i.e. red -> green -> red -> green)
    ts.simulateTraffic(2)

    print("Traffic simulator queue size at end of simulation =", ts.size())
    print("Traffic simulator queue at end of simulation:")
    print(ts)
