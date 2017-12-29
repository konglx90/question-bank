# -*-coding:utf-8 -*-
from django.db import models
from django.conf import settings
from bson import json_util
import json
from django import forms

AUTH_USER_MODEL = getattr(settings, 'AUTH_USER_MODEL', 'auth.User')

class QuestionType:
    def __init__(self, type_value=1, type_text='单选题'):
        self.type_value = type_value
        self.type_text = type_text

QUESTION_TYPE = {
    'single_chioce': QuestionType(1, '单选题'),
    'multi_chioce': QuestionType(2, '多选题'),
    'judge': QuestionType(3, '判断题'),
    'fill_bank': QuestionType(4, '填空题'),
    'brief': QuestionType(5, '问答题')
}

QUESTION_TYPE_CHIOCE = (
    (1, u'单选题'),
    (2, u'多选题'),
    (3, u'判断题'),
    (4, u'填空题'),
    (5, u'问答题')
)

QUESTION_POINT_CHIOCE = (
    (1, u'短路的基本知识'),
    (2, u'标幺制'),
    (3, u'无限大电源'),
    (4, u'运用曲线法计算短路电流'),
    (5, u'知识点E'),
    (6, u'知识点F'),
    (7, u'知识点G'),
    (8, u'知识点H'),
    (9, u'知识点I'),
    (10, u'知识点J'),
)
for q_p_i in range(11, 101):
    QUESTION_POINT_CHIOCE += (
        (q_p_i, u'知识点'+unicode(q_p_i)),
    )

class BaseModel:
    def toJSON(self):
        import json
        return json.dumps(dict([(attr, getattr(self, attr)) for attr in [f.name for f in self._meta.fields]]),
                default=json_util.default)

    def toDict(self):
        return dict([(attr, getattr(self, attr)) for attr in [f.name for f in self._meta.fields]])

class Question(models.Model, BaseModel):
    topic = models.TextField(verbose_name=u'题目')
    difficulty = models.FloatField(verbose_name=u'难度系数', default=0.30)
    score = models.IntegerField(verbose_name=u'分数', default=3)
    _type = models.IntegerField(verbose_name=u'类型', default=QUESTION_TYPE['single_chioce'].type_value, choices=QUESTION_TYPE_CHIOCE)
    points = models.CharField(verbose_name=u'知识点', default='', max_length=255)
    ctime = models.DateTimeField(verbose_name=u'创建时间', auto_now_add=True, null=True)

    answer = models.TextField(verbose_name=u'答案', blank=True) # 问答题的答案
    is_right = models.BooleanField(verbose_name=u'是否为正确判断', blank=True, default=False)

    def set_points(self, x):
        self.points = json.dumps(x)

    def get_points(self):
        return json.loads(self.points)

    class Meta:
        verbose_name = u'题库'
        verbose_name_plural = verbose_name
        ordering = ['-ctime']

    def __unicode__(self):
        return self.topic


class Option(models.Model, BaseModel):
    question = models.ForeignKey(Question, verbose_name=u'所属题目', related_name='option')
    topic = models.TextField(verbose_name=u'内容')
    is_right = models.BooleanField(verbose_name=u'是否为正确选项', default=True)
    ctime = models.DateTimeField(verbose_name=u'创建时间', auto_now_add=True, null=True)

    class Meta:
        verbose_name = u'选项'
        verbose_name_plural = verbose_name
        ordering = ['-ctime']

    def __unicode__(self):
        return u'选项'

    def toDict(self):
        return dict([(attr, getattr(self, attr)) for attr in [f.name for f in self._meta.fields if f.name != 'question']])


class Paper(models.Model, BaseModel):
    question_list = models.CharField(verbose_name=u'知识点', default='', max_length=255)
    title = models.CharField(verbose_name=u'标题', default='', max_length=255)
    adaptation_degree = models.FloatField(verbose_name=u'适应度')
    p_coverage = models.FloatField(verbose_name=u'知识点覆盖率')
    ctime = models.DateTimeField(verbose_name=u'创建时间', auto_now_add=True, null=True)
    question_count = models.IntegerField(verbose_name=u'题目数', default=26)
    sum_score = models.IntegerField(verbose_name=u'总分', default=100)
    difficulty = models.FloatField(verbose_name=u'难度系数', default=0.72)

    class Meta:
        verbose_name = u'试卷'
        verbose_name_plural = verbose_name
        ordering = ['-ctime']

    def __unicode__(self):
        return u'试卷'

    def set_question_list(self, x):
        self.question_list = json.dumps(x)

    def get_question_list(self):
        return json.loads(self.question_list)

    # @property
    # def question_count(self):
    #     # 题目个数
    #     return len(self.question_list)

    # @property
    # def sum_score(self):
    #     # 总分
    #     _sum = 0
    #     for p in self.question_list:
    #         _sum += p.score
    #     return _sum

    # @property
    # def difficulty(self):
    #     # 试卷的难度系数 与问题的难度系数有关
    #     diff = 0.00
    #     for p in self.question_list:
    #         diff += p.difficulty * p.score
    #     return diff / self.sum_score
