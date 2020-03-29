

def reproduction_recursive(month: int, initate_sequence: int) -> int:
    if month == 0:
        return 0
    elif month == 1:
        return 1

    return reproduction_recursive(month - 1, initate_sequence) + initate_sequence * reproduction_recursive(month - 2, initate_sequence)


if __name__ == "__main__":
    print(reproduction_recursive(3, 2))

