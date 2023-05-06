# Generated by Django 4.2 on 2023-04-30 20:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dentist_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='scheduler',
            name='address',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='doctor',
            name='address',
            field=models.TextField(max_length=200),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='phone',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='specialty',
            field=models.CharField(choices=[('Periodontists', 'Periodontists'), ('Prosthodontists', 'Prosthodontists'), ('Pediatric', 'Pediatric'), ('General Checkup', 'General Checkup'), ('Toothache', 'Toothache')], max_length=200),
        ),
        migrations.AlterField(
            model_name='patient',
            name='address',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='patient',
            name='phone',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='scheduler',
            name='email',
            field=models.TextField(max_length=130),
        ),
    ]