# Generated by Django 3.2.21 on 2023-10-01 17:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('core', '0002_user_technical'),
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10, verbose_name='نام واحد')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'کالا',
                'verbose_name_plural': 'کالا ها',
            },
        ),
        migrations.CreateModel(
            name='MaterialRequisition',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(max_length=200, verbose_name='شماره MR')),
                ('date', models.DateField(blank=True, verbose_name='تاریخ تایید')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('created_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='mr', to='core.user', verbose_name='ثبت شده توسط')),
            ],
            options={
                'verbose_name': 'درخواست مواد',
                'verbose_name_plural': 'درخواست های مواد',
                'ordering': ['-created'],
            },
        ),
        migrations.CreateModel(
            name='Warehouse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40, verbose_name='نام انبار')),
                ('address', models.TextField(blank=True, null=True, verbose_name='آدرس')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('created_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='warehouses', to='core.user', verbose_name='ثبت شده توسط')),
                ('users', models.ManyToManyField(blank=True, limit_choices_to={'warehouse_keeper': True}, to='core.User', verbose_name='انباردارها')),
            ],
            options={
                'verbose_name': 'انبار',
                'verbose_name_plural': 'انبارها',
            },
        ),
        migrations.CreateModel(
            name='Unit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10, verbose_name='نام واحد')),
                ('abrv', models.CharField(max_length=10, verbose_name='واحد اختصاری')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('created_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='units', to='core.user', verbose_name='ثبت شده توسط')),
            ],
            options={
                'verbose_name': 'واحد',
                'verbose_name_plural': 'واحد ها',
            },
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40, verbose_name='نام پروژه')),
                ('number', models.CharField(max_length=40, verbose_name='شماره پروژه')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('created_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='projects', to='core.user', verbose_name='ثبت شده توسط')),
            ],
            options={
                'verbose_name': 'پروژه',
                'verbose_name_plural': 'پروژه ها',
            },
        ),
        migrations.CreateModel(
            name='MrItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.PositiveIntegerField(verbose_name='شماره')),
                ('tag_number', models.CharField(max_length=200, verbose_name='Tag/Part number')),
                ('quantity', models.DecimalField(decimal_places=3, max_digits=10, verbose_name='مقدار')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='mritems', to='warehouse.item')),
                ('mr', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='warehouse.materialrequisition')),
                ('unit', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='items', to='warehouse.unit', verbose_name='واحد')),
            ],
            options={
                'verbose_name': 'قلم درخواست  مواد',
                'verbose_name_plural': 'اقلام درخواست های مواد',
            },
        ),
        migrations.AddField(
            model_name='materialrequisition',
            name='project',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='mr', to='warehouse.project', verbose_name='پروژه'),
        ),
    ]
