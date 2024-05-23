from django.shortcuts import render
from django.http import HttpResponse
from pymongo import MongoClient

<<<<<<< HEAD
a= "12345"
client = MongoClient("mongodb+srv://melekmbbal:"+a+"@cluster0.1b265hk.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
db = client["PawCare"] # database
collection = db["Veterinerler"] # collection
collection2 = db["kullanicilar"] # collection
collection3 = db["ilaclar"] # collection


def pull_notlar():
    cursor = collection2.find({})
    
    not_list = []
    
    for document in cursor:
        not_list.append(document["not"])
        
    return not_list

def pull_datas():
        cursor = collection.find({})
=======

class MongoDBClient:
    def __init__(self, uri, db_name):
        self.client = MongoClient(uri)
        self.db = self.client[db_name]

    def get_collection(self, collection_name):
        return self.db[collection_name]


class VeterinerlerService:
    def __init__(self, collection):
        self.collection = collection
>>>>>>> 45df169eca064828fa0865a4706e0498fb3a5a70

    def pull_datas(self):
        cursor = self.collection.find({})
        name_list = []
        city_list = []
        phone_list = []
        address_list = []

        for document in cursor:
<<<<<<< HEAD
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

=======
            name_list.append(document["name"])
            city_list.append(document["city"])
            phone_list.append(document["phone"])
            address_list.append(document["address"])

        return zip(name_list, city_list, phone_list, address_list)


class KullaniciService:
    def __init__(self, collection):
        self.collection = collection

    def authorize_save(self, username, no, password):
        self.collection.insert_one({
            "username": username,
            "no": no,
            "password": password
        })

    def authorize_check(self, no, password):
        cursor = self.collection.find({})
        for document in cursor:
            if document["no"] == no and document["password"] == password:
                return True
        return False


class IlacService:
    def __init__(self, collection):
        self.collection = collection

    def pull_ilac_datas(self):
        cursor = self.collection.find({})
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

        return zip(name_list, purpose_list, frequency_list, how_list, kullanim_list)


# MongoDB connection setup
a = "12345"
client = MongoDBClient(f"mongodb+srv://melekmbbal:{a}@cluster0.1b265hk.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0", "PawCare")

# Services initialization
veterinerler_service = VeterinerlerService(client.get_collection("Veterinerler"))
kullanici_service = KullaniciService(client.get_collection("kullanicilar"))
ilac_service = IlacService(client.get_collection("ilaclar"))


def home(request):
    return render(request, 'pages/home.html')


def kullaniciPage(request):
    return render(request, 'pages/home.html')
>>>>>>> 45df169eca064828fa0865a4706e0498fb3a5a70


def girisPage(request):
    if request.method == 'POST':
        no = request.POST.get('no', '')
        sifre = request.POST.get('password', '')
<<<<<<< HEAD
        
        if authorize_check(no, sifre):
            name = collection2.find_one({"no": no})["username"]
            return render(request, 'pages/kullaniciPage.html', {'name': name})
        
        return notPage(request, no, sifre)  # notPage fonksiyonuna no ve sifre değerlerini geç
       
    return render(request, 'pages/girisPage.html')

def notPage(request, no, sifre):    
    if authorize_check(no, sifre):
        not_ = collection2.find_one({"no": no})
        if not_:
            return render(request, 'pages/notPage.html', {'not': not_['not']})
    return render(request, 'pages/home.html')

def baskaBirFonksiyon(request):
    # Oturum verilerinden no'ya eriş
    no = request.session.get('no')
    sifre = request.session.get('sifre')
    
    return no, sifre
=======

        if kullanici_service.authorize_check(no, sifre):
            name = kullanici_service.collection.find_one({"no": no})["username"]
            return render(request, 'pages/kullaniciPage.html', {'name': name})

    return render(request, 'pages/girisPage.html')

>>>>>>> 45df169eca064828fa0865a4706e0498fb3a5a70

def kayitPage(request):
    if request.method == 'POST':
        patiAdi = request.POST.get('username', '')
        no = request.POST.get('no', '')
        sifre = request.POST.get('password', '')
<<<<<<< HEAD
        
        authorize_save(patiAdi, no, sifre)
        
=======

        kullanici_service.authorize_save(patiAdi, no, sifre)

>>>>>>> 45df169eca064828fa0865a4706e0498fb3a5a70
    return render(request, 'pages/kayitPage.html')


def iletisimPage(request):
    return render(request, 'pages/iletisimPage.html')


def vetPage(request):
    zip_list = veterinerler_service.pull_datas()
    context = {
        'zip_list': zip_list
    }
    return render(request, 'pages/vetPage.html', context)


<<<<<<< HEAD


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
=======
def ilacPage(request):
    zip_list = ilac_service.pull_ilac_datas()
    context = {
        'zip_list': zip_list
    }
>>>>>>> 45df169eca064828fa0865a4706e0498fb3a5a70
    return render(request, 'pages/ilacPage.html', context)
