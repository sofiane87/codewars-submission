
def line_intersection(line1, line2):
    line_type1 = 'hor' if line1[0][1] == line1[1][1] else 'vert'
    line_type2 = 'hor' if line2[0][1] == line2[1][1] else 'vert'
    if line_type1 == line_type2:
        dim = 0 if line_type1 == 'hor' else 1
        range1 = sorted([line1[0][dim], line1[1][dim]])
        range2 = sorted([line2[0][dim], line2[1][dim]])
        if line1[0][1-dim] == line2[0][1-dim]:
            if any([range2[0] <= elem <= range2[1] for elem in range1]):
                return True
            elif any([range1[0] <= elem <= range1[1] for elem in range2]):
                return True
        return False
    else:
        dim1 = 0 if line_type1 == 'hor' else 1
        dim2 = 0 if line_type2 == 'hor' else 1
        range1 = sorted([line1[0][dim1], line1[1][dim1]])
        range2 = sorted([line2[0][dim2], line2[1][dim2]])
        return (range2[0] <= line1[0][dim2] <= range2[1]) and (range1[0] <= line2[0][dim1] <= range1[1] )

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

def get_dir(dir, dim, turn):
    dir = dir * (-1)**((dim + (turn != 'R'))+1)
    dim = 1 - dim
    return dir, dim

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
    # Initial dimension in which the mouse is moving
    # As a convention R is increase and L is decreasing

    dim = 0
    dir = 1
    for move_index, move in enumerate(moves):
        if move[0] is not None:
            dir, dim = get_dir(dir, dim, move[0])
        dir_vector = [0, 0]
        dir_vector[dim] = dir
        current_position[dim] += dir * move[1]
        coordinates.append(list(current_position))
        new_line = coordinates[-2:]
        if move_index > 2:
            for index in range(move_index-1):
                line_1 = coordinates[index: index+2]
                intersect = line_intersection(line_1, new_line)
                if intersect and not(index == 0 and move_index == len(moves) - 1):
                    return None

    if coordinates[-1] != [0, 0] or coordinates[-2][0] == coordinates[1][0] or coordinates[-2][1] == coordinates[1][1]:
        return None

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
