
import copy


def integral_view(image: list[list]) -> list[list]:
    """
    Функция осуществлять расчёт матрицы интегрального представления изображения

    :param image: Матрица контрастности пикселей изображения
    :type image: list[list]
    :return: Матрица интегрально представления изображения
    :rtype: list[list]
    """
    integral_matrix = copy.deepcopy(image)
    integral_element(len(integral_matrix)-1, len(integral_matrix[0])-1, image, integral_matrix)
    return integral_matrix


def integral_element(i, j, matrix, integral_matrix):
    """
    Функция вычисляет i,j элемент матрицы интегрального представления изображения

    :param i: Число - номер строки
    :type i: int
    :param j: Число - номер столбца
    :type j: int
    :param matrix: Матрица контрастности пикселей изображения
    :type matrix: list[list]
    :param integral_matrix: Матрица интегрального представления изображения
    :type integral_matrix: list[list]
    :return: Элемент i,j матрицы интегрального представления изображения
    :rtype: int
    """
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
    """
    Функция находит сумму пикселей произвольного прямоугольника, ограниченного заданными пикселями

    :param image: Матрица контрастности пикселей изображения
    :type image: list[list]
    :param x1: x координата верхнего левого угла прямоугольника
    :type x1: int
    :param y1: y координата верхнего левого угла прямоугольника
    :type y1: int
    :param x2: x координата нижнего правого угла прямоугольника
    :type x2: int
    :param y2: y координата нижнего правого угла прямоугольника
    :type y2: int
    :return: Сумма пикселей прямоугольника
    :rtype: int
    """
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
