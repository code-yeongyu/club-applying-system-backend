# Generated by Django 3.0.3 on 2020-02-14 15:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='application',
            name='email',
            field=models.EmailField(default='example@example.com', max_length=254),
        ),
        migrations.AddField(
            model_name='application',
            name='name',
            field=models.CharField(default='BUG', max_length=4),
        ),
        migrations.AddField(
            model_name='application',
            name='number',
            field=models.CharField(default='10310', max_length=5),
        ),
        migrations.AddField(
            model_name='application',
            name='phone_number',
            field=models.CharField(default='hi', max_length=11),
        ),
    ]