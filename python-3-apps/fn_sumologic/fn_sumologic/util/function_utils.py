# -*- coding: utf-8 -*-
#
# (c) Copyright IBM Corp. 2019. All Rights Reserved.
#
# Util functions


def make_query_string(query, params):
    """
    Substitute parameters into the query
    :param query: input query with params
    :param params: values used to substitute
    :return:
    """
    query_string = query

    index = 1
    for param in params:
        if param:
            to_replace = "%%param%d%%" % index
            query_string = query_string.replace(to_replace, param)
        index += 1

    return query_string
