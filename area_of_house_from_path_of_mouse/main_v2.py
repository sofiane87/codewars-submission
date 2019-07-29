@profile
def PolygonArea(corners):
    # ShoeLace Algorithm
    n = len(corners)
    area = 0.0
    for i in range(n):
        j = (i + 1) % n
        area += corners[i][0] * corners[j][1]
        area -= corners[j][0] * corners[i][1]
    area = abs(area) / 2.0
    return int(area)

@profile
def get_dir(dir, dim, turn):
    dir = dir * (-1)**((dim + (turn != 'R'))+1)
    dim = 1 - dim
    return dir, dim

@profile
def mouse_path(path):
    # Parsing Text
    moves = []
    move_length = ''
    str_index = 0
    previous_char = None
    while str_index < len(path):
        current_char = path[str_index]
        if current_char.isalpha():
            moves.append((previous_char, int(move_length)))
            move_length = ''
            previous_char = current_char
        else:
            move_length += current_char
        str_index += 1

    if len(move_length) > 0:
        moves.append((previous_char, int(move_length)))

    # Initialising Coordinates
    coordinates = [[0, 0]]
    current_position = [0, 0]
    points = dict()
    # Initial dimension in which the mouse is moving
    # As a convention R is increase and L is decreasing

    dim = 0
    dir = 1
    for move in moves:
        if move[0] is not None:
            dir, dim = get_dir(dir, dim, move[0])

        for _mv in range(move[1]):
            visited_point = list(current_position)
            visited_point[dim] += dir * _mv
            visited_point = tuple(visited_point)
            if visited_point in points:
                return None
            else:
                points[visited_point] = None

        dir_vector = [0, 0]
        dir_vector[dim] = dir
        current_position[dim] += dir * move[1]
        coordinates.append(list(current_position))

    # Computing area
    area = PolygonArea(coordinates)
    return area


if __name__ == '__main__':
    tests = [('4R2L1R5R9R4R4L3', 49),
             ('1000000R1000000R1000000R1000000', 1000000000000),
             ('10R5R5R10L5L5', None),
             ('12R6R2R2R1L1L1R2L1L1R4R2L1L5R1L3R6R2R1L2R2L4', None),
             ('14R11R10R4L1L4R3R7R10R3R3L1L4L5L11R3', 132),
             ('4L10L20L30L30L50L40L60L60L85L77L10L67R72R45R47R33R30R17R15R5R5', 2950)
             ]

    for index, (path, outcome) in enumerate(tests):
        area = mouse_path(path)
        print('Expected : {} - Predicted : {}'.format(outcome, area))
    # fig = plt.Figure()
    # for index, (path, outcome) in enumerate(tests):
    #     ax = plt.subplot('32{}'.format(index+1))
    #     coords = mouse_path(path)
    #     x, y = zip(*coords)
    #     ax.plot(x, y, color='#6699cc', alpha=0.7, linewidth=3, solid_capstyle='round', zorder=2)
    #     ax.set_title(path)
    # plt.show()
    #     # print('expected : {} - predicted: {} - Match: {}'.format(outcome, predicted_surface, outcome == predicted_surface))
