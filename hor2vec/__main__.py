import argparse
import sys


HALFWIDTH_SPACE = ' '
FULLWIDTH_SPACE = '　'


def get_args():
    parser = argparse.ArgumentParser()

    parser.add_argument(
        'input',
        type=argparse.FileType('r'),
        nargs='?',
        default=sys.stdin,
        help=(
            "The file contains puretext to be re-arranged. "
            "If not been given in the command, will use the stdin as input."
        )
    )

    parser.add_argument(
        '-s', '--sep', '--seprator',
        type=str,
        default='',
        help=(
            "The seperator between lines. "
            "Default is '', you can use ' ', '|' or any other strings."
        )
    )

    parser.add_argument(
        '-ld', '--line-direction',
        type=str,
        default='l2r',
        choices=['l2r', 'r2l'],
        help=(
            "The reading direction of each line. "
            "Default is 'l2r' (left to right), "
            "you can choose 'r2l' (right to left)."
        )
    )

    parser.add_argument(
        '-wd', '--word-direction',
        type=str,
        default='t2b',
        choices=['t2b', 'b2t'],
        help=(
            "The reading direction of each word. "
            "Default is 't2b' (top to bottom), "
            "you can choose 'b2t' (bottom to top)."
        )
    )

    parser.add_argument(
        '-nr', '--no-rotate',
        action='store_true',
        default=False,
        help="If this optioin has been given, hor2vec won't rotate the input."
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

        line_list = [
            (("{} ", " {}")[args.line_direction == "r2l"]).format(c)
            if is_ascii(c) else c
            for c in line_list
        ]

    line_list += [white_space] * (max_length - len(line_list))
    return tuple(line_list)


def hor2vec(args):
    content = ''.join(args.input.readlines())

    horizontal_lines = content.rstrip().split('\n')

    horizontal_lines_array = tuple(map(tuple, horizontal_lines))
    len_of_longest_line = max(map(len, horizontal_lines_array))
    filled_horizontal_lines_array = tuple(
        fill_white_spaces(line, len_of_longest_line, args)
        for line in horizontal_lines_array
    )

    if args.no_rotate:
        vertical_lines_array = filled_horizontal_lines_array
    else:
        vertical_lines_array = tuple(zip(*filled_horizontal_lines_array))

    vertical_lines = '\n'.join(
        (args.sep).join(vertical_line_array)[::(1 - 2*(args.line_direction == "r2l"))].rstrip()
        for vertical_line_array in vertical_lines_array[::(1 - 2*(args.word_direction == "b2t"))]
    )
    print(vertical_lines)


if __name__ == "__main__":
    args = get_args()
    hor2vec(args)
