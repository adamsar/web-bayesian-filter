"""
File based utility functions
"""
import os.path

def get_parent(file_path, levels=1):
    """
    Gets the parent recursively for a file_path
    levels times
    """
    if levels > 0:
        return get_parent(os.path.dirname(file_path), levels - 1)
    return file_path
    
