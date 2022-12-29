from wsgi_framework.templator import render

class Index:
    def __call__(self, request):
        print(f"GET params: {request.get('get_params')}")
        print(f"POST params: {request.get('post_params')}")
        return '200 OK', render('index.html', 
                                date=request.get('date'),
                                get_params=request.get('get_params'),
                                post_params=request.get('post_params'),
                                title='Guitar shop',
                                header='Welcome to our super cool Guitar shop')


class About:
    def __call__(self, request):
        print(f"GET params: {request.get('get_params')}")
        print(f"POST params: {request.get('post_params')}")
        return '200 OK', render('about.html', 
                                date=request.get('date'),
                                get_params=request.get('get_params'),
                                post_params=request.get('post_params'), 
                                title='About US',
                                header='Here is some info about our Guitar shop')
                            

class NotFound:
    def __call__(self, request):
        print(f"GET params: {request.get('get_params')}")
        print(f"POST params: {request.get('post_params')}")
        return '404 NOT FOUND', render('404.html', 
                                date=request.get('date'),
                                get_params=request.get('get_params'),
                                post_params=request.get('post_params'), 
                                title='404',
                                header='404 Page not found')


class Contacts:
    def __call__(self, request):
        print(f"GET params: {request.get('get_params')}")
        print(f"POST params: {request.get('post_params')}")
        return '200 OK', render('contacts.html', 
                                date=request.get('date'),
                                pget_params=request.get('get_params'),
                                post_params=request.get('post_params'),
                                title='Contacts',
                                header='Our contacts')

