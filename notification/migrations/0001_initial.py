# Generated by Django 2.0.3 on 2018-05-01 18:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('icon', models.ImageField(blank=True, null=True, upload_to='')),
                ('texte', models.CharField(max_length=200)),
                ('titre', models.CharField(max_length=200)),
                ('type', models.CharField(max_length=50)),
                ('importance', models.IntegerField(default=5)),
                ('timestamp', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('sent', models.BooleanField(default=False)),
                ('recieved', models.BooleanField(default=False)),
                ('vue', models.BooleanField(default=False)),
            ],
        ),
    ]
