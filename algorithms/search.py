import time


def linear_search(seq: list | tuple, target: any) -> bool:
    for i in range(len(seq)):
        if seq[i] == target:
            return True
    return False


if __name__ == '__main__':
    a = [n for n in range(1_000_000)]

    # t1 = time.time()
    # print(binary_search(a, 999_999))
    # t = time.time() - t1
    # print(f"Binary Search: {t:.4f} seconds")
    
    t1 = time.time()
    print(linear_search(a, 999_999))
    t = time.time() - t1
    print(f"Linear Search: {t:.4f} seconds")

