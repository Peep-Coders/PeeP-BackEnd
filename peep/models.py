from django.db import models

# Create your models here.
class Peep(models.Model):
    username = models.ForeignKey(
        'users.User', related_name='peeps', on_delete=models.CASCADE)
    post = models.CharField(max_length=140)
    image = models.ImageField(upload_to = 'images/', default= 'images/default.jpg')
    date = models.DateTimeField()

    def __str__(self):
        return self.post


class Chirp(models.Model):
    text = models.CharField(max_length=140)
    post_id = models.ForeignKey(
        Peep, on_delete=models.CASCADE, related_name='chirp')
    user_id = models.ForeignKey(
        'users.User', related_name='chirp', on_delete=models.CASCADE)

    def __str__(self):
        return self.text
