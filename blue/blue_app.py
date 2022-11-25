from wsgiref.simple_server import make_server


def app(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/plain')])
    return [b"Hello Blue, my name is Hiroshi.\n"]


httpd = make_server('0.0.0.0', 8080, app) linter will fail!
httpd.serve_forever()
