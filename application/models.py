# DBの操作を行うファイル
from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=32)
    published = models.DateTimeField()
    image = models.ImageField(upload_to='media/') # pillowで画像を扱う pics/media
    body = models.TextField()

    def __str__(self):
        return self.title # POSTの一覧をpost object=>titleに変更して見やすくした

    def summary(self):
        return self.body[:40]