# Generated by Django 2.1.1 on 2018-09-22 15:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BoreHole',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('diameter', models.FloatField()),
                ('depth', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Casing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('od_size', models.FloatField()),
                ('set_depth', models.FloatField()),
                ('top_depth', models.FloatField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='CsgCement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('top_depth', models.FloatField()),
                ('bottom_depth', models.FloatField()),
                ('casing', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wells.Casing')),
            ],
        ),
        migrations.CreateModel(
            name='Perforation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('top_depth', models.FloatField()),
                ('bottom_depth', models.FloatField()),
                ('casing', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wells.Casing')),
            ],
        ),
        migrations.CreateModel(
            name='Track',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('index', models.IntegerField()),
                ('parent_track', models.IntegerField()),
                ('parent_depth', models.FloatField()),
                ('measured_depth', models.FloatField()),
                ('kick_off_point', models.FloatField()),
                ('true_vertical_depth', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Tubular',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('set_depth', models.FloatField()),
                ('track', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wells.Track')),
            ],
        ),
        migrations.CreateModel(
            name='Well',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('api_no', models.CharField(max_length=50)),
                ('depth_units', models.CharField(default='Feet', max_length=50)),
                ('width_units', models.CharField(default='Inches', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='WellOrientation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('orientation', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='track',
            name='orientation',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wells.WellOrientation'),
        ),
        migrations.AddField(
            model_name='track',
            name='well',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wells.Well'),
        ),
        migrations.AddField(
            model_name='casing',
            name='track',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wells.Track'),
        ),
        migrations.AddField(
            model_name='borehole',
            name='track',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wells.Track'),
        ),
    ]
