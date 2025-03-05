


def pumpkin( m , n , matrix):
    result=[]
    for i in range (m):
        if i % 2 == 0:
            result.extend(matrix[i])
        else:
            result.extend(matrix[i][::-1])
    return result
matrix = [
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12],
    [13,14,15,16]
]
result = pumpkin(4,4,matrix)
print(result)



