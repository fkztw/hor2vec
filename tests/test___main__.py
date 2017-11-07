from hor2vec import __main__    #this import trashed the test coverage

#import hor2vec


import pytest

class TestMain(object):
    
    def test___main___global_variables(self):
        assert __main__.HALFWIDTH_SPACE == ' '
        assert __main__.FULLWIDTH_SPACE == '　'
        
        assert hasattr(__main__, 'get_args')
        assert hasattr(__main__, 'is_ascii')
        assert hasattr(__main__, 'fill_white_spaces')
        assert hasattr(__main__, 'hor2vec')

