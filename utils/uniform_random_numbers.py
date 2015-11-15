import numpy as np

class UniformRandomNumbers:
    """
    Class for storing Randomly Generated Numbers
    Using NumPy
    """

    def __init__(self, low, high, sample_size):
        self.random_numbers = np.random.uniform(low, high, sample_size)
        self.all_numbers = self.random_numbers.tolist()
        self.random_numbers =self.random_numbers.tolist()


    def get_next(self):
        if (self.empty()):
            return None
        return self.random_numbers.pop()


    def empty(self):
        return len(self.random_numbers) == 0


    def get_all_numbers(self):
        return self.all_numbers
