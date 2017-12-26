from django.db import models

class RecipeSource(models.Model):
    title = models.CharField(max_length=250)
    author = models.CharField(blank=True, max_length=250)
    issue = models.CharField(blank=True, max_length=50)
    
    def __str__(self):
        label = self.title
        if len(self.author) > 0: label += ', ' + self.author
        if len(self.issue) > 0: label += ' (' + self.issue + ')'
        return label
    
    class Meta:
        ordering = ['title', 'issue']
    


class Recipe(models.Model):
    name = models.CharField(max_length=250)
    source = models.ForeignKey(RecipeSource, blank=True, null=True, on_delete=models.SET_NULL)
    source_hint = models.CharField(max_length=50, blank=True)
    
    def __str__(self):
        return self.name
    