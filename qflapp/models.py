from django.db import models
from django.utils import timezone
from cloudinary.models import CloudinaryField

class Notice(models.Model):
    title = models.CharField(max_length=200, blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    date_posted = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.title

class Patron(models.Model):
    PATRON_CHOICES = [
        ("Patron", "Patron"),
        ("Vice-Patron", "Vice-Patron")
    ]
    name = models.CharField(max_length=200, blank=True, null=True)
    since = models.CharField(max_length=4,blank=True, null=True)
    designation = models.CharField(max_length=50, choices=PATRON_CHOICES, blank=True, null=True)
    date_posted = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.name

class Person(models.Model):
    name = models.CharField(max_length=255)
    # photo = models.ImageField(upload_to='photo/')  # Assuming media handling is configured
    photo = CloudinaryField('photo')

    def __str__(self):
        return self.name
    
class CommitteeMember(models.Model):
    DESIGNATION_CHOICES = [
        ('Supervision Committee', 'Supervision Committee'),
        ('Chairman', 'Chairman'),
        ('Vice-Chairman', 'Vice-Chairman'),
        ('Secretary', 'Secretary'),
        ('Joint-Secretary', 'Joint-Secretary'),
        ('Treasurer', 'Treasurer'),
        ('Member', 'Member'),
    ]

    person = models.ForeignKey(Person, on_delete=models.CASCADE, related_name='committee_memberships')
    year = models.CharField(max_length=4)
    designation = models.CharField(max_length=100, choices=DESIGNATION_CHOICES)
    order = models.PositiveIntegerField()  # This defines the display order for that year

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f"{self.person.name} ({self.year}) - {self.designation}"
    

class Book(models.Model):
    LANGUAGE_CHOICES = [
        ('English', 'English'),
        ('Gujarati', 'Gujarati'),
        ('Urdu', 'Urdu'),
        ('Others', 'Others'),
    ]

    GENRE_CHOICES = [
        ('Religion', 'Religion'),
        ('Education', 'Education'),
        ('General Knowledge', 'General Knowledge'),
        ('Fiction', 'Fiction'),
        ('Current Affairs', 'Current Affairs'),
    ]

    code = models.CharField(max_length=50, unique=True)
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    genre = models.CharField(max_length=100, choices=GENRE_CHOICES)
    language = models.CharField(max_length=50, choices=LANGUAGE_CHOICES)
    file_id = models.CharField(max_length=100, null=True, blank=True)  # Google Drive file ID field

    def __str__(self):
        return self.title