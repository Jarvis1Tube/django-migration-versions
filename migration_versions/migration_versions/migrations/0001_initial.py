# Generated by Django 3.2 on 2021-04-17 13:20

import uuid
from typing import List

import django.core.validators
import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies: List[str] = []

    operations = [
        migrations.CreateModel(
            name="Migrations",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4, primary_key=True, serialize=False
                    ),
                ),
                ("app", models.CharField(max_length=255)),
                ("name", models.CharField(max_length=255)),
                ("applied", models.DateTimeField(default=django.utils.timezone.now)),
            ],
            options={
                "db_table": "django_migrations_with_versions",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="ApplicationVersion",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4, primary_key=True, serialize=False
                    ),
                ),
                ("created_at", models.DateTimeField(default=django.utils.timezone.now)),
                (
                    "major",
                    models.SmallIntegerField(
                        validators=[django.core.validators.MinValueValidator(0)]
                    ),
                ),
                (
                    "minor",
                    models.SmallIntegerField(
                        validators=[django.core.validators.MinValueValidator(0)]
                    ),
                ),
                (
                    "patch",
                    models.SmallIntegerField(
                        validators=[django.core.validators.MinValueValidator(0)]
                    ),
                ),
            ],
            options={
                "verbose_name": "Application version",
                "verbose_name_plural": "Application version",
            },
        ),
        migrations.CreateModel(
            name="MigrationToApplicationVersion",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "application_version",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="migration_versions.applicationversion",
                    ),
                ),
                (
                    "migration",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="migration_versions.migrations",
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="applicationversion",
            name="migrations",
            field=models.ManyToManyField(
                related_name="_migration_versions_applicationversion_migrations_+",
                through="migration_versions.MigrationToApplicationVersion",
                to="migration_versions.Migrations",
            ),
        ),
        migrations.AddConstraint(
            model_name="applicationversion",
            constraint=models.UniqueConstraint(
                fields=("major", "minor", "patch"), name="unique_version"
            ),
        ),
    ]