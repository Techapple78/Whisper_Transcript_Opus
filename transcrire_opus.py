import whisper
import os

# === CONFIGURATION ===
DOSSIER_AUDIO = "audios"  # Nom du dossier contenant les fichiers .opus
LANGUE = "fr"             # Langue cible (français)

# === INITIALISATION ===
model = whisper.load_model("large")  # Tu peux aussi tester "small", "large", etc.

# === TRAITEMENT ===
for filename in os.listdir(DOSSIER_AUDIO):
    if filename.lower().endswith(".opus"):
        chemin_fichier = os.path.join(DOSSIER_AUDIO, filename)
        print(f"Transcription de : {filename}...")

        result = model.transcribe(chemin_fichier, language=LANGUE)
        
        # Enregistre la transcription dans un fichier .txt
        nom_txt = os.path.splitext(filename)[0] + ".txt"
        with open(os.path.join(DOSSIER_AUDIO, nom_txt), "w", encoding="utf-8") as f:
            f.write(result["text"])

        print(f"✅ Transcription sauvegardée : {nom_txt}")