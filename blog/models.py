from django.db import models


class Post(models.Model):
    Chem_ID = models.TextField()
    Name = models.TextField()
    Date = models.TextField()
    PMID = models.TextField()
    Properties = models.TextField()
    Type = models.TextField()
    Effect_to_PrP = models.TextField()
    Effect_to_Diseases_progression = models.TextField()
    Materials = models.TextField()
    Information_of_Materials = models.TextField()
    Treatement = models.TextField()
    Binding_site = models.TextField()
    PubChem = models.TextField()

class Submit(models.Model):
    Name = models.CharField(max_length=50)
    Date = models.CharField(max_length=11)
    PMID = models.CharField(max_length=20)
    Properties = models.CharField(max_length=50)
    Type = models.CharField(max_length=50)
    Effect_to_PrP = models.CharField(max_length=50)
    Effect_to_Diseases_progression = models.CharField(max_length=50)
    Materials = models.CharField(max_length=50)
    Information_of_Materials = models.CharField(max_length=50)
    Treatement = models.CharField(max_length=50)
    Binding_site = models.CharField(max_length=50)
    PubChem = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    cdate = models.DateTimeField(auto_now_add=True)
