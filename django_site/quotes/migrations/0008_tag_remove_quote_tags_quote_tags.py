# Generated by Django 5.1.2 on 2024-11-04 10:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quotes', '0007_testquote'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25, unique=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='quote',
            name='tags',
        ),
        migrations.AddField(
            model_name='quote',
            name='tags',
            field=models.ManyToManyField(to='quotes.tag'),
        ),
    ]