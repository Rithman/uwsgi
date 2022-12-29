from datetime import date
from views import Index, About, NotFound, Contacts 

def date_front(request):
    request['date'] = date.today()

fronts = [date_front]

routes = {'/': Index(),
          '/about/': About(),
          '/404/': NotFound(),
          '/contacts/': Contacts()}