# Generated by Django 4.2.16 on 2024-10-16 20:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('foodie_app', '0002_comment_parent_alter_recipe_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='replies', to='foodie_app.comment'),
        ),
    ]
