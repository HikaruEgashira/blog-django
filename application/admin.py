from django.contrib import admin

# Register your models here.
# /admin/application/post/
from .models import Post

admin.site.register(Post) # adminsiteでmodel.pyで定義したPostをいじれるように