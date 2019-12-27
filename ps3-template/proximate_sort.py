def proximate_sort(A, k):
    '''
    Return an array containing the elements of
    input tuple A appearing in sorted order.
    Input:  k | an integer < len(A)
            A | a k-proximate tuple
    '''
    B = list(A)
    Q = []
    result = []

    def insert(Q, v):
        Q.append(v)
        min_heapify_up(Q, len(Q) - 1)

    def min_heapify_up(Q, i):
        if i > 0 and Q[i] < Q[(i-1)//2]:
            temp = Q[i]
            Q[i] = Q[(i-1)//2]
            Q[(i-1)//2] = temp
            min_heapify_up(Q, (i-1)//2)

    def min_heapify_down(Q, i, size):
        min = i
        left = 2*i+1
        right = 2*i+2

        if left < size and Q[i] > Q[left]:
            min = left
        if right < size and Q[min] > Q[right]:
            min = right
        if i != min:
            temp = Q[min]
            Q[min] = Q[i]
            Q[i] = temp
            min_heapify_down(Q, min, size)

    def remove_min(Q):
        min = 0
        temp = Q[0]
        Q[0] = Q[len(Q)-1]
        Q[len(Q)-1] = temp
        min = Q.pop()
        min_heapify_down(Q, 0, len(Q))
        return min

    for i in range(k+1):
        insert(Q, A[i])
    print(Q)
    result.append(remove_min(Q))


    for i in range(k+1, len(B)):
        insert(Q, A[i])
        result.append(remove_min(Q))

    while len(Q) > 0:
        result.append(remove_min(Q))

    return result


print(proximate_sort([-2,0,-5,-3,4,1,7,10,12,13], 3))