# Generated by Django 3.2.5 on 2021-08-02 17:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('aplicatie2', '0002_companies_location'),
        ('aplicatie1', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='location',
            name='company',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='companie', to='aplicatie2.companies'),
            preserve_default=False,
        ),
    ]
