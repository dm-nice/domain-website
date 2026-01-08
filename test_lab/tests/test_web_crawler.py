import pytest
from unittest.mock import patch, Mock
import requests
import sys
import os

# Add local directory to path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from web_crawler import fetch_titles, download_data

class TestWebCrawler:

    @patch('requests.get')
    def test_fetch_titles_success(self, mock_get):
        """測試成功抓取並解析 H1 標題"""
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.text = "<html><body><h1> Title 1 </h1><h1>Title 2</h1></body></html>"
        mock_get.return_value = mock_response

        titles = fetch_titles("http://example.com")

        assert titles == ["Title 1", "Title 2"]

        # 驗證請求包含必要的反爬蟲機制（User-Agent）和超時設定
        args, kwargs = mock_get.call_args
        assert "User-Agent" in kwargs['headers']
        assert kwargs['timeout'] == 10

    @patch('requests.get')
    def test_fetch_titles_404(self, mock_get):
        """驗證 404 錯誤時返回空列表而非拋出異常（防禦性編程）"""
        mock_response = Mock()
        mock_response.status_code = 404
        mock_response.raise_for_status.side_effect = requests.exceptions.HTTPError("404 Client Error")
        mock_get.return_value = mock_response

        titles = fetch_titles("http://example.com/404")

        assert titles == []

    @patch('requests.get')
    def test_fetch_titles_network_error(self, mock_get):
        """驗證網路連線錯誤時返回空列表而非拋出異常（容錯性）"""
        mock_get.side_effect = requests.exceptions.ConnectionError("Connection Refused")

        titles = fetch_titles("http://down.com")
        assert titles == []

    @patch('time.sleep')
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
        # 驗證禮貌性延遲機制（避免被反爬蟲系統封鎖）
        assert mock_sleep.call_count == 2
