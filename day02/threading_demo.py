import time
import threading

begin_time = time.time()


def foo(n):
    print('foo%s'%n)
    time.sleep(1)
    print('end foo')


def bar(n):
    print('bar%s'%n)
    time.sleep(2)
    print('end bar')


# foo()
# bar()

t1 = threading.Thread(target=foo, args=(1,))
t2 = threading.Thread(target=bar, args=(2,))
t1.start()
t2.start()

print('...main...')

t1.join()
t2.join()

end_time = time.time()


print(end_time - begin_time)