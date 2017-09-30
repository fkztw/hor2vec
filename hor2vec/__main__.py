import sys


HALFWIDTH_SPACE = ' '
FULLWIDTH_SPACE = '　'


def is_ascii(c):
    if ord(c) < 128:
        return True
    return False


def fill_white_spaces(line_tuple, max_length):
    line_list = list(line_tuple)
    white_space = HALFWIDTH_SPACE
    if not all(map(is_ascii, line_tuple)):
        white_space = FULLWIDTH_SPACE
        # line_list = [c + ' ' if is_ascii(c) else c for c in line_list]
        line_list = [' ' + c if is_ascii(c) else c for c in line_list]

    line_list += [white_space] * (max_length - len(line_list))
    return tuple(line_list)


def hor2vec():
    content = ''.join(sys.stdin.readlines())

    horizontal_lines = content.rstrip().split('\n')

    horizontal_lines_array = tuple(map(tuple, horizontal_lines))
    len_of_longest_line = max(map(len, horizontal_lines_array))
    filled_horizontal_lines_array = tuple(
        fill_white_spaces(line, len_of_longest_line)
        for line in horizontal_lines_array
    )

    vertical_lines_array = tuple(zip(*filled_horizontal_lines_array))

    vertical_lines = '\n'.join(
        # ''.join(vertical_line_array).rstrip()
        ''.join(vertical_line_array)[::-1].rstrip()
        for vertical_line_array in vertical_lines_array
    )
    print(vertical_lines)


if __name__ == "__main__":
    hor2vec()
