# Generated by Django 4.0.1 on 2024-04-01 15:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('GamesLibrary', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='rating',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='gamesimages',
            name='game',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='GamesLibrary.game'),
        ),
        migrations.AddField(
            model_name='game',
            name='developer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='GamesLibrary.developers'),
        ),
        migrations.AddField(
            model_name='game',
            name='genres',
            field=models.ManyToManyField(to='GamesLibrary.Genre'),
        ),
        migrations.AddField(
            model_name='developers',
            name='user',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='comments',
            name='game',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='GamesLibrary.game'),
        ),
        migrations.AddField(
            model_name='comments',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
