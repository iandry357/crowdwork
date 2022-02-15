from django.shortcuts import get_object_or_404, render
# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader

from django.http import Http404
from django.urls import reverse
from django.views import generic
from django.contrib import messages

from .models import Infos, Infos1

# Create your views here.
'''
def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")
'''

def index(request):
    return render(request, 'job/collect.html')

'''
created = models.DateTimeField('date created')
    JobTitre = models.CharField(max_length=1000)
    Secteur = models.CharField(max_length=1000)
    nbCandidat = models.CharField(max_length=1000)
    DureeAttente = models.CharField(max_length=1000)
    StatusOffre = models.CharField(max_length=1000)
    Entreprise = models.CharField(max_length=1000)
    Lieu= models.CharField(max_length=1000)
    Taille= models.CharField(max_length=100)
    Mission= models.TextField('type mission')
    TypeRecrutement= models.CharField(max_length=1000)
    CompTechnique= models.TextField('competence tech')
    CompHumaine= models.TextField('competence hum')
    Profile= models.TextField('profile type')
'''

from datetime import date, datetime


def saveInfos(request):

    testGabarit = "HELLO"

    if request.method == 'POST':
        jobInfo = Infos1()
        jobInfo.created = datetime.now()
        jobInfo.plateform = request.POST.get('plateform')
        jobInfo.lang = request.POST.get('lang')
        jobInfo.JobTitre = request.POST.get('JobTitre')
        jobInfo.Secteur = request.POST.get('Secteur')
        jobInfo.nbCandidat = request.POST.get('nbCandidat')
        jobInfo.DureeAttente = request.POST.get('DureeAttente')
        jobInfo.StatusOffre = request.POST.get('StatusOffre')
        jobInfo.Entreprise = request.POST.get('Entreprise')
        jobInfo.Lieu = request.POST.get('Lieu')
        jobInfo.Taille = request.POST.get('Taille')
        jobInfo.Mission = request.POST.get('Mission')
        jobInfo.Propos = request.POST.get('Propos')
        jobInfo.TypeRecrutement = request.POST.get('TypeRecrutement')
        jobInfo.CompTechnique = request.POST.get('CompTechnique')
        jobInfo.CompHumaine = request.POST.get('CompHumaine')
        jobInfo.Profile = request.POST.get('Profile')
        jobInfo.Experience = request.POST.get('Experience')
        jobInfo.Diplome = request.POST.get('Diplome')
        jobInfo.save()

        messages.success(request, 'Informations Ajoutées')

        return render(request, 'job/collect.html', { 'salutation': testGabarit })
        #return HttpResponseRedirect(reverse('job/saveInfo'))
    else:
        return render(request, 'job/collect.html', { 'salutation': testGabarit })
        



