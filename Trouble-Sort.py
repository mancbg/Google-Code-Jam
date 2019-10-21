def trouble_sort_checker(lst):
    # list(even list, odd list)
    lists = [list(), list()]

    # Partition the list based on the indices
    lists[0] = lst[::2]
    lists[1] = lst[1::2]

    # Sort both the lists
    lists[0] = sorted(lists[0])
    lists[1] = sorted(lists[1])

    even, odd = 0, 0
    while even < len(lists[0]) and odd < len(lists[1]):
        if lists[0][even] > lists[1][odd]:
            return even + odd
        even += 1
        if even == len(lists[0]):
            return 'OK'
        if lists[1][odd] > lists[0][even]:
            return even + odd
        odd += 1

    return 'OK'


def main():
    T = int(input())

    for i in range(T):
        int(input())
        lst = list(map(int, input().strip().split()))

        print("Case #" + str(i + 1) + ": " + str(trouble_sort_checker(lst)))

    # lst = list(map(int, input().strip().split()))
    #
    # print("Case #" + str(0 + 1) + ": " + str(trouble_sort_checker(lst)))


if __name__ == '__main__':
    main()
