from time import sleep

from .celery import app


@app.task
def receivedata(x):
    print('receivedata before' + str(x))
    # sleep(5)
    # result = parsedata.delay(x)
    # add.apply_async((2, 2))
    # print(result)
    # print(x)
    print('receivedata after' + str(x))
    return x


@app.task
def parsedata(x):
    print('parsedata before')
    result = forwarddata.delay(x)
    print(result)
    # add.apply_async((2, 2))
    print('parsedata after')

    return x


@app.task
def forwarddata(numbers):
    print('forwarddata before')
    sleep(3)
    print('forwarddata after')
    # return numbers


# 这个hello函数不需要返回有用信息，设置ignore_rsult可以忽略任务结果
@app.task(ignore_result=True)
def printMessage():
    print('abc')
