import time


def linear_search(seq: list | tuple, target: any) -> bool:
    for i in range(len(seq)):
        if seq[i] == target:
            return True
    return False


def binary_search(seq: list | tuple, target: any) -> bool:
    """Returns `True` if target is in the sequence,
    else returns `False`
    
    Time Complexity: O(log n)"""
    if not seq:
        return False
    
    mid = len(seq) // 2
    left_half  = seq[:mid]
    right_half = seq[mid+1:]

    if target == seq[mid]:
        return True

    if target < seq[mid]:
        return binary_search(left_half, target)

    if target > seq[mid]:
        return binary_search(right_half, target)


if __name__ == '__main__':
    a = [n for n in range(1_000_000)]

    t1 = time.time()
    print(binary_search(a, 999_999))
    t = time.time() - t1
    print(f"Binary Search: {t:.4f} seconds")
    
    t1 = time.time()
    print(linear_search(a, 999_999))
    t = time.time() - t1
    print(f"Linear Search: {t:.4f} seconds")

