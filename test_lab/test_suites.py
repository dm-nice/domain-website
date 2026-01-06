import pytest
import sys
import os

# Add local directory to path so we can import modules
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from bad_math import calculate_sum
from todo_list import create_empty_task

def test_calculate_sum_integers():
    """Test basic integer addition"""
    assert calculate_sum(5, 3) == 8
    assert calculate_sum(-1, 1) == 0

def test_calculate_sum_floats():
    """Test floating point addition"""
    assert calculate_sum(2.5, 1.5) == 4.0
    assert calculate_sum(0.1, 0.2) == pytest.approx(0.3)

def test_create_empty_task_defaults():
    """Verify empty task structure and default values"""
    task = create_empty_task()
    assert isinstance(task, dict)
    assert task['id'] is None
    assert task['title'] == ''
    assert task['completed'] is False
    assert 'created_at' in task
