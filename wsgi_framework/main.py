

class Framework:
    def __init__(self, routes, fronts):
        self.routes = routes
        self.fronts = fronts


    def __call__(self, environ, start_response):
        request_method = environ.get('REQUEST_METHOD')
        request_path = environ.get('PATH_INFO')
        if not request_path.endswith('/'):
            request_path += '/'

        if request_path in self.routes:
            view = self.routes[request_path]
        else:
            view = self.routes['/404/']

        request = {}
        for front in self.fronts:
            front(request)
        request['get_params'], request['post_params'] = self.get_request_params(environ)

        code, body = view(request)
        start_response(code, [('Content-Type', 'text/html')])
        return [body.encode('utf-8')]


    # Return GET and POST params in tuple of dicts
    def get_request_params(self, environ):
        get_data = environ['QUERY_STRING'] if environ['QUERY_STRING'] else ''
        post_length_data = environ.get('CONTENT_LENGTH')
        post_length = int(post_length_data) if post_length_data else 0
        post_data = environ['wsgi.input'].read(post_length).decode('utf-8') if post_length > 0 else 0
        return self.parse_params(get_data), self.parse_params(post_data)


    @staticmethod
    def parse_params(data):
        params_dict = {}
        if data:
            elements = data.split("&")
            params_dict = {k: v for k, v in (el.split("=") for el in elements)}
        return params_dict

