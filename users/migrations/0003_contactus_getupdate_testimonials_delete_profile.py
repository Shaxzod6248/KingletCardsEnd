# Generated by Django 4.1.5 on 2023-01-30 09:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_profile_card_number'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactUs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('your_name', models.CharField(max_length=50, null=True)),
                ('email_address', models.CharField(max_length=100, null=True)),
                ('whatsapp_number', models.CharField(max_length=20, null=True)),
                ('message', models.TextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='GetUpdate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30, null=True)),
                ('last_name', models.CharField(max_length=50, null=True)),
                ('your_email', models.CharField(max_length=300, null=True)),
                ('instagram_accaount', models.CharField(max_length=300, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Testimonials',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=300, null=True)),
                ('comment', models.TextField(null=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Profile',
        ),
    ]