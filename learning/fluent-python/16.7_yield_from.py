"""
yield from 是全新的语言结构。它的作用比 yield 多很 多，因此人们认为继续使用那个关键字多少会引起误解。
在其他语言 中，类似的结构使用 await 关键字，这个名称好多了，因为它传达了 至关重要的一点：
在生成器 gen 中使用 yield from subgen() 时，subgen 会获得控制权，把产出的值传给 gen 的调用方，
    即调用方 可以直接控制 subgen。与此同时，gen 会阻塞，等待 subgen 终止。
1. yield from 可用于简化 for 循环中的 yield 表达式
yield from x 表达式对 x 对象所做的第一件事是，调用 iter(x)，从 中获取迭代器。因此，x 可以是任何可迭代的对象

!!! 2. yield from 的主要功能是打开双向通道，把最外层的调用方与最内层 的子生成器连接起来，这样二者可以直接发送和产出值，
还可以直接传 入异常，而不用在位于中间的协程中添加大量处理异常的样板代码。有 了这个结构，协程可以通过以前不可能的方式委托职责。
引入 yield from 结构的目的是为了支持实现了 __next__、send、close 和 throw 方法的生成器
调用方 main; 委派生成器 grouper； 子生成器 averager

yield from 做了什么
1。 子生成器产出的值都直接传给委派生成器的调用方
2。 使用 send() 方法发给委派生成器的值都直接传给子生成器
3。 生成器退出时，生成器（或子生成器）中的 return expr 表达式 会触发 StopIteration(expr) 异常抛出
4。 yield from 表达式的值是子生成器终止时传给 StopIteration的第一个参数
5。 传入委派生成器的异常，除了 GeneratorExit 之外都传给子生成 器的 throw() 方法

"""
import sys
from typing import Generator

# yield from 伪代码
# RESULT = yield from EXPR
EXPR = list()


def yield_from_for_learning(expr_in):
    """
    !!? 不能在代码中替换 yield from，返回异常 GeneratorExit
    _i 子生成器
    _y 子生成器产出的值
    _r 最终结果
    _s 调用方发给委派生成器的值，会被转发给子生成器
    _e 异常
    """
    if isinstance(expr_in, Generator):
        _i = expr_in
    else:
        _i = iter(expr_in)
    try:
        _y = next(_i)  # 预激子生成器
    except StopIteration as _e:
        _r = _e.value
    else:
        while 1:  # 运行这个循环时，委派生成器会阻塞，只作为调用方和子生成器之 间的通道。
            try:
                _s = yield _y  # 产出子生成器当前产出的元素；等待调用方发送 _s 中保存的值
            except GeneratorExit as _e:
                # close
                try:
                    _m = _i.close
                except AttributeError:
                    pass
                else:
                    _m()
                raise _e
            except BaseException as _e:  # 处理调用方通过 .throw(...) 方法传入的异常。可能没有throw
                # throw
                try:
                    _m = _i.throw
                except AttributeError:
                    raise _e
                else:  # 如果子生成器有 throw 方法，调用它并传入调用方发来的异常
                    try:
                        _y = _m(*sys.exc_info())
                    except StopIteration as _e:
                        _r = _e.value
                        break
            else:
                try:  # 尝试让子生成器向前执行
                    if _s is None:
                        _y = next(_i)
                    else:
                        _y = _i.send(_s)  # 试让子生成器向前执行，转发调用方发送的 _s
                except StopIteration as _e:
                    _r = _e.value
                    break
    return _r


def gen_yield():
    for c in 'as':
        yield c
    for i in range(4):
        yield i


def gen_yield_from():
    yield from 'as'
    yield from range(4)


print(list(gen_yield()), list(gen_yield_from()))


def chain(*iterables):
    for it in iterables:
        yield from it


# 调用方 main; 委派生成器 grouper； 子生成器 averager
def averager():
    _avg = 0
    _total = 0
    _count = 0
    while True:
        tmp = yield  # 接收值
        if tmp is None:
            break
        _count += 1
        _total += tmp
        _avg = _total / _count
    return _avg


def grouper(results, key):
    while True:
        # grouper 发送的每个值都会经由 yield from 处理，通过管道传给 averager 实例。
        # grouper 会在 yield from 表达式处暂停，等待 averager 实例处理客户端发来的值。
        # averager 实例运行完毕后，返 回的值绑定到 results[key] 上。
        # while 循环会不断创建 averager 实 例，处理更多的值。
        print("grouper", results, key)
        avg = averager()
        results[key] = yield from avg


def main(data_in):
    results = {}
    for key, vals in data_in.items():
        group = grouper(results, key)
        next(group)
        for val in vals:
            group.send(val)
        group.send(None)

    print(results)


if __name__ == '__main__':
    data = {
        'girls;kg': [40.9, 38.5, 44.3, 42.2, 45.2, 41.7, 44.5, 38.0, 40.6, 44.5],
        'girls;m': [1.6, 1.51, 1.4, 1.3, 1.41, 1.39, 1.33, 1.46, 1.45, 1.43],
        'boys;kg': [39.0, 40.8, 43.2, 40.8, 43.1, 38.6, 41.4, 40.6, 36.3],
        'boys;m': [1.38, 1.5, 1.32],
    }

    main(data)
