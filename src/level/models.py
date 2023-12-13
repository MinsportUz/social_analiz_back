from django.db import models
from django.utils import timezone

from organization.models import Organization


class Level(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Levels'
        verbose_name = 'Level'
        db_table = 'level'

    def save(self, *args, **kwargs):
        self.updated_at = timezone.now()
        super(Level, self).save(*args, **kwargs)
        return self


class LevelOrganization(models.Model):
    level = models.ForeignKey(Level, on_delete=models.SET_NULL, null=True)
    organization = models.ForeignKey(Organization, on_delete=models.SET_NULL, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        try:
            return self.level.name + " " + self.organization.shortname
        except:
            return self.level.name

    class Meta:
        verbose_name_plural = 'Level Organizations'
        verbose_name = 'Level Organization'
        db_table = 'level_organization'

    def save(self, *args, **kwargs):
        self.updated_at = timezone.now()
        super(LevelOrganization, self).save(*args, **kwargs)
        return self