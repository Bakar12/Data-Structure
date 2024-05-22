class DoubleArray:

    # Initialize the array with default capacity
    def __init__(self):
        self.capacity = 1
        self.length = 0
        self.array = [None] * self.capacity

    # Method to get the value at a particular index
    def __getitem__(self, index):
        if not 0 <= index < self.length:
            raise IndexError("Index out of range")
        return self.array[index]

    # Method to set the value at a particular index
    def __setitem__(self, index, value):
        if not 0 <= index < self.length:
            raise IndexError("Index out of range")
        self.array[index] = value

    # Method to append a value to the end of the array
    def append(self, value):
        if self.length == self.capacity:
            self._resize(2 * self.capacity)  # Double the capacity if the array is full
        self.array[self.length] = value
        self.length += 1

    # Method to resize the array
    def _resize(self, new_capacity):
        new_array = [None] * new_capacity  # Create a new array with the new capacity
        for i in range(self.length):
            new_array[i] = self.array[i]  # Copy elements from the old array to the new array
        self.array = new_array
        self.capacity = new_capacity

    # Method to get the length of the array
    def __len__(self):
        return self.length

    # Method to print the capacity and length of the array
    def print_capacity_length(self):
        print(f"Capacity: {self.capacity}, Length: {self.length}")

    # Method to input values until the user decides to quit
    def input_until_quit(self):
        while True:  # Keep asking for input until the user decides to quit
            value = input("Enter a value (or 'q' to quit): ")
            if value.lower() == 'q':  # If the user enters 'q', quit the loop
                break
            self.append(value)  # Append the value to the array
            self.print_capacity_length()  # Print the capacity and length of the array

arr = DoubleArray()
arr.input_until_quit()