from django.db import models

class Objective(models.Field):

    def __init__(self, id, deadline):
        self.id = id;
		seld.deadline = deadline;
		self.description = description;
        super(HandField, self).__init__(*args, **kwargs)