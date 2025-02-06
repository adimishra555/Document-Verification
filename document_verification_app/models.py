from django.db import models

# Create your models here.
class DocumentVerificationDB(models.Model):
    sellername = models.CharField(max_length=100, null=True, blank=True)
   
    phone_no=models.CharField(max_length=10, null=True, blank=True, unique=True)
    role_choices = (("Seller", "Seller"), ("Buyer", "Buyer"))
    role = models.CharField(max_length=10, choices=role_choices, default=role_choices[1][0])
    created_at = models.DateTimeField( null=True, blank=True)
    status = models.BooleanField(default=False,null=True, blank=True)

    def key_document_verification(self):
        if self.sellername and self.phone_no and self.role  and self.created_at :
            self.status = True
            self.save()
            return True
        else:
            return False

    def __str__(self):
        return f" {self.sellername}"
       