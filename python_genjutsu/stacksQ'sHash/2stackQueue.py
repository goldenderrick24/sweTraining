class QueueFromStacks(object):


    def __init__(self):

        self.left_stack = Stack()

        self.right_stack = Stack()



    def shift_stacks(self, source, destination):

        while source.peek() is not None:

            destination.push(source.pop())



    def enqueue(self, data):

        self.shift_stacks(self.right_stack, self.left_stack)

        self.left_stack.push(data)



    def dequeue(self):

        self.shift_stacks(self.left_stack, self.right_stack)

        return self.right_stack.pop()


from nose.tools import assert_equal


class TestQueueFromStacks(object):


    def test_queue_from_stacks(self):

        print('Test: Dequeue on empty stack')

        queue = QueueFromStacks()

        assert_equal(queue.dequeue(), None)


        print('Test: Enqueue on empty stack')

        print('Test: Enqueue on non-empty stack')

        print('Test: Multiple enqueue in a row')

        num_items = 3

        for i in range(0, num_items):

            queue.enqueue(i)


        print('Test: Dequeue on non-empty stack')

        print('Test: Dequeue after an enqueue')

        assert_equal(queue.dequeue(), 0)



        print('Test: Multiple dequeue in a row')

        assert_equal(queue.dequeue(), 1)

        assert_equal(queue.dequeue(), 2)


        print('Test: Enqueue after a dequeue')

        queue.enqueue(5)

        assert_equal(queue.dequeue(), 5)


        print('Success: test_queue_from_stacks')



def main():

    test = TestQueueFromStacks()

    test.test_queue_from_stacks()



if __name__ == '__main__':

    main()