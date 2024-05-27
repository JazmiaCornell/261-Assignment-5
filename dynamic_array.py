# Name: Jazmia Cornell
# OSU Email: cornellj@oregonstate.edu
# Course: CS261 - Data Structures
# Assignment: 02
# Due Date: 4/29/2024
# Description: The following functions are designed to implement a DynamicArray class and assigned complexity.


from static_array import StaticArray


class DynamicArrayException(Exception):
    """
    Custom exception class to be used by Dynamic Array
    DO NOT CHANGE THIS CLASS IN ANY WAY
    """
    pass


class DynamicArray:
    def __init__(self, start_array=None):
        """
        Initialize new dynamic array
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self._size = 0
        self._capacity = 4
        self._data = StaticArray(self._capacity)

        # populate dynamic array with initial values (if provided)
        # before using this feature, implement append() method
        if start_array is not None:
            for value in start_array:
                self.append(value)

    def __str__(self) -> str:
        """
        Return content of dynamic array in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        out = "DYN_ARR Size/Cap: "
        out += str(self._size) + "/" + str(self._capacity) + ' ['
        out += ', '.join([str(self._data[_]) for _ in range(self._size)])
        return out + ']'

    def __iter__(self):
        """
        Create iterator for loop
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self._index = 0
        return self

    def __next__(self):
        """
        Obtain next value and advance iterator
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        try:
            value = self[self._index]
        except DynamicArrayException:
            raise StopIteration

        self._index += 1
        return value

    def get_at_index(self, index: int) -> object:
        """
        Return value from given index position
        Invalid index raises DynamicArrayException
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        if index < 0 or index >= self._size:
            raise DynamicArrayException
        return self._data[index]

    def set_at_index(self, index: int, value: object) -> None:
        """
        Store value at given index in the array
        Invalid index raises DynamicArrayException
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        if index < 0 or index >= self._size:
            raise DynamicArrayException
        self._data[index] = value

    def __getitem__(self, index) -> object:
        """
        Same functionality as get_at_index() method above,
        but called using array[index] syntax
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self.get_at_index(index)

    def __setitem__(self, index, value) -> None:
        """
        Same functionality as set_at_index() method above,
        but called using array[index] syntax
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self.set_at_index(index, value)

    def is_empty(self) -> bool:
        """
        Return True is array is empty / False otherwise
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self._size == 0

    def length(self) -> int:
        """
        Return number of elements stored in array
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self._size

    def get_capacity(self) -> int:
        """
        Return the capacity of the array
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self._capacity

    def print_da_variables(self) -> None:
        """
        Print information contained in the dynamic array.
        Used for testing purposes.
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        print(f"Length: {self._size}, Capacity: {self._capacity}, {self._data}")

    # -----------------------------------------------------------------------

    def resize(self, new_capacity: int) -> None:
        """
        Returns None if new_capacity is negative, equal to zero, or less than self._size. If None is not returned
        updates self._capacity and self._data, which resizes the DynamicArray.

        :param new_capacity: an integer that is passed to resize the array.

        :return: an updated/resized DynamicArray or None if new_capacity is less than self._size or not positive.
        """
        # checks if new_capacity is positive or less than self._size
        if new_capacity < self._size or new_capacity <= 0:
            return None

        # if not, updates capacity and resizes new array
        self._capacity = new_capacity
        temp = StaticArray(self._capacity)

        # moves values from old array to new array
        for i in range(self._size):
            temp[i] = self._data[i]
        self._data = temp

    def append(self, value: object) -> None:
        """
        Returns updated array to add value to end, if self._size == self._capacity, resizes array

        :param value: an object that will be added to array

        :return: returns an updated array with value added to the end or None if appending isn't allowed
        """
        # checks if size and capacity are equal, if so resizes new array
        if self._size == self._capacity:
            new_capacity = self._size * 2
            self.resize(new_capacity)
        # if size < capacity, increases size and adds value to end of array
        self._size += 1
        self.set_at_index(self._size - 1, value)
        return None

    def insert_at_index(self, index: int, value: object) -> None:
        """
        Returns updated DynamicArray by inserting value at desired index and moving other values if needed, else
        returns None

        :param index: the desired destination for value
        :param value: an object that will be inserted at index

        :return: returns an updated array with value at desired index if allowed, else returns None and raises an
        exception
        """
        # raises exception if index is negative or >= array size
        if index < 0 or index >= self._size + 1:
            raise DynamicArrayException

        # resizes array if size and capacity are equal (doubles capacity)
        if self._size == self._capacity:
            new_capacity = self._size * 2
            self.resize(new_capacity)

        # inserts value at given index
        self._size += 1
        # if array is empty, inserts value at beginning
        if self._size == 1:
            self.set_at_index(self._size - 1, value)
        # if array has values, moves values at and after desired index down 1 index, then inserts value at desired index
        if self._size > 1:
            for i in range(self._size-1, 0, -1):
                if i == index:
                    self.set_at_index(index, value)
                    return
                temp = self._data[i-1]
                self.set_at_index(i, temp)
            self.set_at_index(index, value)
        return None

    def remove_at_index(self, index: int) -> None:
        """
        Returns an updated array with removed value at passed index, then fills gap with remaining values. Otherwise,
        raises exception if out of bounds and resizes the array if capacity is > 10 and less than 1/4 of capacity.

        :param index: passed to the method, determines the location to remove value

        :return: a modified array with removed value at passed index, otherwise returns None
        """
        # raises exception if index is negative or >= array size
        if index < 0 or index > self._size - 1:
            raise DynamicArrayException

        # checks capacity and size, reduces capacity accordingly
        if self._capacity > 10 and self._size < (self._capacity * 1/4):
            new_capacity = self._size * 2
            if new_capacity < 10:
                new_capacity = 10
            self.resize(new_capacity)

        # If removing the last element, simply decrement the size
        if index == self._size - 1:
            self._size -= 1
        else:
            # Shift elements to the left to fill the gap
            for i in range(index, self._size - 1):
                self.set_at_index(i, self.get_at_index(i + 1))
            self._size -= 1

        return None

    def slice(self, start_index: int, size: int) -> "DynamicArray":
        """
        Returns a new DynamicArray with values from old array from start_index to (start_index + size). If start_index
        or size is invalid or range, from start_index to (start_index + size), is not possible an exception is
        raised.

        :param start_index: an integer passed that determines the starting value for new DynamicArray
        :param size: a passed integer that determines the ending position/value for new DynamicArray

        :return: a new DynamicArray with values from start_index to start_index + size of old DynamicArray.
        """
        # checks if start_index is non-negative or if size !> than capacity or
        # requested range !> than size of values in array
        if start_index < 0 or (start_index + size) > self._size or size < 0 or start_index == self.length():
            raise DynamicArrayException

        # creates new DynamicArray and moves values from range (start_index to size) to new array
        slice_arr = DynamicArray()
        for i in range(start_index, start_index + size):
            slice_arr.append(self._data[i])

        # increases capacity if new array size > new array capacity
        while slice_arr._size > slice_arr._capacity:
            slice_arr.resize(slice_arr._capacity * 2)
        return slice_arr

    def map(self, map_func) -> "DynamicArray":
        """
        Returns a new DynamicArray with elements from old array that have  had map_func applied.

        :param map_func: is a function passed to the method that manipulates each element of the old array

        :return: a new DynamicArray with modified values (via map_func) form the old array.
        """
        # create new DynamicArray
        map_arr = DynamicArray()

        # iterates through old array and performs map_func, then adds new value to new array
        for i in range(0, self._size):
            temp = map_func(self._data[i])
            map_arr.append(temp)

        return map_arr

    def filter(self, filter_func) -> "DynamicArray":
        """
        Returns a new DynamicArray with elements that pass the filter_func test.

        :param filter_func: is a passed function that checks a certain condition, if true then element is moved to the
        new array

        :return: a new DynamicArray with elements that passed filer_func
        """
        # creates new array
        filter_arr = DynamicArray()

        # iterated through old array, adds element to new array if it passed filter_func condition
        for i in range(0, self._size):
            if filter_func(self._data[i]) is True:
                filter_arr.append(self._data[i])

        return filter_arr

    def reduce(self, reduce_func, initializer=None) -> object:
        """
        Returns the resulting value of the application of the reduce_func on the elements of the array. If initializer
        is None x = initializer, if not x = index 0

        :param reduce_func: is a function that is sequentially applied to each element of the array
        :param initializer: can be assigned or None, determines starting int of reduce_func (x) if not None

        :return: the results (value) from performing reduce_func on array
        """
        # determines the initial value, starting x value for reduce_func
        if initializer is None:
            if self._size > 0:
                value = self._data[0]
            else:
                return None
        else:
            value = initializer

        # iterates through array, performs reduce_func to each value
        for i in range(0, self._size):
            if initializer is not None:
                y = self._data[i]
                value = reduce_func(value, y)
            elif initializer is None and i < self._size - 1:
                y = self._data[i+1]
                value = reduce_func(value, y)
        return value


def chunk(arr: DynamicArray) -> "DynamicArray":
    """
    Returns an array of arrays called chunk_arr, with arrays of ascending elements from arr

    :param arr: is a DynamicArray of elements

    :return: an array of arrays containing elements from arr in ascending order
    """
    # creates main array and starting values
    chunk_arr = DynamicArray()
    start_index = 0
    size = 1
    # iterates through old array, counting size if elements are in ascending order
    for i in range(start_index, arr.length()):
        if i <= arr.length() - 2 and arr.get_at_index(i) <= arr.get_at_index(i+1):
            size += 1

        # if not in ascending order or i == arr.length(),
        # slices old array to create a new array and appends it to DynamicArray
        if i == arr.length() - 1 or (arr.get_at_index(i) > arr.get_at_index(i+1)):
            new_arr = arr.slice(start_index, size)
            chunk_arr.append(new_arr)
            start_index = i + 1
            size = 1

            # increases capacity if new array size > new array capacity
            # while chunk_arr.length() > chunk_arr.get_capacity():
            #    chunk_arr.resize(chunk_arr.length() * 2)

    return chunk_arr


def find_mode(arr: DynamicArray) -> tuple[DynamicArray, int]:
    """
    Returns a tuple with mode_arr and frequency of element(s) in mode_arr.

    :param arr: a DynamicArray of elements passed to this function.

    :return: tuple with the DynamicArray of modes and an int of the frequency of those nodes
    """
    count = 0
    temp = 0
    mode_arr = DynamicArray()
    # iterates through arr determining the freq of mode(s)
    for i in range(0, arr.length()):
        if i == 0:
            count += 1
        # index > 0, compares current index to previous index. if not equal, starts a new count at 1
        else:
            if arr.get_at_index(i) == arr.get_at_index(i - 1):
                count += 1
            elif arr.get_at_index(i) != arr.get_at_index(i - 1):
                count = 1

        # if count > previous count, replaces mode_arr with new highest mode
        if count > temp:
            temp = count
            if mode_arr.length() > 0:
                mode_arr = DynamicArray()
            mode_arr.append(arr.get_at_index(i))
        # if count is equal to previous count, adds mode to array
        elif count == temp:
            temp = count
            mode_arr.append(arr.get_at_index(i))

    return mode_arr, temp


# ------------------- BASIC TESTING -----------------------------------------


if __name__ == "__main__":

    print("\n# resize - example 1")
    da = DynamicArray()

    # print dynamic array's size, capacity and the contents
    # of the underlying static array (data)
    # da.print_da_variables()
    # da.resize(8)
    # da.print_da_variables()
    # da.resize(2)
    # da.print_da_variables()
    # da.resize(0)
    # da.print_da_variables()

    print("\n# resize - example 2")
    # da = DynamicArray([1, 2, 3, 4, 5, 6, 7, 8])
    # print(da)
    # da.resize(20)
    # print(da)
    # da.resize(4)
    # print(da)

    print("\n# append - example 1")
    # da = DynamicArray()
    # da.print_da_variables()
    # da.append(1)
    # da.print_da_variables()
    # print(da)

    print("\n# append - example 2")
    # da = DynamicArray()
    # for i in range(9):
    #    da.append(i + 101)
    #    print(da)

    print("\n# append - example 3")
    # da = DynamicArray()
    # for i in range(600):
    #    da.append(i)
    # print(da.length())
    # print(da.get_capacity())

    print("\n# insert_at_index - example 1")
    # da = DynamicArray([100])
    # print(da)
    # da.insert_at_index(0, 200)
    # da.insert_at_index(0, 300)
    # da.insert_at_index(0, 400)
    # print(da)
    # da.insert_at_index(3, 500)
    # print(da)
    # da.insert_at_index(1, 600)
    # print(da)

    print("\n# insert_at_index example 2")
    # da = DynamicArray()
    # try:
    #    da.insert_at_index(-1, 100)
    # except Exception as e:
    #    print("Exception raised:", type(e))
    # da.insert_at_index(0, 200)
    # try:
    #    da.insert_at_index(2, 300)
    # except Exception as e:
    #    print("Exception raised:", type(e))
    # print(da)

    print("\n# insert at index example 3")
    # da = DynamicArray()
    # for i in range(1, 10):
    #    index, value = i - 4, i * 10
    #    try:
    #        da.insert_at_index(index, value)
    #    except Exception as e:
    #        print("Cannot insert value", value, "at index", index)
    # print(da)

#    print("\n# remove_at_index - example 1")
#    da = DynamicArray([10, 20, 30, 40, 50, 60, 70, 80])
#    print(da)
#    da.remove_at_index(0)
#    print(da)
#    da.remove_at_index(6)
#    print(da)
#    da.remove_at_index(2)
#    print(da)

#    print("\n# remove_at_index - example 2")
#    da = DynamicArray([1024])
#    print(da)
#    for i in range(17):
#        da.insert_at_index(i, i)
#    print(da.length(), da.get_capacity())
#    for i in range(16, -1, -1):
#        da.remove_at_index(0)
#    print(da)

#    print("\n# remove_at_index - example 3")
#    da = DynamicArray()
#    print(da.length(), da.get_capacity())
#    [da.append(1) for i in range(100)]  # step 1 - add 100 elements
#    print(da.length(), da.get_capacity())
#    [da.remove_at_index(0) for i in range(68)]  # step 2 - remove 68 elements
#    print(da.length(), da.get_capacity())
#    da.remove_at_index(0)  # step 3 - remove 1 element
#    print(da.length(), da.get_capacity())
#    da.remove_at_index(0)  # step 4 - remove 1 element
#    print(da.length(), da.get_capacity())
#    [da.remove_at_index(0) for i in range(14)]  # step 5 - remove 14 elements
#    print(da.length(), da.get_capacity())
#    da.remove_at_index(0)  # step 6 - remove 1 element
#    print(da.length(), da.get_capacity())
#    da.remove_at_index(0)  # step 7 - remove 1 element
#    print(da.length(), da.get_capacity())

#    for i in range(14):
#        print("Before remove_at_index(): ", da.length(), da.get_capacity(), end="")
#        da.remove_at_index(0)
#        print(" After remove_at_index(): ", da.length(), da.get_capacity())#

 #   print("\n# remove at index - example 4")
 #   da = DynamicArray([1, 2, 3, 4, 5])
 #   print(da)
 #   for _ in range(5):
 #       da.remove_at_index(0)
 #       print(da)

#    print("\n# slice example 1")
#    da = DynamicArray([1, 2, 3, 4, 5, 6, 7, 8, 9])
#    da_slice = da.slice(1, 3)
#    print(da, da_slice, sep="\n")
#    da_slice.remove_at_index(0)
#   print(da, da_slice, sep="\n")

#    print("\n# slice example 2")
#    da = DynamicArray([10, 11, 12, 13, 14, 15, 16])
#    print("SOURCE:", da)
#    slices = [(0, 7), (-1, 7), (0, 8), (2, 3), (5, 0), (5, 3), (6, 1), (6, -1)]
#    for i, cnt in slices:
#        print("Slice", i, "/", cnt, end="")
#        try:
#            print(" --- OK: ", da.slice(i, cnt))
#        except:
#            print(" --- exception occurred.")

#    print("\n# map example 1")
#    da = DynamicArray([1, 5, 10, 15, 20, 25])
#    print(da)
#    print(da.map(lambda x: x ** 2))

#    print("\n# map example 2")


#    def double(value):
#        return value * 2


    def square(value):
        return value ** 2


    def cube(value):
        return value ** 3


    def plus_one(value):
        return value + 1


#    da = DynamicArray([plus_one, double, square, cube])
#    for value in [1, 10, 20]:
#        print(da.map(lambda x: x(value)))

    print("\n# filter example 1")


    def filter_a(e):
        return e > 10


#    da = DynamicArray([1, 5, 10, 15, 20, 25])
#    print(da)
#    result = da.filter(filter_a)
#    print(result)
#    print(da.filter(lambda x: (10 <= x <= 20)))

    print("\n# filter example 2")


    def is_long_word(word, length):
        return len(word) > length


#    da = DynamicArray("This is a sentence with some long words".split())
#    print(da)
#    for length in [3, 4, 7]:
#        print(da.filter(lambda word: is_long_word(word, length)))

    print("\n# reduce example 1")
#    values = [100, 5, 10, 15, 20, 25]
#    da = DynamicArray(values)
#    print(da)
#    print(da.reduce(lambda x, y: (x // 5 + y ** 2)))
#    print(da.reduce(lambda x, y: (x + y ** 2), -1))

    print("\n# reduce example 2")
#    da = DynamicArray([100])
#    print(da.reduce(lambda x, y: x + y ** 2))
#    print(da.reduce(lambda x, y: x + y ** 2, -1))
#    da.remove_at_index(0)
#    print(da.reduce(lambda x, y: x + y ** 2))
#    print(da.reduce(lambda x, y: x + y ** 2, -1))

    def print_chunked_da(arr: DynamicArray):
        if len(str(arr)) <= 100:
            print(arr)
        else:
            print(f"DYN_ARR Size/Cap: {arr.length()}/{arr.get_capacity()}")
            print('[\n' + ',\n'.join(f'\t{chunk}' for chunk in arr) + '\n]')

    print("\n# chunk example 1")
    test_cases = [
        [10, 20, 30, 30, 5, 10, 1, 2, 3, 4],
        ['App', 'Async', 'Cloud', 'Data', 'Deploy',
         'C', 'Java', 'Python', 'Git', 'GitHub',
         'Class', 'Method', 'Heap']
    ]

    for case in test_cases:
        da = DynamicArray(case)
        chunked_da = chunk(da)
        print(da)
        print_chunked_da(chunked_da)

    print("\n# chunk example 2")
    test_cases = [[], [261], [1, 2, 4, 8, 16, 32, 64, 128, 256, 512]]

    for case in test_cases:
        da = DynamicArray(case)
        chunked_da = chunk(da)
        print(da)
        print_chunked_da(chunked_da)

    print("\n# find_mode - example 1")
    test_cases = (
        [1, 1, 2, 3, 3, 4],
        [1, 2, 3, 4, 5],
        ["Apple", "Banana", "Banana", "Carrot", "Carrot",
         "Date", "Date", "Date", "Eggplant", "Eggplant", "Eggplant",
         "Fig", "Fig", "Grape"]
    )

    for case in test_cases:
        da = DynamicArray(case)
        mode, frequency = find_mode(da)
        print(f"{da}\nMode: {mode}, Frequency: {frequency}\n")

    case = [4, 3, 3, 2, 2, 2, 1, 1, 1, 1]
    da = DynamicArray()
    for x in range(len(case)):
        da.append(case[x])
        mode, frequency = find_mode(da)
        print(f"{da}\nMode: {mode}, Frequency: {frequency}")
