# lambda语句中，冒号前是参数，可以有多个，用逗号隔开，冒号右边的返回值。lambda语句构建的其实是一个函数对象
def f(x):
    return x**2
print(f(2))

g = lambda x,y : x**2-y
print(g(4,4))

import time
# 测试的Def函数
def square1(n):
    return n ** 2
# 测试的Lambda函数
square2 = lambda n: n ** 2
print(time.time())

# 使用Def函数
i = 0
while i < 10000:
    square1(10)
    i += 1
print(time.time())

# 使用lambda函数
i = 0
while i < 10000:
    square2(10)
    i += 1

print(time.time())
print(time.localtime(time.time()))