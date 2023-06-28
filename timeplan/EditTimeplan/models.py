from django.db import models
from django.utils import timezone
from django.db import models
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User

class Promotion(models.Model):
    nom = models.CharField(max_length=100)
    
    class Annee(models.TextChoices):
        LICENCE_1 = 'L1', 'Licence 1'
        LICENCE_2 = 'L2', 'Licence 2'
        LICENCE_3 = 'L3', 'Licence 3'
        MASTER_1 = 'M1', 'Master 1'
        MASTER_2 = 'M2', 'Master 2'
    
    annee = models.CharField(choices=Annee.choices, max_length=2)

    class Groupe(models.TextChoices):
        GROUPE_1 = 'G1', 'Groupe 1'
        GROUPE_2 = 'G2', 'Groupe 2'
    
    groupe = models.CharField(choices=Groupe.choices, max_length=2, null=True, blank=True)
    class Meta:
        db_table = "Promotion"


    def __str__(self):
        return self.nom
    

class Matiere(models.Model):
    nom = models.CharField(max_length=100)
    enseignant = models.CharField(max_length=128)
    timing= models.IntegerField(default=0)
    Informations=models.CharField(max_length=500)

    def __str__(self):
        return self.nom
    class Meta:
        db_table = "Matiere"

class Salle(models.Model):
    nom = models.CharField(max_length=100)

    def __str__(self):
        return self.nom
    class Meta:
        db_table = "Salle"



#On vas creer trois admin par defauts.Pour en creer de nouveau on ira sur la page admin de django
class AdminUser(models.Model):
    nom = models.CharField(max_length=100, default="")
    prenom = models.CharField(max_length=100, default="")
    email = models.EmailField(unique=True, default="")
    numero_telephone = models.CharField(max_length=20, default="")
    mot_de_passe = models.CharField(max_length=128, default="")
    promotion = models.CharField(max_length=2,default='')
    Code_confirmation= models.IntegerField(null=True, blank=True, default=000000)


    class Meta:
        db_table = "admin"

    def save(self, *args, **kwargs):
        # Hacher le mot de passe avant de l'enregistrer
        #self.mot_de_passe = make_password(self.mot_de_passe)
        super().save(*args, **kwargs)


class CoursProgrammer(models.Model):
    #date = models.DateField()
    jour = models.CharField(max_length=100)
    promotion = models.CharField(max_length=128)
    heure_debut = models.TimeField()  #Je reviendrais regler l'erreur de format qui se pose lorsqu'on met TimeField
    heure_fin = models.TimeField()
    matiere = models.CharField(max_length=150)
    salle = models.CharField(max_length=150)
    teacher=models.CharField(max_length=128, default='')
    class Meta:
        db_table = "coursProgrammer"


   
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)


#ForeignKey(Promotion, on_delete=models.CASCADE)
#models.ForeignKey(Matiere, on_delete=models.CASCADE)
#models.ForeignKey(Salle, on_delete=models.CASCADE)

#Inserons la les groupe de la L1
class CoursProgrammerL1(models.Model):
    Date= models.DateField(default='2023-05-10')
    jour= models.CharField(max_length=128)
    promotion = models.CharField(max_length=128)
    heure_debut = models.CharField(max_length=150)
    heure_fin = models.CharField(max_length=150)
    matiere = models.CharField(max_length=150)
    salle = models.CharField(max_length=150)
    teacher=models.CharField(max_length=128, default='')
    groupe=models.CharField(max_length=128)  #Je veux que lorsque l'admin tape sur G1 ou G1 Groupe 1 ou..
    #Aparaisse dans la base de donné
    class Meta:
        db_table = "coursProgrammerL1"


  