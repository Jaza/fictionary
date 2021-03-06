import logging
import random
import re

import mock
import pytest

import fictionary



def test_weighted():
    # Mock out randint, because py2 & py3 generate different sequences for the
    # same seed:
    with mock.patch('random.randint') as randint_mock:
        randint_mock.side_effect = [6, 8, 5, 12, 0, 13]
        rc = fictionary.RandomCounter('aaaaaaaaaaaaab')
        assert [rc.random_choice() for i in range(6)] == list('aaaaab')

def test_unweighted():
    # Mock out randint, because py2 & py3 generate different sequences for the
    # same seed:
    with mock.patch('random.choice') as randint_mock:
        randint_mock.side_effect = 'ababab'
        rc = fictionary.RandomCounter('aaaaaaaaaaaaab')
        assert [rc.random_choice(weighted=False) for i in range(6)] == list('ababab')

def test_pick():
    rc = fictionary.RandomCounter('aaaaaaaaaaaaab')
    assert rc.pick(0) == 'a'
    assert rc.pick(12) == 'a'
    assert rc.pick(13) == 'b'

def test_pick():
    rc = fictionary.RandomCounter('aaaaaaaaaaaaab')
    with pytest.raises(IndexError):
        rc.pick(14)
