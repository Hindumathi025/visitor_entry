from django.db import models
 
class Visitor(models.Model):
    """A model representing a visitor log entry with attributes for name, contact details, visit time, and optional additional information.
    Parameters:
        - name (str): The name of the visitor, with a maximum length of 100 characters.
        - mobile_number (str): The mobile phone number of the visitor, with a maximum length of 15 characters.
        - visit_time (datetime): The date and time of the visitor's log entry, automatically set to the current date and time.
        - address (str, optional): The address of the visitor, optional and can be left blank.
        - purpose (str, optional): The purpose of the visit, optional and can be left blank.
    Processing Logic:
        - The `__str__` method returns the name of the visitor, providing a readable representation of the Visitor object instance."""
    name = models.CharField(max_length=100)
    mobile_number = models.CharField(max_length=15)
    visit_time = models.DateTimeField(auto_now_add=True)
    # Optional fields
    address = models.TextField(blank=True, null=True)
    purpose = models.TextField(blank=True, null=True)
 
    def __str__(self):
        return self.name