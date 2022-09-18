
import copy


def integral_view(image: list[list]) -> list[list]:
    integral_matrix = copy.deepcopy(image)
    integral_element(len(integral_matrix)-1, len(integral_matrix[0])-1, image, integral_matrix)
    return integral_matrix


def integral_element(i, j, matrix, integral_matrix):
    if i == 0 and j == 0:
        integral_matrix[i][j] = matrix[i][j]
    elif i == 0:
        integral_matrix[i][j] = matrix[i][j] + integral_element(i, j-1, matrix, integral_matrix)
    elif j == 0:
        integral_matrix[i][j] = matrix[i][j] + integral_element(i-1, j, matrix, integral_matrix)
    else:
        integral_matrix[i][j] = matrix[i][j] - integral_element(i-1, j-1, matrix, integral_matrix) +\
                                integral_element(i, j-1, matrix, integral_matrix) +\
                                integral_element(i-1, j, matrix, integral_matrix)
    return integral_matrix[i][j]


def rect_sum(image: list[list], x1: int, y1: int, x2: int, y2: int) -> int:
    integral_matrix = integral_view(image)
    if x1 >= x2 or y1 >= y2 or x1 < 0 or y1 < 0:
        return 0
    elif x1 == 0 and y1 == 0:
        return integral_matrix[y2 - 1][x2 - 1]
    elif x1 == 0:
        return integral_matrix[y2 - 1][x2 - 1] - integral_matrix[y1-1][x2-1]
    elif y1 == 0:
        return integral_matrix[y2 - 1][x2 - 1] - integral_matrix[y2-1][x1-1]
    else:
        return integral_matrix[y2-1][x2-1] + integral_matrix[y1-1][x1-1] - \
               integral_matrix[y2-1][x1-1] - integral_matrix[y1-1][x2-1]


if __name__ == "__main__":
    input_matrix = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
    print(integral_view(input_matrix))
    print(rect_sum(input_matrix, 1, 0, 2, 3))
