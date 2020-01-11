from django.db import models

# Create your models here.


class AppUser(models.Model):  # django.contrib.auth.User
    pass


class Comment(models.Model):
    user = models.ForeignKey(AppUser, null=True, on_delete=models.SET_NULL)
    text = models.CharField(max_length=5000)
    date = models.DateField()


class Entry(models.Model):
    user = models.ForeignKey(AppUser, null=True, on_delete=models.SET_NULL)

    title = models.CharField(max_length=300)
    description = models.CharField(max_length=5000)
    date = models.DateField()

    comments = models.ManyToManyField(Comment)

    votes = models.IntegerField()

    def upvote(self):
        pass

    def downvote(self):
        pass

    def add_comment(self, comment):
        self.comments.add(comment)


class Problem(Entry):
    solutions = models.ManyToManyField('Solution')


class Solution(Entry):
    improvements = models.ManyToManyField('self')
    source_problem = models.ForeignKey(Problem, on_delete=models.CASCADE)


class Initiative(Entry):
    improvements = models.ManyToManyField('self')
