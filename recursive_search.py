"""7. BONUS write a recursive searching algorithm to search for a number 
entered by user in a list of numbers.
"""

def main():
    nums = [1,5,2,5,2,1,5,6,3,6,23,12,6,7]

    target = int(input("Please enter a number to search: "))

    print(f"{target} was found at index {recursive_search(nums, target)}")


def recursive_search(arr, target, index=0):
    """
    Recursively searches for a target number in a list.

    Args:
        arr (list): The list of numbers to search.
        target (int): The number to search for.
        index (int): The current index in the list being checked (default is 0).

    Returns:
        int: The index of the target number if found, otherwise -1.
    """
    # Base case: If we've reached the end of the list, return -1 (not found)
    if index >= len(arr):
        return -1

    # If the current element matches the target, return the current index
    if arr[index] == target:
        return index

    # Recur to the next element in the list
    return recursive_search(arr, target, index + 1)
    

if __name__ == '__main__':
    main()
