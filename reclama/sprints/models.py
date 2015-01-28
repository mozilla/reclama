from django.db import models
from django.contrib.auth.models import User

from uuslug import uuslug


class Event(models.Model):
    """Event model."""
    name = models.CharField(max_length=400)
    archived = models.BooleanField(default=False)
    slug = models.SlugField(max_length=400, blank=True)
    link = models.CharField(max_length=400)
    created_at = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User)

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ['-created_at']

    def save(self, *args, **kwargs):
        if not self.pk:
            self.slug = uuslug(self.name, instance=self)
        super(Event, self).save(*args, **kwargs)

    @property
    def bug_count(self):
        return self.bugs.all().count()


class Prize(models.Model):
    """Prize model."""
    name = models.CharField(max_length=400)

    def __unicode__(self):
        return self.name


class Bug(models.Model):
    """Bug model."""
    number = models.PositiveIntegerField()
    event = models.ManyToManyField(Event, related_name='bugs')
    prize = models.ForeignKey(Prize, related_name='prizes')
    created_at = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return 'Bug #{no}'.format(no=self.number)

    class Meta:
        ordering = ['-created_at']

    @property
    def bug_url(self):
        return ('https://bugzilla.mozilla.org/show_bug.cgi?id={no}'
                .format(no=self.number))
