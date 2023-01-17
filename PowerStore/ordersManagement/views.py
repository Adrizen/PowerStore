from django.shortcuts import render
from django.http import HttpResponse
from ordersManagement.models import Item

# Create your views here.

def search_item(request):

    return render(request, "search_item.html")

def search(request):
    if request.GET["item"]:
        # message = f'Item: {request.GET["item"]}'
        item_name = request.GET["item"]
        items = Item.objects.filter(name__icontains = item_name)
        return render(request, "search_result.html", {"items": items, "query": item_name})
    
    else:
        message = 'You need to write a item to search'

    return HttpResponse(message)