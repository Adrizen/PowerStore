from django.shortcuts import render
from django.http import HttpResponse
from ordersManagement.models import Item
from ordersManagement.forms import ContactForm

# Create your views here.

def home(request):
    return render(request, "home.html")

def services(request):
    return render(request, "services.html")

def store(request):
    return render(request, "store.html")

def contact(request):
    if request.method == "POST":
        myForm = ContactForm(request.POST)
        
        if myForm.is_valid():
            dataForm = myForm.cleaned_data
            print(dataForm)
            return render(request, 'thankyou.html')
    else:
        myForm = ContactForm()
    return render(request, 'contact_form.html',{'form': myForm})

def blog(request):
    return render(request, "blog.html")

def search_item(request):
    return render(request, "search_item.html")

def search(request):
    if request.GET["item"]:
        item_name = request.GET["item"]

        if len(item_name) > 20:
            message = 'Search term too long (max 20 characters)'

        else:
            items = Item.objects.filter(name__icontains = item_name)
            return render(request, "search_result.html", {"items": items, "query": item_name})
    
    else:
        message = 'You need to write a item to search'

    return HttpResponse(message)

