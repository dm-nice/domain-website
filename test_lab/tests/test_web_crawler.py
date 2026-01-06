import pytest
from unittest.mock import patch, Mock
import requests
import sys
import os

# Add local directory to path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from web_crawler import fetch_titles, download_data

class TestWebCrawler:

    # --- fetch_titles tests ---

    @patch('requests.get')
    def test_fetch_titles_success(self, mock_get):
        """測試成功抓取並解析 H1 標題"""
        # Mock Response
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.text = "<html><body><h1> Title 1 </h1><h1>Title 2</h1></body></html>"
        mock_get.return_value = mock_response

        titles = fetch_titles("http://example.com")
        
        assert titles == ["Title 1", "Title 2"] # strip() test
        # 驗證 headers 與 timeout
        args, kwargs = mock_get.call_args
        assert "User-Agent" in kwargs['headers']
        assert kwargs['timeout'] == 10

    @patch('requests.get')
    def test_fetch_titles_404(self, mock_get):
        """測試 404 情況 - 應優雅處理 (Robustness)"""
        # 模擬 raise_for_status 行為
        mock_response = Mock()
        mock_response.status_code = 404
        mock_response.raise_for_status.side_effect = requests.exceptions.HTTPError("404 Client Error")
        mock_get.return_value = mock_response

        titles = fetch_titles("http://example.com/404")
        
        # 修復後應抓到異常並返回空列表
        assert titles == []

    @patch('requests.get')
    def test_fetch_titles_network_error(self, mock_get):
        """測試網路連線錯誤 - 應優雅處理"""
        mock_get.side_effect = requests.exceptions.ConnectionError("Connection Refused")
        
        # 修復後不應崩潰，而是返回 []
        titles = fetch_titles("http://down.com")
        assert titles == []

    # --- download_data tests ---

    @patch('time.sleep') # Mock sleep to speed up test
    @patch('requests.get')
    def test_download_data_basic(self, mock_get, mock_sleep):
        """測試批次下載"""
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.text = "data"
        mock_get.return_value = mock_response

        urls = ["http://a.com", "http://b.com"]
        results = download_data(urls)
        
        assert len(results) == 2
        assert results[0] == "data"
        assert mock_get.call_count == 2
        assert mock_sleep.call_count == 2 # 確保有呼叫 sleep (禮貌機制)
