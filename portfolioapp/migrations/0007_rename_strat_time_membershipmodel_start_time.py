# Generated by Django 4.2.4 on 2024-01-26 12:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolioapp', '0006_remove_transactionlogmodel_back_acc_no_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='membershipmodel',
            old_name='strat_time',
            new_name='start_time',
        ),
    ]