def binary_search(arr, target):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = left + (right - left) // 2  # Calculate the middle index

        # Check if the target is equal to the middle element
        if arr[mid] == target:
            return mid

        # If the target is greater, ignore the left half
        elif arr[mid] < target:
            left = mid + 1

        # If the target is smaller, ignore the right half
        else:
            right = mid - 1

    # If the target is not in the list, return -1
    return -1

def main():
    arr = [2, 3, 4, 10, 40]
    target = 10

    result = binary_search(arr, target)

    if result != -1:
        print(f"Element {target} is found at index {result}")
    else:
        print(f"Element {target} is not found in the array")

main()
