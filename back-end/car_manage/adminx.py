# -*-coding:utf-8 -*-

from models import Question, Option, Paper
import xadmin
from xadmin.views import ModelAdminView

xadmin.autodiscover()

QUESTION_TYPE_DICT = {
    1: '单选题',
    2: '多选题',
    3: '判断题',
    4: '填空题',
    5: '问答题'
}


class QuestionAdmin(object):
    list_display = (
       'pk', 'topic', 'score', 'change_type', 'ctime'
    )

    def change_type(self, obj):
        return QUESTION_TYPE_DICT[obj._type]
    change_type.short_description = '题目类型'


class OptionAdmin(object):
    list_display = (
       'question', 'topic', 'is_right', 'ctime'
    )


class PaperAdmin(object):
    list_display = (
       'title', 'pk', 'question_list', 'difficulty', 'adaptation_degree', 'p_coverage', 'ctime'
    )

xadmin.site.register(Question, QuestionAdmin)
xadmin.site.register(Option, OptionAdmin)
xadmin.site.register(Paper, PaperAdmin)
