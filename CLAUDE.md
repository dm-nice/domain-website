# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## 專案概述 (Project Overview)

DGtech 是一個混合型專案,包含:
1. **前端網站 (Frontend)**: 企業形象網站 (HTML5, Tailwind CSS, Vanilla JavaScript)
2. **測試實驗室 (Backend/Testing Lab)**: Python 測試框架,用於 AI 驅動的 DevSecOps

### 專案類型
- **形象網站**: 單頁式應用程式 (SPA)
- **技術棧**: 現代化前端 + Python 測試自動化
- **部署**: GitHub Pages (自動化 CI/CD)
- **開發模式**: AI 輔助開發與測試

## 快速開發指令 (Quick Development Commands)

### 前端開發 (Frontend Development)

```bash
# 從 Tailwind 建置 CSS
npm run build:css

# 監看 CSS 變更 (開發模式)
npm run watch:css

# 本地預覽網站
python -m http.server 8000
# 或使用
npx http-server

# 然後在瀏覽器開啟
# http://localhost:8000
```

**重要提醒**: 專案使用雙重 CSS 策略
- **CDN 模式**: `index.html` 內嵌 Tailwind CDN (適合快速預覽)
- **建置模式**: `dist/output.css` (18KB, 適合正式部署)

### 後端測試 (Backend Testing)

```bash
# 執行所有測試
pytest test_lab/

# 執行特定測試檔案
pytest test_lab/test_math_tool.py

# 執行 tests/ 子目錄測試
pytest test_lab/tests/

# 詳細輸出模式
pytest test_lab/ -v

# 執行特定測試案例
pytest test_lab/test_math_tool.py::TestMathTool::test_divide_numbers_happy_path

# 執行效能基準測試
pytest test_lab/tests/test_math_tool_extended.py -v
```

**測試檔案結構**:
```
test_lab/
├── math_tool.py                    # 數學工具模組
├── web_crawler.py                  # 網路爬蟲工具
├── todo_list.py                    # 待辦事項管理
├── test_math_tool.py              # 單元測試
├── test_suites.py                 # 測試套件
└── tests/
    ├── test_math_tool_extended.py # 進階測試 + 效能基準
    └── test_web_crawler.py        # 爬蟲測試 (含 Mock)
```

### 安全掃描與代碼審查 (Security & Code Review)

```bash
# Bandit 安全掃描 (排除 test_lab)
bandit -r . --exclude ./test_lab

# Claude Code 整合式審查
/review-code
```

### 部署 (Deployment)

專案使用 GitHub Actions (`.github/workflows/main.yml`) 自動執行:
1. Python 環境設置 (Python 3.9)
2. Bandit 安全掃描
3. 部署至 GitHub Pages (gh-pages 分支)

**觸發方式**:
- 自動: 推送至 `main` 或 `master` 分支
- 手動: GitHub Actions 頁面點擊 `workflow_dispatch` 按鈕

**部署 URL**: https://dm-nice.github.io/domain-website/

## 架構概覽 (Architecture Overview)

### 前端結構 (Frontend Structure)

**檔案位置**: `index.html` (單頁式應用程式)

**頁面區塊** (依序):
1. **導覽列 (Navigation)** - 固定頂部標頭,Logo、選單連結、響應式漢堡選單
2. **主視覺 (Hero)** - 主標語「引領科技,驅動未來」、CTA 按鈕
3. **服務項目 (Services)** - 三個服務卡片 (系統整合、軟體開發、技術諮詢)
4. **趨勢洞察 (Trends Insights)** - 影片區塊 + 手風琴式 UI (可展開/收合)
5. **關於我們 (About)** - 公司願景/使命 + 漸層背景
6. **聯絡我們 (Contact)** - 電話、Email、地址、營業時間 + SVG 圖標
7. **頁腳 (Footer)** - Logo 與版權宣告

**樣式設計**:
- Tailwind CSS 配置於 `<head>` 內嵌設定
- 主色調: `#1e3a8a` (深藍色)
- 次色調: `#3b82f6` (亮藍色)
- 漸層效果: 135° 從主色到次色
- 響應式斷點: `md` (768px)

**互動功能**:
- 平滑滾動導覽
- 手機版漢堡選單 (點擊連結自動關閉)
- 卡片懸停效果 (縮放/陰影)
- 漸層按鈕過渡動畫
- 服務卡片浮動動畫
- 影片區塊摺疊/展開效果 (max-height transition)

**SEO 優化**:
- Meta description 與 keywords
- Open Graph 標籤 (社群分享優化)
- 語義化 HTML5 標籤
- 無障礙 ARIA 屬性

### 後端結構 (Backend Structure)

**檔案位置**: `test_lab/` 目錄

**核心模組**:
- `math_tool.py` - 數學工具函式 (含錯誤處理)
- `web_crawler.py` - HTTP 請求工具 (含速率限制)
- `todo_list.py` - 待辦事項管理模組
- `bad_math.py` - 負面測試案例 (已知錯誤代碼)
- `math_tool_ERROR_TEST.py` - 錯誤測試腳本

**測試組織架構**:
- `test_math_tool.py` - 數學函式單元測試
- `test_suites.py` - 測試套件整合
- `tests/test_math_tool_extended.py` - 效能基準測試 + 安全性測試
- `tests/test_web_crawler.py` - 爬蟲測試 (使用 Mock)

**測試模式**:
- 類別導向組織 (例: `TestMathTool`)
- 例外測試 (使用 `pytest.raises()`)
- 外部相依性模擬 (`unittest.mock`)
- 效能斷言 (`@pytest.mark.benchmark`)
- 安全性測試 (指令注入防護)

### Python 測試架構 (Python Testing Architecture)

**測試覆蓋範圍**:
1. **單元測試 (Unit Tests)** - 正常路徑、邊界案例、類型錯誤
2. **錯誤處理 (Error Handling)** - ZeroDivisionError, TypeError, HTTPError, 網路逾時
3. **效能測試 (Performance)** - Fibonacci 基準測試 + 時間斷言
4. **安全性 (Security)** - 指令注入驗證 (透過 `shlex.quote()`)
5. **模擬測試 (Mocking)** - 外部 HTTP 呼叫、檔案操作

**測試最佳實踐**:
- 空列表處理回傳 0 (避免崩潰)
- HTTP 錯誤回傳空列表 (避免例外拋出)
- 網路逾時優雅處理
- 速率限制強制執行 (請求間隔 1 秒)
- 防禦性程式設計 (Defensive Programming)

## 建置與 CSS (Build & CSS)

**Tailwind CSS 配置**:
- 來源檔: `src/input.css`
- 輸出檔: `dist/output.css` (18KB, 已編譯)
- CDN 模式: `index.html` 內嵌 Tailwind CDN (快速預覽)
- 建置工具: PostCSS + Autoprefixer
- 配置檔: `tailwind.config.js`

**雙重 CSS 策略**:
1. **開發模式**: 使用 CDN (即時預覽,無需建置)
2. **正式部署**: 使用編譯後的 `dist/output.css` (效能最佳)

**顏色客製化**:
編輯 `tailwind.config.js` (或 `index.html` 的內嵌配置):
```javascript
colors: {
  primary: '#1e3a8a',    // 主色 - 深藍色
  secondary: '#3b82f6',  // 次色 - 亮藍色
}
```

**自訂樣式**:
`src/input.css` 包含:
- Tailwind 基礎層 (`@tailwind base`)
- 自訂漸層背景類別 (`.gradient-bg`)
- 無障礙焦點樣式 (`:focus-visible`)
- 平滑滾動 (`scroll-behavior: smooth`)

## 部署方式 (Deployment)

**主要部署**: GitHub Pages (`gh-pages` 分支)
- 推送至 `main` 分支時自動部署 (透過 GitHub Actions)
- 部署整個根目錄 (`.`)
- 訪問網址: https://dm-nice.github.io/domain-website/

**GitHub Actions 工作流程** (`.github/workflows/main.yml`):
1. Checkout 代碼
2. 設置 Python 3.9 環境
3. 安裝 Bandit 安全掃描工具
4. 執行基礎安全檢查 (`bandit -r . -x ./test_lab`)
5. 部署至 GitHub Pages (使用 JamesIves/github-pages-deploy-action@v4)

**替代部署方式**:
- **直接開啟**: `index.html` (雙擊或拖曳至瀏覽器)
- **本地伺服器**: `python -m http.server 8000` 或 `npx http-server`
- **靜態主機**: Netlify, Vercel, Cloudflare Pages
- **傳統主機**: FTP 上傳至網站根目錄

**手動觸發部署**:
- GitHub 專案頁面 → Actions → Website Update & Deploy → Run workflow

## 瀏覽器支援 (Browser Support)

- ✅ Chrome 90+
- ✅ Firefox 88+
- ✅ Safari 14+
- ✅ Edge 90+
- ✅ 行動瀏覽器 (iOS Safari, Chrome Mobile)
- ✅ 響應式設計 (手機、平板、桌機)

## AI 驅動的 DevSecOps 整合 (AI-Driven DevSecOps Integration)

本專案使用 Claude Code 進行自動化測試與代碼審查:

### 核心指令
- **`/review-code`** - 分析 Clean Code 原則與架構設計
- **`/project-tester`** - 多階段測試流程:
  - 測試生成 (Test Generation)
  - 基準測試 (Benchmarking)
  - 安全掃描 (Security Scanning)
  - 自動修復 (Auto-Repair)

### CI/CD 管道
`.github/workflows/main.yml` 自動執行:
- ✅ Bandit 安全漏洞掃描
- ✅ 代碼檢查 (Python 3.9)
- ✅ 自動部署至 GitHub Pages

### 安全特性
- 指令注入防護 (`shlex.quote()`)
- 輸入驗證與錯誤處理
- 速率限制 (Rate Limiting)
- 防禦性程式設計

## 重要檔案 (Important Files)

### 前端檔案
- `index.html` - 主要網站 (正式交付檔案)
- `index_bak.html` - 備份檔案
- `package.json` - 前端相依套件與建置腳本
- `package-lock.json` - 相依套件版本鎖定
- `tailwind.config.js` - Tailwind CSS 配置
- `src/input.css` - 自訂 CSS 來源檔
- `dist/output.css` - 編譯後的 CSS (18KB)

### 後端測試檔案
- `test_lab/` - Python 測試框架目錄
  - `math_tool.py` - 數學工具模組
  - `web_crawler.py` - 網路爬蟲模組
  - `todo_list.py` - 待辦事項模組
  - `test_*.py` - 測試檔案

### 配置與部署
- `.github/workflows/main.yml` - GitHub Actions CI/CD 管道
- `.claude/` - Claude Code 設定目錄
- `.agent/workflows/` - AI Agent 工作流程定義
- `README.md` - 專案說明文件
- `CLAUDE.md` - Claude Code 使用指南 (本檔案)

### Python 環境
- `venv32/` - Python 虛擬環境目錄
- `requirements.txt` - Python 相依套件清單 (如有)

## 專案檔案結構 (Project File Structure)

```
DGtech/
├── .agent/                      # AI Agent 工作流程定義
│   └── workflows/
│       ├── review-code.md      # 代碼審查工作流程
│       ├── project-tester.md   # 專案測試工作流程
│       └── final-check.md      # 最終檢查工作流程
├── .claude/                     # Claude Code 配置
│   ├── skills/                 # 自訂技能
│   │   └── review-code/       # 代碼審查技能
│   └── settings.local.json    # 本地設定
├── .github/
│   └── workflows/
│       └── main.yml           # GitHub Actions CI/CD
├── .vscode/                    # VS Code 配置
│   └── settings.json
├── dist/                       # 建置輸出
│   └── output.css             # 編譯後的 Tailwind CSS
├── node_modules/               # Node.js 相依套件
├── src/                        # 來源檔案
│   └── input.css              # Tailwind CSS 來源
├── test_lab/                   # Python 測試實驗室
│   ├── tests/                 # 進階測試
│   ├── math_tool.py
│   ├── web_crawler.py
│   ├── todo_list.py
│   └── test_*.py
├── venv32/                     # Python 虛擬環境
├── index.html                  # 主要網站檔案 ⭐
├── index_bak.html             # 備份檔案
├── package.json               # NPM 配置
├── tailwind.config.js         # Tailwind 配置
├── README.md                  # 專案說明
└── CLAUDE.md                  # 本檔案
```

## 開發工作流程 (Development Workflow)

### 1. 前端開發流程
```bash
# 1. 安裝相依套件 (首次)
npm install

# 2. 啟動 CSS 監看模式
npm run watch:css

# 3. 啟動本地伺服器
python -m http.server 8000

# 4. 在瀏覽器開啟
# http://localhost:8000

# 5. 編輯 index.html
# → Tailwind CSS 自動重新編譯
# → 瀏覽器手動重新整理查看變更
```

### 2. 測試開發流程
```bash
# 1. 啟動虛擬環境 (Windows)
venv32\Scripts\activate

# 2. 安裝測試相依套件
pip install pytest

# 3. 執行測試
pytest test_lab/ -v

# 4. 執行安全掃描
bandit -r . --exclude ./test_lab
```

### 3. 部署流程
```bash
# 1. 確認所有測試通過
pytest test_lab/

# 2. 建置 CSS (可選)
npm run build:css

# 3. 提交變更
git add .
git commit -m "描述變更內容"

# 4. 推送至 GitHub (自動觸發部署)
git push origin main

# 5. 檢查 GitHub Actions 狀態
# https://github.com/dm-nice/domain-website/actions
```

## 常見任務 (Common Tasks)

### 更新網站內容
1. 編輯 `index.html` 中的文字內容
2. 儲存檔案
3. 在瀏覽器中重新整理查看變更
4. 推送至 GitHub 自動部署

### 修改顏色配置
1. 編輯 `tailwind.config.js` 中的 `colors` 物件
2. 或編輯 `index.html` 中的內嵌 Tailwind 配置
3. 執行 `npm run build:css` 重新建置
4. 重新整理瀏覽器查看變更

### 新增服務卡片
1. 在 `index.html` 中找到 `<section id="services">` 區塊
2. 複製現有的服務卡片 HTML 結構
3. 修改圖標、標題與描述
4. 儲存並重新整理瀏覽器

### 新增測試案例
1. 在 `test_lab/` 目錄建立新的測試檔案
2. 遵循現有的測試模式 (類別導向組織)
3. 執行 `pytest test_lab/ -v` 驗證測試
4. 提交至 GitHub (CI 會自動執行測試)

## 疑難排解 (Troubleshooting)

### CSS 沒有更新
```bash
# 方案 1: 重新建置 CSS
npm run build:css

# 方案 2: 清除瀏覽器快取
# Ctrl+Shift+R (Windows) 或 Cmd+Shift+R (Mac)

# 方案 3: 檢查 Tailwind 配置
# 確認 tailwind.config.js 中的 content 路徑正確
```

### 本地伺服器無法啟動
```bash
# 方案 1: 檢查埠號是否被佔用
netstat -ano | findstr :8000  # Windows
lsof -i :8000                 # Mac/Linux

# 方案 2: 使用其他埠號
python -m http.server 8001

# 方案 3: 使用 npx http-server
npx http-server -p 8000
```

### 測試失敗
```bash
# 方案 1: 檢查虛擬環境是否啟動
# 終端機提示符應顯示 (venv32)

# 方案 2: 重新安裝相依套件
pip install --upgrade pytest

# 方案 3: 執行詳細模式查看錯誤
pytest test_lab/ -v --tb=short
```

### GitHub Actions 部署失敗
1. 前往 GitHub 專案頁面
2. 點擊 "Actions" 標籤
3. 查看失敗的工作流程日誌
4. 常見問題:
   - 權限不足: 檢查 Repository Settings → Actions → General
   - Bandit 錯誤: 檢查代碼是否有安全漏洞
   - 建置失敗: 檢查 `main.yml` 配置

## 效能優化建議 (Performance Optimization)

### 前端優化
- ✅ 使用編譯後的 CSS (而非 CDN) 於正式環境
- ✅ SVG 圖標直接內嵌 (減少 HTTP 請求)
- ✅ 單一 HTML 檔案設計 (快速載入)
- ✅ 最小化 JavaScript 使用
- 🔄 考慮添加圖片壓縮 (如使用圖片)
- 🔄 考慮添加 Service Worker (PWA)

### 後端優化
- ✅ 速率限制 (Rate Limiting)
- ✅ 錯誤處理與防禦性程式設計
- ✅ 單元測試覆蓋率
- 🔄 考慮添加快取機制
- 🔄 考慮添加日誌記錄

## 安全性檢查清單 (Security Checklist)

- ✅ Bandit 安全掃描通過
- ✅ 指令注入防護 (`shlex.quote()`)
- ✅ 輸入驗證與錯誤處理
- ✅ HTTPS 部署 (GitHub Pages 預設)
- ✅ 無敏感資訊外洩
- ✅ 相依套件安全性檢查
- 🔄 考慮添加 CSP (Content Security Policy)
- 🔄 考慮添加 CORS 配置

## 版本歷史 (Version History)

- **v1.0.0** (2026-01-02) - 初始版本發布
  - 完整的企業形象網站
  - Python 測試框架整合
  - GitHub Actions CI/CD 自動化
  - Claude Code 整合

## 貢獻指南 (Contributing)

1. Fork 本專案
2. 建立功能分支 (`git checkout -b feature/AmazingFeature`)
3. 提交變更 (`git commit -m 'Add some AmazingFeature'`)
4. 推送至分支 (`git push origin feature/AmazingFeature`)
5. 開啟 Pull Request

## 授權資訊 (License)

© 2026 DGtech. All rights reserved.

---

**最後更新**: 2026-01-14
**文件版本**: 2.0
**維護者**: Claude Code
**狀態**: ✅ 正式版本
