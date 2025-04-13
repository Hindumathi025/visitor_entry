from django.db import models
 
class Visitor(models.Model):
    name = models.CharField(max_length=100)
    mobile_number = models.CharField(max_length=15)
    visit_time = models.DateTimeField(auto_now_add=True)
    # Optional fields
    address = models.TextField(blank=True, null=True)
    purpose = models.TextField(blank=True, null=True)
 
    def __str__(self):
        return self.name