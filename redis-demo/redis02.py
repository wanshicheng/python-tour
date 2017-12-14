import redis

pool = redis.ConnectionPool(host='192.168.0.152', password='112358132134', port='6379')
r = redis.Redis(connection_pool=pool)

pipe = r.pipeline(transaction=True)
pipe.set('foo', 'Bar')
pipe.set('name', 'wsc')

pipe.execute()

print(r.keys())