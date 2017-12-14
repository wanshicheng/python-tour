import redis

r = redis.Redis(host='192.168.0.152', password='112358132134', port='6379')
r.set('foo', 'Bar')

print(r.get('foo'))