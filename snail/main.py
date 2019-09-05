import numpy as np


def snail(snail_map):
    snail_array = np.array(snail_map)
    if snail_array.shape[1] == 0:
        return []
    n = snail_array.shape[0]
    explored = [None for x in range(n**2)]
    results = [None for x in range(n**2)]
    current_direction = np.array([0, 1])
    current_coordinates = np.array([0, 0])
    current_index = 0
    for current_index in range(n**2):
        new_coordinates = current_coordinates + current_direction
        if not((new_coordinates >= 0).all() and (new_coordinates < n).all() and tuple(new_coordinates) not in explored) and (current_index != n**2-1):
            current_direction = current_direction[::-1] * ((-1) ** (np.argmax(np.abs(current_direction)) + 1))
            new_coordinates = current_coordinates + current_direction
        explored[current_index] = tuple(current_coordinates)
        results[current_index] = snail_array[current_coordinates[0], current_coordinates[1]]
        current_coordinates = new_coordinates

    return results


if __name__ == '__main__':
    array = [[1, 2, 3],
             [4, 5, 6],
             [7, 8, 9]]
    expected = [1, 2, 3, 6, 9, 8, 7, 4, 5]
    print(snail(array) == expected)

    array = [[1, 2, 3],
             [8, 9, 4],
             [7, 6, 5]]
    expected = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    print(snail(array) == expected)
