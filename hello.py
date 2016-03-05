def wsgi_app(env, start_responce):
    status = 'OK'
    headers = [('Content-Type', 'text/plain')]
    body = env['QUERY_STRING'].split('&')
    start_responce(status, headers)
    return body
