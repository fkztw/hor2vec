from hor2vec import __main__    #this import trashed the test coverage

#import hor2vec


import pytest
import argparse
import sys

class TestMain(object):
    
    @pytest.fixture
    def fixture_args(self):
        cases_to_save = {
            'case0': [
                        'tests/data/english_test_data.txt'],
            'case1': [
                        'input','tests/data/english_test_data.txt'],
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
                        'input', 'tests/data/ascii_test_data.txt']
        }
        
        cases_saved ={}
        for name, case in cases_to_save.items():
            if case[0] != 'input':
                case.insert(0, 'input')
            sys.argv = case
            args = __main__.get_args()
            cases_saved[name] = args
        return cases_saved
    
    def test___main___global_variables(self):
        assert __main__.HALFWIDTH_SPACE == ' '
        assert __main__.FULLWIDTH_SPACE == '　'
        
        assert hasattr(__main__, 'get_args')
        assert hasattr(__main__, 'is_ascii')
        assert hasattr(__main__, 'fill_white_spaces')
        assert hasattr(__main__, 'hor2vec')

    def test___main___get_args(self,fixture_args):
        args = fixture_args['case0']
        assert args is not None
        assert isinstance(args, argparse.Namespace)
        assert len(vars(args)) == 5
        assert 'input' in vars(args)
        assert 'sep' in vars(args)
        assert 'line_direction' in vars(args)
        assert 'word_direction' in vars(args)
        assert 'no_rotate' in vars(args)
        assert args.input.name == 'tests/data/english_test_data.txt'
        assert args.sep == ''
        assert args.line_direction == 'l2r'
        assert args.word_direction == 't2b'
        assert args.no_rotate == False
        
        args = fixture_args['case1']
        assert args is not None
        assert isinstance(args, argparse.Namespace)
        assert len(vars(args)) == 5
        assert 'input' in vars(args)
        assert 'sep' in vars(args)
        assert 'line_direction' in vars(args)
        assert 'word_direction' in vars(args)
        assert 'no_rotate' in vars(args)
        assert args.input.name == 'tests/data/english_test_data.txt'
        assert args.sep == ''
        assert args.line_direction == 'l2r'
        assert args.word_direction == 't2b'
        assert args.no_rotate == False

        args = fixture_args['case2']
        assert args is not None
        assert isinstance(args, argparse.Namespace)
        assert len(vars(args)) == 5
        assert 'input' in vars(args)
        assert 'sep' in vars(args)
        assert 'line_direction' in vars(args)
        assert 'word_direction' in vars(args)
        assert 'no_rotate' in vars(args)
        assert args.input.name == 'tests/data/english_test_data.txt'
        assert args.sep == ' '
        assert args.line_direction == 'l2r'
        assert args.word_direction == 't2b'
        assert args.no_rotate == False
        
        args = fixture_args['case3']
        assert args is not None
        assert isinstance(args, argparse.Namespace)
        assert len(vars(args)) == 5
        assert 'input' in vars(args)
        assert 'sep' in vars(args)
        assert 'line_direction' in vars(args)
        assert 'word_direction' in vars(args)
        assert 'no_rotate' in vars(args)
        assert args.input.name == 'tests/data/english_test_data.txt'
        assert args.sep == ' '
        assert args.line_direction == 'r2l'
        assert args.word_direction == 't2b'
        assert args.no_rotate == False
        
        args = fixture_args['case4']
        assert args is not None
        assert isinstance(args, argparse.Namespace)
        assert len(vars(args)) == 5
        assert 'input' in vars(args)
        assert 'sep' in vars(args)
        assert 'line_direction' in vars(args)
        assert 'word_direction' in vars(args)
        assert 'no_rotate' in vars(args)
        assert args.input.name == 'tests/data/english_test_data.txt'
        assert args.sep == ' '
        assert args.line_direction == 'r2l'
        assert args.word_direction == 'b2t'
        assert args.no_rotate == False
        
        args = fixture_args['case5']
        assert args is not None
        assert isinstance(args, argparse.Namespace)
        assert len(vars(args)) == 5
        assert 'input' in vars(args)
        assert 'sep' in vars(args)
        assert 'line_direction' in vars(args)
        assert 'word_direction' in vars(args)
        assert 'no_rotate' in vars(args)
        assert args.input.name == 'tests/data/english_test_data.txt'
        assert args.sep == ' '
        assert args.line_direction == 'r2l'
        assert args.word_direction == 'b2t'
        assert args.no_rotate == True
        
        args = fixture_args['case6']
        assert args is not None
        assert isinstance(args, argparse.Namespace)
        assert len(vars(args)) == 5
        assert 'input' in vars(args)
        assert 'sep' in vars(args)
        assert 'line_direction' in vars(args)
        assert 'word_direction' in vars(args)
        assert 'no_rotate' in vars(args)
        assert args.input.name == 'tests/data/ascii_test_data.txt'
        assert args.sep == ''
        assert args.line_direction == 'l2r'
        assert args.word_direction == 't2b'
        assert args.no_rotate == False
        
    def test___main___is_ascii(self):
        for n in range(0,128):
            assert __main__.is_ascii(chr(n)) == True
        
        for n in range(128,300):
            assert __main__.is_ascii(chr(n)) == False
    
