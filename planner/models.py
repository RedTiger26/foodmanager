from django.db import models
from datetime import timedelta

from recipes.models import Recipe


class Calendar(models.Model):
    name = models.CharField(max_length=250)
    num_entries_per_day = models.PositiveSmallIntegerField()
    
    def entries_num_range(self):
        return range(0, self.num_entries_per_day)
    
    def get_entries(self, start, days):
        """Returns a full set of entries to display."""
        result = []
        
        for d in (start + timedelta(n) for n in range(0, days)):
            e = {}
            e['date'] = d
            
            for i in range(0, self.num_entries_per_day+1):
                e[i] = CalendarEntry.objects.filter(calendar=self).filter(date=d).filter(num_entry=i).first()
            
            result.append(e)
        
        return result
    
    
    def __str__(self):
        return self.name    
    
    class Meta:
        ordering = ['name']



class CalendarEntry(models.Model):
    calendar = models.ForeignKey(Calendar, on_delete=models.CASCADE)
    date = models.DateField()
    num_entry = models.PositiveSmallIntegerField()
    
    recipe = models.ForeignKey(Recipe, blank=True, on_delete=models.CASCADE)
    text = models.CharField(max_length=250, blank=True) 
    
    def __str__(self):
        return '[' + self.date.strftime('%d.%m.%Y') + '] ' + str(self.recipe)
    
    class Meta:
        ordering = ['date', 'num_entry'] 