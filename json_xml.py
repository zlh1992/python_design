# -*- coding: utf-8 -*-
# @Time : 2021/11/8 下午10:35
# @Author : zhenglinghan
# @Email : zhenglinghan.zlh@antgroup.com
# @File : json_xml.py
# @Project : python_design

import json
import xml.etree.ElementTree as etree


class JSONDataExtractor:
    def __init__(self, filepath):
        self.data = dict()
        with open(filepath, mode="r", encoding="utf-8") as f:
            self.data = json.load(f)

        @property
        def parsed_data(self):  # 属性而非方法
            return self.data


class XMLDataEXtractor:
    def __init__(self, filepath):
        self.tree = etree.parse(filepath)

        @property
        def parsed_data(self):
            return self.tree


# 做一个工厂方法 根据输入的文件扩展名返回以上两个实例
def dataextraction_factory(filepath):
    if filepath.endswith("json"):
        extractor = JSONDataExtractor
    elif filepath.endswith("xml"):
        extractor = XMLDataEXtractor
    else:  # 安全防护
        raise ValueError("Cannot extract data from {}".format(filepath))
    return extractor

# 为以上函数做一个装饰器
def extract_data_from(filepath):
    factory_obj = None
    try:
        factory_obj = dataextraction_factory(filepath)
    except ValueError as e:
        print(e)
    return factory_obj
