def second_largest():
    lst = list(map(int, input("Enter numbers separated by space: ").split()))
    lst = list(set(lst))  # remove duplicates
    lst.sort()
    if len(lst) < 2:
        print("No second largest number.")
    else:
        print("Second largest number is:", lst[-2])

if __name__ == "__main__":
    second_largest()