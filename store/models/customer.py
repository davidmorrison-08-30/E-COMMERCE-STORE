from django.db import models

class Customer(models.Model):
    name = models.CharField(max_length=250)
    username = models.CharField(max_length=250, primary_key=True)
    password = models.CharField(max_length=250)

    #to save the data
    def register(self):
        self.save()


    @staticmethod
    def get_customer_by_username(username):
        try:
            return Customer.objects.get(username= username)
        except:
            return False


    def isExists(self):
        if Customer.objects.filter(username = self.username):
            return True
        return False