from wsgiref.simple_server import make_server

from wsgi_framework.main import Framework
from urls import fronts, routes


application = Framework(routes, fronts)

with make_server('127.0.0.1', 8000, application) as httpd:
    print("Server is running at 127.0.0.1:8000 ...")
    httpd.serve_forever()
