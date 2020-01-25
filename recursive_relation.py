

def reproduction_recursive(n, k):
    if n == 0:
        return 0
    elif n == 1:
        return 1

    return reproduction_recursive(n - 1, k) + k * reproduction_recursive(n - 2, k)


if __name__ == "__main__":
    print(reproduction_recursive(34, 2))

