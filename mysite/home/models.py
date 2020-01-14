from django.db import models
# Create your models here.


class SHell(models.Model):
    bash_in = models.CharField(max_length=30)
    bash_out = models.CharField(max_length=2000)

    def __str__(self):
        return "*".join([self.bash_in, self.bash_out])
