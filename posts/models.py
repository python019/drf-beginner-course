from django.db import models

CATEGORIYA_TANLOVI = (
    ('Dj', 'Django'),
    ('Py', 'Python')
)

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=255)
    post_id = models.IntegerField()
    categoriya = models.TextField(max_length=255, choices=CATEGORIYA_TANLOVI)
    start_sanasi = models.DateTimeField(auto_now_add=True)
    ozgartirilgan_sanasi = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    