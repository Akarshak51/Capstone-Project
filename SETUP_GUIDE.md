# SupportHub AI - Quick Setup & Commands Guide

## 📋 STEP-BY-STEP SETUP INSTRUCTIONS

### STEP 1: Create Project Directory

```bash
# Create folder for project
mkdir supporthub-ai
cd supporthub-ai
```

### STEP 2: Create Virtual Environment

**On Windows (PowerShell):**
```bash
python -m venv venv
venv\Scripts\Activate.ps1
```

**On Windows (Command Prompt):**
```bash
python -m venv venv
venv\Scripts\activate.bat
```

**On Mac/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### STEP 3: Set Environment Variables

**On Windows (PowerShell):**
```powershell
$env:GEMINI_API_KEY="AIzaSyDqAthpwhYNsaGIHvLiy7t6lfOngTMsa2A"
$env:GOOGLE_API_KEY="AIzaSyDqAthpwhYNsaGIHvLiy7t6lfOngTMsa2A"
```

**On Windows (Command Prompt):**
```cmd
set GEMINI_API_KEY=AIzaSyDqAthpwhYNsaGIHvLiy7t6lfOngTMsa2A
set GOOGLE_API_KEY=AIzaSyDqAthpwhYNsaGIHvLiy7t6lfOngTMsa2A
```

**On Mac/Linux:**
```bash
export GEMINI_API_KEY="AIzaSyDqAthpwhYNsaGIHvLiy7t6lfOngTMsa2A"
export GOOGLE_API_KEY="AIzaSyDqAthpwhYNsaGIHvLiy7t6lfOngTMsa2A"
```

### STEP 4: Install Dependencies

```bash
pip install -r requirements.txt
```

### STEP 5: Run the Agent

**Basic test:**
```bash
python agent.py
```

**Run with ADK Web UI (Interactive):**
```bash
pip install adk-webui
adk web
```

Then open: http://localhost:8000

## 🧪 RUNNING TESTS

```bash
# Install pytest if not already installed
pip install pytest pytest-asyncio

# Run integration tests
python -m pytest tests/test_agent.py -v

```

## 📂 Project File Structure

Create these files in your `supporthub-ai` folder:

```
supporthub-ai/
├── agent.py              ← Main agent code
├── config.py             ← Configuration & API key
├── evaluator.py          ← Testing framework
├── requirements.txt      ← Dependencies
├── .gitignore           ← Git ignore rules
├── README.md            ← Documentation
├── WRITEUP.md           ← Kaggle submission
├── LICENSE              ← Apache 2.0
└── tests/
    └── test_agent.py    ← Integration tests
```

## 📝 Creating Individual Files

### 1. Create config.py
```bash
# Copy the config.py content provided
```

### 2. Create requirements.txt
```bash
# Copy the requirements.txt content provided
```

### 3. Create agent.py
```bash
# Copy the agent.py content provided
```

## 🚀 GITHUB SETUP & DEPLOYMENT

### Initialize Git Repository

```bash
# Initialize git
git init

# Add all files
git add .

# Create first commit
git commit -m "Initial commit: SupportHub AI enterprise agent"

# Create GitHub repo (via github.com first, then):
git remote add origin https://github.com/YOUR_USERNAME/supporthub-ai.git

# Push to GitHub
git branch -M main
git push -u origin main
```

## 📤 KAGGLE SUBMISSION

1. **Go to:** https://www.kaggle.com/competitions/agents-intensive-capstone

2. **Click:** "Create Writeup"

3. **Fill in:**
   - **Title:** "SupportHub AI - Enterprise Customer Support Agent"
   - **Subtitle:** "Multi-Agent System for Intelligent Support Automation"
   - **Track:** Enterprise Agents
   - **Code:** Add GitHub repo URL
   - **Description:** Paste content from WRITEUP.md

4. **Submit before:** December 1, 2025, 11:59 AM PT

## ✅ VERIFICATION COMMANDS

Check if everything is set up correctly:

```bash
# Test Python installation
python --version  # Should be 3.11+

# Test virtual environment
which python  # (Mac/Linux) or where python (Windows)

# Test Gemini API key
echo $GEMINI_API_KEY  # Should show your API key

# Test imports
python -c "import google.generativeai; print('Gemini API OK')"
python -c "from google.adk.agents import LlmAgent; print('ADK OK')"
```

## 🐛 TROUBLESHOOTING

### Issue: "ModuleNotFoundError: No module named 'google'"
**Solution:**
```bash
pip install --upgrade google-generativeai google-adk
```

### Issue: "API key not found"
**Solution:** Make sure you set the environment variable:
```bash
# Check if set

echo $GEMINI_API_KEY  # Mac/Linux
echo %GEMINI_API_KEY%  # Windows
```

### Issue: "python: command not found"
**Solution:** Use `python3` instead of `python`:
```bash
python3 agent.py
python3 -m pip install -r requirements.txt
```

### Issue: Virtual environment not activating
**Solution:** Try again with explicit path:
```bash
# Windows
.\venv\Scripts\activate

# Mac/Linux
source ./venv/bin/activate
```

## 📞 QUICK REFERENCE

| Command | Purpose |
|---------|---------|
| `python agent.py` | Run agent |
| `adk web` | Launch web UI |
| `pip install -r requirements.txt` | Install dependencies |
| `git init` | Initialize git |
| `git commit -am "message"` | Commit changes |
| `git push origin main` | Push to GitHub |
| `python -m pytest tests/` | Run tests |

## 🎯 Final Submission Checklist

- [ ] All files created in project folder
- [ ] Virtual environment set up
- [ ] Dependencies installed
- [ ] Agent runs without errors
- [ ] Git repository initialized
- [ ] Files pushed to GitHub
- [ ] GitHub repo is PUBLIC
- [ ] Kaggle writeup created
- [ ] Code linked in Kaggle submission
- [ ] Submitted before deadline

---

**You're all set! Good luck with your submission! 🚀**
