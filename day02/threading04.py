import time
import threading

def addNum():
    global num #在每个线程中都获取这个全局变量
    # num-=1

    temp=num
    t = threading.current_thread()
    print('--get num:',num, t.getName())
    time.sleep(0.1)
    num =temp-1 #对此公共变量进行-1操作


num = 100  #设定一个共享变量
thread_list = []
for i in range(100):
    t = threading.Thread(target=addNum)
    t.start()
    thread_list.append(t)

for t in thread_list: #等待所有线程执行完毕
    t.join()

t = threading.current_thread()

print('final num:', num , t.getName())