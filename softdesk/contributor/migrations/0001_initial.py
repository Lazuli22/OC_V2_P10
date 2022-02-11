# Generated by Django 4.0 on 2022-02-07 22:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contributor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('permission', models.CharField(choices=[('R', 'read'), ('RW', 'Read_Write'), ('RWD', 'Read_Write_Delete')], max_length=50)),
                ('role', models.CharField(choices=[('ad', 'admin'), ('te', 'technicien'), ('cu', 'customer')], max_length=20)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.project')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.user')),
            ],
        ),
    ]
