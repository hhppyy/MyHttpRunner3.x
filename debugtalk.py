import time
import re
from lxml import etree

from httprunner import __version__


def get_httprunner_version():
    return __version__


def sum_two(m, n):
    return m + n


def sleep(n_secs):
    time.sleep(n_secs)

def reg_req_body(responseBody):
    # 返回的 body 为 byte 类型，调用 decode 将中文转化
    response=responseBody.decode()
    # 处理 response 对象判断字符 checkstr 是否在 response 响应里面，存在返回 1 不存在返回 0
    req = re.findall(" <strong>(.*?)</strong>",response)
    return req

def re_body(body):
    req = etree.HTML(body)
    body = req.xpath(".//*[@name='csrfmiddlewaretoken']/@value")
    return body