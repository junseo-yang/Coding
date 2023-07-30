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
    def _resize(self, new_cap):
        B = self.ma
    def append(self, e):
        """
        Add an element to the end of the array
        """
        if self.n == self.capacity:

        self.A[self.n] = e
        self.n += 1
    def __get_item__(self, i):
        """
        Returns an element at index i
        """
        if not 0 <= i < self.n:
            return IndexError(f'index {i} is out of bounds')
        return self.A[i]
    
da = DynamicArray()

# len
print(len(da))

# is_empty
print(da.is_empty())

print(da.get_item())