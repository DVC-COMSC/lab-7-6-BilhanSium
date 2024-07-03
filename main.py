def getInput():
    """
    Prompts the user to enter multiple values in a single line.
    Splits these values and converts them into a list of integers.
    Returns the list of integers.
    """
    user_input = input("Enter multiple values separated by space: ")
    return list(map(int, user_input.split()))

def evenList(numbers):
    """
    Takes a list of numbers as input and returns a new list with the numbers at the even index.
    """
    result = []
    for i in range(len(numbers)):
        if i % 2 == 0:
            result.append(numbers[i])
    return result

def main():
    numbers = getInput()
    ret = evenList(numbers)
    print(f'The result values are: {ret}')

if __name__ == '__main__':
    main()
