# Generated by Django 3.2.5 on 2021-07-03 11:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pictures', '0002_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='pictures/')),
                ('name', models.CharField(max_length=60)),
                ('description', models.TextField()),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='pictures.category')),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='pictures.location')),
            ],
        ),
    ]
