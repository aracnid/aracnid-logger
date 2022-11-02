"""Test functions for Aracnid Logger import.
"""
from aracnid_logger import __version__

def test_version():
    """Tests that Aracnid Logger was imported successfully.
    """
    assert __version__
