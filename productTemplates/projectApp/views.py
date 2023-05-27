from django.shortcuts import render

# Create your views here.
def electronics(request):
    product_dict ={
        "product1": "Mac",
        "product2": "Iphone",
        "product3": "Hp"
    }
    return render(request, 'productApp/product.html', product_dict)


def toys(request):
    product_dict ={
        "product1": "Drone",
        "product2": "Kit",
        "product3": "Remote Car"
    }
    return render(request, 'productApp/product.html', product_dict)



def shoes(request):
    product_dict ={
        "product1": "Nike",
        "product2": "Prade",
        "product3": "Gucci"
    }
    return render(request, 'productApp/product.html', product_dict)


def index(request):
    return render(request, 'productApp/index.html')

