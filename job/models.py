from django.db import models

# Create your models here.
class Infos(models.Model):
    """
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    """
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
    Propos = models.TextField('a propos', null=True)
    TypeRecrutement= models.CharField(max_length=1000)
    CompTechnique= models.TextField('competence tech')
    CompHumaine= models.TextField('competence hum')
    Profile= models.TextField('profile type')

class Infos1(models.Model):
    """
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    """
    plateform = models.CharField(max_length=100, null=True)
    created = models.DateTimeField('date created')
    lang = models.CharField(max_length=100, null=True)
    JobTitre = models.CharField(max_length=1000)
    Secteur = models.CharField(max_length=1000)
    nbCandidat = models.CharField(max_length=1000)
    DureeAttente = models.CharField(max_length=1000)
    StatusOffre = models.CharField(max_length=1000)
    Entreprise = models.CharField(max_length=1000)
    Lieu= models.CharField(max_length=1000)
    Taille= models.CharField(max_length=100)
    Mission= models.TextField('type mission')
    Propos = models.TextField('a propos')
    TypeRecrutement= models.CharField(max_length=1000)
    CompTechnique= models.TextField('competence tech')
    CompHumaine= models.TextField('competence hum')
    Profile= models.TextField('profile type')
    Experience = models.TextField('experience')
    Diplome = models.TextField('diplome')
    


