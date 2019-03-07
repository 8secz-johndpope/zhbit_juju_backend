#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-02-08 15:49
# @Author  : ┏ (゜ω゜)=☞ Airy
# @Email   : a532710813@gmail.com
# @File    : InteractiveController.py
# @Software: PyCharm

from django.http import HttpRequest
from apps.http.db import models
from apps.Utils.validation.ParamValidation import validate_and_return
from apps.Utils import ReturnResult as rS


def follow(request: HttpRequest):
    """
    关注
    :param request:
    :return:
    """
    _param = validate_and_return(request, {
        'group_id': '',
        'require_user_id': ''
    })

    user = models.User.objects.get(pk=_param['require_user_id'])
    group = models.Group.objects.get(pk=_param['group_id'])

    if user is None:
        rS.fail(rS.ReturnResult.UNKNOWN_ERROR, '没有找到用户')

    if group is None:
        rS.fail(rS.ReturnResult.UNKNOWN_ERROR, '没有该群组')

    mapping = models.UserFollowGroupMapping.objects.create(group=group, user=user)

    if mapping:
        rS.success()
    else:
        rS.fail(rS.ReturnResult.UNKNOWN_ERROR, '关注失败')


def dis_follow(request: HttpRequest):
    """
    取消关注
    :param request:
    :return:
    """
    _param = validate_and_return(request, {
        'group_id': '',
        'require_user_id': ''
    })

    user = models.User.objects.get(pk=_param['require_user_id'])
    group = models.Group.objects.get(pk=_param['group_id'])

    if user is None:
        rS.fail(rS.ReturnResult.UNKNOWN_ERROR, '没有找到用户')

    if group is None:
        rS.fail(rS.ReturnResult.UNKNOWN_ERROR, '没有该群组')

    mapping = models.UserFollowGroupMapping.objects.get(user=user, group=group)

    if mapping:
        mapping.delete()
        rS.success()
    else:
        rS.fail(rS.ReturnResult.UNKNOWN_ERROR, '取消关注失败')
