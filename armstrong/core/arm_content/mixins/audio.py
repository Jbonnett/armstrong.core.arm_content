from django.db import models
from ..fields import AudioField


class AudioMixin(models.Model):

    file = AudioField(upload_to='audio/')
    playtime = models.PositiveIntegerField("playtime in seconds",
                                           null=True,
                                           blank=True)

    filetype = models.CharField("filetype",
                                max_length=16,
                                null=True,
                                blank=True)

    artist = models.CharField("artist",
                              max_length=100,
                              null=True,
                              blank=True,
                             )

    genre = models.CharField("genre",
                              max_length=100,
                              null=True,
                              blank=True,
                            )

    def __unicode__(self):
        return unicode(self.__str__())

    def __str__(self):
        return "%s by %s on %s" % (self.file, self.artist, self.album)

    @property
    def html(self):
        return self.file.render()

    class Meta:
        abstract = True
