from django.shortcuts import render
from django.http import HttpResponse
from pymongo import MongoClient

a= "12345"
client = MongoClient("mongodb+srv://melekmbbal:"+a+"@cluster0.1b265hk.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
db = client["PawCare"] # database
collection = db["Veterinerler"] # collection
collection2 = db["kullanicilar"] # collection
collection3 = db["ilaclar"] # collection


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
    
def authorize_save(username, no, password):
    collection2.insert_one({
        "username": username,
        "no": no,
        "password": password
    })
    
def authorize_check(no, password):
    cursor = collection2.find({})
    
    for document in cursor:
        if document["no"] == no and document["password"] == password:
            return True
    return False
        


def home(request):
    return render(request, 'pages/home.html')  

def kullaniciPage(request):
    return render(request, 'pages/home.html') 

def girisPage(request):
    if request.method == 'POST':
        no = request.POST.get('no', '')
        sifre = request.POST.get('password', '')
        
        if authorize_check(no, sifre):
            name = collection2.find_one({"no": no})["username"]
            return render(request, 'pages/kullaniciPage.html', {'name': name})
        
    return render(request, 'pages/girisPage.html')

def kayitPage(request):
    if request.method == 'POST':
        patiAdi = request.POST.get('username', '')
        no = request.POST.get('no', '')
        sifre = request.POST.get('password', '')
        
        authorize_save(patiAdi, no, sifre)
        
    return render(request, 'pages/kayitPage.html')

def iletisimPage(request):
    return render(request, 'pages/iletisimPage.html')

def vetPage(request):
    zip_list = pull_datas()
    context = {
                    'zip_list': zip_list
            }
    return render(request, 'pages/vetPage.html', context)

def ilacPage(request):
    cursor = collection3.find({})

    name_list = []
    purpose_list = []
    frequency_list = []
    how_list = []
    kullanim_list = []

    for document in cursor:
        name_list.append(document["name"])
        purpose_list.append(document["purpose"])
        frequency_list.append(document["frequency"])
        how_list.append(document["how"])
        kullanim_list.append(document["kullanim"])
                
    zip_list = zip(name_list, purpose_list, frequency_list, how_list, kullanim_list)
                
    context = {
                    'zip_list': zip_list
            }
    return render(request, 'pages/ilacPage.html', context)
