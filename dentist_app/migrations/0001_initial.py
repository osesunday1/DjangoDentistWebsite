# Generated by Django 4.2 on 2023-05-13 17:32

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('is_patient', models.BooleanField(default=False)),
                ('is_doctor', models.BooleanField(default=False)),
                ('is_scheduler', models.BooleanField(default=False)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=130)),
                ('specialty', models.CharField(choices=[('Periodontists', 'Periodontists'), ('Prosthodontists', 'Prosthodontists'), ('Pediatric', 'Pediatric'), ('General Checkup', 'General Checkup'), ('Toothache', 'Toothache')], max_length=200)),
                ('address', models.TextField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=130)),
                ('address', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Scheduler',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=100)),
                ('email', models.TextField(max_length=130)),
                ('address', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='MedicalRecord',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bp', models.CharField(max_length=100, null=True)),
                ('weight', models.CharField(max_length=100, null=True)),
                ('height', models.CharField(max_length=100, null=True)),
                ('family', models.CharField(max_length=100, null=True)),
                ('allergies', models.CharField(max_length=100, null=True)),
                ('others', models.TextField(max_length=500, null=True)),
                ('patient_name', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='dentist_app.patient')),
            ],
        ),
        migrations.CreateModel(
            name='Consultation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('diagnostics', models.CharField(max_length=300)),
                ('treatment', models.CharField(max_length=300)),
                ('date', models.DateField(auto_now_add=True, null=True)),
                ('doctor_name', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='dentist_app.doctor')),
                ('patient_name', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='dentist_app.patient')),
            ],
        ),
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(verbose_name='Appointment Date')),
                ('issue', models.CharField(blank=True, choices=[('Whitening', 'Whitening'), ('Toothache', 'Toothache')], max_length=120, null=True)),
                ('time', models.CharField(blank=True, choices=[('08 AM to 09 AM', '08 AM to 09 AM'), ('09 AM to 10 AM', '09 AM to 10 AM'), ('10 AM to 11 AM', '10 AM to 11 AM'), ('11 AM to 12 PM', '11 AM to 12 PM'), ('12 PM to 01 PM', '12 PM to 01 PM'), ('01 PM to 02 PM', '01 PM to 02 PM'), ('03 PM to 03 PM', '02 PM to 03 PM'), ('04 PM to 05 PM', '04 PM to 05 PM')], max_length=120, null=True)),
                ('doctor_name', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='dentist_app.doctor')),
                ('patient_name', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='dentist_app.patient')),
            ],
        ),
    ]
