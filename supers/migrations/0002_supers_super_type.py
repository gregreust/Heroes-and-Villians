# Generated by Django 4.1 on 2022-08-23 15:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('super_types', '0001_initial'),
        ('supers', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='supers',
            name='super_type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='super_types.supertype'),
        ),
    ]
