import ckan.plugins.toolkit as tk


def mobidrom_theme_required(value):
    if not value or value is tk.missing:
        raise tk.Invalid(tk._("Required"))
    return value


def get_validators():
    return {
        "mobidrom_theme_required": mobidrom_theme_required,
    }
