



from django.db import models
# from django.contrib.auth.models import User
from django.db.models.signals import post_save
# from chats.models import Chatroom
# from article.models import Article
from PIL import Image
from decimal import Decimal
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
from datetime import date
from django.core.cache import cache 
import datetime
from uuid import uuid4

# from marketplace.models import Product

CREATOR_RATING = (
	(Decimal("1.0"), "★☆☆☆☆ (1/5)"),
	(Decimal("2.0"), "★★☆☆☆ (2/5)"),
	(Decimal("3.0"), "★★★☆☆ (3/5)"),
	(Decimal("4.0"), "★★★★☆ (4/5)"),
	(Decimal("5.0"), "★★★★★ (5/5)"),
)

class User(AbstractUser):
    email = models.EmailField(unique=True, null=True)
    username = models.CharField(max_length=10000)
    is_student = models.BooleanField(default=True)
    is_teacher = models.BooleanField(default=False)
    verified = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
	

    def __str__(self):
        return f"{self.username}"



# uploading user files to a specific directory
def user_directory_path(instance, filename):
	return 'user_{0}/{1}'.format(instance.user.id, filename)


class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	full_name = models.CharField(max_length=1000)
	bio = models.CharField(max_length=100)
	country = models.CharField(max_length=100, null=True)
	about_me = models.TextField(blank=True, null=True, default="I am a DexxaEd User")
	profile_image = models.ImageField(upload_to=user_directory_path, default="default_profile_image.jpg")


	address = models.CharField(max_length=1000, null=True, blank=True)
	phone = models.CharField(default="+123456789", max_length=100, blank=True, null=True)

	website = models.URLField(default="https://dexxaed.com/", null=True, blank=True)
	facebook = models.URLField(default="https://facebook.com/", null=True, blank=True)
	twitter = models.URLField(default="https://twitter.com/", null=True, blank=True)
	instagram = models.URLField(default="https://instagram.com/", null=True, blank=True)		

	
	
	rooms = models.ManyToManyField('chats.Chatroom', related_name="chat_room",	 blank=True)

	def __str__(self):
		try:
			# Note: you can make this look better and be in a tabular form using Admin (admin.py)
			return f"{self.full_name} - {self.user.username} - {self.user.email} "
		except:
			return self.user.username
	
	def save(self, *args, **kwargs):
		super().save(*args, **kwargs)

		img = Image.open(self.profile_image.path)
		if img.height > 300 or img.width > 300:
			output_size = (300, 300)
			img.thumbnail(output_size)
			img.save(self.profile_image.path)

def create_user_profile(sender, instance, created, **kwargs):
	if created:
		Profile.objects.create(user=instance)

def save_user_profile(sender, instance, **kwargs):
	instance.profile.save()

post_save.connect(create_user_profile, sender=User)
post_save.connect(save_user_profile, sender=User)

class Follow(models.Model):
    follower = models.ForeignKey(User, on_delete=models.CASCADE, related_name='follower')
    following = models.ForeignKey(User, on_delete=models.CASCADE, related_name='following')