from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible

@python_2_unicode_compatible
class MachineStatus(models.Model): 
    machine_name = models.CharField(max_length=20)
    machine_state = models.CharField(max_length=50)

    def __str__(self): 
        return self.machine_name
