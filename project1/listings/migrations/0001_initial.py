# Generated by Django 2.2.10 on 2020-10-02 18:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('realtors', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='listings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('address', models.CharField(max_length=150)),
                ('city', models.CharField(max_length=150)),
                ('state', models.CharField(max_length=150)),
                ('zip_code', models.CharField(max_length=150)),
                ('desc', models.CharField(max_length=150, verbose_name='Description')),
                ('price', models.IntegerField()),
                ('bedrooms', models.CharField(max_length=150)),
                ('garage', models.BooleanField()),
                ('sqft', models.IntegerField()),
                ('lot_size', models.DecimalField(decimal_places=2, max_digits=5)),
                ('is_published', models.BooleanField()),
                ('photo_main', models.ImageField(upload_to='photos/%y/%m/%d')),
                ('photo_1', models.ImageField(upload_to='photos/%y/%m/%d')),
                ('photo_2', models.ImageField(upload_to='photos/%y/%m/%d')),
                ('photo_3', models.ImageField(upload_to='photos/%y/%m/%d')),
                ('photo_4', models.ImageField(upload_to='photos/%y/%m/%d')),
                ('photo_5', models.ImageField(upload_to='photos/%y/%m/%d')),
                ('photo_6', models.ImageField(upload_to='photos/%y/%m/%d')),
                ('list_date', models.DateTimeField(auto_now_add=True)),
                ('update', models.DateTimeField(auto_now=True)),
                ('realtor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='realtors.Realtor')),
            ],
        ),
    ]
