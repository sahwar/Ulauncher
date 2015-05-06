import pytest


class DictHasValus(dict):
    """
    DictHasValus({('foo', 'bar'): 'hello'}) == {'foo': {'bar': 'hello'}}
    """

    def __eq__(self, other):
        try:
            return all([self.find(k, other) == v for k, v in self.items()])
        except KeyError:
            return False

    def find(self, keys, other):
        if type(keys) != tuple:
            keys = (keys,)
        return reduce(lambda d, key: d[key], keys, other)


pytest.DictHasValus = DictHasValus


def test_DictWithValues():

    assert DictHasValus({'test': 'hello'}) == {'test': 'hello', 'other': False}
    assert DictHasValus({('test',): 'hello'}) == {'test': 'hello'}
    assert DictHasValus({('foo', 'bar'): 'hello'}) == {'foo': {'bar': 'hello', 1: 2}}
    assert DictHasValus({(1, 'bar'): 'hello'}) == {1: {'bar': 'hello'}}

    assert DictHasValus({'test': 'hello'}) != {'test': 'wrong val', 'other': False}
    assert DictHasValus({('foo', 'bar'): 'hello'}) != {'foo': None}