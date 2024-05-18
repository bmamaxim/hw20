# Generated by Django 4.2 on 2024-05-17 11:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_payment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='payment_date',
            field=models.DateField(auto_now_add=True, null=True, verbose_name='дата оплаты'),
        ),
        migrations.AlterField(
            model_name='payment',
            name='payment_method',
            field=models.CharField(blank=True, choices=[('cash', 'налиный'), ('non-cash', 'безнал')], max_length=100, null=True, verbose_name='способ оплаты'),
        ),
    ]