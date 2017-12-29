# -*- coding: utf-8 -*-
from ..utils import const_to_list
from .. import const

question_schema = {
    # Schema definition, based on Cerberus grammar. Check the Cerberus project
    # (https://github.com/pyeve/cerberus) for details.
    # 题目
    'topic': {
        'type': 'string',
        'minlength': 1,
        'maxlength': 200,
        'required': True,
    },
    # 选项
    'options': {
        'type': 'list',
        'minlength': 2,
        'maxlength': 5,
    },
    # 正确答案
    'answer': {
        'type': 'string',
        # ''
    },
    # 题目的类型， 选择 解答 等
    'type': {
        'type': 'string',
        'minlength': 1,
        'maxlength': 20,
        'allowed': const_to_list(const.QUESTION_TYPE),
    }
}

question = {
    # 'title' tag used in item links. Defaults to the resource title minus
    # the final, plural 's' (works fine in most cases but not for 'people')
    'item_title': 'qt',

    # by default the standard item entry point is defined as
    # '/people/<ObjectId>'. We leave it untouched, and we also enable an
    # additional read-only entry point. This way consumers can also perform
    # GET requests at '/people/<lastname>'.
    'additional_lookup': {
        # 'url': 'regex("[\w]+")',
        # 'field': '_id'
    },

    # We choose to override global cache-control directives for this resource.
    'cache_control': 'max-age=10,must-revalidate',
    'cache_expires': 10,

    # most global settings can be overridden at resource level
    'resource_methods': ['GET', 'POST'],

    'schema': question_schema
}
