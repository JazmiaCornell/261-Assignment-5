# Name: Jazmia Cornell
# OSU Email: cornellj@oregonstate.edu
# Course: CS261 - Data Structures
# Assignment: 05
# Due Date: 05/28/2024
# Description:


from dynamic_array import *


class MinHeapException(Exception):
    """
    Custom exception to be used by MinHeap class
    DO NOT CHANGE THIS CLASS IN ANY WAY
    """
    pass


class MinHeap:
    def __init__(self, start_heap=None):
        """
        Initialize a new MinHeap
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self._heap = DynamicArray()

        # populate MinHeap with initial values (if provided)
        # before using this feature, implement add() method
        if start_heap:
            for node in start_heap:
                self.add(node)

    def __str__(self) -> str:
        """
        Return MinHeap content in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        heap_data = [self._heap[i] for i in range(self._heap.length())]
        return "HEAP " + str(heap_data)

    def add(self, node: object) -> None:
        """
        TODO: Write this implementation
        """
        node_val = node
        self._heap.append(node)

        parent = int((((self._heap.length() - 1) - 1) / 2))
        node_index = self._heap.length() - 1
        while True:
            if node_index == 0 or self._heap.get_at_index(parent) < self._heap.get_at_index(node_index):
                break
            else:
                temp = self._heap.get_at_index(parent)
                self._heap.set_at_index(parent, node_val)
                self._heap.set_at_index(node_index, temp)
                node_index = parent
                parent = int((parent - 1) / 2)

    def is_empty(self) -> bool:
        """
        Returns True if the heap is empty, else returns False.

        :return: a Boolean value, True if the heap is empty, False if not
        """
        # checks if the heap (dynamic array) is empty, if so returns True
        if self._heap.is_empty():
            return True
        else:
            # if not empty returns False
            return False

    def get_min(self) -> object:
        """
        Returns an object that is the minimum key, without removing it from the min_heap. Otherwise,
        raises an exception if the heap is empty.

        :return: an object that is the minimum key of the heap, else raises an exception.
        """
        # checks if heap is empty
        if self._heap.is_empty():
            raise MinHeapException

        # returns min key of heap (root)
        return self._heap.get_at_index(0)

    def remove_min(self) -> object:
        """
        TODO: Write this implementation
        """
        pass

    def build_heap(self, da: DynamicArray) -> None:
        """
        TODO: Write this implementation
        """
        pass

    def size(self) -> int:
        """
        TODO: Write this implementation
        """
        pass

    def clear(self) -> None:
        """
        TODO: Write this implementation
        """
        pass


def heapsort(da: DynamicArray) -> None:
    """
    TODO: Write this implementation
    """
    pass


# It's highly recommended that you implement the following optional          #
# helper function for percolating elements down the MinHeap. You can call    #
# this from inside the MinHeap class. You may edit the function definition.  #

def _percolate_down(da: DynamicArray, parent: int) -> None:
    """
    TODO: Write your implementation
    """
    pass


# ------------------- BASIC TESTING -----------------------------------------


if __name__ == '__main__':

    print("\nPDF - add example 1")
    print("-------------------")
    h = MinHeap()
    print(h, h.is_empty())
    for value in range(300, 200, -15):
        h.add(value)
        print(h)

    print("\nPDF - add example 2")
    print("-------------------")
    h = MinHeap(['LTU^MizEy', 'Tgnhih', 'nMoCpkdgGxc', 'x\\mCzZv'])
    print(h)
    for value in ['LTU^MizEy']:
        h.add(value)
        print(h)

    print("\nPDF - is_empty example 1")
    print("-------------------")
    h = MinHeap([2, 4, 12, 56, 8, 34, 67])
    print(h.is_empty())

    print("\nPDF - is_empty example 2")
    print("-------------------")
    h = MinHeap()
    print(h.is_empty())

    print("\nPDF - get_min example 1")
    print("-----------------------")
    h = MinHeap(['fish', 'bird'])
    print(h)
    print(h.get_min(), h.get_min())

    # print("\nPDF - remove_min example 1")
    # print("--------------------------")
    # h = MinHeap([1, 10, 2, 9, 3, 8, 4, 7, 5, 6])
    # while not h.is_empty() and h.is_empty() is not None:
    #     print(h, end=' ')
    #     print(h.remove_min())
    #
    # print("\nPDF - build_heap example 1")
    # print("--------------------------")
    # da = DynamicArray([100, 20, 6, 200, 90, 150, 300])
    # h = MinHeap(['zebra', 'apple'])
    # print(h)
    # h.build_heap(da)
    # print(h)
    #
    # print("--------------------------")
    # print("Inserting 500 into input DA:")
    # da[0] = 500
    # print(da)
    #
    # print("Your MinHeap:")
    # print(h)
    # if h.get_min() == 500:
    #     print("Error: input array and heap's underlying DA reference same object in memory")
    #
    # print("\nPDF - size example 1")
    # print("--------------------")
    # h = MinHeap([100, 20, 6, 200, 90, 150, 300])
    # print(h.size())
    #
    # print("\nPDF - size example 2")
    # print("--------------------")
    # h = MinHeap([])
    # print(h.size())
    #
    # print("\nPDF - clear example 1")
    # print("---------------------")
    # h = MinHeap(['monkey', 'zebra', 'elephant', 'horse', 'bear'])
    # print(h)
    # print(h.clear())
    # print(h)
    #
    # print("\nPDF - heapsort example 1")
    # print("------------------------")
    # da = DynamicArray([100, 20, 6, 200, 90, 150, 300])
    # print(f"Before: {da}")
    # heapsort(da)
    # print(f"After:  {da}")
    #
    # print("\nPDF - heapsort example 2")
    # print("------------------------")
    # da = DynamicArray(['monkey', 'zebra', 'elephant', 'horse', 'bear'])
    # print(f"Before: {da}")
    # heapsort(da)
    # print(f"After:  {da}")
