from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50)

    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'

    def __str__(self):
        return self.name


class Recipe(models.Model):
    picture = models.ImageField(upload_to='articles/')
    title = models.CharField(max_length=100)
    cook_time = models.IntegerField(null=True, blank=True)
    products = models.TextField()
    recipe = models.TextField()
    tag = models.ManyToManyField(Tag, related_name='related_tag')

    class Meta:
        verbose_name = 'Рецепт'
        verbose_name_plural = 'Рецепты'

    def __str__(self):
        return self.title
