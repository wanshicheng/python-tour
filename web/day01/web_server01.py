from wsgiref.simple_server import make_server


def application(environ, start_response):
    print('environ', environ['PATH_INFO'])
    start_response('200 OK', [('Content-Type', 'text/html')])
    return [b'<h1>Hello, web!</h1>']


# 封装 socket 对象以及准备过程（socket、bind、listen）
httpd = make_server('', 8080, application)

print('Serving HTTP on port 8080...')
# 开始监听HTTP请求:
httpd.serve_forever()
