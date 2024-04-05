from django.db import models

from app.settings import MEDIA_URL



class  InputTextFile(models.Model):
    file = models.FileField(upload_to='.')
    date = models.DateField(auto_now_add=True)
    # library_id = models.ForeignKey()

