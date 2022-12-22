from jinja2 import Environment, FileSystemLoader
from os import chdir
from pathlib import Path

chdir(Path(__file__).parent.resolve())


temp_loader = FileSystemLoader(searchpath='./templates')
env = Environment(loader=temp_loader)


def index_view(params): 
    index_page = env.get_template('index.html')
    res = index_page.render(title='Main page', header='Main page description', params=params)
    return [res.encode("utf-8")]

def about_view(params):
    about_page = env.get_template('about.html')
    res = about_page.render(title='About page', header='About page description', params=params)
    return [res.encode("utf-8")]

def notfound_view(params):
    index_page = env.get_template('notfound.html')
    res = index_page.render(title='404', header='404 Page not found', params=params)
    return [res.encode("utf-8")]