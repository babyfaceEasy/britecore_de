# Generated by Django 2.2.1 on 2019-05-24 05:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('risk', '0004_auto_20190523_1146'),
    ]

    operations = [
        migrations.CreateModel(
            name='EnumValues',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('enumField', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='enumField', to='risk.Field')),
            ],
        ),
    ]