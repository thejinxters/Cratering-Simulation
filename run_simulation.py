from utils import *


def main():
    random_numbers = UniformRandomNumbers(0, 500, 100)

    while not random_numbers.empty():
        print random_numbers.get_next()






if __name__ == "__main__":
    main()
