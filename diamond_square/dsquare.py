import random

x, y = 5, 5
matrix = [[0 for _ in range(y)] for _ in range(x)]
heights = [1, 8]
random_range = [-2, 2]

def get_random():
    return random.randint(random_range[0], random_range[1])

def get_random_height():
    return random.randint(heights[0], heights[1])

def show(matrix, show_brackets =True):
    for row in matrix:
        if show_brackets:
            print(row)
        else:
            print(" ".join(row))

def get_dimensions(matrix):
    return len(matrix), len(matrix[0])

def get_corners_position(matrix):
    dimensions = get_dimensions(matrix)
    x, y = dimensions[0] - 1, dimensions[1] - 1

    return (0, 0), (0, y), (x, 0), (x, y)

def assign_corner_height(matrix):
    corners = get_corners_position(matrix)
    
    for coord in corners:
        x, y = coord
        matrix[x][y] = get_random_height()


def get_mid_point(matrix):
    rows, columns = get_dimensions(matrix)

    return int((rows - 1) / 2), int((columns - 1) / 2)

def get_corner_average_and_assing_mid_point(matrix):
    corners = get_corners_position(matrix)
    corner_average = int(sum([matrix[x][y] for x, y in corners]) / 4)

    mid_x, mid_y = get_mid_point(matrix)
    
    matrix[mid_x][mid_y] = corner_average + get_random()

def get_mid_edge_point(matrix):
    dims = get_dimensions(matrix)
    x, y = dims[0] - 1, dims[1] - 1
    
    mid_top = 0, int(y / 2)
    mid_bottom = x, int(y / 2)
    mid_left = int(x / 2), 0
    mid_right = int(x / 2), y

    return mid_top, mid_bottom, mid_left, mid_right

#(0, 0) (0, 1) (0, 2)
#(1, 0) (1, 1) (1, 2)
#(2, 0) (2, 1) (2, 2)

def get_edge_value(matrix, x, y):
    rows, columns = get_dimensions(matrix)
    
    if x == 0:
        return matrix[0][0] + matrix[0][columns - 1]
    elif x == (rows - 1):
        return matrix[rows - 1][0] + matrix[rows - 1][columns - 1]
    elif y == 0:
        return matrix[0][0] + matrix[rows - 1][0]
    elif y == (columns - 1):
        return matrix[0][columns -1] + matrix[rows - 1][columns - 1]


def assign_mid_point_value(matrix):
    mid_x, mid_y = get_mid_point(matrix)
    edge_values = get_mid_edge_point(matrix)


    for x, y in edge_values:
        value = get_edge_value(matrix, x, y)
        matrix[x][y] = int(((value + matrix[mid_x][mid_y]) / 3) + get_random())


assign_corner_height(matrix)
get_corner_average_and_assing_mid_point(matrix)
assign_mid_point_value(matrix)

show(matrix)


