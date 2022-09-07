class Array:

    def __init__(self, capacity, fill_value = None) :

        self.items = list()
        
        for i in range(capacity):
            self.items.append(fill_value)

    def __len__(self):
        """
        Returns the lenght of the Array
        """
        return len(self.items)

    def __str__(self):
        """
            Return the content of the array cast as a String
        """
        return str(self.items)

    def __iter__(self) -> str:
        """
            Return the array as a iterable
        """
        return iter(self.items)

    def __get_item__(self, index) -> int:
        """
            Return de item that has been indicated in the index
        """
        return self.items[index]

    def __set_item__(self, index, value) -> None:
        """
            Replace the value of the current index by the new value
        """
        self.items[index] = value