import pytest
import sys
import os

# Add local directory to path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from math_tool import divide_numbers, calculate_average

class TestMathTool:
    
    # --- divide_numbers tests ---
    
    def test_divide_numbers_happy_path(self):
        assert divide_numbers(10, 2) == 5.0
        assert divide_numbers(9, 3) == 3.0
        assert divide_numbers(-10, 2) == -5.0

    def test_divide_numbers_float(self):
        assert divide_numbers(5, 2) == 2.5

    def test_divide_by_zero(self):
        """驗證自定義 ValueError 被拋出（防禦性編程）"""
        with pytest.raises(ValueError):
            divide_numbers(10, 0)

    # --- calculate_average tests ---

    def test_calculate_average_happy_path(self):
        assert calculate_average([1, 2, 3, 4, 5]) == 3.0
        assert calculate_average([10, 20]) == 15.0

    def test_calculate_average_empty_list(self):
        """驗證空列表返回 0 而非拋出異常（符合防禦性編程原則）"""
        assert calculate_average([]) == 0

    def test_calculate_average_type_error(self):
        """驗證型別檢查：非可迭代物件應拋出 TypeError"""
        with pytest.raises(TypeError):
            calculate_average("not a list")
