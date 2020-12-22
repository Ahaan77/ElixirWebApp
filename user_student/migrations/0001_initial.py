# Generated by Django 2.2.13 on 2020-12-18 08:24

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user_admin', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='student_status',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_time', models.DateTimeField()),
                ('score', models.IntegerField(validators=[django.core.validators.MinValueValidator(0)])),
                ('status', models.CharField(choices=[('S_Pass', 'S_Pass'), ('S_Fail', 'S_Fail'), ('I_Pass', 'I_Pass'), ('I_Fail', 'I_Fail'), ('AV_Pass', 'AV_Pass'), ('AV_Fail', 'AV_Fail'), ('C_Pass', 'C_Pass'), ('C_Fail', 'C_Fail')], max_length=100)),
                ('batch_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user_admin.batch')),
                ('level_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user_admin.module_level')),
                ('module_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user_admin.program_module')),
                ('program_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user_admin.program')),
                ('student_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user_admin.student')),
            ],
            options={
                'verbose_name_plural': 'student_statuses',
            },
        ),
        migrations.CreateModel(
            name='scores',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_score', models.IntegerField()),
                ('date_time', models.DateTimeField(blank=True, null=True)),
                ('total_score', models.IntegerField(default=0)),
                ('assesment_type', models.CharField(default='Narrative', max_length=20)),
                ('batch_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='user_admin.batch')),
                ('level_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='user_admin.module_level')),
                ('question_content_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='user_admin.question_content')),
                ('student_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='user_admin.student')),
            ],
        ),
    ]
