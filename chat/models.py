from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


MY_CHOICES2 = (
    ('01:00 am', '01:00 am'),
	('02:00 am', '02:00 am'),
	('03:00 am', '03:00 am'),
    ('04:15 am', '04:00 am'),
	('05:00 am', '05:00 am'),
	('06:00 am', '06:00 am'),
	('07:00 am', '07:00 am'),
	('08:00 am', '08:00 am'),
	('09:00 am', '09:00 am'),
    ('10:00 am', '10:00 am'),
	('11:00 am', '11:00 am'),
	('12:00 am', '12:00 am'),
    ('01:00 pm', '01:00 pm'),
	('02:00 pm', '02:00 pm'),
	('03:00 pm', '03:00 pm'),
    ('04:00 pm', '04:00 pm'),
	('05:00 pm', '05:00 pm'),
	('06:00 pm', '06:00 pm'),
	('07:00 pm', '07:00 pm'),
	('08:00 pm', '08:00 pm'),
	('09:00 pm', '09:00 pm'),
    ('10:15 pm', '10:00 pm'),
	('11:00 pm', '11:00 pm'),
	('12:00 pm', '12:00 pm'),
	
    
    
)
MY_CHOICES3 = (
    
	('01:00 am', '01:00 am'),
	('02:00 am', '02:00 am'),
	('03:00 am', '03:00 am'),
    ('04:15 am', '04:00 am'),
	('05:00 am', '05:00 am'),
	('06:00 am', '06:00 am'),
	('07:00 am', '07:00 am'),
	('08:00 am', '08:00 am'),
	('09:00 am', '09:00 am'),
    ('10:00 am', '10:00 am'),
	('11:00 am', '11:00 am'),
	('12:00 am', '12:00 am'),
    ('01:00 pm', '01:00 pm'),
	('02:00 pm', '02:00 pm'),
	('03:00 pm', '03:00 pm'),
    ('04:00 pm', '04:00 pm'),
	('05:00 pm', '05:00 pm'),
	('06:00 pm', '06:00 pm'),
	('07:00 pm', '07:00 pm'),
	('08:00 pm', '08:00 pm'),
	('09:00 pm', '09:00 pm'),
    ('10:15 pm', '10:00 pm'),
	('11:00 pm', '11:00 pm'),
	('12:00 pm', '12:00 pm'),
    
    
)

OPTIONS = (
     ("Mon", "Mon"),
                ("Tue", "Tue"),
                ("Wed", "Wed"),
                ("Thu", "Thu"),
				("Fri", "Fri"),
                ("Sat", "Sat"),
			    ("Sun", "Sun"),
			   )
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    utype = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)

@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()
	
def get_absolute_url(self):
        return reverse('server_edit', kwargs={'pk': self.pk})

class Chat(models.Model):
    created = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User)
    message = models.CharField(max_length=200)
    Image = models.ImageField(upload_to='profile_image', blank=True)
    document = models.FileField(upload_to='static/documents/', blank=True)

def __unicode__(self):
        return self.message	

class Createclass(models.Model):
    user = models.ForeignKey(User)
    Title = models.CharField(max_length=200, default='')
    Subject = models.CharField(max_length=200, default='')
    date = models.CharField(max_length=200, default='') 
    From = models.CharField(max_length=60,choices=MY_CHOICES2, default='')
    to = models.CharField(max_length=60,choices=MY_CHOICES3, default='')
    instructor = models.CharField(max_length=60, default='')
    description = models.TextField(default='')

			