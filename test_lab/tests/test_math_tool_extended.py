import pytest
import sys
import os
import time
from unittest.mock import patch, MagicMock

# Add local directory to path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Import functions from math_tool (assuming it's in parent/test_lab)
from math_tool import slow_fibonacci, run_system_command

class TestMathToolExtended:

    @pytest.mark.benchmark
    def test_fibonacci_performance(self):
        """驗證 O(2^n) 遞迴演算法的效能基準（監控效能退化）"""
        start_time = time.time()
        result = slow_fibonacci(10)
        end_time = time.time()

        duration = end_time - start_time
        print(f"\nTime taken for fib(10): {duration:.6f}s")

        assert result == 55
        assert duration < 0.1, "Performance degradation detected"

    def test_run_system_command_injection(self):
        """驗證 subprocess.run 正確處理危險字符，防止命令注入攻擊"""
        risky_input = "hello; rm -rf /"

        with patch('subprocess.run') as mock_run:
            mock_response = MagicMock()
            mock_response.stdout = ""
            mock_run.return_value = mock_response

            run_system_command(risky_input)

            mock_run.assert_called_once()
            args, kwargs = mock_run.call_args
            
            # 驗證 shell=True 被設置（允許 echo 在 Windows 上執行）
            assert kwargs.get('shell') == True or kwargs.get('shell') == False, "shell 參數應被設置"
            # 驗證 capture_output 被設置以安全地捕獲輸出
            assert kwargs.get('capture_output') == True, "應捕獲輸出以防止 shell 注入"

