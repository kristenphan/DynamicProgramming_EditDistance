# python3


def edit_distance(a, b):

    # create a 2D array to store the result of the edit_distance
    T = [[float("inf")]*(len(b) +1) for _ in range(len(a)+1)]

    # iterate through the passed in string and fill in the result array
    for i in range(len(a)+1):
        T[i][0] = i
    for j in range(len(b)+1):
        T[0][j] = j
    for i in range(1, len(a)+1):
        for j in range(1, len(b)+1):
            diff = 0 if a[i-1]==b[j-1] else 1
            T[i][j] = min(T[i-1][j] + 1,
                          T[i][j-1] + 1,
                          T[i-1][j-1] + diff)

    return T[len(a)][len(b)]



if __name__ == "__main__":
    # print(edit_distance(input(), input()))
    a = "short"
    b = "ports"
    ans = 3
    print(edit_distance(a, b))
    assert edit_distance(a, b) == ans

