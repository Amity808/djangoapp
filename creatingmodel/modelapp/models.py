from django.db import models

# Create your models here.
class Empolyee(models.Model):
    firstname = models.CharField(max_length=30)
    lastname = models.CharField(max_length=30)
    salary = models.FloatField()
    email = models.CharField(max_length=40)



class Programmer(models.Model):
    name=models.CharField(max_length=20)
    salary=models.IntegerField()


class Project(models.Model):
    name= models.CharField(max_length=30)
    #to define relationship
    Programmers=models.ManyToManyField(Programmer)



class Customer(models.Model):
    name=models.CharField(max_length=30)


class PhoneNumber(models.Model):
    type = models.CharField(max_length=12)
    number = models.CharField(max_length=15)
    #on_delete will delete the customer details and number
    customer=models.ForeignKey(Customer, on_delete=models.CASCADE)


class Person(models.Model):
    firstname=models.CharField(max_length=10)
    lastname=models.CharField(max_length=20)
    age=models.IntegerField()


class Licence(models.Model):
    type= models.CharField(max_length=10)
    validForm=models.DateField()
    validTo=models.DateField()
    person=models.OneToOneField(Person,on_delete=models.CASCADE)
