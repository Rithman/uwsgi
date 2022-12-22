from os import chdir, listdir
from os.path import isfile, join
from pathlib import Path

import views

chdir(Path(__file__).parent.resolve())


class Application:
    def __init__(self):
        self.templates_list = self.get_templetes()
        self.views_list = [el.split('_')[:-1][0] for el in dir(views) if el.endswith('_view')]


    def __call__(self, environ, start_response):
        start_response('200 OK', [('Content-Type', 'text/html')])
        request_path = environ['PATH_INFO']
        
        # Process root path
        if request_path == "/":
            return views.index_view(self.get_params(environ))


        # Process other paths. Custom view MUST be named 'TemplateFileName_view'. 
        # Complex paths like '/main/sub_chapter/' are not supported yet.
        elif environ['PATH_INFO'].strip('/') in self.views_list:
            view = getattr(views, environ['PATH_INFO'].strip('/')+'_view')
            return self.call_view(view, environ)


        # If there is no view for the path - 404
        elif request_path not in self.templates_list:
            return views.notfound_view(self.get_params(environ))
        

    def call_view(self, view, environ):
        return view(self.get_params(environ))


    @staticmethod
    def get_params(environ):
        if environ['QUERY_STRING']:
            params = environ['QUERY_STRING'].split("&")
            res_dict = {k: v for k, v in (el.split("=") for el in params)}
        else:
            res_dict = {}
        return res_dict


    @staticmethod
    def get_templetes():
        files_list = [f for f in listdir('templates') if (isfile(join('templates', f)) and (f.endswith('.html')) or f.endswith('htm'))]
        templates_list = [_.split('.')[:-1][0] for _ in files_list]
        return templates_list


app = Application()


