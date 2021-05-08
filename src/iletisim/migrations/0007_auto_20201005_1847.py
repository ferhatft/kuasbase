# Generated by Django 3.1.1 on 2020-10-05 15:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('iletisim', '0006_auto_20200926_1639'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='i̇nfo',
            name='closedat',
        ),
        migrations.RemoveField(
            model_name='i̇nfo',
            name='location',
        ),
        migrations.RemoveField(
            model_name='i̇nfo',
            name='startedat',
        ),
        migrations.AddField(
            model_name='i̇nfo',
            name='campanydescrp',
            field=models.CharField(blank=True, max_length=500, null=True, verbose_name='Şirket Açıklaması '),
        ),
        migrations.AddField(
            model_name='i̇nfo',
            name='campanyname',
            field=models.CharField(blank=True, max_length=500, null=True, verbose_name='Şirket ismi '),
        ),
        migrations.AddField(
            model_name='i̇nfo',
            name='city',
            field=models.CharField(max_length=300, null=True, verbose_name='Şehir'),
        ),
        migrations.AddField(
            model_name='i̇nfo',
            name='detay',
            field=models.CharField(blank=True, max_length=300, null=True, verbose_name='Varsa ekstra detaylar'),
        ),
        migrations.AddField(
            model_name='i̇nfo',
            name='main_context',
            field=models.FileField(blank=True, null=True, upload_to='', verbose_name='Ana Parağraf Ekleyin'),
        ),
        migrations.AddField(
            model_name='i̇nfo',
            name='postcode',
            field=models.CharField(max_length=300, null=True, verbose_name='Posta Kodu'),
        ),
        migrations.AddField(
            model_name='i̇nfo',
            name='street',
            field=models.CharField(max_length=300, null=True, verbose_name='Sokak'),
        ),
        migrations.AddField(
            model_name='i̇nfo',
            name='subtitle',
            field=models.CharField(blank=True, max_length=500, null=True, verbose_name='Alt Başlık '),
        ),
    ]