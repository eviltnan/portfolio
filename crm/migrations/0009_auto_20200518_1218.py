# Generated by Django 2.2.12 on 2020-05-18 12:18

from django.db import migrations


def fix_wagtail_5832(apps, schema_editor):
    # https://github.com/wagtail/wagtail/issues/5832
    fields = ['notes', 'payment_address', 'experience_overview', 'education_overview', 'contact_details',
              'languages_overview', 'rate_overview', 'working_permit', 'default_experience_overview',
              'default_education_overview', 'default_contact_details', 'default_languages_overview',
              'default_rate_overview',
              'default_working_permit', 'payment_address', 'bank_account', 'contact_data', 'default_bank_account',
              'default_contact_data', 'notes']

    for model in apps.get_models():
        ex_markdown_fields = [field.name for field in model._meta.fields if field.name in fields]
        if ex_markdown_fields:
            print(f"{model.__name__}: {ex_markdown_fields}")
        for instance in model.objects.all():
            for field in ex_markdown_fields:
                original_value = getattr(instance, field)
                setattr(
                    instance, field,
                    original_value.replace("<br>", "<br/>")
                )
                instance.save(update_fields=[field])


class Migration(migrations.Migration):
    dependencies = [
        ('crm', '0008_auto_fixing_markdown'),
    ]

    operations = [
        migrations.RunPython(fix_wagtail_5832),
    ]
