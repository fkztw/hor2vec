from hor2vec import __version__

import pytest  # noqa: F401

import re


class TestVersion(object):

    def test___version__(self):

        module_version = __version__.__version__

        # regex from https://www.python.org/dev/peps/pep-0440/
        pep440_pattern = r"""
            ^                       #start of string
            ([1-9]\d*!)?            #group 1
                                    #   () group
                                    #   [1-9] char in 1 to 9
                                    #   \d* digit zero-∞ times
                                    #   ! match literally
                                    #   ? Match zero-1 times as many
            (0|[1-9]\d*)            #group 2
                                    #   () group
                                    #   0 char 0
                                    #   | or
                                    #   [1-9] char in 1 to 9
                                    #   \d* digit zero-∞ times
            (\.(0|[1-9]\d*))*       #group 3
                                    #   () group
                                    #   \. Match a . dot
                                    #   (0|[1-9]\d*) Same as group 2
                                    #   * Match zero-∞ times as many
            ((a|b|rc)(0|[1-9]\d*))? #group 4
                                    #   (()()) group and group
                                    #   (a|b|rc) char a or b or rc
                                    #   (0|[1-9]\d*) Same as group 2
                                    #   ? Match zero-1 times as many
            (\.post(0|[1-9]\d*))?   #group 5
                                    #   () group
                                    #   \. Match a . dot
                                    #   post string post
                                    #   (0|[1-9]\d*) Same as group 2
                                    #   ? Match zero-1 times as many
            (\.dev(0|[1-9]\d*))?    #group 6
                                    #   () group
                                    #   \. Match a . dot
                                    #   dev string dev
                                    #   (0|[1-9]\d*) Same as group 2
                                    #   ? Match zero-1 times as many
            $                       #end of string
        """
        pep440_regex = re.compile(pep440_pattern, re.VERBOSE)
        assert module_version is not None
        assert type(module_version) is str
        assert re.match(pep440_regex, module_version) is not None
        assert re.match(pep440_regex, module_version).group is not None
