# Generated by Django 5.1.4 on 2025-01-15 08:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travels', '0002_referral_userprofile'),
    ]

    operations = [
        migrations.CreateModel(
            name='Testimonial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=255)),
                ('content', models.TextField()),
                ('age', models.PositiveIntegerField(default=55)),
                ('company', models.CharField(max_length=50)),
            ],
        ),
        migrations.AlterField(
            model_name='raffleentry',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
    ]
