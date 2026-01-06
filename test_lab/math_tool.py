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
    
    import time
import os

# 1. 效能測試目標：極其低效的費氏數列計算 (遞迴且無快取)
def slow_fibonacci(n):
    """
    計算第 n 個費氏數列。
    (故意使用 O(2^n) 的複雜度來測試效能監控)
    """
    if n <= 1:
        return n
    return slow_fibonacci(n - 1) + slow_fibonacci(n - 2)

# 2. 安全測試目標：存在命令注入風險的系統呼叫
def run_system_command(user_input):
    """
    根據用戶輸入執行系統指令。
    (故意直接拼接字串，模擬常見的 Security Vulnerability)
    """
    import shlex
    # ✅ 安全修復：使用 shlex.quote 過濾 shell 字符
    safe_input = shlex.quote(user_input)
    command = "echo " + safe_input
    os.system(command)
    return f"Executed: {command}"