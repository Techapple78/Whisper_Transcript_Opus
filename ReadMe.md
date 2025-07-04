# 🎙️ Whisper Transcription – Batch `.opus` to Text Converter

This project allows you to automatically transcribe all `.opus` files in a folder into `.txt` files using **OpenAI Whisper** with Python 3.10 on Windows.

---

## ✅ Prerequisites

### 🔐 Allow PowerShell scripts
```powershell
Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned
```

### 🎧 Install FFmpeg
1. Download and extract: [https://www.gyan.dev/ffmpeg/builds/](https://www.gyan.dev/ffmpeg/builds/)
2. Add FFmpeg to your system `PATH`:
```powershell
[Environment]::SetEnvironmentVariable("Path", $env:Path + ";C:\ffmpeg\ffmpeg-6.1.1-full_build\bin", "Machine")
```
> Example path: `C:\ffmpeg\ffmpeg-6.1.1-full_build\bin`

---

### 🐍 Install Python 3.10
Check installation:
```bash
py -3.10 --version
```

---

### 🧰 Install Git for Windows
- Download: [https://git-scm.com/download/win](https://git-scm.com/download/win)
- Ensure the **"Add Git to PATH"** option is selected
- Verify:
```bash
git --version
```

---

## 📦 Set up the virtual environment

```bash
py -3.10 -m venv venv
.\venv\Scripts\activate
```

---

## 🔧 Install dependencies

### 1. Install official Whisper from OpenAI
```bash
pip install git+https://github.com/openai/whisper.git
```

### 2. Install PyTorch:

#### If you have an Nvidia GPU:
```bash
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
```

#### If you **don’t have** an Nvidia GPU:
```bash
pip install torch torchvision torchaudio
```

---

## 🧪 Validate the installation

```bash
python -c "import whisper; print(whisper.__file__)"
```

> Expected result: `.../site-packages/whisper/__init__.py`

---

## 🚀 Launch the transcription

Place your `.opus` audio files into the `audios/` folder, then run:

```bash
python transcrire_opus.py
```

---

## 📁 Recommended project structure

```
whisper_transcription/
├── venv/                    # Python virtual environment
├── transcrire_opus.py       # Main script
└── audios/                  # Folder with audio files to transcribe
    ├── file1.opus
    ├── file2.opus
    └── ...
```
