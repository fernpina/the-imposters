# Generated by Django 4.1.3 on 2022-11-25 20:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0014_alter_recipe_region'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='region',
            field=models.CharField(choices=[('NORTH AMERICAN', 'North America'), ('SOUTH AMERICAN', 'South America'), ('CENTRAL AMERICAN', 'Central America'), ('EUROPEAN', 'Europe'), ('ASIAN', 'Asia'), ('MIDDLE EASTERN', 'Middle East'), ('AFRICAN', 'Africa'), ('OCEANIC', 'Oceania')], default='NORTH AMERICAN', max_length=16),
        ),
    ]