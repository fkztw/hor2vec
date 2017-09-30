import sys
from argparse import ArgumentParser


HALFWIDTH_SPACE = ' '
FULLWIDTH_SPACE = '　'


def get_args():
    parser = ArgumentParser()

    parser.add_argument(
        'content',
        type=str,
        nargs='?',
        help="Pure text to be rearrange. If not been given in the command, will use the stdin as input."
    )

    parser.add_argument(
        '-s', '--sep', '--seprator',
        type=str,
        default='',
        help="The seperator between lines. Default is '', you can use ' ', '|' or any other strings."
    )

    parser.add_argument(
        '-ld', '--line-direction',
        type=str,
        default='l2r',
        choices=['l2r', 'r2l'],
        help="The reading direction of each line. Default is 'l2r' (left to right), you can choose 'r2l' (right to left)."
    )

    parser.add_argument(
        '-wd', '--word-direction',
        type=str,
        default='t2b',
        choices=['t2b', 'b2t'],
        help="The reading direction of each word. Default is 't2b' (top to bottom), you can choose 'b2t' (bottom to top)."
    )

    return parser.parse_args()


def is_ascii(c):
    if ord(c) < 128:
        return True
    return False


def fill_white_spaces(line_tuple, max_length, args):
    line_list = list(line_tuple)
    white_space = HALFWIDTH_SPACE
    if not all(map(is_ascii, line_tuple)):
        white_space = FULLWIDTH_SPACE

        if args.line_direction == 'l2r':
            line_list = [c + ' ' if is_ascii(c) else c for c in line_list]
        elif args.line_direction == 'r2l':
            line_list = [' ' + c if is_ascii(c) else c for c in line_list]

    line_list += [white_space] * (max_length - len(line_list))
    return tuple(line_list)


def hor2vec(args):
    content = args.content or ''.join(sys.stdin.readlines())

    horizontal_lines = content.rstrip().split('\n')

    horizontal_lines_array = tuple(map(tuple, horizontal_lines))
    len_of_longest_line = max(map(len, horizontal_lines_array))
    filled_horizontal_lines_array = tuple(
        fill_white_spaces(line, len_of_longest_line, args)
        for line in horizontal_lines_array
    )

    vertical_lines_array = tuple(zip(*filled_horizontal_lines_array))

    if args.line_direction == "l2r":
        vertical_lines = '\n'.join(
            (args.sep).join(vertical_line_array).rstrip()
            for vertical_line_array in vertical_lines_array
        )
    elif args.line_direction == "r2l":
        vertical_lines = '\n'.join(
            (args.sep).join(vertical_line_array)[::-1].rstrip()
            for vertical_line_array in vertical_lines_array
        )
    print(vertical_lines)


if __name__ == "__main__":
    args = get_args()
    hor2vec(args)
