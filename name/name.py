print("first " + __name__)


'''
一个python的文件有两种使用的方法，第一是直接作为脚本执行，
第二是import到其他的python脚本中被调用（模块重用）执行。
因此if __name__ == 'main': 的作用就是控制这两种情况执行代码的过程，
在if __name__ == 'main': 下的代码只有在第一种情况下即文件作为脚本直接执行才会被执行，
而import到其他脚本中是不会被执行的。
'''
if __name__ == "__main__":
    print("second " + __name__)