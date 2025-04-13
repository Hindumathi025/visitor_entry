from django.db import models

class Visitor(models.Model):
    name = models.CharField(max_length=100)
    mobile_number = models.CharField(max_length=15)
    address = models.TextField()
    purpose = models.TextField()
    visit_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
