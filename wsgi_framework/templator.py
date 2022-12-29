from jinja2 import Environment, FileSystemLoader


template_loader = FileSystemLoader(searchpath='templates')
env = Environment(loader=template_loader)

def render(template, **kwargs):
    page = env.get_template(template)
    res = page.render(**kwargs)
    return res

        

