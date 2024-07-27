# Generated by Django 5.0.7 on 2024-07-26 08:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goals', '0002_alter_goal_beer_goal_alter_goal_mak_goal_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goal',
            name='beer_goal',
            field=models.DecimalField(decimal_places=1, default=0.0, max_digits=4),
        ),
        migrations.AlterField(
            model_name='goal',
            name='mak_goal',
            field=models.DecimalField(decimal_places=1, default=0.0, max_digits=4),
        ),
        migrations.AlterField(
            model_name='goal',
            name='soju_goal',
            field=models.DecimalField(decimal_places=1, default=0.0, max_digits=4),
        ),
        migrations.AlterField(
            model_name='goal',
            name='wine_goal',
            field=models.DecimalField(decimal_places=1, default=0.0, max_digits=4),
        ),
    ]