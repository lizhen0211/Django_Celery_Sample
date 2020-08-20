from time import sleep

from .celery import app


@app.task
def receivedata(x, y):
    print('receivedata before')
    # sleep(5)
    result = parsedata.delay(1, 2)
    # add.apply_async((2, 2))
    print(result)
    print('receivedata after')

    return x + y


@app.task
def parsedata(x, y):
    print('parsedata before')
    result = forwarddata.delay(1)
    print(result)
    # add.apply_async((2, 2))
    print('parsedata after')

    return x * y


@app.task
def forwarddata(numbers):
    print('forwarddata before')
    sleep(3)
    print('forwarddata after')
    return ''


# 这个hello函数不需要返回有用信息，设置ignore_rsult可以忽略任务结果
@app.task(ignore_result=True)
def printMessage():
    print('abc')
