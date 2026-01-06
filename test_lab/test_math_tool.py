import pytest
import sys
import os

# Add local directory to path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from math_tool import divide_numbers, calculate_average

class TestMathTool:
    
    # --- divide_numbers tests ---
    
    def test_divide_numbers_happy_path(self):
        """測試正常的除法功能"""
        assert divide_numbers(10, 2) == 5.0
        assert divide_numbers(9, 3) == 3.0
        assert divide_numbers(-10, 2) == -5.0

    def test_divide_numbers_float(self):
        """測試浮點數除法"""
        assert divide_numbers(5, 2) == 2.5

    def test_divide_by_zero(self):
        """測試除以零應該拋出異常"""
        # 預期這會失敗，因為目前的代碼沒有特別處理，但 Python 原生會拋出 ZeroDivisionError
        # 測試應該捕獲這個原生錯誤，或者我們預期它應該被優雅處理？
        # 根據 Workflow，我們應該測試它是否符合預期。
        # 如果目標是"修復代碼"，這裡應該寫出"期望的行為"。
        # 假設我們期望它拋出 ZeroDivisionError，或者自定義錯誤。
        # 目前先測試原生行為。
        with pytest.raises(ZeroDivisionError):
            divide_numbers(10, 0)

    # --- calculate_average tests ---

    def test_calculate_average_happy_path(self):
        """測試正常的平均值計算"""
        assert calculate_average([1, 2, 3, 4, 5]) == 3.0
        assert calculate_average([10, 20]) == 15.0

    def test_calculate_average_empty_list(self):
        """測試空列表的情況 - 期望返回 0 (Robustness)"""
        assert calculate_average([]) == 0

    def test_calculate_average_type_error(self):
         """測試傳入非列表的情況 (防禦性編程)"""
         # 這是額外的健壯性測試
         with pytest.raises(TypeError):
             calculate_average("not a list")
