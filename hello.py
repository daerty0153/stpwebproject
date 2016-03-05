def wsgi_app(env, start_responce):
    status = 'OK'
    headers = [('Content-Type', 'text/plain')]
    body = 'Hello, world!'
    start_responce(status, hearders)
    return [body]
