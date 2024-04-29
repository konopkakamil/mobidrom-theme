"""Tests for validators.py."""

import pytest

import ckan.plugins.toolkit as tk

from ckanext.mobidrom_theme.logic import validators


def test_mobidrom_theme_reauired_with_valid_value():
    assert validators.mobidrom_theme_required("value") == "value"


def test_mobidrom_theme_reauired_with_invalid_value():
    with pytest.raises(tk.Invalid):
        validators.mobidrom_theme_required(None)
