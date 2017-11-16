from django.db import models

class Comment(models.Model):
    company_id = models.IntegerField(db_index=True)
    comment = models.TextField()
    raiting = models.CharField(max_length=1, default=None, null=True)
    review_id = models.CharField(max_length=32)
    post_date = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)

class AnalyzeSentiment(models.Model):
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)
    score = models.DecimalField(max_digits=14, decimal_places=4, default=0.0000)
    magnitude = models.DecimalField(max_digits=14, decimal_places=4, default=0.0000)
    created_at = models.DateTimeField(auto_now_add=True)
