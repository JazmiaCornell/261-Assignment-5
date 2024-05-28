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
        Inserts node object into min_heap, then sorts from min to max (top to bottom).

        :param node: a passed object that is inserted into the heap

        :return: an updated min_heap with passed object inserted and organized correctly (top is min)
        """
        # sets node value to node_val and adds node to dynamic array
        node_val = node
        self._heap.append(node)

        # calculate the parent of node, calculate the index of node
        parent = int((((self._heap.length() - 1) - 1) / 2))
        node_index = self._heap.length() - 1

        # sorts node in array if value is < parent, else inserts next node
        while True:
            # if reached beginning of array or parent < node, exit loop
            if node_index == 0 or self._heap.get_at_index(parent) < self._heap.get_at_index(node_index):
                break
            else:
                # swaps value from node and parent node, calculate new parent and node_index
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
        Returns removed_min from min_heap and updates the heap to be in order (min val to max)

        :return: the removed_min from the heap
        """
        # if heap empty, raise exception
        if self.is_empty():
            raise MinHeapException

        # swaps value of min_val and tail_val, removes min node
        removed_node = self._heap[0]
        tail = self._heap.length() - 1
        end_val = self._heap.get_at_index(tail)
        self._heap.set_at_index(tail, removed_node)
        self._heap.set_at_index(0, end_val)
        self._heap.remove_at_index(tail)

        # reorders heap, min to max (top to bottom of tree)
        index = 0
        child_index = None
        child_val = None

        while True:
            # calculates index of left and right child
            left_child = 2 * index + 1
            right_child = 2 * index + 2
            # if left child is in bounds and less than index val, sets child_val and child_index to left_child
            if left_child <= self._heap.length() - 1:
                child_val = self._heap[left_child]
                child_index = left_child

            # if right child is in bounds and less than left_child, sets child_val and child_index to right_child
            if (right_child <= self._heap.length() - 1 and self._heap[right_child] < self._heap[left_child]
                    and index != child_index):
                child_val = self._heap[right_child]
                child_index = right_child

            # checks if child_index is not None and if it is less than the val at index
            if child_index is None or self._heap[index] <= self._heap[child_index]:
                break

            # if index = child index, exit loop
            if index == child_index:
                break

            # swaps values at index_val and child_val, sets new index
            index_val = self._heap[index]
            self._heap.set_at_index(child_index, index_val)
            self._heap.set_at_index(index, child_val)
            index = child_index

        # returns removed_node (min_val)
        return removed_node

    def build_heap(self, da: DynamicArray) -> None:
        """
        Overrides initial heap with passed DynamicArray, with elements sorted.

        :param da: a DynamicArray of values passed to the method

        :return: an updated min_head with passed values (array) sorted in correct order
        """
        # clears heap
        self.clear()

        # adds element to heap (array)
        for i in range(da.length()):
            self._heap.append(da.get_at_index(i))

        # percolates down the heap (first non-leaf element)
        for i in range((self.size() // 2 - 1), -1, -1):
            _percolate_down(self._heap, i)

    def size(self) -> int:
        """
        Returns an integer that is the size of the min_head.

        :return: an integer that is the size of the heap
        """
        # returns size of heap
        return self._heap.length()

    def clear(self) -> None:
        """
        Returns an empty, cleared heap

        :return: a cleared heap
        """
        # clears heap
        self._heap = DynamicArray()


def heapsort(da: DynamicArray) -> None:
    """
    TODO: Write this implementation
    """
    # length of da
    k = da.length()

    for i in range((k // 2 - 1), -1, -1):
        index = i
        while True:
            left_child = 2 * index + 1
            right_child = 2 * index + 2
            temp = index

            if left_child < k and da[left_child] < da[index]:
                index = left_child

            if right_child < k and da[right_child] < da[index]:
                index = right_child

            if index != temp:
                da[temp], da[index] = da[index], da[temp]
                temp = index
            else:
                break

    for i in range(k-1, 0, -1):
        da[i], da[0] = da[0], da[i]
        index = 0
        size = i
        while True:
            left_child = 2 * index + 1
            right_child = 2 * index + 2
            temp = index

            if left_child < size and da[left_child] < da[index]:
                index = left_child
            if right_child < size and da[right_child] < da[index]:
                index = right_child

            if index != temp:
                da[temp], da[index] = da[index], da[temp]
                temp = index
            else:
                break


def _percolate_down(da: DynamicArray, parent: int) -> None:
    """
    Percolates elements down the min_heap, sorting elements in order (min = top)

    :param da: an array (the min_heap) that is passed to the function, what is being sorted
    :param: an integer passed, that is the parent Node of a particular subtree (starting point)

    :return: an updated heap, with elements sorted (min to max)
    """

    while True:
        # calculates/sets root, left_child and right_child
        index = parent
        left_child = 2 * index + 1
        right_child = 2 * index + 2

        # if left is in bounds and less than parent node, index is left
        if left_child <= da.length() - 1 and da[left_child] < da[index]:
            index = left_child
        # if right is in bounds, and less than index value, sets right to index
        if right_child <= da.length() - 1 and da[right_child] < da[index]:
            index = right_child
        # if index != parent, swaps values at index and parent nodes
        if index != parent:
            temp = da[parent]
            da.set_at_index(parent, da[index])
            da.set_at_index(index, temp)
            parent = index
        else:
            # else returns to calling function
            break


# ------------------- BASIC TESTING -----------------------------------------


if __name__ == '__main__':

    # print("\nPDF - add example 1")
    # print("-------------------")
    # h = MinHeap()
    # print(h, h.is_empty())
    # for value in range(300, 200, -15):
    #     h.add(value)
    #     print(h)
    #
    # print("\nPDF - add example 2")
    # print("-------------------")
    # h = MinHeap(['LTU^MizEy', 'Tgnhih', 'nMoCpkdgGxc', 'x\\mCzZv'])
    # print(h)
    # for value in ['LTU^MizEy']:
    #     h.add(value)
    #     print(h)
    #
    # print("\nPDF - is_empty example 1")
    # print("-------------------")
    # h = MinHeap([2, 4, 12, 56, 8, 34, 67])
    # print(h.is_empty())
    #
    # print("\nPDF - is_empty example 2")
    # print("-------------------")
    # h = MinHeap()
    # print(h.is_empty())
    #
    # print("\nPDF - get_min example 1")
    # print("-----------------------")
    # h = MinHeap(['fish', 'bird'])
    # print(h)
    # print(h.get_min(), h.get_min())
    #
    # print("\nPDF - remove_min example 1")
    # print("--------------------------")
    # h = MinHeap([5319, 26916, 76634, 94376, 43420, 79029])
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

    print("\nPDF - heapsort example 1")
    print("------------------------")
    da = DynamicArray([100, 20, 6, 200, 90, 150, 300])
    print(f"Before: {da}")
    heapsort(da)
    print(f"After:  {da}")

    print("\nPDF - heapsort example 2")
    print("------------------------")
    da = DynamicArray(['monkey', 'zebra', 'elephant', 'horse', 'bear'])
    print(f"Before: {da}")
    heapsort(da)
    print(f"After:  {da}")
