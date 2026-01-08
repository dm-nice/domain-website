# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

DGtech is a hybrid project consisting of:
1. **Frontend**: A production corporate website (HTML5, Tailwind CSS, Vanilla JavaScript)
2. **Backend/Testing Lab**: Python-based testing framework for AI-driven DevSecOps

## Quick Development Commands

### Frontend (Website)

```bash
# Build CSS from Tailwind
npm run build:css

# Watch CSS for changes during development
npm run watch:css

# Preview website locally
python -m http.server 8000
# or
npx http-server

# Then open http://localhost:8000
```

### Backend (Testing)

```bash
# Run all tests
pytest test_lab/

# Run specific test file
pytest test_lab/test_math_tool.py

# Run tests in tests/ subdirectory
pytest test_lab/tests/

# Run with verbose output
pytest test_lab/ -v

# Run a specific test
pytest test_lab/test_math_tool.py::TestMathTool::test_divide_numbers_happy_path

# Run with performance benchmarks
pytest test_lab/tests/test_math_tool_extended.py -v
```

### Security & Code Review

```bash
# Bandit security scan (excludes test_lab)
bandit -r . --exclude ./test_lab

# Claude Code integrated review
/review-code
```

### Deployment

The project uses GitHub Actions (`.github/workflows/main.yml`) to automatically:
1. Run Bandit security scan
2. Deploy to GitHub Pages (gh-pages branch)

Trigger by pushing to `main` branch or manually via `workflow_dispatch`.

## Architecture Overview

### Frontend Structure

**Location**: `index.html` (single-page application)

**Key Sections** (in order):
1. **Navigation** - Fixed header with logo, menu links, responsive hamburger
2. **Hero** - Main tagline "引領科技，驅動未來", CTA buttons
3. **Services** - Three service cards (系統整合, 軟體開發, 技術諮詢)
4. **Trends Insights** - Video section with accordion UI
5. **About** - Company vision/mission with gradient background
6. **Contact** - Phone, email, address, hours with SVG icons
7. **Footer** - Logo and copyright

**Styling**:
- Tailwind CSS configured in `<head>` with inline config
- Primary color: `#1e3a8a` (deep blue)
- Secondary color: `#3b82f6` (bright blue)
- Uses gradient: 135° from primary to secondary
- Responsive breakpoint at `md` (768px)

**Interactive Features**:
- Smooth scrolling navigation
- Mobile hamburger menu (auto-closes on link click)
- Card hover effects (scale/shadow)
- Gradient button transitions
- Floating animations on service cards

### Backend Structure

**Location**: `test_lab/` directory

**Core Modules**:
- `math_tool.py` - Mathematical utilities with error handling
- `web_crawler.py` - HTTP request utilities with rate limiting
- `todo_list.py` - Task management module

**Test Organization**:
- `test_math_tool.py` - Unit tests for math functions
- `tests/test_math_tool_extended.py` - Performance benchmarks and security tests
- `tests/test_web_crawler.py` - Web crawler tests with mocking

**Key Testing Patterns**:
- Class-based organization (e.g., `TestMathTool`)
- Exception testing with `pytest.raises()`
- Mocking external dependencies (`unittest.mock`)
- Performance assertions (`@pytest.mark.benchmark`)
- Security tests for command injection

### Python Testing Architecture

**Test Coverage Areas**:
1. **Unit Tests** - Happy path, edge cases, type errors
2. **Error Handling** - ZeroDivisionError, TypeError, HTTPError, network timeouts
3. **Performance** - Fibonacci benchmarks with timing assertions
4. **Security** - Command injection validation via `shlex.quote()`
5. **Mocking** - External HTTP calls, file operations

**Testing Best Practices in Codebase**:
- Empty list handling returns 0 instead of crashing
- HTTP errors return empty list instead of raising
- Network timeouts gracefully handled
- Rate limiting enforced (1s sleep between requests)

## Build & CSS

**Tailwind CSS Setup**:
- Source: `src/input.css`
- Output: `dist/output.css`
- Also uses CDN in `index.html` for instant preview
- Build tool: PostCSS + Autoprefixer

**Color Customization**:
Edit `tailwind.config.js` (or inline config in `index.html`):
```javascript
colors: {
  primary: '#1e3a8a',    // Deep blue
  secondary: '#3b82f6',  // Bright blue
}
```

## Deployment

**Primary**: GitHub Pages (`gh-pages` branch)
- Auto-deployed via GitHub Actions when pushing to `main`
- Deploys entire repository root (`.`)
- Access: https://dm-nice.github.io/domain-website/

**Alternative Methods**:
- Direct file: `index.html` (double-click or drag to browser)
- Local server: `python -m http.server 8000`
- Static hosting: Netlify, Vercel, or traditional FTP

## Browser Support

- Chrome 90+
- Firefox 88+
- Safari 14+
- Edge 90+
- Mobile browsers (iOS Safari, Chrome Mobile)

## AI-Driven DevSecOps Integration

This project uses Claude Code for automated testing and code review:
- `/review-code` - Analyzes Clean Code principles and architecture
- `/project-tester` - Multi-stage testing: generation, benchmarking, security scanning, auto-repair

The CI/CD pipeline in `.github/workflows/main.yml` runs Bandit security scanning automatically.

## Important Files

- `index.html` - Main website (production deliverable)
- `package.json` - Frontend dependencies and build scripts
- `tailwind.config.js` - Tailwind CSS configuration
- `.github/workflows/main.yml` - GitHub Actions CI/CD pipeline
- `test_lab/` - Python testing framework
- `dist/output.css` - Compiled Tailwind CSS (18KB)
