import ctypes

class DynamicArray(object):
    '''
    Dynamic Array Class (Similar to Python List)
    '''
    def __init__(self):
        self.n = 0
        self.capacity = 1
        self.A = self.make_array(self.capacity)

    def make_array(self, new_cap):
        """
        Returns a new array with new_cap capacity
        """
        return (new_cap * ctypes.py_object) ()

    def __len__(self):
        return self.n

    def is_empty(self):
        if self.n == 0:
            return True
        else:
            return False
da = DynamicArray()

# len
print(len(da))

print(da.is_empty())