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
7.1.1旧式的字符串格式 %
7.2读写文件
f = open('filename','r/w/a'),返回一个文件对象
7.2.1文件对象的方法
f.read(size) 省略size则是读取全部内容
f.readline() 读取一行数据
f.readlines() 把所有行读到一个list中
f.wirte(string) 把string 的内容写入文件并返回None
f.tell()  f.seek(offset,from_what)
f.close() 使用完一个文件一定要记得close!
7.2.2使用json存储结构化数据

8.错误和异常
8.1语法错误 SyntaxError
8.2异常
8.3处理异常
try:
    xxx
except xxxError :
    xxx
 Try语句按以下方式工作。

    首先，执行try 子句（try和except关键字之间的语句）。
    如果未发生任何异常，忽略except 子句且try语句执行完毕。
    如果在 try 子句执行过程中发生异常，跳过该子句的其余部分。如果异常的类型与except关键字后面的异常名匹配, 则执行 except 子句，然后继续执行try语句之后的代码。
    如果异常的类型与 except 关键字后面的异常名不匹配，它将被传递给上层的try语句；如果没有找到处理这个异常的代码，它就成为一个未处理异常，程序会终止运行并显示一条如上所示的信息。
8.4引发异常
raise()
8.5用户定义的异常
class MyError(Exception):
    xxx
异常类通常继承Exception类
8.6定义清理操作
try:
    xxx
finally:
    xxx
不管有没有发生异常，在离开try语句之前总是会执行finally 子句
8.7清理操作的预定义


9.类
9.1名称和对象
9.2Python作用域和命名空间
命名空间是从名称到对象的映射，不同命名空间内的名称绝对没有任何关系
作用域是Python程序中可以直接访问一个命名空间的代码区域
9.3初识类
9.3.1类定义
class className(object):
    pass
9.3.2类对象
支持属性引用和实例化
属性引用： obj.name
实例化： 使用函数的符号， x = MyClass()
9.3.3实例对象， 其唯一可用的操作就是属性引用，包括数据属性和方法
9.3.4方法对象
9.3.5类和实例变量
一般来说，实例变量用于对每一个实例都是唯一的数据，类变量用于类的所有实例共享的属性和方法
可变对象例如列表和字典不应该用作类变量
9.4补充说明
9.5继承
class derivedClassName(baseClassName):
    pass
父类与子类必须定义在一个作用域内
使用isinstance()检查实例类型
使用issubclass()检查类的继承
9.5.1多继承
class derivedClassName(Base1,Base2,Base3):
    pass
9.6私有变量和类本地引用
_spam
__spam
9.7零碎的说明
9.8异常也是类
9.9迭代器
9.10生成器：创建迭代器的工具
9.11生成器表达式，类似于列表表达式，简单的可以用()代替[]

'''