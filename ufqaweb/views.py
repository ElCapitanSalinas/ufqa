from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.core.files.storage import FileSystemStorage
from django.db.models import F
import os, os.path
import unidecode


from django.contrib.auth.hashers import make_password
from django.contrib.auth.hashers import check_password

from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User


# Create your views here.
from .models import TextosBase, Estadisticas, Casos, Donadores, AdminUser, Images
from .forms import ImageForm
from datetime import datetime

def index(request):
    casos = Casos.objects.all()
    

    casosShow = []
    for caso in casos:
        imagen = Images.objects.filter(project_id=caso.id)[:1]
        banner = None
        for image in imagen:
            banner = image.image

        casoCompl = {
            'id': len(casosShow)+1,
            'caseid': caso.id,
            'titulo': caso.titulo,
            'desc': caso.descb,
            'porc': caso.get_percentage,
            'recolectado': caso.recolectado,
            'banner': banner
        }
        casosShow.append(casoCompl)

    impcasos = casosShow[0:2]
    defcasos = casosShow[2:8]
    
    
        
    return render(request, 'main/index.html', {'casos': defcasos, 'impcasos':impcasos})

def about(request):

    que_es = TextosBase.objects.get(titulo='que_es')
    quienes_somos = TextosBase.objects.get(titulo='quienes_somos')
    nuestra_historia = TextosBase.objects.get(titulo='nuestra_historia')
    que_hacemos = TextosBase.objects.get(titulo='que_hacemos')
    nuestro_enfoque = TextosBase.objects.get(titulo='nuestro_enfoque')
    mision = TextosBase.objects.get(titulo='mision')
    vision = TextosBase.objects.get(titulo='vision')
    join_us = TextosBase.objects.get(titulo='join_us')

    
    return render(request, 'about/index.html', {'que_es' : que_es.contenido, 'quienes_somos' : quienes_somos.contenido,'nuestra_historia' : nuestra_historia.contenido,'que_hacemos' : que_hacemos.contenido, 'nuestro_enfoque' : nuestro_enfoque.contenido,'mision' : mision.contenido,'vision' : vision.contenido,'join_us' : join_us.contenido})

def caseprofile(request, id):
    casoData = Casos.objects.get(id=id)
    images = Images.objects.filter(project_id=id)
    donators = Donadores.objects.filter(project_id=casoData)
    bannerimgs = images

    for image in bannerimgs:
        print(image.image)
        
    casos = Casos.objects.all()

    casosShow = []
    for caso in casos:
        imagen = Images.objects.filter(project_id=caso.id)[:1]
        banner = None
        for image in imagen:
            banner = image.image

        casoCompl = {
            'id': len(casosShow)+1,
            'caseid': caso.id,
            'titulo': caso.titulo,
            'desc': caso.descb,
            'porc': caso.get_percentage,
            'recolectado': caso.recolectado,
            'banner': banner
        }
        casosShow.append(casoCompl)
    
    otherCases = casosShow[0:5]

    return render(request, 'caso/index.html', {'caso': casoData, 'bannerimgs': bannerimgs, 'donators': donators, 'otherCases': otherCases})

def allcases(request):
    casos = Casos.objects.all()

    casosShow = []
    for caso in casos:
        imagen = Images.objects.filter(project_id=caso.id)[:1]
        banner = None
        for image in imagen:
            banner = image.image

        casoCompl = {
            'id': len(casosShow)+1,
            'caseid': caso.id,
            'titulo': caso.titulo,
            'desc': caso.descb,
            'porc': caso.get_percentage,
            'recolectado': caso.recolectado,
            'banner': banner
        }
        casosShow.append(casoCompl)


    return render(request, 'casos/index.html', {'allcases': casosShow})


def register(request):
 
    # if this is a POST request we need to process the form data
    if request.method == 'POST':

                if request.POST['email'] and request.POST['username'] :
                    if request.POST['password']:
                        if request.POST['password'] == request.POST['password2']:

                                user = User.objects.create_user(request.POST['username'], request.POST['email'], request.POST['password'])
                                user.save()
                                print("GUARDADO")
                                return HttpResponseRedirect(f'/admin/')
                            
                        else:
                            return render(request, 'admin/register.html', {'message': 'La contraseña no coincide'})
                else:
                    return render(request, 'admin/register.html', {'message': 'Faltan campos por llenar'})
    else:
        form = None



    return render(request, 'admin/register.html', {})

def adminPanel(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        # try:
        print(password)
        # useradmin = AdminUser.objects.get(correo=mail)
        user = authenticate(username=username, password=password)
        # if check_password(password, useradmin.contrasena):
        if user is not None:
            login(request, user)
            casos = Casos.objects.all()
            return render(request, 'admin/admin.html', {'casos': casos[0:3]})
        else:
            return render(request, 'admin/login.html', {'message': 'Correo o Contraseña incorrectos',})
        # except AdminUser.DoesNotExist or user :
        #     return render(request, 'admin/login.html', {'message': 'Correo o Contraseña incorrectos',})
    elif request.user.is_authenticated:
        casos = Casos.objects.all()
        return render(request, 'admin/admin.html', {'casos': casos[0:3]})
    else:
        return render(request, 'admin/login.html', {})


def casos(request):
    if request.user.is_authenticated:
        casos = Casos.objects.all()
        return render(request, 'admin/cases.html', {'casos': casos})
    else:
        HttpResponseRedirect(f'/admin/')


def vercaso(request, id):
    if request.user.is_authenticated:
        casoData = Casos.objects.get(id=id)
        donators = Donadores.objects.filter(project_id=casoData)


        return render(request, 'admin/vercaso.html', {'caso': casoData, 'donators': donators})
    else:
        HttpResponseRedirect(f'/admin/')

def createUpdate(request, id):
    if request.user.is_authenticated:
        if request.method == 'POST':
            casoData = Casos.objects.get(id=id)
            update = request.POST['updateText']

            if update:
                casoData.last_update = datetime.today().strftime('%Y-%m-%d')
                casoData.update = update
                casoData.save()
                return HttpResponseRedirect(f'/admin/casos/vercaso/{id}')
        else:
            return HttpResponseRedirect(f'/admin/casos/vercaso/{id}')
    else:
        HttpResponseRedirect(f'/admin/')

def addDonator(request, id):
    if request.user.is_authenticated:
        if request.method == 'POST':
            casoData = Casos.objects.get(id=id)
            newDonator = request.POST['donatorName']

            if newDonator:
                donator = Donadores(project=casoData, donatorName=newDonator, amount = int(request.POST['donationAmount']) )
                donator.save()

                casoData.recolectado = casoData.recolectado + int(request.POST['donationAmount'])
                casoData.save()
                return HttpResponseRedirect(f'/admin/casos/vercaso/{id}')
        else:
            return HttpResponseRedirect(f'/admin/casos/vercaso/{id}')
    else:
        HttpResponseRedirect(f'/admin/')

def deleteDonator(request, id):
    if request.user.is_authenticated:
            donador = Donadores.objects.get(id=id)

            projectid = donador.project_id
            amtDonated = donador.amount
            if donador:
                casoData = Casos.objects.get(id=projectid)

                casoData.recolectado = casoData.recolectado - int(amtDonated)
                casoData.save()
                donador.delete()
            return HttpResponseRedirect(f'/admin/casos/vercaso/{projectid}')
    else:
        HttpResponseRedirect(f'/admin/')

def isNum(data):
    try:
        int(data)
        return True
    except ValueError:
        return False

def editcase(request, id):
    if request.user.is_authenticated:
        if request.method == 'POST':
            # apartment = Apartamentos(userid = request.GET['uid'], direccion = request.POST['neighborhood'], area = request.POST['area'], precio = request.POST['price'], precio_nuevo = pricetotal, precio_remo = priceremo, estrato = "Not defined", comodidades = request.POST['comodities'])
            if request.POST['campaign_title'] and request.POST['short_desc'] and request.POST['long_desc'] and request.POST['location'] and request.POST['benefits'] and request.POST['objective'] and request.POST['account'] and request.POST['bank'] and request.POST['collected'] and isNum(request.POST['collected']) and isNum(request.POST['objective']) : 
                caso = Casos.objects.get(id=id)
                caso.titulo = request.POST['campaign_title']
                caso.descb = request.POST['short_desc']
                caso.descl = request.POST['long_desc']
                caso.meta = request.POST['objective']
                caso.recolectado = int(request.POST['collected'])
                caso.donadores = []
                caso.beneficiados = request.POST['benefits'] 
                caso.ubicacion = request.POST['location']
                caso.tiktok_url = request.POST['tiktokurl']

                directDonation = False
                if request.POST.get('directDonation', '0') == 'True' :
                    directDonation = True
                else:
                    directDonation = False
                print(request.POST.get('directDonation', '0'))
                caso.directDonation = directDonation
                caso.accNumber = request.POST['account']
                caso.accBank = request.POST['bank']

                caso.save()
                print('GUARDADO')
                return HttpResponseRedirect(f'/admin/casos/vercaso/{id}')

        # print(TextosBase.objects.all())
        caso = Casos.objects.get(id=id)
        if caso:
            return render(request, 'admin/edit.html', {'caso': caso})
        else:
            return HttpResponseRedirect(f'/admin/crearcaso')
    else:
        HttpResponseRedirect(f'/admin/')



def createcase(request):
    if request.user.is_authenticated:
        return render(request, 'admin/createcase.html', locals())
    else:
        HttpResponseRedirect(f'/admin/')

def uploadCase(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            if request.POST['campaign_title'] and request.POST['short_desc'] and request.POST['long_desc'] and request.POST['location'] and request.POST['benefits'] and request.POST['objective'] and request.POST['collected'] and isNum(request.POST['collected']) and isNum(request.POST['objective']): 
                directDonation = False
                if request.POST['directDonation'] == 'True':
                    directDonation = True
                else:
                    directDonation = False
                newCampaign = Casos(titulo = request.POST['campaign_title'], descb = request.POST['short_desc'], descl = request.POST['long_desc'], meta = request.POST['objective'], recolectado = request.POST['collected'], beneficiados = request.POST['benefits'], ubicacion = request.POST['location'], directDonation = directDonation, accNumber = request.POST['account'], accBank = request.POST['bank'] )
                newCampaign.save()
                print('GUARDADO')
                return HttpResponseRedirect(f'/admin/casos/')
            else:
                return render(request, 'admin/createcase.html', {'error': "Te falta completar algunos campos."})
        else:
            return HttpResponseRedirect(f'/admin/')
    else:
        HttpResponseRedirect(f'/admin/')    
    

def deleteCase(request, id):
    if request.user.is_authenticated:
        caso = Casos.objects.get(id=id)
        if caso:
            caso.delete()
            return HttpResponseRedirect(f'/admin/casos/')
        else:
            return HttpResponseRedirect(f'/admin/casos/')
    else:
        HttpResponseRedirect(f'/admin/')
    
def uploadImg(request, id):

    if request.user.is_authenticated:
        caso = Casos.objects.get(id=id)

        if request.method == "POST":
            files = request.FILES.getlist('image')
            if caso:
                for i in files:
                    print('uploaded:', i)
                    file = Images(project=caso, image=i)
                    file.save()
                return HttpResponseRedirect(f'/admin/casos/vercaso/{id}')
        else:
            form = ImageForm()

        form = ImageForm()
        images = Images.objects.filter(project_id=id)

        bannerimgs = images[0:3]

        imagescont = images[3:len(images)]
        for image in bannerimgs:
            print(image.image)

        return render(request, 'admin/uploadimages.html', {'imageform': form, 'images':bannerimgs, 'cont_imgs':imagescont})
    else:
        HttpResponseRedirect(f'/admin/')

def deleteImg(request, id):
    if request.user.is_authenticated:
        img = Images.objects.get(id=id)

        if img:
            os.remove(f'./media/{img.image}')
            img.delete()

        return HttpResponseRedirect(f'/admin/casos/') 
    else:
        HttpResponseRedirect(f'/admin/')

def contenido(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            # apartment = Apartamentos(userid = request.GET['uid'], direccion = request.POST['neighborhood'], area = request.POST['area'], precio = request.POST['price'], precio_nuevo = pricetotal, precio_remo = priceremo, estrato = "Not defined", comodidades = request.POST['comodities'])
            for item in request.POST:
                if item != 'csrfmiddlewaretoken':
                    exist = TextosBase.objects.filter(titulo=item)
                    print(request.POST[item] != '')
                    # if request.POST[item]:
                    # print(exist)
                    if request.POST[item] != '':
                        if exist:
                            texto = TextosBase.objects.filter(titulo=item).update(contenido=request.POST[item])
                        else:
                            texto = TextosBase(titulo = item, contenido = request.POST[item])
                            texto.save()
                        print("GUARDADO")

        # print(TextosBase.objects.all())
        que_es = TextosBase.objects.get(titulo='que_es')
        quienes_somos = TextosBase.objects.get(titulo='quienes_somos')
        nuestra_historia = TextosBase.objects.get(titulo='nuestra_historia')
        que_hacemos = TextosBase.objects.get(titulo='que_hacemos')
        nuestro_enfoque = TextosBase.objects.get(titulo='nuestro_enfoque')
        mision = TextosBase.objects.get(titulo='mision')
        vision = TextosBase.objects.get(titulo='vision')
        join_us = TextosBase.objects.get(titulo='join_us')
        # que_es = TextosBase.objects.get(title='que_es')

        return render(request, 'admin/content.html', {'que_es' : que_es.contenido, 'quienes_somos' : quienes_somos.contenido,'nuestra_historia' : nuestra_historia.contenido,'que_hacemos' : que_hacemos.contenido, 'nuestro_enfoque' : nuestro_enfoque.contenido,'mision' : mision.contenido,'vision' : vision.contenido,'join_us' : join_us.contenido})   
    else:
        HttpResponseRedirect(f'/admin/')