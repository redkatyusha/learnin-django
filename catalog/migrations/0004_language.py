# Generated by Django 2.2.2 on 2019-06-19 23:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0003_auto_20190619_1913'),
    ]

    operations = [
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text="Enter the book's natural language (ex. English, Spanish, German, etc.", max_length=200)),
            ],
        ),
    ]
