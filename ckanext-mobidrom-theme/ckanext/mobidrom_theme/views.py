from flask import Blueprint


mobidrom_theme = Blueprint(
    "mobidrom_theme", __name__)


def page():
    return "Hello, mobidrom_theme!"


mobidrom_theme.add_url_rule(
    "/mobidrom_theme/page", view_func=page)


def get_blueprints():
    return [mobidrom_theme]
