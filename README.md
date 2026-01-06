# DGtech 公司形象網站

> 引領科技，驅動未來

## 專案簡介

DGtech.com.tw 的官方公司形象網站，採用現代化的單頁式設計（Single Page Application），展示公司的核心服務、企業願景與聯絡資訊。

## 技術架構

- **HTML5** - 語義化標籤結構
- **Tailwind CSS** - 現代化 CSS 框架（CDN）
- **Vanilla JavaScript** - 輕量互動功能
- **SVG Icons** - 向量圖標（Lucide 風格）

## 設計特色

### 視覺風格
- 🎨 深藍與白色專業配色方案
- 💎 簡潔大氣的現代設計
- 🌊 漸層背景增添科技感
- ✨ 流暢的動畫與過渡效果

### 響應式設計
- 📱 完美支援手機裝置
- 📲 平板最佳化顯示
- 💻 桌面版完整體驗
- 🔄 自適應導覽選單

## 網站架構

```
├── 頂部導覽列
│   ├── Logo
│   └── 導覽選單（產品服務、關於我們、聯絡我們）
│
├── Hero 主視覺區
│   ├── 主標語：引領科技，驅動未來
│   └── CTA 按鈕（了解服務、立即諮詢）
│
├── 核心服務區塊
│   ├── 系統整合
│   ├── 軟體開發
│   └── 技術諮詢
│
├── 關於我們
│   └── 公司願景與使命
│
├── 聯絡我們
│   ├── 電話
│   ├── 電子郵件
│   ├── 地址
│   └── 營業時間
│
└── 頁腳
    ├── Logo
    └── 版權宣告
```

## 核心功能

### 導覽功能
- 固定式頂部導覽列
- 平滑滾動至指定區塊
- 響應式行動選單
- 點擊連結自動關閉選單

### 互動效果
- 卡片懸停放大效果
- 按鈕顏色漸變過渡
- 服務卡片向上浮動動畫
- 連結懸停狀態變化

### 區塊設計
- **服務卡片**：圖標 + 標題 + 描述
- **關於區塊**：漸層背景 + 多段落內容
- **聯絡資訊**：圖標式資訊展示
- **CTA 按鈕**：雙重行動呼籲設計

## 快速開始

### 預覽網站

1. 直接開啟檔案：
   ```bash
   # Windows
   start index.html

   # macOS
   open index.html

   # Linux
   xdg-open index.html
   ```

2. 或使用本地伺服器：
   ```bash
   # Python 3
   python -m http.server 8000

   # Node.js (http-server)
   npx http-server
   ```

3. 瀏覽器訪問：
   ```
   http://localhost:8000
   ```

## 自訂設定

### 修改配色

在 `<head>` 區塊中找到 Tailwind 配置：

```javascript
tailwind.config = {
    theme: {
        extend: {
            colors: {
                primary: '#1e3a8a',    // 主要深藍色
                secondary: '#3b82f6',  // 次要藍色
            }
        }
    }
}
```

### 更新內容

- **公司資訊**：修改頁腳與 Hero 區的文字
- **服務項目**：編輯服務卡片內的標題與描述
- **聯絡方式**：更新聯絡我們區塊的資訊
- **願景描述**：調整關於我們的段落內容

## 瀏覽器支援

- ✅ Chrome 90+
- ✅ Firefox 88+
- ✅ Safari 14+
- ✅ Edge 90+
- ✅ 主流行動瀏覽器

## 檔案結構

```
DGtech/
├── index.html          # 主要網頁檔案
└── README.md          # 專案說明文件
```

## 效能優化

- 使用 CDN 載入 Tailwind CSS
- SVG 圖標直接內嵌，減少請求
- 單一 HTML 檔案，載入速度快
- 最小化 JavaScript 使用

## 部署建議

### GitHub Pages
```bash
git init
git add .
git commit -m "Initial commit"
git branch -M main
git remote add origin https://github.com/yourusername/dgtech.git
git push -u origin main
```

在 GitHub 專案設定中啟用 GitHub Pages。

### Netlify / Vercel
直接拖曳 `index.html` 到部署區域即可。

### 傳統主機
使用 FTP 上傳 `index.html` 到網站根目錄。

## 維護說明

- 定期更新聯絡資訊
- 檢查外部 CDN 連結有效性
- 測試各裝置與瀏覽器相容性
- 根據需求更新服務內容

## 授權資訊

© 2026 DGtech. All rights reserved.

---

**開發時間**：2026-01-02
**版本**：1.0.0
**狀態**：✅ 已完成

==========================================================================

---

## 🤖 AI 自動化開發與測試體系 (AI-Driven DevSecOps)

本專案整合了基於 Claude Code 的自動化工作流，實現了從代碼編寫到安全發佈的全自動化守護。

### 🛠️ 核心自動化指令
您可以透過支援 Claude Code 的終端機執行以下專屬指令：

* **`/review-code`**: 啟動全域代碼審查，檢查 Clean Code 規範與邏輯優化。
* **`/project-tester`**: 執行企業級測試工作流，包含以下階段：
    * **智慧測試生成**: 自動識別技術棧並生成覆蓋邊界案例的測試腳本。
    * **效能基準測試 (Benchmark)**: 監控核心演算法效率，防止效能退步。
    * **安全性掃描**: 自動偵測指令注入 (Command Injection) 等漏洞並建議修補方案。
    * **自動修復閉環**: 針對測試失敗或安全漏洞進行自動診斷與代碼修復。

### 🛡️ 安全與效能保證
* **指令安全**: 透過 `shlex.quote` 確保所有系統呼叫均經過安全轉義。
* **防護機制**: 已針對空列表 (ZeroDivisionError) 與無效輸入建立防禦性邏輯。

### ⚙️ CI/CD 整合
本專案已配置 **GitHub Actions (`main.yml`)**，每當代碼 Push 至 GitHub 時，將自動觸發：
1.  **Pytest** 邏輯驗證。
2.  **Bandit** 安全漏洞掃描。
3.  **Benchmark** 效能數據記錄。

---





