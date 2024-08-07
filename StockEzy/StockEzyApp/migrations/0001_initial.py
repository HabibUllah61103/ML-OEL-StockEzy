# Generated by Django 5.0.6 on 2024-07-07 08:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customers',
            fields=[
                ('custid', models.AutoField(db_column='CustID', primary_key=True, serialize=False)),
                ('cname', models.CharField(blank=True, db_column='CName', max_length=60, null=True)),
                ('cemail', models.CharField(blank=True, db_column='CEmail', max_length=40, null=True, unique=True)),
                ('cpassword', models.CharField(blank=True, db_column='CPassword', max_length=20, null=True)),
                ('createdat', models.DateTimeField(blank=True, db_column='CreatedAt', null=True)),
                ('updatedat', models.DateTimeField(blank=True, db_column='UpdatedAt', null=True)),
                ('deletedat', models.DateTimeField(blank=True, db_column='DeletedAt', null=True)),
                ('last_login', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'customers',
                'managed': True,
            },
        ),
    ]
