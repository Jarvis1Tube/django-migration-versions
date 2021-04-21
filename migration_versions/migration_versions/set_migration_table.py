from uuid import uuid4

from django.db import models
from django.db.migrations.recorder import MigrationRecorder
from django.utils.timezone import now


class Migrations(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField(default=now)

    class Meta:
        db_table = "django_migrations_with_versions"
        managed = False


MigrationRecorder._migration_class = Migrations  # pylint: disable=protected-access
