# Generated by Django 3.0.5 on 2020-11-29 18:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tweet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=200)),
                ('media', models.CharField(max_length=200, null=True)),
                ('username', models.CharField(max_length=200)),
                ('type', models.CharField(max_length=200)),
                ('created_at', models.DateTimeField()),
            ],
        ),
    ]