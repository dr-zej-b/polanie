from django.db import models

GENDER = (("M","Male"), ("F","Female"), ("U","Unisex"))
REGION = (("KR","Krakowski"), ("LW","Lowicki"), ("SZ","Szlachecki"),("N","None"))
SIZE   = (("S","Small"), ("M","Medium"), ("L","Large"))
STATUS = ((1,"Available"), (0,"On loan"))
COSTUME_TYPE = (("Hat","Hat"),("Pants","Pants"),('Boots','Boots'))
TRANSACTION_TYPE = ((1,"Rental"), (0,"Return"))

class Greeting(models.Model):
    when = models.DateTimeField('date created', auto_now_add=True)

class UserProfile(models.Model):  
    joined       = models.DateTimeField('date created', auto_now_add=True)  
    firstname    = models.CharField(max_length=30, blank=True)
    lastname     = models.CharField(max_length=30, blank=True)
    email        = models.EmailField(max_length=30, blank=True)
    phone_number = models.CharField(max_length=30, blank=True)

    def __unicode__(self):
        return "{} {}".format(self.firstname, self.lastname)

class Supplier(models.Model):      
    name         = models.CharField(max_length=30, blank=True)    
    email        = models.CharField(max_length=30, blank=True)
    phone_number = models.CharField(max_length=30, blank=True)
    address      = models.CharField(max_length=30, blank=True)
    url          = models.URLField(blank=True)

    def __unicode__(self):
        return "{}".format(self.name)

class Item(models.Model):
    serial_number = models.CharField(max_length=30, blank=True)
    description   = models.CharField(max_length=300, default="")
    costume_type  = models.CharField(max_length=300, default="", choices=COSTUME_TYPE)
    region        = models.CharField(max_length=30, blank=True,choices=REGION)
    size          = models.CharField(max_length=30, blank=True, choices=SIZE)
    gender        = models.CharField(max_length=1, blank=True, default="U", choices=GENDER)
    status        = models.IntegerField(default=1,choices=STATUS)
    supplier      = models.ForeignKey(Supplier)
    cost          = models.DecimalField(max_digits=10, decimal_places=2, default=-1)    

    def __unicode__(self):
        return "{} {}".format(self.region, self.serial_number)

    def show_rented(self):
        rented = self.status == 0
        return rented

class Transaction(models.Model):
    date        = models.DateTimeField('Transaction date', auto_now_add=True)  
    user        = models.ForeignKey(UserProfile)
    items       = models.ManyToManyField(Item)
    rent_return = models.IntegerField(default=1, choices=TRANSACTION_TYPE)

    def __unicode__(self):
        return "{} {} {}" .format(self.date, self.user, self.rent_return)

