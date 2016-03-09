pidfile = "/home/box/web/gunicorn/gunicorn.pid"
accesslog = "/home/box/web/gunicorn/access.log"
errorlog = "/home/box/web/gunicorn/error.log"
pythonpath = "/home/box/web/ask/ask"
workers = 16
timeout = 60

def wsgi_app(env, start_responce):
    status = '200 OK'
    headers = [('Content-Type', 'text/plain')]
    body = '\r\n'.join(env['QUERY_STRING'].split('&'))
    start_responce(status, headers)
    return body
