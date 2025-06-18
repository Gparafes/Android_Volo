from django.db import models

LANGUAGE_CHOICES = [('abap','ABAP'),('abnf','ABNF'),('ada','ADA'),('adl','ADL'),
                    ('agda','AGDA'),('python','PYTHON')]
STYLE_CHOICES = [('algol','algol'),('algol_nu','algol_nu'),('friendly','friendly')]

class Snippet(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default='')
    code = models.TextField()
    linenos = models.BooleanField(default=False)
    language = models.CharField(choices=LANGUAGE_CHOICES, default='python', max_length=100)
    style = models.CharField(choices=STYLE_CHOICES, default='friendly', max_length=100)
    owner = models.ForeignKey('auth.User', related_name='snippets', on_delete=models.CASCADE, null=True)
    class Meta:
        ordering = ['created']


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class Sight(models.Model):
    name = models.CharField(max_length=200)
    area = models.CharField(max_length=200)
    construction_date = models.CharField(max_length=20, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='sights', null=True, blank=True)
    description = models.TextField(blank=True)
    cover_image = models.ImageField(upload_to='sight_images/', null=True, blank=True)

    def __str__(self):
        return self.name




