from django.contrib import admin
from .models import Post

# Register your models here.

admin.site.register(Post)     #This is to ensure that the imorted model, in this case Post is visible on the admin page
							  #We want to add db.sqlite3 in the .gitignore as the git will have its own database; however to make our own data available we will have to add it afterwards
							  