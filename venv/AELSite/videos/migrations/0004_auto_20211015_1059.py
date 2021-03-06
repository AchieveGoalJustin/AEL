# Generated by Django 3.2.8 on 2021-10-15 01:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0003_auto_20211014_1903'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='associated_course',
        ),
        migrations.RemoveField(
            model_name='video',
            name='category',
        ),
        migrations.RemoveField(
            model_name='video',
            name='course',
        ),
        migrations.AddField(
            model_name='category',
            name='order',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='category',
            name='videos',
            field=models.ManyToManyField(to='videos.Video'),
        ),
        migrations.AddField(
            model_name='course',
            name='categories',
            field=models.ManyToManyField(to='videos.Category'),
        ),
        migrations.RemoveField(
            model_name='video',
            name='additional_skills',
        ),
        migrations.AddField(
            model_name='video',
            name='additional_skills',
            field=models.ManyToManyField(blank=True, null=True, to='videos.Skill'),
        ),
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('skills_tested', models.ManyToManyField(to='videos.Skill')),
            ],
        ),
    ]
