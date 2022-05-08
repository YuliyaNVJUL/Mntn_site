# Generated by Django 4.0.3 on 2022-04-16 08:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mountains', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='equipment',
            name='available',
            field=models.CharField(choices=[('None', 'Choose:'), ('Available', 'Available'), ('Do dyspozycji', 'Do dyspozycji'), ('On order', 'On order'), ('Na zamówienie', 'Na zamówienie'), ('On sale soon', 'On sale soon'), ('Wkrotce na wyprzedazy', 'Wkrotce na wyprzedazy')], max_length=50, verbose_name='Available'),
        ),
        migrations.AlterField(
            model_name='equipment',
            name='available_en',
            field=models.CharField(choices=[('None', 'Choose:'), ('Available', 'Available'), ('Do dyspozycji', 'Do dyspozycji'), ('On order', 'On order'), ('Na zamówienie', 'Na zamówienie'), ('On sale soon', 'On sale soon'), ('Wkrotce na wyprzedazy', 'Wkrotce na wyprzedazy')], max_length=50, null=True, verbose_name='Available'),
        ),
        migrations.AlterField(
            model_name='equipment',
            name='available_pl',
            field=models.CharField(choices=[('None', 'Choose:'), ('Available', 'Available'), ('Do dyspozycji', 'Do dyspozycji'), ('On order', 'On order'), ('Na zamówienie', 'Na zamówienie'), ('On sale soon', 'On sale soon'), ('Wkrotce na wyprzedazy', 'Wkrotce na wyprzedazy')], max_length=50, null=True, verbose_name='Available'),
        ),
    ]
