#coding=utf-8

'''
5.数据结构
5.1 list
list方法：
append(x)
extend(L)
insert(i,x)
remove(x):删除第一个值为x的元素
pop([i])
index(x):返回第一个值为x的元素的索引
count(x)
sort(cmp=None,key=None,reverse=False)
reverse()

insert,remove,sort方法只修改列表没有返回值（认为返回了None）
5.1.1 list 用作 stack (容易)
5.1.2 list 用作 queue （效率不高）
    使用collections.deque来实现队列
5.1.3函数式编程工具
filter(function,sequence)返回的序列由function(item)结果为真的元素组成。
如果sequence是一个字符串或元祖，结果将是相同的类，否则结果将始终是列表
map(function,sequence)为序列的每一个元素调用function(item)并返回结果的列表
reduce(function,sequence)只返回一个值，function必须是二元函数，它首先以序列的前两个元素调用function,然后
再以返回的结果和下一个元素继续调用；可以传入第三个参数作为初始值
5.1.4列表推导式
用括号括起来，括号里面包括一个表达式，表达式后面跟着一个for语句，或者跟多个for 或if 语句
>>>squares = [x**2 for x in range(10)] ;
>>>[(x,y) for x in [1,2,3] for y in [3,2,4] if x != y]

注意：
>>>vec = [[1,2,3], [4,5,6], [7,8,9]]
>>>print [num for elem in vec for num in elem]  ==>>  [1, 2, 3, 4, 5, 6, 7, 8, 9]
>>>print [num for num in elem for elem in vec]  ==>>  [7, 7, 7, 8, 8, 8, 9, 9, 9]
结果不一样,顺序问题

5.1.4.1列表推导式的嵌套

5.2 del语句：根据索引来删除元素

5.3 元祖和序列

5.4集合：元素没有顺序且没有重复
花括号或set()函数可以用于创建集合。注意：若要创建一个空的集合你必须使用set()，不能用{}；后者将创建一个空的字典

5.5字典

5.6遍历技巧
使用enumerate()同时获得索引和对应的值
>>>for i,v in enumerate(['z','b','c'])
遍历多个序列使用zip()函数成对读取元素
遍历字典使用iteritems()方法：
>>>for k,v in kw.iteritems()

若要在循环内部修改正在遍历的序列（例如复制某些元素），建议您首先制作副本。
在序列上循环不会隐式地创建副本。切片表示法使这尤其方便：
>>> words = ['cat', 'window', 'defenestrate']
>>> for w in words[:]:  # Loop over a slice copy of the entire list.
...     if len(w) > 6:
...         words.insert(0, w)
...
>>> words  ==>>['defenestrate', 'cat', 'window', 'defenestrate']
使用for w in words: 会有问题

5.7深入条件控制

5.8序列与其他类型的比较

6.模块
6.1深入模块
from module import *
这种方式不会导入以下划线 (_) 开头的名称，但不赞成这么使用
注意：出于性能考虑，每个模块在每个解释器会话中只导入一遍。因此，如果你修改了你的模块，
你必需重新启动解释器 —— 或者，如果你就是想交互式的测试这么一个模块，可以使用reload()，例如reload(modulename)。
6.1.1执行模块
if __name__ == '__main__' 既可以让文件作为脚本执行，又可以作为模块导入（用作测试非常方便）
6.1.2 模块搜索路径 sys.path
6.1.3“编译过的” python 文件
.pyc .pyo文件可以使文件加载速度加速，程序并不能运行的更快
6.2标准模块
6.3 dir()函数：找出模块中定义了哪些名字
>>>dir(modulename)
6.4包 目录下必须包含__init__.py文件（一般为空文件）
6.4.1 从包中导入*  ：不赞成这么导入
使用import modulename ,from modulename import submodulename or functionname as xxx
6.4.2包内引用
6.4.3包含多个目录的包


7.输入和输出
7.1格式化输出
 str()函数的用意在于返回人类可读的表现形式，而repr()的用意在于生成解释器可读的表现形式
>>> s = 'Hello, world.'
>>> str(s)
'Hello, world.'
>>> repr(s)
"'Hello, world.'"
>>> str(1.0/7.0)
'0.142857142857'
>>> repr(1.0/7.0)
'0.14285714285714285'
str.rjust()/ljust()/center()方法：右/左/中对齐，这些方法不会输出任何内容，它们只返回新的字符串。如果输入的字符串太长，它们不会截断字符串，而是保持原样返回
另外一种方法 str.zfill()，它向数值字符串左侧填充零。该函数可以正确识别正负号
>>>'-3.14'.zfill(7)  ==>> '-003.14'
str.format()方法：'{}'.format(str),{}中可以使用关键字参数和位置参数
{}字段名后允许可选的':'和格式指令：  '{0:.3f}'.format(3.1415926) ==>> '3.142'保留三位小数
':'后面紧跟一个整数可以限定该字段的最小宽度
7.1.1

'''