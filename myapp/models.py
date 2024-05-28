from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name

class Places(models.Model):
    place_id = models.AutoField(primary_key=True)
    place_name = models.CharField(max_length=255)
    place_desc = models.TextField(blank=True, null=True)
    category = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    rating = models.FloatField(blank=True, null=True)
    num_reviews = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'places'


class Keywords(models.Model):
    test_id = models.AutoField(primary_key=True)
    test_name = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'keywords'

class PlacesKeywords(models.Model):
    place = models.OneToOneField(Places, models.DO_NOTHING, primary_key=True)  # The composite primary key (place_id, test_id) found, that is not supported. The first column is selected.
    test = models.ForeignKey(Keywords, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'places_keywords'
        unique_together = (('place', 'test'),)