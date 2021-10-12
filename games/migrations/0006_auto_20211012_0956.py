# Generated by Django 3.2.8 on 2021-10-12 09:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0005_auto_20211011_1534'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gamesmodel',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='GameModel_CategoryModel', to='games.categorymodel'),
        ),
        migrations.AlterField(
            model_name='gamesmodel',
            name='publisher',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='GameModel_PublisherModel', to='games.publishermodel'),
        ),
    ]
