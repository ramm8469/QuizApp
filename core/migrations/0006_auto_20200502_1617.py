# Generated by Django 3.0 on 2020-05-02 16:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_auto_20200502_1606'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='quizdestributormodel_10',
            name='questions_list',
        ),
        migrations.AddField(
            model_name='quizdestributormodel_10',
            name='questions_list',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, related_name='+', to='core.QuestionSet10'),
            preserve_default=False,
        ),
        migrations.RemoveField(
            model_name='quizdestributormodel_5',
            name='questions_list',
        ),
        migrations.AddField(
            model_name='quizdestributormodel_5',
            name='questions_list',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, related_name='+', to='core.QuestionSet5'),
            preserve_default=False,
        ),
    ]
