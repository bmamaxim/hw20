# Generated by Django 4.2 on 2024-05-24 15:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_alter_payment_payment_method'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='payment',
            name='payment_sum',
        ),
        migrations.AddField(
            model_name='payment',
            name='amount',
            field=models.PositiveIntegerField(blank=True, help_text='сумма оплаты', null=True, verbose_name='сумма оплаты'),
        ),
    ]