# Generated by Django 3.2.18 on 2023-04-10 06:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0014_auto_20230405_1131'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tagrecipe',
            options={'verbose_name': 'Тег рецепта', 'verbose_name_plural': 'Теги'},
        ),
        migrations.AddConstraint(
            model_name='ingredientrecipe',
            constraint=models.UniqueConstraint(fields=('recipe', 'ingredient'), name='recipe_ingredient'),
        ),
    ]
