# Generated by Django 3.2.5 on 2021-07-21 18:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Companies',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('website', models.CharField(max_length=50)),
                ('company_type', models.CharField(choices=[('SRL', 'S.R.L.'), ('SA', 'S.A.')], max_length=5)),
            ],
        ),
    ]
