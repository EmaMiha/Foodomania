# Generated by Django 4.2.16 on 2024-10-16 20:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foodie_app', '0003_alter_comment_parent'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='recipes/images/'),
        ),
    ]
