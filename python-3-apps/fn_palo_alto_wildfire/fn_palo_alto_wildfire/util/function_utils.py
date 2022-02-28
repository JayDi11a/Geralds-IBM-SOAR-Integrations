# -*- coding: utf-8 -*-
#
# (c) Copyright IBM Corp. 2019. All Rights Reserved.
#
# Util functions

from collections import OrderedDict

def listRecursive(d, key):
    """
        Traverses through nested ordered dictionaries and returns values for given key
        :param d: input ordered dictionary
        :param key: key value
        :return: None
        """
    for k, v in d.items():
        if isinstance(v, OrderedDict):
            for found in listRecursive (v, key):
                yield found
        if k == key:
                yield v