# https://www.cnblogs.com/wupeiqi/articles/5132791.html

import redis

r = redis.Redis(host='192.168.0.152', password='112358132134', port='6379')

# 在name对应的list中添加元素，
# 每个新的元素都添加到列表的最左边
# 保存顺序为: 33,22,11
# r.lpush('list01', 11,22,33)
# r.lpushx('list01', 100)
# rpush(name, values) 表示从右向左操作
print(r.llen('list01'))

# 在name对应的list中删除指定的值
# 参数：
# name，redis的name
# value，要删除的值
# num，  num=0，删除列表中所有的指定值；
# num=2,从前到后，删除2个；
# num=-2,从后向前，删除2个
r.lrem('list01', 33, 1)