def getInput():
    """
    Prompts the user to enter multiple values in a single line.
    Splits these values and converts them into a list of integers.
    Returns the list of integers.
    """
    user_input = input("Enter multiple values separated by space: ")
    return list(map(int, user_input.split()))

def makeReverse(numbers):
    """
    Takes a list of numbers, creates a new list with the numbers in reverse order,
    and returns the new list.
    """
    result = []
    while numbers:
        result.append(numbers.pop())
    return result

def main():
    numbers = getInput()
    ret = makeReverse(numbers)
    print(f'The result values are: {ret}')

if __name__ == '__main__':
    main()
