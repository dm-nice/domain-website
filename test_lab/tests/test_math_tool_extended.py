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

    # --- 效能測試案例 (Benchmark) ---
    @pytest.mark.benchmark
    def test_fibonacci_performance(self):
        """
        基準測試：費氏數列計算效能。
        當 n=30 時，O(2^n) 應該會顯著變慢，這是一個效能監控點。
        """
        start_time = time.time()
        result = slow_fibonacci(10)  # 使用較小的 n 以快速驗證邏輯
        end_time = time.time()
        
        duration = end_time - start_time
        print(f"\nTime taken for fib(10): {duration:.6f}s")
        
        assert result == 55
        # 效能斷言：簡單計算不應超過 0.1 秒
        assert duration < 0.1

    # --- 安全性測試案例 (Security) ---
    def test_run_system_command_injection(self):
        """
        安全性測試：檢查命令注入風險。
        我們期望系統不應該直接執行危險字符。
        但原本的代碼存在風險，所以我們預期這個測試能捕捉到注入行為，
        或者我們 mock os.system 來驗證它被呼叫的參數。
        """
        risky_input = "hello; rm -rf /"
        
        # 使用 mock 來攔截 system call，避免真的執行危險指令
        with patch('os.system') as mock_system:
            run_system_command(risky_input)
            
            # 驗證被執行的命令
            mock_system.assert_called_once()
            args, _ = mock_system.call_args
            executed_cmd = args[0]
            
            # 安全斷言：驗證危險字符已被轉義
            # 例如 hello; rm -rf / 應該變成 'hello; rm -rf /' (在 Windows 可能不同，shlex.quote 使用單引號包裹)
            # 我們檢查它是否不再是原本的裸露危險字串
            if "echo hello; rm -rf /" in executed_cmd:
                 pytest.fail(f"Security Vulnerability Detected: Command NOT sanitized: '{executed_cmd}'")
            
            # 通過標準 Check：shlex.quote 應該加上引號
            assert "'" in executed_cmd or '"' in executed_cmd, "Command should be quoted for safety"

