import base64
import uuid

from django.db import models

HOST = "http://localhost:8000/"

class Url(models.Model):
    url = models.URLField()
    url_hash = models.CharField(max_length=10, unique=True, db_index=True)
    short_url = models.URLField(blank=True, null=True)

    def save(self, *args, **kwargs):
        self.url_hash = self.generate_hash()
        self.short_url = self.create_short_url()
        super(Url, self).save(*args, **kwargs)

    def generate_hash(self):
        hash = base64.urlsafe_b64encode(uuid.uuid1().bytes)[:5]
        hash_exist = Url.objects.filter(url_hash=hash)
        while hash_exist:
            hash = base64.urlsafe_b64encode(uuid.uuid1().bytes)[:5]
            hash_exist = Url.objects.filter(url_hash=hash)
    
        hash = hash.decode("utf-8")
    
        return hash
    
    def create_short_url(self):
        return HOST + self.url_hash

        
        

