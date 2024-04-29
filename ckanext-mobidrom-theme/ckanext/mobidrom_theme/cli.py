import click


@click.group(short_help="mobidrom_theme CLI.")
def mobidrom_theme():
    """mobidrom_theme CLI.
    """
    pass


@mobidrom_theme.command()
@click.argument("name", default="mobidrom_theme")
def command(name):
    """Docs.
    """
    click.echo("Hello, {name}!".format(name=name))


def get_commands():
    return [mobidrom_theme]
