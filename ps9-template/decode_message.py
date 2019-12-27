def decode_message(A):
    """
    Return the first half of the longest palindrome subsequence of string A
    """
    m = len(A)
    B = A[::-1]

    x = [[0] * (m+1) for _ in range(m+1)]

    for i in range(1, m+1):
        for j in range(1, m+1):
            if A[i-1] == B[j-1]:
                x[i][j] = x[i-1][j-1]+1
            else:
                if x[i][j-1] < x[i-1][j]:
                    x[i][j] = x[i-1][j]
                else:
                    x[i][j] = x[i][j-1]

    a = m
    b = m
    result = []
    while a > 0 and b > 0:
        if A[a-1] == B[b-1]:
            result.append(A[a-1])
            a -= 1
            b -= 1
        elif x[a-1][b] < x[a][b-1]:
            b -= 1
        else:
            a -= 1

    return ''.join(result)[:(int(x[m][m]/2)+1)]