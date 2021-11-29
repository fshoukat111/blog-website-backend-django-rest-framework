# Generated by Django 3.2.8 on 2021-11-24 17:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_post', '0005_alter_categories_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='posts',
            options={'ordering': ['-created'], 'verbose_name': 'Posts', 'verbose_name_plural': 'Posts'},
        ),
        migrations.AlterField(
            model_name='posts',
            name='body_content',
            field=models.TextField(),
        ),
    ]