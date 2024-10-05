

from django.db import migrations

def populate_status(apps, schemaeditor):
    entries = {
        "to do": "An issue for which work has not started",
        "in progress": "An issue activity being worked on",
        "done": "An issue that has been completed"
    }
    Status = apps.get_model("issues", "Status")
    for key, value in entries.items():
        status = Status(name=key, description=value)
        status.save()

class Migration(migrations.Migration):

    dependencies = [
        ('issues', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(populate_status)
    ]