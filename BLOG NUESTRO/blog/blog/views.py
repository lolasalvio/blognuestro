from django.http import HttpResponse
from django.template import loader


#Class BlogList(listview):
   # model = blogmodel
    #template_name = "blog\index.html"

#loader.get_template("index.html")
#loader.get_template("nosotros.html")
#loader.get_template("register.html")
#loader.get_template("blogs.html")

def index(request):
    return HttpResponse("PAGINA BIENVENIDA")


def nosotros(request):
    return HttpResponse("ABOUT US")

def register(request):
    return HttpResponse("REGISTRATE")

def blogs(request):
    return HttpResponse("ENTRADAS")