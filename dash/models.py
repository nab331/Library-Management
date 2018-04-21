from django.db import models
import datetime
from django.contrib.auth.models import User
# Create your models here.
class Type(models.Model):

    TYPE_CHOICES = (
        ('student', 'student'),
        ('staff', 'staff'),
        ('admin', 'admin'),
    )

    userName = models.CharField(default=None,max_length=100)
    userType = models.CharField(max_length=100,choices=TYPE_CHOICES)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.userName


class Issued(models.Model):

    IssueID = models.CharField(default=None,max_length=100)
    userName = models.CharField(default=None,max_length=100)
    ISBN = models.CharField(max_length=100)
    Issued_date = models.DateField(auto_now_add=True)
    Return_date = models.DateField(blank=True,null=True)

    def __str__(self):
        return self.ISBN+self.userName




class book(models.Model):
    ISBN=models.CharField(primary_key=True,max_length=100)
    title=models.CharField(max_length=200)
    author=models.CharField(max_length=200)
    publisher=models.CharField(max_length=200)
    category=models.CharField(max_length=200)
    bookcount=models.IntegerField(default=1)

    def __str__(self):

        return self.title





class bookInstance(models.Model):
    id=models.IntegerField(primary_key=True)
    Book = models.ForeignKey(book, on_delete=models.CASCADE)
    due_back = models.DateField(default= datetime.datetime.now() + datetime.timedelta(days=15), null=True, blank=True)
    LOAN_STATUS = (
        ('m', 'Maintenance'),
        ('o', 'On loan'),
        ('a', 'Available'),
        ('r', 'Reserved'),
    )
    status = models.CharField(max_length=1, choices=LOAN_STATUS, blank=True, default='m', help_text='Book availability')

    class Meta:
        ordering = ["due_back"]

    def __str__(self):
        """
        String for representing the Model object
        """
        return '{0} ({1})'.format(self.id, self.Book.title)

