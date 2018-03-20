# Generated by Django 2.0.3 on 2018-03-20 10:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='employees',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('employeeNo', models.IntegerField()),
                ('name', models.CharField(max_length=100)),
                ('image', models.CharField(blank=True, max_length=500, null=True)),
                ('mobileNo', models.CharField(blank=True, max_length=200, null=True, unique=True)),
                ('isActive', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'employees',
            },
        ),
        migrations.CreateModel(
            name='issueInvoice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(max_length=30)),
                ('qty', models.IntegerField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.employees')),
            ],
            options={
                'db_table': 'issue_inovice',
            },
        ),
        migrations.CreateModel(
            name='items',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True, null=True)),
                ('image', models.CharField(blank=True, max_length=500, null=True)),
                ('qty', models.IntegerField(blank=True, default=0, null=True)),
                ('sku', models.CharField(blank=True, max_length=200, null=True)),
                ('costPrice', models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True)),
                ('totalAmount', models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True)),
                ('isActive', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.categories')),
            ],
            options={
                'db_table': 'items',
            },
        ),
        migrations.CreateModel(
            name='psDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('totalAmount', models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True)),
                ('qty', models.IntegerField(blank=True, default=0, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.items')),
            ],
            options={
                'db_table': 'ps_invoice_details',
            },
        ),
        migrations.CreateModel(
            name='purchaseInvoive',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(max_length=30)),
                ('totalAmount', models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'purchase_inovice',
            },
        ),
        migrations.CreateModel(
            name='users',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=30, unique=True)),
                ('password', models.CharField(max_length=150)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('salt', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'users',
            },
        ),
        migrations.CreateModel(
            name='userType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'user_types',
            },
        ),
        migrations.CreateModel(
            name='vendors',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('image', models.CharField(blank=True, max_length=500, null=True)),
                ('mobileNo', models.CharField(blank=True, max_length=200, null=True, unique=True)),
                ('address', models.CharField(blank=True, max_length=200, null=True)),
                ('isActive', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'vendors',
            },
        ),
        migrations.AddField(
            model_name='users',
            name='type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.userType'),
        ),
        migrations.AddField(
            model_name='purchaseinvoive',
            name='vendor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.vendors'),
        ),
        migrations.AddField(
            model_name='psdetails',
            name='master_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.purchaseInvoive'),
        ),
        migrations.AddField(
            model_name='items',
            name='vendor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.vendors'),
        ),
        migrations.AddField(
            model_name='issueinvoice',
            name='item',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.items'),
        ),
    ]
