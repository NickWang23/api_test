# !/usr/bin/env python
# -*-coding: utf-8-*-

# @ProjectName : api_test
# @FileName : basic_knowledge.py
# @Time : 2019/3/28 14:39
# @Author : Nick
# @description : python语言的基础知识回顾

"""
在Pycharm中自动添加时间日期作者等信息:
	https://blog.csdn.net/u010105243/article/details/76154251

question1： utf-8 如何转换为GBK的编码：
	Python2中的字符串进行字符编码转换过程是：
	
		字节串-->decode('原来的字符编码')-->Unicode字符串-->encode('新的字符编码')-->字节串
	Python3中定义的字符串默认就是unicode，因此不需要先解码，可以直接编码成新的字符编码：
		字符串-->encode('新的字符编码')
		
	python3最重要的新特性大概要算对文本和二进制数据做了更为清晰的区分，文本总是unicode字符集，有str类型表示，二进制数据则有bytes类型表示。
		
	Python3中定义的:
			#字符串默认就是unicode,当使用encode方法是，是将str编码成相应编码的bytes类型
			str.encode(‘新的bytes的编码类型’) -> bytes
			#当bytes类型使用decode的时，是将相应类型的bytes，	解码成unicode的str类型
			bytes.decode(‘原来的bytes的编码类型’) -> str

# UTF_8_STR1 = '阿贵，你好'
# GBK_str1 = utf_8_str1.encode(encoding='gbk')
# print(type(utf_8_str1))

2019-03-29 :

1.继续学习python基础知识：list,tuple,str,dict
2.json在线地址：https://www.bejson.com/jsonviewernew/
3.开放平台接口：https://www.apiopen.top/api.html

question2:  Pycharm设置让制表符显示为→
File -> Settings -> Editor -> Appearance -> 勾选“Show line numbers”、“Show whitespaces”、“Show method separators 勾选完之后就可以了

"""
#
# str_test = " I'm a new student in python's study "
# str_test1 = " I would rather make a friend  with people who has an interesting soul "
# str.format()方法通过字符串中的花括号{}来识别替换字段（replacement field），从而完成字符串的格式化。
# str.format() 方法还可以使用 *元组 和 **字典 的形式传参，两者可以混合使用。
# 位置参数、关键字参数、*元组 和 **字典 也可以同时使用，但是要注意，位置参数要在关键字参数前面，*元组 要在 **字典 前面。
# 替换字段 由字段名field name和转换字段conversion field以及格式说明符 format specifier 组成，
# 即一般形式为 {字段名!转换字段:格式说明符} 转换字段和格式说明符都是可选的
# 字段名分为简单字段名（simple field name）和复合字段名( compound field name)
# 简单字段名有三种写法：
#
# 1.省略不写{}
# 注：花括号个数可以少于位置参数的个数，反之亦然。
# print("format method: testing simple field, {} nothing in a pair of big braces".format('括号中省略位置参数'))
# print("one sentence: {0}".format(str_test), '\n')
# print("my name is {name},I'm from {hometown} and I'm {age}".format_map(
# 															{'name': 'Ben', 'hometown': 'tianshui', 'age': 19}))
# print(str_test+str_test1, '\n')
#
# 2.数字{十进制非负整数}:
# 注： 数字必须是大于等于0的整数； 带数字的替换字段可以重复使用；
# print('my name is {0},not {1},please remember {0}, ok!!'.format(*['nick', 'Tom']))
#      数字形式的简单字段名相当于把format中的所有位置参数整体当作一个元组，通过字段名中的数字进行取值。
#      即{0}等于tuple[0],所以花括号内的数字不能越界
# print('height:{0},weight:{1},address:{2}'.format(*[168, 50, 'Eco-Tech Park']))
#
# 3.变量名{合法的Python标识符}:关键字参数的位置可以随意调换
# print('我不做大哥好多年，江湖都忘了我的传说，我叫{nicky_name}。 让别人记起你的最好方式就是恐惧，所以我回来了，\
# {city}将是我的天下!!'.format(**{'nicky_name': "刮骨王", 'city': '深圳'}))
#
# print("it's a {0:s}, {1:0.2f} long".format('stick', 123.455))
# 对象可以自定义格式说明符来替换标准格式说明符，比如 datetime 类。
# from datetime import datetime
# print("Today is: {0:%a %b %d %H:%M:%S %Y}".format(datetime.now()))
# 今天是：Thu Nov 15 13:05:09 2018
# join的用法：
# 'sep'.join(seq)
# sep：分隔符。可以为空
# seq：要连接的元素序列、字符串、元组、字典
# 上面的语法即：以sep作为分隔符，将seq所有的元素合并成一个新的字符串
# 返回值：返回一个以分隔符sep连接各个元素后生成的字符串
# print(' '.join(['I', "don't", "wanna", 'change', 'myself', 'to', 'make', 'others', 'happy']))
# dict_test = {'name': 'Nick', 'age': '38', 'gender': 'male'}
# print(' '.join(dict_test.values()))
#
# print(str_test.capitalize())
# print(str_test.casefold())
# print(str_test.lower())
# print(str_test.center(50, '-'))
# print(str_test.count('s'))
# print(str_test.encode('utf-8'))
# print(str_test.endswith('dy'), str_test.endswith('a'))

"""
函数： 可变参数*args，**kwargs

*args:传入的可变无名参数全部存在一个tuple
**kwargs:传入的可变关键字参数都存在一个dict里

def func_test(*args, **kwargs):
	print("args include: {}".format(args))
	print('type of args is : ', type(args))
	print("kwargs include: {}".format(kwargs))
	print('type of kwargs is : ', type(kwargs))


func_test(1, 2, 4, code=200, status='success')
test_data_list = [1, 2, 3, 4, 5]
test_data_dict = {'name': 'nick', 'gender': 'male', 'pos': 'manager'}
# 通过*可以对将序列类型（list,str,tuple,bytes）解包，作为可变无名参数传入
# 通过**可以对将字典类型解包，作为可变关键字参数传入
func_test(*test_data_list, **test_data_dict)
"""






