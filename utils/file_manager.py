from pathlib import Path
import shutil


def clean_directory(path):
    folder = Path(path)

    if folder.exists():
        shutil.rmtree(folder)

    folder.mkdir(parents=True, exist_ok=True)