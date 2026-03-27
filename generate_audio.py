import os
from pathlib import Path

# Create audio directory if it doesn't exist
audio_dir = Path("audio")
audio_dir.mkdir(exist_ok=True)

# Pa'O alphabet list (က to အံ)
pao_alphabets = [
    "က", "ခ", "ဂ", "ဃ", "င",
    "စ", "ဆ", "ည", "ဇ", "ဈ",
    "ည", "ဋ", "ဌ", "ဍ", "ဎ",
    "ဏ", "ပ", "ဖ", "ဗ", "ဘ",
    "မ", "ယ", "ရ", "လ", "ဝ",
    "သ", "ဟ", "ဠ", "အ", "ာ",
    "ိ", "ီ", "ု", "ူ", "ေ",
    "ဲ", "ံ"
]

# Create placeholder audio files with metadata
for i, letter in enumerate(pao_alphabets):
    filename = f"audio/pao_{i:02d}_{letter}.txt"
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(f"Placeholder for audio: {letter}\n")
        f.write(f"Index: {i}\n")
        f.write(f"Note: Replace with actual MP3 audio file\n")

print(f"Created {len(pao_alphabets)} audio placeholder files")
