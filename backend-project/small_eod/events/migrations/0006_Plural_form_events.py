# Generated by Django 3.0.5 on 2020-04-27 10:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    replaces = [('events', '0006_auto_20200427_0903'), ('events', '0007_auto_20200427_0932')]

    dependencies = [
        ('cases', '0011_auto_20200420_0717'),
        ('events', '0005_auto_20200306_2101'),
    ]

    operations = [
        migrations.RenameField(
            model_name='event',
            old_name='comment',
            new_name='comments',
        ),
        migrations.RenameField(
            model_name='event',
            old_name='case',
            new_name='cases',
        ),
        migrations.AlterField(
            model_name='event',
            name='cases',
            field=models.ForeignKey(help_text='Cases for this event.', on_delete=django.db.models.deletion.DO_NOTHING,
                                    to='cases.Case', verbose_name='Cases'),
        ),
        migrations.AlterField(
            model_name='event',
            name='comments',
            field=models.CharField(help_text='Comments text.', max_length=256, verbose_name='Comments'),
        ),
    ]
