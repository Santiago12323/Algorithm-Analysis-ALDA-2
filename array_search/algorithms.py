def binary_search(list, element):  # O(log n)
    left = 0  # O(1)
    right = len(list) - 1  # O(1)
    while left <= right:  # Executes O(log n) times
        middle: int = (right + left) // 2  # O(1)
        if list[middle] == element:  # O(1)
            return middle  # O(1)
        if list[middle] < element:  # O(1)
            left = middle + 1  # O(1)
        else:
            right = middle - 1  # O(1)
    return -1  # O(1)

def linear_search(list, element):  # O(n)
    for i in range(len(list)):  # Executes O(n) times
        if list[i] == element:  # O(1)
            return i  # O(1)
    return -1  # O(1)

def ternary_search(list, element):  # O(log₃ n)
    left = 0  # O(1)
    right = len(list) - 1  # O(1)
    while left <= right:  # Executes O(log₃ n) times
        middleleft = left + (right - left) // 3  # O(1)
        middleright = right - (right - left) // 3  # O(1)
        if list[middleleft] == element:  # O(1)
            return middleleft  # O(1)
        if list[middleright] == element:  # O(1)
            return middleright  # O(1)
        if element < list[middleleft]:  # O(1)
            right = middleleft - 1  # O(1)
        elif element > list[middleright]:  # O(1)
            left = middleright + 1  # O(1)
        else:
            left = middleleft + 1  # O(1)
            right = middleright - 1  # O(1)
    return -1  # O(1)
