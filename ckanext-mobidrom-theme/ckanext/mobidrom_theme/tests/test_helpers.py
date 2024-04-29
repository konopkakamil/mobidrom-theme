"""Tests for helpers.py."""

import ckanext.mobidrom_theme.helpers as helpers


def test_mobidrom_theme_hello():
    assert helpers.mobidrom_theme_hello() == "Hello, mobidrom_theme!"
