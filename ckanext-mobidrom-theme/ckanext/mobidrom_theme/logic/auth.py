import ckan.plugins.toolkit as tk


@tk.auth_allow_anonymous_access
def mobidrom_theme_get_sum(context, data_dict):
    return {"success": True}


def get_auth_functions():
    return {
        "mobidrom_theme_get_sum": mobidrom_theme_get_sum,
    }
