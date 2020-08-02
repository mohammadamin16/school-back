from django.db import models


class Comment(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey('accounts.User', on_delete=models.CASCADE, null=True)
    text = models.TextField(null=True)

    def __str__(self):
        return f'({self.user}), {self.text[:30]}'


class Day(models.Model):
    date = models.DateField(auto_now_add=True)
    items = models.ManyToManyField('Item')
    comment = models.ForeignKey('Comment', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.date.strftime('%y-%m-%d')

    @property
    def total_time(self):
        total = 0
        for item in self.items.all():
            total += item.duration
        return total


class Item(models.Model):
    # COURSE_CHOICES = (
    #     ('P', 'Physics'),
    #     ('G', 'Geometry'),
    #     ('C', 'Chemistry'),
    # )
    course = models.CharField(max_length=100)
    duration = models.IntegerField()
    tests_desc = models.CharField(max_length=500)
    study_desc = models.CharField(max_length=500)

    def __str__(self):
        return f"{self.course}, ({self.duration}')"
