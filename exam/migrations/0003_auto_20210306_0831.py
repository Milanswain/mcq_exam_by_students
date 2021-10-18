# Generated by Django 3.1.7 on 2021-03-06 08:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("exam", "0002_remove_student_user"),
    ]

    operations = [
        migrations.AlterField(
            model_name="standard",
            name="class_name",
            field=models.CharField(
                choices=[
                    ("1", "1"),
                    ("2", "2"),
                    ("3", "3"),
                    ("4", "4"),
                    ("5", "5"),
                    ("6", "6"),
                    ("7", "7"),
                    ("8", "8"),
                    ("9", "9"),
                    ("10", "10"),
                ],
                max_length=4,
                unique=True,
            ),
        ),
    ]
