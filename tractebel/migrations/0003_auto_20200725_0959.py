# Generated by Django 2.0.1 on 2020-07-25 12:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tractebel', '0002_auto_20200725_0937'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='profitcenter',
            options={'ordering': ['businessline', 'description']},
        ),
        migrations.AlterField(
            model_name='profitcenter',
            name='description',
            field=models.CharField(default='New Profit Center', max_length=50),
        ),
        migrations.AlterUniqueTogether(
            name='profitcenter',
            unique_together={('businessline', 'description')},
        ),
    ]
