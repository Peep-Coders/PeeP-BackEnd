# Generated by Django 4.0.2 on 2022-02-14 17:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('peep', '0002_rename_username_peep_owner_remove_peep_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='peep',
            name='image',
            field=models.ImageField(default='images/default.jpg', upload_to='images/'),
        ),
    ]
