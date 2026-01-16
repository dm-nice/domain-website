# test_lab/math_tool.py

import time
import os
import shlex
import subprocess
from typing import List
from functools import lru_cache

def divide_numbers(numerator: float, denominator: float) -> float:
    """
    將分子除以分母並返回結果。
    """
    if denominator == 0:
        raise ValueError("分母不能為零")
    return numerator / denominator

def calculate_average(numbers: List[float]) -> float:
    """
    計算數字列表的平均值。若列表為空則返回 0。
    """
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)

@lru_cache(maxsize=128)
def slow_fibonacci(n: int) -> int:
    """
    計算第 n 個費氏數列。
    使用 @lru_cache 備忘錄來優化效能。
    """
    if n <= 1:
        return n
    return slow_fibonacci(n - 1) + slow_fibonacci(n - 2)

def _execute_windows_command(user_input: str) -> subprocess.CompletedProcess:
    """在 Windows 上執行 echo 命令。"""
    return subprocess.run(
        f'echo {user_input}',
        shell=True,
        capture_output=True,
        text=True,
        timeout=5
    )

def _execute_unix_command(user_input: str) -> subprocess.CompletedProcess:
    """在 Unix/Linux 上執行 echo 命令。"""
    return subprocess.run(
        ["echo", user_input],
        capture_output=True,
        text=True,
        timeout=5
    )

def run_system_command(user_input: str) -> str:
    """
    根據用戶輸入執行系統指令。
    使用 subprocess.run 搭配 shell=False 來防止命令注入。
    """
    try:
        import platform
        if platform.system() == "Windows":
            result = _execute_windows_command(user_input)
        else:
            result = _execute_unix_command(user_input)
        return f"Executed: echo {user_input}\nOutput: {result.stdout.strip()}"
    except subprocess.TimeoutExpired:
        raise RuntimeError("命令執行逾時")
    except Exception as error:
        raise RuntimeError(f"命令執行失敗: {error}")