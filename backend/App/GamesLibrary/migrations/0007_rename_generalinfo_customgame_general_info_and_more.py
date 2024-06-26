# Generated by Django 4.0.1 on 2024-04-12 16:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GamesLibrary', '0006_customgame'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customgame',
            old_name='generalinfo',
            new_name='general_info',
        ),
        migrations.RemoveField(
            model_name='customgame',
            name='userTechLevel',
        ),
        migrations.AddField(
            model_name='customgame',
            name='prototype',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='customgame',
            name='prototype_game',
            field=models.FileField(blank=True, null=True, upload_to='prototype_games/'),
        ),
        migrations.AddField(
            model_name='customgame',
            name='user_tech_level',
            field=models.CharField(choices=[('beginner', 'Beginner'), ('entry_level', 'Entry Level'), ('junior_level', 'Junior Level'), ('senior_level', 'Senior Level')], default='beginner', max_length=25),
        ),
        migrations.AlterField(
            model_name='customgame',
            name='game_complexity',
            field=models.CharField(choices=[('fast_game', 'Fast Game'), ('entry_level', 'Entry Level'), ('medium_game', 'Medium Game'), ('big_game_project', 'Big Game Project'), ('aaa_level', 'AAA Level')], default='fast_game', max_length=25),
        ),
        migrations.AlterField(
            model_name='customgame',
            name='game_status',
            field=models.CharField(choices=[('draft', 'Draft'), ('lore_design', 'Lore Design'), ('characters_design', 'Characters Design'), ('graphics_design', 'Graphics Design'), ('adding_sounds', 'Adding Sounds'), ('game_ui', 'Game UI'), ('testing', 'Testing'), ('published_soon', 'Published Soon'), ('game_ready', 'Game Ready')], default='draft', max_length=20),
        ),
    ]
