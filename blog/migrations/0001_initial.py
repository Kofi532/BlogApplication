# Generated by Django 3.2 on 2021-04-30 18:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=105)),
                ('body', models.TextField()),
                ('date_published', models.DateTimeField()),
                ('status', models.CharField(choices=[('draft', 'draft'), ('published', 'published')], max_length=10)),
                ('category', models.CharField(choices=[('software', 'software'), ('technology', 'technology'), ('news', 'news')], max_length=10)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
