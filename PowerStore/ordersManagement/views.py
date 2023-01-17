from django.shortcuts import render
from django.http import HttpResponse
from ordersManagement.models import Item

# Create your views here.

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

def contact(request):

    if request.method == "POST":
        return render(request, 'thankyou.html')

    return render(request, 'contact.html')