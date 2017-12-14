import time


def show_time(func):
    def inner():
        start_time = time.time()
        print(start_time)
        func()
        time.sleep(1)
        end_time = time.time()
        print(end_time)
        print('spend: %s' % (end_time - start_time))
    return inner


@show_time
def foo():
    print('foo...')


def bar():
    print('bar...')


foo()
