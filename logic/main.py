from logic.get_data import get_data
from logic.write_data import write_data


def get_number_of_possible_ways(matrix: list, height: int, width: int, exits: tuple, chars: list):

    # number of solutions from every cell of the most left column
    solutions_for_each_char_in_first_col = [0 for _ in range(height)]

    path_through_char_count = {char: 0 for char in chars}

    for i in exits:
        solutions_for_each_char_in_first_col[i] = 1
        path_through_char_count[matrix[i][width - 1]] += 1

    # loop in reverse order
    # start from `width-2` (prelast col), to `-1` (first col), with step `-1`
    for j in range(width - 2, -1, -1):
        found_solutions = {}

        for i in range(height):
            current_cell_char = matrix[i][j]
            if current_cell_char == matrix[i][j + 1]:
                current_solution = path_through_char_count[current_cell_char]
            else:
                current_solution = solutions_for_each_char_in_first_col[i] + path_through_char_count[current_cell_char]
            solutions_for_each_char_in_first_col[i] = current_solution

            if found_solutions.keys().__contains__(current_cell_char):
                found_solutions[current_cell_char] += current_solution
            else:
                found_solutions[current_cell_char] = current_solution

        for char, found_solutions_quantity in found_solutions.items():
            path_through_char_count[char] += found_solutions_quantity

    return sum(solutions_for_each_char_in_first_col)


def main():
    FILE_NUMBER = 3

    data = get_data(FILE_NUMBER)

    width = data['width']
    height = data['height']
    matrix = data['matrix']
    chars = data['chars']

    exits = (0, height - 1)

    result = get_number_of_possible_ways(matrix, height, width, exits, chars)

    write_data(FILE_NUMBER, result)

    print(result)


if __name__ == '__main__':
    main()
