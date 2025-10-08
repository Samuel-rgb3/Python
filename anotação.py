from django.db import models
from django.utils import timezone


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title
class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    comment = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    def __str__(self):

        def __str__(self):
            try:
            return f'{self.post.title} comentário: {self.comment[:20]}...'
        except:
            return f'{self.post.title} comentário: {self.comment}
