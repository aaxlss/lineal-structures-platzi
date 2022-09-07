from pickletools import read_uint1
from Array import Array

class Grid():

    def __init__(self, rows, columns, fill_value = None):
        self.data = Array(rows)
        for i in range(self.data.__len__()):
            self.data.__set_item__(i, Array(columns))

            
    def __get_heigh__(self):
        return self.data.__len__()

    def __get_width__(self):
        item = self.data.__get_item__(0)
        return item.__len__()

    def __get_item__(self,index):
        return self.data[index]

    def __set_item__(self, column, row, value):
        self.data.__get_item__(row).__set_item_(column, value)

    def __str__(self):
        result = ''

        for row in range(self.__get_heigh__()):
            for col in range(self.__get_width__()):
                result += str(self.data[row][col])
            
            result += "\n"

        return result
