# 🎙️ Whisper Transcription - Batch de fichiers .opus vers texte

Ce projet permet de transcrire automatiquement tous les fichiers `.opus` d’un dossier en fichiers `.txt` (ou plus), en utilisant **Whisper d’OpenAI** via Python 3.10 sur Windows.

---

## ✅ Prérequis

### 🔐 Autoriser les scripts PowerShell
```powershell
Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned
```

### 🎧 Installer FFmpeg
1. Télécharger et extraire : [https://www.gyan.dev/ffmpeg/builds/](https://www.gyan.dev/ffmpeg/builds/)
2. Ajouter FFmpeg au `PATH` :
```powershell
[Environment]::SetEnvironmentVariable("Path", $env:Path + ";C:\ffmpeg\ffmpeg-6.1.1-full_build\bin", "Machine")
```
> Exemple de chemin : `C:\ffmpeg\ffmpeg-6.1.1-full_build\bin`

---

### 🐍 Installer Python 3.10
Vérifier :
```bash
py -3.10 --version
```

---

### 🧰 Installer Git pour Windows
- Télécharger : [https://git-scm.com/download/win](https://git-scm.com/download/win)
- Cocher l’option **"Add Git to PATH"**
- Vérifier :
```bash
git --version
```

---

## 📦 Installation de l’environnement virtuel

```bash
py -3.10 -m venv venv
.\venv\Scripts\activate
```

---

## 🔧 Installation des dépendances

### 1. Installer Whisper officiel
```bash
pip install git+https://github.com/openai/whisper.git
```

### 2. Installer PyTorch :

#### Si vous avez un GPU Nvidia :
```bash
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
```

#### Si vous **n’avez pas** de GPU Nvidia :
```bash
pip install torch torchvision torchaudio
```

---

## 🧪 Vérification de Whisper

```bash
python -c "import whisper; print(whisper.__file__)"
```

> Résultat attendu : `.../site-packages/whisper/__init__.py`

---

## 🚀 Lancer la transcription

Placez vos fichiers `.opus` dans le dossier `audios/`, puis lancez :

```bash
python transcrire_opus.py
```

---

## 📁 Structure recommandée du projet

```
whisper_transcription/
├── venv/                    # Environnement Python
├── transcrire_opus.py       # Script principal
└── audios/                  # Dossier contenant les fichiers à transcrire
    ├── fichier1.opus
    ├── fichier2.opus
    └── ...
```

---