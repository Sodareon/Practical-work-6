
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


if __name__ == "__main__":
    input_matrix = [[1, 2], [1, 0]]
    print(integral_view(input_matrix))
