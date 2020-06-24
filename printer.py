#!/usr/bin/env python
import os
import django
from pc import PlayerCharacter
from django.template import Template, Context
from django.conf import settings

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['/path/to/template'],
    }
]
settings.configure(TEMPLATES=TEMPLATES)
django.setup()

# Random template. TODO Move this to a separate file when gets more complicated :D.
template = """
<html>
<head>
<title>Template {{ title }}</title>
</head>
<body>
Body with {{ mystring }}.
</body>
</html>
"""

t = Template(template)


def print_char_pdf(player):
    c = Context({"title": "title from code",
                 "mystring": "string from code"})
    script_dir = os.path.dirname(__file__)  # <-- absolute dir the script is in
    rel_path = "created_chars\\{}.html".format(player.name)
    abs_file_path = os.path.join(script_dir, rel_path)
    print(abs_file_path)
    text_file = open(abs_file_path, "w")
    text_file.write("{}\n".format(t.render(c)))


def print_char(player, format="console"):
    if format == "console":
        print("Created char: {}".format(player.name))
        for trait in player.background:
            print(trait.name)
            print_stats(player.stats)
    elif format == "textfile":
        print_char_to_txt(player)
    else:
            raise Exception("Format not supported, supported printing:\nconsole\ntextfile")


def print_char_to_txt(player):
    script_dir = os.path.dirname(__file__)  # <-- absolute dir the script is in
    rel_path = "created_chars\\{}.txt".format(player.name)
    abs_file_path = os.path.join(script_dir, rel_path)
    print(abs_file_path)
    text_file = open(abs_file_path, "w")
    text_file.write("{}\n".format(player.name))
    for stat in player.stats:
            text_file.write("{}:{}\n".format(player.stats[stat].description, str(player.stats[stat].number)))


def print_stats(list_of_stats):
    for stat in list_of_stats:
        print("{}:{}".format(list_of_stats[stat].description, list_of_stats[stat].number))