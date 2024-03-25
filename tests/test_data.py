import os
from project_paths import RAW_DATA


def test_RAW_DATA__present():
    """Test if raw data is in place."""
    N_files = len([x for x in os.listdir(RAW_DATA) if x != ".gitkeep"])
    assert 2 <= N_files, "There are lacking files in RAW_DATA directory"
