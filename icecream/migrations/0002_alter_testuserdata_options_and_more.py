# Generated by Django 4.0.4 on 2022-06-08 12:08

from django.db import migrations, models
import icecream.models


class Migration(migrations.Migration):

    dependencies = [
        ('icecream', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='testuserdata',
            options={},
        ),
        migrations.AlterModelManagers(
            name='testuserdata',
            managers=[
            ],
        ),
        migrations.RenameField(
            model_name='testuserdata',
            old_name='is_verified',
            new_name='is_admin',
        ),
        migrations.RemoveField(
            model_name='testuserdata',
            name='email_token',
        ),
        migrations.RemoveField(
            model_name='testuserdata',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='testuserdata',
            name='forget_password',
        ),
        migrations.RemoveField(
            model_name='testuserdata',
            name='groups',
        ),
        migrations.RemoveField(
            model_name='testuserdata',
            name='last_login_time',
        ),
        migrations.RemoveField(
            model_name='testuserdata',
            name='last_logout_time',
        ),
        migrations.RemoveField(
            model_name='testuserdata',
            name='last_name',
        ),
        migrations.RemoveField(
            model_name='testuserdata',
            name='phone',
        ),
        migrations.RemoveField(
            model_name='testuserdata',
            name='user_permissions',
        ),
        migrations.AddField(
            model_name='testuserdata',
            name='hide_email',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='testuserdata',
            name='profile_image',
            field=models.ImageField(blank=True, default=icecream.models.get_default_profile_image, max_length=255, null=True, upload_to=icecream.models.get_profile_image_filepath),
        ),
        migrations.AddField(
            model_name='testuserdata',
            name='username',
            field=models.CharField(default='Example', max_length=30, unique=True),
        ),
        migrations.AlterField(
            model_name='testuserdata',
            name='date_joined',
            field=models.DateTimeField(auto_now_add=True, verbose_name='datejoined'),
        ),
        migrations.AlterField(
            model_name='testuserdata',
            name='email',
            field=models.EmailField(max_length=60, unique=True, verbose_name='email'),
        ),
        migrations.AlterField(
            model_name='testuserdata',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='testuserdata',
            name='is_staff',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='testuserdata',
            name='is_superuser',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='testuserdata',
            name='last_login',
            field=models.DateTimeField(auto_now=True, verbose_name='lstlogin'),
        ),
    ]
