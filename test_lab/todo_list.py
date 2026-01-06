"""
Task management module for handling todo list operations.
"""


def create_empty_task():
    """
    Create and return an empty task dictionary.

    Returns:
        dict: An empty task dictionary with default values

    Examples:
        >>> task = create_empty_task()
        >>> task['title']
        ''
    """
    return {
        'id': None,
        'title': '',
        'description': '',
        'completed': False,
        'created_at': None
    }
