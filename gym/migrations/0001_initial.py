# Generated by Django 3.0.7 on 2020-06-30 12:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Enquipment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('price', models.CharField(max_length=10)),
                ('unit', models.CharField(max_length=30)),
                ('date', models.CharField(max_length=10)),
                ('description', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Enquiry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('contact', models.CharField(max_length=10)),
                ('emailid', models.CharField(max_length=30)),
                ('age', models.CharField(max_length=5)),
                ('gender', models.CharField(max_length=7)),
            ],
        ),
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('contact', models.CharField(max_length=10)),
                ('emailid', models.CharField(max_length=30)),
                ('age', models.CharField(max_length=5)),
                ('gender', models.CharField(max_length=7)),
                ('plan', models.CharField(max_length=50)),
                ('joindate', models.CharField(max_length=50)),
                ('expireddate', models.CharField(max_length=50)),
                ('initialamount', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Plan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('amount', models.CharField(max_length=10)),
                ('duration', models.CharField(max_length=30)),
            ],
        ),
    ]
