# Generated by Django 5.0.2 on 2024-03-05 05:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PPRSS', '0006_features'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='features',
            name='AddressOfEntryPoint',
        ),
        migrations.RemoveField(
            model_name='features',
            name='CheckSum',
        ),
        migrations.RemoveField(
            model_name='features',
            name='DirectoryEntryExport',
        ),
        migrations.RemoveField(
            model_name='features',
            name='DirectoryEntryImport',
        ),
        migrations.RemoveField(
            model_name='features',
            name='DirectoryEntryImportSize',
        ),
        migrations.RemoveField(
            model_name='features',
            name='DllCharacteristics',
        ),
        migrations.RemoveField(
            model_name='features',
            name='ImageBase',
        ),
        migrations.RemoveField(
            model_name='features',
            name='ImageDirectoryEntryImport',
        ),
        migrations.RemoveField(
            model_name='features',
            name='ImageDirectoryEntryResource',
        ),
        migrations.RemoveField(
            model_name='features',
            name='ImageDirectoryEntrySecurity',
        ),
        migrations.RemoveField(
            model_name='features',
            name='MajorLinkerVersion',
        ),
        migrations.RemoveField(
            model_name='features',
            name='SectionMaxPhysical',
        ),
        migrations.RemoveField(
            model_name='features',
            name='SectionMaxPointerData',
        ),
        migrations.RemoveField(
            model_name='features',
            name='SectionMinEntropy',
        ),
        migrations.RemoveField(
            model_name='features',
            name='SectionMinVirtualSize',
        ),
        migrations.RemoveField(
            model_name='features',
            name='SizeOfCode',
        ),
        migrations.RemoveField(
            model_name='features',
            name='SizeOfImage',
        ),
        migrations.RemoveField(
            model_name='features',
            name='SizeOfInitializedData',
        ),
        migrations.RemoveField(
            model_name='features',
            name='SizeOfStackReserve',
        ),
        migrations.RemoveField(
            model_name='features',
            name='e_lfanew',
        ),
        migrations.AddField(
            model_name='features',
            name='features_vector',
            field=models.TextField(default='{}'),
        ),
    ]
