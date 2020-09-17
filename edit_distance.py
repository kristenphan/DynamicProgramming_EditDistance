# python3


def edit_distance(a, b):
    """ Compute the edit distance of string a and b
    Runtime: O(m x n) with m = len(a) and n = len(b)
    Space complexity: O(m x n)
    Example:
    input:
    a = "editing"
    b = "distance"
    output: 5
    explanation: an alignment of total cost of 5
    e d i - t i n g -
    - d i s t a n c e
    """

    # Create a 2D array d to store the edit distances (ED) for all substrings of a and b
    d = [[float("inf")]*(len(b) + 1) for _ in range(len(a)+1)]

    # If one of the substrings is empty, ED equals to length of the other substring
    for i in range(len(a)+1):
        d[i][0] = i
    for j in range(len(b)+1):
        d[0][j] = j

    # For any two substrings, the last column of the optimal alignment is
    # either an insertion, a deletion or a match/mismatch
    # What is left is to ensure the optimal alignment of the prefixes of the two substrings
    for i in range(1, len(a)+1):
        for j in range(1, len(b)+1):
            diff = 0 if a[i-1] == b[j-1] else 1
            d[i][j] = min(d[i-1][j] + 1,        # insertion
                          d[i][j-1] + 1,        # deletion
                          d[i-1][j-1] + diff)   # match/ mismatch

    return d[len(a)][len(b)]


if __name__ == "__main__":
    print(edit_distance(input(), input()))
