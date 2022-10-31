from wsgiref.simple_server import make_server


def app(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/plain')])
    return [b"Hello World, my name is Hiroshi.\n"]


httpd = make_server('0.0.0.0', 8080, app)
httpd.serve_forever()
