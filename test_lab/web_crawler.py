import requests
from bs4 import BeautifulSoup
import time
from typing import List, Optional

# 設定 User-Agent 避免被擋
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

def fetch_titles(url: str) -> List[str]:
    """
    抓取指定網頁的所有 <h1> 標題。
    具備錯誤處理與 User-Agent 設定。
    """
    try:
        # 設定 timeout 避免無限等待
        response = requests.get(url, headers=HEADERS, timeout=10)
        response.raise_for_status() # 檢查 4xx/5xx錯誤
        
        soup = BeautifulSoup(response.text, 'html.parser')
        titles = [t.get_text().strip() for t in soup.find_all('h1')]
        return titles
        
    except requests.exceptions.RequestException as e:
        print(f"Error fetching {url}: {e}")
        return []

def download_data(urls: List[str]) -> List[Optional[str]]:
    """
    批次下載資料。
    包含延遲機制(Rate Limiting)以避免被封鎖。
    """
    results = []
    for url in urls:
        try:
            # 禮貌性延遲
            time.sleep(1) 
            
            res = requests.get(url, headers=HEADERS, timeout=10)
            res.raise_for_status()
            results.append(res.text)
            
        except requests.exceptions.RequestException as e:
            print(f"Error downloading {url}: {e}")
            results.append(None) # 標記失敗
            
    return results