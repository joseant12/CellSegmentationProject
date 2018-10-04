# Generated by Django 2.1 on 2018-10-04 01:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ImageApp', '0015_auto_20181003_1929'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Post',
        ),
        migrations.AddField(
            model_name='usuario',
            name='email',
            field=models.CharField(default=False, max_length=25),
        ),
        migrations.AddField(
            model_name='usuario',
            name='nombre',
            field=models.CharField(default='default_name', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='usuario',
            name='password',
            field=models.CharField(default=False, max_length=20),
        ),
    ]