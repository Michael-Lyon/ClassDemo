lst = [1, 30, 3, 40, 10, 10, 25, 50]

def large(param: list):
    """This function takes in a list and returns the largest number in it."""
    largest = 0
    for x in param:
        if x > largest:
            largest = x
    return largest


print(large(lst))


