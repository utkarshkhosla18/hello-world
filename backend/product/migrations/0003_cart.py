# Generated by Django 3.1 on 2022-05-04 19:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_auto_20220504_1923'),
        ('product', '0002_product_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.IntegerField(max_length=10000)),
                ('quantity', models.IntegerField(max_length=10000)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='customer_carts', to='user.customer')),
            ],
        ),
    ]
