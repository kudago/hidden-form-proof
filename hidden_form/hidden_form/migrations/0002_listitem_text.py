# Generated by Django 2.1.2 on 2018-10-08 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hidden_form', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='listitem',
            name='text',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
    ]
