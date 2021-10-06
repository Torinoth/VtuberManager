from django.db import models

class Talent(models.Model):
    name = models.CharField(verbose_name='名前',
                            max_length=50,
                            null=True,
                            blank=True,
                            )
    affiliation = models.CharField(verbose_name="所属",
                                   max_length=50,
                                   null=True,
                                   blank=True,
                                   )
    youtube = models.URLField(verbose_name="youtubeURL",
                                 null=True,
                                 blank=True,
                                 )
    twitter = models.URLField(verbose_name="Twitter",
                              null=True,
                              blank=True,
                              )

    def __str__(self):
        return self.name