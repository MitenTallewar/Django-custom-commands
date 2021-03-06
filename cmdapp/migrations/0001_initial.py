# Generated by Django 2.2.3 on 2020-08-27 06:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Emp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('age', models.IntegerField()),
                ('balance', models.FloatField()),
                ('role', models.CharField(max_length=50)),
                ('photo', models.ImageField(default='NA', upload_to='user_photos/')),
                ('active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=50)),
                ('pincode', models.IntegerField()),
                ('state', models.CharField(max_length=50)),
                ('active', models.BooleanField(default=True)),
                ('emps', models.ManyToManyField(null=True, related_name='adrs', to='cmdapp.Emp')),
            ],
        ),
    ]
