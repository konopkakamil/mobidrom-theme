"""Tests for views.py."""

import pytest

import ckanext.mobidrom_theme.validators as validators


import ckan.plugins.toolkit as tk


@pytest.mark.ckan_config("ckan.plugins", "mobidrom_theme")
@pytest.mark.usefixtures("with_plugins")
def test_mobidrom_theme_blueprint(app, reset_db):
    resp = app.get(tk.h.url_for("mobidrom_theme.page"))
    assert resp.status_code == 200
    assert resp.body == "Hello, mobidrom_theme!"
