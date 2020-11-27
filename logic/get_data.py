def get_data(file_number):
    with open('../in/in' + str(file_number), 'r') as file:
        width, height = [int(number) for number in file.readline().split()]
        matrix = []
        chars = []

        for row in file.readlines():
            matrix.append(row.replace('\n', ''))
            for sym in row:
                if sym != '\n' and sym not in chars:
                    chars.append(sym)

        chars.sort()

    return {'width': width, 'height': height, 'matrix': matrix, 'chars': chars}


if __name__ == '__main__':
    print(get_data(1))
