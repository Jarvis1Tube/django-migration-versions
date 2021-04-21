from uuid import uuid4

from django.core.validators import MinValueValidator
from django.db import models
from django.utils.timezone import now

from .set_migration_table import Migrations


class ApplicationVersion(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4)
    created_at = models.DateTimeField(default=now)

    major = models.SmallIntegerField(validators=[MinValueValidator(0)])
    minor = models.SmallIntegerField(validators=[MinValueValidator(0)])
    patch = models.SmallIntegerField(validators=[MinValueValidator(0)])

    migrations = models.ManyToManyField(
        "Migrations",
        related_name="+",
        through="MigrationToApplicationVersion",
    )

    class Meta:
        verbose_name = "Application version"
        verbose_name_plural = "Application version"
        constraints = [
            models.UniqueConstraint(
                fields=["major", "minor", "patch"],
                name="unique_version",
            ),
        ]


class MigrationToApplicationVersion(models.Model):
    migration = models.OneToOneField(Migrations, on_delete=models.CASCADE)
    application_version = models.ForeignKey(
        ApplicationVersion, on_delete=models.CASCADE
    )
