from django.shortcuts import render
from django.http import HttpResponse
from pymongo import MongoClient

a= "12345"
client = MongoClient("mongodb+srv://melekmbbal:"+a+"@cluster0.1b265hk.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
db = client["PawCare"] # database
collection = db["Veterinerler"] # collection


def pull_datas():
        cursor = collection.find({})

        name_list = []
        city_list = []
        phone_list = []
        address_list = []

        for document in cursor:
                name_list.append(document["name"])
                city_list.append(document["city"])
                phone_list.append(document["phone"])
                address_list.append(document["address"])
                
        zip_list = zip(name_list, city_list, phone_list, address_list)
                
        return zip_list


def home(request):
    return render(request, 'pages/home.html')   

def girisPage(request):
    return render(request, 'pages/girisPage.html')

def kayitPage(request):
    return render(request, 'pages/kayitPage.html')

def iletisimPage(request):
    return render(request, 'pages/iletisimPage.html')

def vetPage(request):
    zip_list = pull_datas()
    context = {
                    'zip_list': zip_list
            }
    return render(request, 'pages/vetPage.html', context)
