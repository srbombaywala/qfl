# Generated by Django 5.1.1 on 2024-10-03 10:33

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qflapp', '0002_patron_alter_notice_content_alter_notice_title'),
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('photo', models.ImageField(upload_to='media/')),
            ],
        ),
        migrations.CreateModel(
            name='CommitteeMember',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.CharField(max_length=4)),
                ('designation', models.CharField(choices=[('Supervision Committee', 'Supervision Committee'), ('Chairman', 'Chairman'), ('Vice-Chairman', 'Vice-Chairman'), ('Secretary', 'Secretary'), ('Joint-Secretary', 'Joint-Secretary'), ('Treasurer', 'Treasurer'), ('Member', 'Member')], max_length=100)),
                ('order', models.PositiveIntegerField()),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='committee_memberships', to='qflapp.person')),
            ],
            options={
                'ordering': ['order'],
            },
        ),
    ]
