#!/usr/bin/python
# -*- coding:utf-8 -*-


from hunaccent import hunaccent


def test_accent_restoration():

    expected1 = "árvíztűrő tükörfúrógép"
    expected2 = "ízékre gondoltam"

    result1 = hunaccent.accentize('arvizturo tukorfurogep')
    result2 = hunaccent.accentize('izekre gondoltam')

    assert expected1 == result1
    assert expected2 == result2
