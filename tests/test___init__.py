# import hor2vec
import importlib
import pytest


class TestInit(object):

    def test___init__(self):
        module_was_imported = importlib.util.find_spec("hor2vec")
        found = module_was_imported is not None
        assert found is True
        assert module_was_imported.name == 'hor2vec'
        assert '/hor2vec' in module_was_imported.submodule_search_locations[0]
