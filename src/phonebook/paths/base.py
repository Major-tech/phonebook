from pathlib import Path


def get_home_dir() -> Path:
    """Return the user's home directory in a cross-platform way"""
    
    return Path.home() 


