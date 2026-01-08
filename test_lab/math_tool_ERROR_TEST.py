# test_lab/math_tool.py

def divide_numbers(numerator, denominator):
    """
    將分子除以分母並返回結果。
    (注意：這段代碼故意沒有處理除以零的情況，也沒有型別檢查)
    """
    return numerator / denominator

def calculate_average(numbers):
    """
    計算列表的平均值。
    (注意：如果列表為空，這會導致錯誤)
    """
    return sum(numbers) / len(numbers)