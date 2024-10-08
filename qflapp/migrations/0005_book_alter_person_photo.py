# Generated by Django 5.1.1 on 2024-10-05 09:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qflapp', '0004_alter_person_photo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=50, unique=True)),
                ('title', models.CharField(max_length=200)),
                ('author', models.CharField(max_length=200)),
                ('genre', models.CharField(choices=[('Religion', 'Religion'), ('Education', 'Education'), ('General Knowledge', 'General Knowledge'), ('Fiction', 'Fiction'), ('Current Affairs', 'Current Affairs')], max_length=100)),
                ('language', models.CharField(choices=[('English', 'English'), ('Gujarati', 'Gujarati'), ('Urdu', 'Urdu'), ('Others', 'Others')], max_length=50)),
            ],
        ),
        migrations.AlterField(
            model_name='person',
            name='photo',
            field=models.ImageField(upload_to='media/'),
        ),
    ]
