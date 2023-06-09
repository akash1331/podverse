# Generated by Django 4.2 on 2023-04-23 15:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_alter_podcastdetails_likes'),
    ]

    operations = [
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lang', models.CharField(choices=[('EN', 'English'), ('ES', 'Spanish'), ('FR', 'French'), ('DE', 'German'), ('IT', 'Italian'), ('PT', 'Portuguese'), ('RU', 'Russian'), ('ZH', 'Chinese'), ('JA', 'Japanese'), ('KO', 'Korean'), ('AR', 'Arabic'), ('HI', 'Hindi'), ('BN', 'Bengali'), ('UR', 'Urdu'), ('FA', 'Persian')], max_length=15)),
            ],
            options={
                'verbose_name': 'Language',
                'verbose_name_plural': 'Languages',
            },
        ),
        migrations.AddField(
            model_name='podcastdetails',
            name='Land',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.language'),
        ),
    ]
