"""Given an n x n array, return the array elements arranged from outermost elements to the middle element, traveling clockwise."""

def snail(snail_map):
    answer = []
    matrix_size = len(snail_map[0])

    for i in range(matrix_size):
        number = snail_map[0][i]
        answer.append(number)

    for j in range(0, matrix_size // 2):

        for i in range(1, matrix_size - 2 * j):
            number = snail_map[j + i][matrix_size - 1 - j]
            answer.append(number)
        for i in range(1, matrix_size - 2 * j):
            number = snail_map[matrix_size - 1 - j][matrix_size - 1 - i - j]
            answer.append(number)
        for i in range(1, matrix_size - (2 * j + 1)):
            number = snail_map[matrix_size - i - j - 1][j]
            answer.append(number)
        for i in range(1, matrix_size - (2 * j + 1)):
            number = snail_map[j + 1][i + j]
            answer.append(number)

    return answer
