from django.db import migrations


def load_initial_videogames(apps, schema_editor):
    Videogame = apps.get_model('videogames', 'Videogame')
    videogames = [
        {
            'title': 'League of Legends',
            'genre': 'MOBA',
            'platform': 'PC',
            'release_year': 2009,
            'description': 'A multiplayer online battle arena game developed by Riot Games.',
        },
        {
            'title': 'Minecraft',
            'genre': 'Sandbox',
            'platform': 'PC/Console',
            'release_year': 2011,
            'description': 'A sandbox game about building and exploration.',
        },
        {
            'title': 'God of War',
            'genre': 'Action-Adventure',
            'platform': 'PlayStation',
            'release_year': 2018,
            'description': 'An action-adventure game following Kratos and his son Atreus.',
        },
    ]
    for data in videogames:
        Videogame.objects.create(**data)


def remove_initial_videogames(apps, schema_editor):
    Videogame = apps.get_model('videogames', 'Videogame')
    Videogame.objects.filter(
        title__in=['League of Legends', 'Minecraft', 'God of War']
    ).delete()


class Migration(migrations.Migration):

    dependencies = [
        ('videogames', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(load_initial_videogames, remove_initial_videogames),
    ]
