# -*- coding: utf-8 -*-
from string import ascii_lowercase
from random import choice, random, randint
from prettytable import PrettyTable

class Question:
    '''题目'''
    def __init__(self, id=0,
                       type=0,
                       score=0,
                       difficulty=0.00,
                       points=None):
        self.id = id
        self.type = type
        self.score = score
        self.difficulty = difficulty
        if points is None:
            points = []
        self.points = points

class DB:
    '''模拟数据库'''
    def __init__(self):
        self.question_db = []
        for i in range(5000):
            model = Question()
            model.id = i

            # 试题难度取0.3 到 1 之间随机值
            model.difficulty = randint(3, 10) * 0.1

            # 单选题3分
            if i < 1001:
                model.type = 1
                model.score = 3

            # 多选题5分
            if 1000 < i < 2001:
                model.type = 2
                model.score = 5

            # 判断题4分
            if 2000 < i < 3001:
                model.type = 3
                model.score = 4

            # 填空题1-4分
            if 3000 < i < 4001:
                model.type = 4
                model.score = randint(1, 5)

            # 问答题分数为难度系数*10
            if 4000 < i < 5001:
                model.type = 5
                model.score = model.difficulty * 10 if model.difficulty > 0.3 else 3

            # 每题1到4个知识点
            points = []
            count = randint(1, 5)
            for j in range(count):
                points.append(randint(1, 100))

            model.points = points
            self.question_db.append(model)

class Paper:
    '''目标试卷'''
    def __init__(self, id=0, total_score=100, difficulty=0.00, points=[], each_type_count=[]):
        '''id::编号
           total_score::总分
           difficulty::难度系数
           points::知识点
           each_type_count::各种题型题数'''
        self.id = id
        self.total_score = total_score
        self.difficulty = difficulty
        self.points = points
        self.each_type_count = each_type_count

# ****开始遗传算法***** #

class Unit:
    '''试题组合'''
    def __init__(self, id=0, adaptation_degree=0.00, p_coverage=0.00, question_list=None):
        '''id::编号
           adaptation_degree::适应度
           p_coverage::知识点覆盖率
           problem_list::题目列表'''
        self.id = id
        self.adaptation_degree = adaptation_degree
        self.p_coverage = p_coverage
        if question_list is None:
            question_list = []
        self.question_list = question_list

    @property
    def difficulty(self):
        # 试卷的难度系数 与问题的难度系数有关
        diff = 0.00
        for p in self.question_list:
            diff += p.difficulty * p.score
        return diff / self.sum_score

    @property
    def question_count(self):
        # 题目个数
        return len(self.question_list)

    @property
    def sum_score(self):
        # 总分
        _sum = 0
        for p in self.question_list:
            _sum += p.score
        return _sum

def is_contain(paper, question):
    '''题目知识点是否符合试卷要求
       paper::期望试卷
       question::一道试题'''
    for point in question.points:
        if point in paper.points:
            return True
    return False


def get_p_coverage(unit_list, paper):
    '''计算知识点覆盖率
    unit_list::种群
    paper::期望试卷
    return:>list
    '''
    for unit in unit_list:
        points = []
        for question in unit.question_list:
            points = points + question.points
        point_set = set(points)
        common = list(point_set & set(paper.points))    # 交集
        unit.p_coverage = len(common) * 1.00 / len(paper.points)
    return unit_list


def get_adaptation_degree(unit_list, paper, p_coverage=0.3, difficulty=0.7):
    '''计算种群适应度
    unit_list::种群
    paper::期望试卷
    p_coverage::知识点分布在适应度计算中所占权重
    difficulty::试卷难度系数在适应度计算中所占权重
    return:>list
    '''
    unit_list = get_p_coverage(unit_list, paper)
    for unit in unit_list:
        unit.adaptation_degree = 1 - (1 - unit.p_coverage) * p_coverage - abs(unit.difficulty - paper.difficulty) * difficulty

    return unit_list


def CSZQ(count, paper, question_list):
    '''count::个体数量
       paper::期望试卷
       problem_list::题库
       return:>初始种群
     '''
    unit_list = []
    each_type_count = paper.each_type_count
    for i in range(count):
        unit = Unit()
        unit.question_list[:] = []
        unit.id = i + 1
        unit.adaptation_degree = 0.00

        # 总分限制
        while paper.total_score != unit.sum_score:
            unit.question_list[:] = []  # clear question_list

            for j in range(len(each_type_count)):
                one_type_question = [each_question for each_question in question_list if
                                    each_question.type == j+1 and is_contain(paper, each_question)]
                for k in range(each_type_count[j]):
                    index = randint(0, len(one_type_question) - k - 1)
                    unit.question_list.append(one_type_question[index])

                    temp_question = one_type_question[len(one_type_question)-1-k]
                    one_type_question[len(one_type_question)-1-k] = one_type_question[index]
                    one_type_question[index] = temp_question
        unit_list.append(unit)

    # 计算适应度
    unit_list = get_adaptation_degree(unit_list, paper)

    return unit_list


def show_unit_list(unit_list):
    '''
    显示种群个体题目编号
    '''
    mix = PrettyTable()
    mix.field_names = ['编号', '知识点覆盖率', '难度系数', '适应度']
    for unit in unit_list:
        mix.add_row([unit.id, round(unit.p_coverage, 3), round(unit.difficulty, 3), round(unit.adaptation_degree, 3)])
    # print mix

def select(unit_list, count):
    '''选择算子（轮盘赌选择）
    unit_list::种群
    count::选择次数
    return:>进入下一代的种群
    '''
    select_unit_list = []
    # 种群个体适应度和
    all_adaptation_degree = 0.0
    for unit in unit_list:
        all_adaptation_degree += unit.adaptation_degree

    while(len(select_unit_list) != count):
        # 选择一个0—1的随机数字
        degree = 0.00
        rand_degree = randint(0, 100) * 0.01 * all_adaptation_degree

        for unit in unit_list:
            degree += unit.adaptation_degree
            if degree >= rand_degree:
                if unit not in select_unit_list:
                    select_unit_list.append(unit)
                    break
    return select_unit_list


# def distinct(unit_list):
#     '''unit_list列表去重
#     '''
#     new_list = []
#     count = len(unit_list)
#
#     for i in range(0, count-1):
#         for j in range(i+1, count):
#             x = unit_list[i]
#             y = unit_list[j]
#
#             for k in range(x.question_count):
#                 if x.question_list[k].id != y.question_list[k].id:
#                     new_list.append(x)
#     return new_list

def distinct_2(seq, idfun=None):
    # order preserving
    if idfun is None:
        def idfun(x): return x
    seen = {}
    result = []
    for item in seq:
        marker = idfun(item)
        # in old Python versions:
        # if seen.has_key(marker)
        # but in new ones:
        if marker in seen: continue
        seen[marker] = 1
        result.append(item)
    return result

def cross(unit_list, count, paper):
    '''交叉算子
    '''
    cross_unit_list = []
    while(len(cross_unit_list) != count):
        # 随机选择两个个体
        index_one = randint(0, len(unit_list)-1)
        index_two = randint(0, len(unit_list)-1)

        if index_one != index_two:
            unit_one = unit_list[index_one]
            unit_two = unit_list[index_two]

            # 随机选择一个交叉位置
            cross_position = randint(0, unit_one.question_count - 2)

            # 保证交叉题目分数和相同 简化算法(采用单点交叉， 且只交叉2道题)
            score_one = unit_one.question_list[cross_position].score + unit_one.question_list[cross_position+1].score
            score_two = unit_two.question_list[cross_position].score + unit_two.question_list[cross_position+1].score

            if score_one == score_two:
                # 两个新个体
                unit_new_one = Unit()
                unit_new_one.question_list = [question for question in unit_one.question_list]
                unit_new_two = Unit()
                unit_new_two.question_list = [question for question in unit_two.question_list]

                # 交叉两道题
                for i in range(cross_position, cross_position+2):
                    unit_new_one.question_list[i] = unit_two.question_list[i]
                    unit_new_two.question_list[i] = unit_one.question_list[i]

                # 添加到新的种群
                unit_new_one.id = len(cross_unit_list) + 1
                unit_new_two.id = unit_new_one.id + 1
                if len(cross_unit_list) < count:
                    cross_unit_list.append(unit_new_one)
                if len(cross_unit_list) < count:
                    cross_unit_list.append(unit_new_two)
        # 过滤掉重复个体
        cross_unit_list = distinct_2(cross_unit_list, lambda x:x.id)

    # 计算适应度
    cross_unit_list = get_adaptation_degree(cross_unit_list, paper)
    return cross_unit_list


def is_get_target(unit_list, end_condition):
    '''是否达到目标
    unit_list::种群
    end_condition::结束条件（适应度要求）
    return:>bool
    '''
    if len(unit_list) > 0:
        for unit in unit_list:
            if unit.adaptation_degree >= end_condition:
                return True
    return False

def show_result(unit_list, expend):
    '''打印结果
    '''
    mix = PrettyTable()
    l = []
    mix.field_names = ['题目编号', '题目数量', '知识点覆盖率', '难度系数', '适应度']
    for unit in unit_list:
        if unit.adaptation_degree >= expend:
            mix.add_row([unit.id, unit.question_count, round(unit.p_coverage, 3), round(unit.difficulty, 3), round(unit.adaptation_degree, 3)])
            l.append([unit.id, unit.question_count, round(unit.p_coverage, 3), round(unit.difficulty, 3), round(unit.adaptation_degree, 3)])
    # print mix
    return l




def output(total_score=100, difficulty=0.72):
    db = DB()
    paper = Paper(id=1,
                  total_score=total_score,
                  difficulty=difficulty,
                  points=[1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29,
                        31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59,
                        61, 63, 65, 67, 69, 71, 73, 75, 77, 79, 81],
                  each_type_count=[10, 4, 5, 5, 2])

    # 迭代计数器
    count = 1

    # 适应度期望值
    wish_adaptation_degree = 0.91

    # 最大迭代次数
    run_count = 500
    # init

    unit_list = CSZQ(20, paper, db.question_db)

    # print ("\n\n      -------遗传算法组卷系统---------\n\n")
    # print("初始种群：")
    show_unit_list(unit_list)
    # print ("-----------------------迭代开始------------------------")

    while not is_get_target(unit_list, wish_adaptation_degree):
        count += 1
        # print ("在第 " + str(count-1) + " 代未得到结果")
        if count > run_count:
            # print ("计算 " + str(run_count) + " 代仍没有结果，请重新设计条件！")
            break

        # 选择
        unit_list = select(unit_list, 10)
        # 交叉
        unit_list = cross(unit_list, 20, paper)

        if is_get_target(unit_list, wish_adaptation_degree):
            break

        # 变异
        # unit_list = change(unit_list, db.question_db, paper)
    x = False
    if count < run_count:
        # print ("在第 " + str(count) + " 代得到结果，结果为：\n")
        # print ("期望试卷难度：" + str(paper.difficulty) + "\n")
        x = show_result(unit_list, wish_adaptation_degree)

    if x is False:
        return False

    return (count, paper.difficulty) + tuple(x, )
