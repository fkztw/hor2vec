#!/usr/bin/env python3

import argparse
import string
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
            "The file has horizontal pure text to be changed to vertical. "
            "If not been given in the command, will use the stdin as input."
        )
    )

    parser.add_argument(
        '-s', '--sep', '--separator',
        type=str,
        default='',
        help=(
            "The separator between lines. "
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
            "The reading direction of each word/character. "
            "Default is 't2b' (top to bottom), "
            "you can choose 'b2t' (bottom to top)."
        )
    )

    parser.add_argument(
        '-nr', '--no-rotate',
        action='store_true',
        default=False,
        help="If this option has been given, hor2vec won't rotate the input."
    )

    parser.add_argument(
        '-fw', '--full-width',
        action='store_true',
        default=False,
        help="If this option has been given, hor2vec will use fullwidth characters instead of halfwidth characters."
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


def turn_to_full_width_char(char):
    full_width_char = chr(0x0FEE0 + ord(char))
    return full_width_char


def turn_to_full_width_chars(input_lines):
    for i, line in enumerate(input_lines):
        for j, char in enumerate(line):
            if is_ascii(char):
                input_lines[i] = (
                    input_lines[i][:j] +
                    turn_to_full_width_char(char) +
                    input_lines[i][j+1:]
                )
    return input_lines


def hor2vec(args):
    content = ''.join(args.input.readlines())

    input_lines = content.rstrip().split('\n')

    if args.full_width:
        turn_to_full_width_chars(input_lines)

    input_lines_array = tuple(map(tuple, input_lines))
    len_of_longest_line = max(map(len, input_lines_array))
    filled_input_lines_array = tuple(
        fill_white_spaces(line, len_of_longest_line, args)
        for line in input_lines_array
    )

    if args.no_rotate:
        output_lines_array = filled_input_lines_array
    else:
        output_lines_array = tuple(zip(*filled_input_lines_array))

    output_lines = '\n'.join(
        (args.sep).join(output_line_array)[
            ::(1 - 2*(args.line_direction == "r2l"))].rstrip()
        for output_line_array in output_lines_array[
            ::(1 - 2*(args.word_direction == "b2t"))]
    )
    print(output_lines)


def main():
    args = get_args()
    hor2vec(args)


if __name__ == "__main__":
    main()
