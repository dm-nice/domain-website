# test_lab/math_tool.py

def divide_numbers(numerator: float, denominator: float) -> float:
    """
    將分子除以分母並返回結果。
    (注意：這段代碼故意沒有處理除以零的情況)
    """
    return numerator / denominator

def calculate_average(numbers: list[float]) -> float:
    """
    計算數字列表的平均值。若列表為空則返回 0。
    """
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)