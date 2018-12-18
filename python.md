# python基础复习
1.break 跳出当前的循环
2.continue 跳过本次的循环继续下一次的循环?
### 1.列表List[ ]
作用:对列表的操作,添加,删除,排序, # 列表是可以嵌套的
List是一种有序的集合,可以随时添加和删除其中的元素,字符串的元素索引从0开始递增,逆着字符串元素索引从-1开始递减。元素通过索引访问
列表可以包含其他列表,构成信息列表,这个列表就是一个数据库
list是处理一组有序项目的数据结构
对列表的操作,添加,删除,排序
```python
myList = [['a','b','c'],['d','e','f']]
#索引  myList[0]  'a'
myList =[myList1,myList2]
```
字符串转变为列表?
在列表中如何插入一个值?
### 2.元组tuple()
```python
zoo=('wolf','elephant','penguin')
```
作用:元组通常用用在是语句或用户定义的函数能够安全的采用一组值的时候
Tuple和List的区别在于,tuple一旦初始化就不能修改,个别值不能进行删除,但是可以删除整个元组
### 3.集合set { }
作用:去除重复的数据(去重)
集合可以做差集、并集、交集、补集
集合的创建:可以使用大括号{}或者set()来创建
注意:创建一个空集合必须使用set()而不是{} 因为使用{}创建的是一个字典
### 4.字典dict
#### 字典类似于你通过联系人名称查找地址和联系人详细情况的地址簿,把键(名字)和值(详细情况)联系在一起。。注意:键必须是唯一的,如果有同名的存在,就无法找到正确的信息
d = {key1:value1,key2:value2}
注意:字典中的键值对是没有顺序的
字典的操作:添加,删除,打印
```
dict1={'zhang':'张家辉','wang':'王宝强','li':'李冰冰','zhao':'赵薇'}
dict1['huang']='黄家驹'
del dict1['zhao']
for firstname,name in dict1.items():
print firstname,name
结果:
li 李冰冰
wang 王宝强
huang 黄家驹
zhang 张家辉
```
###
python中append()和expend() 的区别?
append()是像向list里追加内容的
如果你有一个list,并且向list的尾部添加对象那么就可以用append()
例如
list.append(对象)
添加到列表末尾的对象,该方法无返回值,但是会修改原来的列表。
expend()相当于列表的拼接
extend()和append()功能类似,但在处理多个列表时,返回的结果完全不同。
```python
>>> a=[1,2,3]
>>> b=[4,5,6]
>>> a.append(b)
>>> a
[1, 2, 3, [4, 5, 6]]
>>> a=[1,2,3]
>>> a.extend(b)
>>> a
[1, 2, 3, 4, 5, 6]
```
### 5.流程的控制分为哪几种?
顺序结构分支结构选择结构
### 程序的执行流程?
顺序执行选择执行循环执行
函数及面向对象的运行过程
## 函数
函数可以重名,但是会被覆盖
6.变量的作用域
(1)全局变量
(2)局部变量
?(3)关键字global 声明函数内外使用同一个变量
?(4)关键字nonlocal 在函数的嵌套时可以获取外层函数的变量函数内外都使用的同一个变量
?(5)可变类型不可变类型
##### 可变类型:比如列表你只是修改了列表中的某一个值但是本身没有动
##### 不可变类型:比如字符串,int    当你在给一个新的值的时候那么原来的值会被丢弃那么此刻会生成一个新的变量
## 函数的几种导入的方式
```python
import myfunction.returnfunction# import myfunction.returnfunction
print(myfunction.returnfunction.demo(10,20))
from myfunction import returnfunction #从myfunction的文件夹里导入returnfunction文件
print(returnfunction.demo1(10,20,30))
from myfunction import returnfunction as func  #从myfunction的文件夹里导入returnfunction文件  as func 起一个别名
print(func.demo1(10,20,30))
import random as ran   #起一个别名
ran.randint()
```
### 7.列表推导式
提供了创建列表的简单途径
## 8.迭代器
可迭代对象
可以直接作用于for循环的对象称为可迭代对象(lterable)可以通过isinstance判断是否为可迭代对象
可以用于for循环的数据类型
list string dict set tuple
判断是否为可迭代对象需要引入Iterable来进行判断
```python
from collections import Iterable
#判断是否为可迭代对象
print(isinstance([],Iterable))
print(isinstance({},Iterable))
print(isinstance("",Iterable))
print(isinstance(1,Iterable))
```
#### 迭代器
1. 迭代器是从对象集合的第一个元素开始访问只能前进不能后退
2. 迭代器有俩个方法 iter()  next() *iter时将可迭代对象转换成迭代器  next是可以将迭代器的元素一个一个的进行访问 *)
3. 当迭代器的元素都访问完以后再次访问会报StopIteration 的错误
## 9.生成器
使用了yield的函数称为生成器
生成器也实现了迭代器的功能
使用列表生成器生成出来的(x for x in range(1,5))是生成器并不是像列表一样一个一个的生产而是用一个产一个
使用yield的函数好处,节约资源,加上yield函数(调用一次执行一次避免了全部执行完节约电脑资源)
配合
yield
next()
yield想当于暂停键,调用一次执行一次,暴力破解密码或者网站的时候可以用生成器去实现,不然电脑存放不了那么大的数据
## 10.异常处理
需求:当程序出现问题时不让程序结束而是越过错误继续执行抛出异常
一个try语句可以包含多个except子句分别来处理不同的异常最多只有一个分支会执行1. 一个except子句可以包含多个异常这些异常的名称放在括号里或者称为元组里
#### 主体结构:
```python
try:
#可能会发生异常的代码
except: #捕获所有的异常
#处理出现的异常
```
#### (1) 捕获特定一个错误的异常处理
```python
#捕获特定一个错误的异常处理
try:
# 1+'a'
int('a')
except TypeError as e:
print(e)
```
#### (2) 一个try 语句对应多个 except子句
```python
一个try 语句对应多个 except子句
try:
# 1+'a'
int('a')
except TypeError as e:
print(e)
except ValueError as v:
print(v)
```
#### (3) 一个except 子句捕获特定的n个异常
```python
#一个except 子句捕获特定的n个异常
try:
1+'a'
# int('a')
except (TypeError,ValueError) as e:
print(e)
```
#### (4) 可选的 else 子句
##### 如果想使用 else子句必须放在 except之后这个子句将在try语句没有任何异常的时候去执行(没异常会执行)
**格式:**
try....except.....else
```python
try:
1+1
except (TypeError,ValueError) as e:
print(e)
else:
print("只有在没有任何异常的情况下你才能够看到我")
```
#### (5) finally
##### try子句有没有发生异常都会去执行(不管有没有异常都会去执行)
```python
try:
1+1
except (TypeError,ValueError) as e:
print(e)
else:
print("只有在没有任何异常的情况下你才能够看到我")
finally:
print("你有没有异常我都执行")
```
#### (6)手动抛出异常
##### raise   异常名称("输出的提示信息")
例如:
```python
raise NameError("我出错了")
Traceback (most recent call last):
File "C:\/Users\/xlg\/PycharmProjects\/shPython1701\/day8文件操作\/1raise.py", line 2, in <module>
raise NameError("我出错了")
NameError: 我出错了
```
## 11.装饰器??
# 文件操作
## 二 os模块
##### 如果想使用os模块那么你需要先导入 os模块
##### import os
|           函数名           |                  函数的说明                   |
| :---------------------: | :--------------------------------------: |
|         os.name         | 获取操作系统的类型(nt->windows  posix->Linux,Unix) | | os.environ | 获取操作系统中的环境变量|
| os.environ.get("path")  |                获取某一个的环境变量                | |        os.curdir        |                 获取当前的目录                  |
| os.getcwd() | 获取当前工作目录的绝对路径|
|      os.listdir()       |           以列表的形式返回当前目录下的所有文件|
|       os.mkdir()        |                   创建目录                   |
|       os.rmdir()        |                  删除文件夹                   |
|   os.rename(old,new)    |                   重命名                    |
| os.path.join(path,file) |                拼成一个正确的路径                 | |   os.path.splitext()    |                 获取文件扩展名                  |
|     os.path.isdir()     |                 判断是否是目录                  |
|    os.path.isfile()     |                 判断是否是文件                  |
| os.path.exists() | 判断文件或者路径是否存在|
|    os.path.getsize()    |               获取文件的大小(字节)                | |    os.path.dirname()    |                  获取目录名                   |
|   os.path.basename()    |                  获取文件名                   |
| os.path.abspath() | 获取一个文件的绝对路径|
|     os.path.split()     |                   拆分路径                   |
### ??匿名函数
**关键字:** lambda
**注意:**
1. lambda只是一个表达式函数体比def简单很多
2. lambda主体是一个表达式而不是一个代码块仅仅能在 lambda表达式中封装有限的逻辑进去
```python
#lambda匿名函数的使用
# func = lambda a,b:a+b
# print(func(3,5))
#定义并调用
# print((lambda a,b:a+b)(3,5))
# a = 10
# func = lambda:a
# print(func())
```
## ???二文件的操作
##### **(1)**  file = open(path,打开的方式)   #打开文件将会返回一个file对象使用这种方式的打开就需要去关闭
#### open的打开方式
| 函数名  |                  函数的说明                   |
| :--: | :--------------------------------------: |
|  r   |         以只读的方式打开文件的描述符放在文件的开头         |
|  rb  |        以二进制读的格式打开文件的描述符放在文件的开头        |
|  w   |       以清空写的方式打开如果文件存在则清空不存在则尝试创建       |
|  wb  |     以二进制清空写的格式打开如果文件存在则清空不存在则尝试创建     | |  a   | 打开一个文件用于追加写如果文件存在文件描述会放在文件的末尾不存在则
尝试创建 |
|  ab  |               以二进制追加写的方式打开               |
|      |                                          |
|      |                                          |
|      |                                          |
## ???(2) 文件的读取
file.read([size]) 读取文件下的所有内容(默认)  如果给指定了的size 会按照你的size去进行读取
file.readline()  读取一行
file.readlines() 读取所有的行以列表的形式返回
##### (3) 文件的写
file.write(str)  将字符串写入文件
file.writelines()   将字符串放在列表里如果需要换行则自己每个加入一个换行符
##### (4) 字符的编码
encode(字符编码)
闭包:调用函数A, 函数A返回了一个函数B,这个函数B就叫做闭包


