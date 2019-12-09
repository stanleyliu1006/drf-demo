from django.db import models
import datetime
class AddressModel(models.Model):

    id = models.BigAutoField(primary_key=True)
    first_name = models.CharField(max_length=255, null=False)
    last_name = models.CharField(max_length=255, null=False)
    phone  = models.CharField(max_length=255, null=False)
    created_at = models.DateTimeField(null=True)

    def __str__(self):
        """Return a human readable representation of the model instance."""
        return "{}".format(self.first_name+" "+self.last_name)

    class Meta:
        db_table = "address"
