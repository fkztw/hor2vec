from hor2vec import __main__    # this import trashed the test coverage

# import hor2vec


import pytest
import argparse
import sys
import string
import io
import os
from collections import deque


class TestMain(object):

    @pytest.fixture
    def fixture_args(self):
        cases_to_save = {
            'case0': [
                        'tests/data/english_test_data.txt'],
            'case1': [
                        'input', 'tests/data/english_test_data.txt'],
            'case2': [
                        'input', 'tests/data/english_test_data.txt',
                        '-s', ' '],
            'case3': [
                        'input', 'tests/data/english_test_data.txt',
                        '-s', ' ',
                        '-ld', 'r2l'],
            'case4': [
                        'input', 'tests/data/english_test_data.txt',
                        '-s', ' ',
                        '-ld', 'r2l',
                        '-wd', 'b2t'],
            'case5': [
                        'input', 'tests/data/english_test_data.txt',
                        '-s', ' ',
                        '-ld', 'r2l',
                        '-wd', 'b2t',
                        '-nr'],
            'case6': [
                        'input', 'tests/data/english_test_data.txt',
                        '-s', ' ',
                        '-ld', 'r2l',
                        '-wd', 'b2t',
                        '-nr',
                        '-fw'],
            'case7': [
                        'input', 'tests/data/ascii_test_data.txt'],
        }

        cases_saved = {}
        for name, case in cases_to_save.items():
            if case[0] != 'input':
                case.insert(0, 'input')
            sys.argv = case
            args = __main__.get_args()
            cases_saved[name] = args
        return cases_saved

    @pytest.fixture
    def fixture_outputs(self):
        cases_outputs = {
            'case0':    'Iwtbyf Cw?\n'
                        ' aoeor ae\n'
                        ' n  ui n\n'
                        ' t  re\n'
                        '     n\n'
                        '     d\n'
                        '     .\n',

            'case1':    'Iwtbyf Cw?\n'
                        ' aoeor ae\n'
                        ' n  ui n\n'
                        ' t  re\n'
                        '     n\n'
                        '     d\n'
                        '     .\n',

            'case2':    'I w t b y f   C w ?\n'
                        '  a o e o r   a e\n'
                        '  n     u i   n\n'
                        '  t     r e\n'
                        '          n\n'
                        '          d\n'
                        '          .\n',

            'case3':    '? w C   f y b t w I\n'
                        '  e a   r o e o a\n'
                        '    n   i u     n\n'
                        '        e r     t\n'
                        '        n\n'
                        '        d\n'
                        '        .\n',

            'case4':    '        .\n'
                        '        d\n'
                        '        n\n'
                        '        e r     t\n'
                        '    n   i u     n\n'
                        '  e a   r o e o a\n'
                        '? w C   f y b t w I\n',

            'case5':    '            ?\n'
                        '          e w\n'
                        '        n a C\n'
                        '\n'
                        '. d n e i r f\n'
                        '      r u o y\n'
                        '          e b\n'
                        '          o t\n'
                        '      t n a w\n'
                        '            I\n',

            'case6':    '　 　 　 　 　 　 ？\n'
                        '　 　 　 　 　 ｅ ｗ\n'
                        '　 　 　 　 ｎ ａ Ｃ\n'
                        '\n'
                        '． ｄ ｎ ｅ ｉ ｒ ｆ\n'
                        '　 　 　 ｒ ｕ ｏ ｙ\n'
                        '　 　 　 　 　 ｅ ｂ\n'
                        '　 　 　 　 　 ｏ ｔ\n'
                        '　 　 　 ｔ ｎ ａ ｗ\n'
                        '　 　 　 　 　 　 Ｉ\n',

            'case7':    'SAcltt1dr:f¼½ac£¥.\n'
                        'eShahh2ee r　　nu\n'
                        'eCarae7cp a　　dr\n'
                        ' Irgn  ir c　　 r\n'
                        ' Ise   me t　　 e\n'
                        '   r   as i　　 n\n'
                        '       le o　　 c\n'
                        '        n n　　 i\n'
                        '        t s　　 e\n'
                        '        a  　　 s\n'
                        '        n\n'
                        '        t\n'
                        '        i\n'
                        '        o\n'
                        '        n\n',
        }
        return cases_outputs

    def test___main___global_variables(self):
        assert __main__.HALFWIDTH_SPACE == ' '
        assert __main__.FULLWIDTH_SPACE == '　'

        assert hasattr(__main__, 'get_args')
        assert hasattr(__main__, 'is_ascii')
        assert hasattr(__main__, 'fill_white_spaces')
        assert hasattr(__main__, 'turn_to_full_width_char')
        assert hasattr(__main__, 'turn_to_full_width_chars')
        assert hasattr(__main__, 'hor2vec')

    def test___main___get_args(self, fixture_args):
        args = fixture_args['case0']
        assert args is not None
        assert isinstance(args, argparse.Namespace)
        assert len(vars(args)) == 6
        assert 'input' in vars(args)
        assert 'sep' in vars(args)
        assert 'line_direction' in vars(args)
        assert 'word_direction' in vars(args)
        assert 'no_rotate' in vars(args)
        assert 'full_width' in vars(args)
        assert args.input.name == 'tests/data/english_test_data.txt'
        assert args.sep == ''
        assert args.line_direction == 'l2r'
        assert args.word_direction == 't2b'
        assert args.no_rotate is False
        assert args.full_width is False

        args = fixture_args['case1']
        assert args is not None
        assert isinstance(args, argparse.Namespace)
        assert len(vars(args)) == 6
        assert 'input' in vars(args)
        assert 'sep' in vars(args)
        assert 'line_direction' in vars(args)
        assert 'word_direction' in vars(args)
        assert 'no_rotate' in vars(args)
        assert 'full_width' in vars(args)
        assert args.input.name == 'tests/data/english_test_data.txt'
        assert args.sep == ''
        assert args.line_direction == 'l2r'
        assert args.word_direction == 't2b'
        assert args.no_rotate is False
        assert args.full_width is False

        args = fixture_args['case2']
        assert args is not None
        assert isinstance(args, argparse.Namespace)
        assert len(vars(args)) == 6
        assert 'input' in vars(args)
        assert 'sep' in vars(args)
        assert 'line_direction' in vars(args)
        assert 'word_direction' in vars(args)
        assert 'no_rotate' in vars(args)
        assert 'full_width' in vars(args)
        assert args.input.name == 'tests/data/english_test_data.txt'
        assert args.sep == ' '
        assert args.line_direction == 'l2r'
        assert args.word_direction == 't2b'
        assert args.no_rotate is False
        assert args.full_width is False

        args = fixture_args['case3']
        assert args is not None
        assert isinstance(args, argparse.Namespace)
        assert len(vars(args)) == 6
        assert 'input' in vars(args)
        assert 'sep' in vars(args)
        assert 'line_direction' in vars(args)
        assert 'word_direction' in vars(args)
        assert 'no_rotate' in vars(args)
        assert 'full_width' in vars(args)
        assert args.input.name == 'tests/data/english_test_data.txt'
        assert args.sep == ' '
        assert args.line_direction == 'r2l'
        assert args.word_direction == 't2b'
        assert args.no_rotate is False
        assert args.full_width is False

        args = fixture_args['case4']
        assert args is not None
        assert isinstance(args, argparse.Namespace)
        assert len(vars(args)) == 6
        assert 'input' in vars(args)
        assert 'sep' in vars(args)
        assert 'line_direction' in vars(args)
        assert 'word_direction' in vars(args)
        assert 'no_rotate' in vars(args)
        assert 'full_width' in vars(args)
        assert args.input.name == 'tests/data/english_test_data.txt'
        assert args.sep == ' '
        assert args.line_direction == 'r2l'
        assert args.word_direction == 'b2t'
        assert args.no_rotate is False
        assert args.full_width is False

        args = fixture_args['case5']
        assert args is not None
        assert isinstance(args, argparse.Namespace)
        assert len(vars(args)) == 6
        assert 'input' in vars(args)
        assert 'sep' in vars(args)
        assert 'line_direction' in vars(args)
        assert 'word_direction' in vars(args)
        assert 'no_rotate' in vars(args)
        assert 'full_width' in vars(args)
        assert args.input.name == 'tests/data/english_test_data.txt'
        assert args.sep == ' '
        assert args.line_direction == 'r2l'
        assert args.word_direction == 'b2t'
        assert args.no_rotate is True
        assert args.full_width is False

        args = fixture_args['case6']
        assert args is not None
        assert isinstance(args, argparse.Namespace)
        assert len(vars(args)) == 6
        assert 'input' in vars(args)
        assert 'sep' in vars(args)
        assert 'line_direction' in vars(args)
        assert 'word_direction' in vars(args)
        assert 'no_rotate' in vars(args)
        assert 'full_width' in vars(args)
        assert args.input.name == 'tests/data/english_test_data.txt'
        assert args.sep == ' '
        assert args.line_direction == 'r2l'
        assert args.word_direction == 'b2t'
        assert args.no_rotate is True
        assert args.full_width is True

        args = fixture_args['case7']
        assert args is not None
        assert isinstance(args, argparse.Namespace)
        assert len(vars(args)) == 6
        assert 'input' in vars(args)
        assert 'sep' in vars(args)
        assert 'line_direction' in vars(args)
        assert 'word_direction' in vars(args)
        assert 'no_rotate' in vars(args)
        assert 'full_width' in vars(args)
        assert args.input.name == 'tests/data/ascii_test_data.txt'
        assert args.sep == ''
        assert args.line_direction == 'l2r'
        assert args.word_direction == 't2b'
        assert args.no_rotate is False
        assert args.full_width is False

    def test___main___is_ascii(self):
        for n in range(0, 128):
            assert __main__.is_ascii(chr(n)) is True

        for n in range(128, 300):
            assert __main__.is_ascii(chr(n)) is False

    def test___main__fill_white_spaces(self, fixture_args):

        def prepare_params(args):
            content = ''.join(args.input.readlines())
            input_lines = content.rstrip().split('\n')
            input_lines_array = tuple(map(tuple, input_lines))
            len_of_longest_line = max(map(len, input_lines_array))
            return (input_lines_array, len_of_longest_line, args)

        for case_name, case_args in fixture_args.items():
            (lines, max_len, rargs) = prepare_params(case_args)
            filled_lines = []
            for line in lines:
                filled = __main__.fill_white_spaces(line, max_len, rargs)
                filled_lines.append(filled)
                assert isinstance(filled, tuple)
                assert not isinstance(filled, list)

                assert len(line) <= max_len
                assert len(line) <= len(filled)
                assert all(word in filled for word in line)

                spaces = [__main__.HALFWIDTH_SPACE, __main__.FULLWIDTH_SPACE]
                if len(line) < max_len:
                    assert any(space in filled for space in spaces)
                else:
                    assert not any(space in filled for space in spaces)

    def test__main__turn_to_full_width_chars(self):
        half_width_ascii_chars = [string.ascii_letters + string.punctuation]
        full_width_ascii_chars = ['ａｂｃｄｅｆｇｈｉｊｋｌｍｎｏｐｑｒｓｔｕｖｗｘｙｚＡＢＣＤＥＦＧＨＩＪＫＬＭＮＯＰＱＲＳＴＵＶＷＸＹＺ！＂＃＄％＆＇（）＊＋，－．／：；＜＝＞？＠［＼］＾＿｀｛｜｝～']
        assert full_width_ascii_chars == __main__.turn_to_full_width_chars(half_width_ascii_chars)

    def test___main__hor2vec(self, fixture_args, fixture_outputs):
        for case_name, case_args in fixture_args.items():
            saved_stdout = sys.stdout
            try:
                out = io.StringIO()
                sys.stdout = out

                __main__.hor2vec(case_args)

                output = out.getvalue()
                assert output == fixture_outputs[case_name]

            finally:
                sys.stdout = saved_stdout

    def test___main__if_name_main(self, monkeypatch):
        # This block of source-code...
        block_if_name_main = 'if __name__ == "__main__":\n'\
                             '    main()\n'                \

        # ...is not covered by the bellow test.

        # Despite this, the bellow test works.
        # But this test is useless, because...
        # ...it can not cover the above block of source-code.
        '''
        def faked_get_args():
            return 'faked get_args mocked successfully!'
        def faked_hor2vec():
            return 'faked hor2vec mocked successfully!'

        monkeypatch.setattr(__main__, 'get_args', faked_get_args)
        monkeypatch.setattr(__main__, 'hor2vec', faked_hor2vec)

        fga = __main__.get_args()
        fhv = __main__.hor2vec()

        assert fga == 'faked get_args mocked successfully!'
        assert fhv == 'faked hor2vec mocked successfully!'
        '''

        # So, below is written a...
        # ... simplistic, ugly and, hard coded test
        module_abspath = os.path.abspath(__main__.__file__)
        with open(module_abspath) as f:
            last_2_lines = deque(f, 2)
            assert ''.join(last_2_lines) == block_if_name_main
