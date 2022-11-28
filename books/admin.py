from django.contrib import admin

from .models import Book

# from django.contrib.auth.models import User
# u = User.objects.get(username='ngj')
# u.set_password('testpass123')
# u.save()

admin.site.register(Book)
