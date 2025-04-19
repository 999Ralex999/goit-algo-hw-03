import argparse
import shutil
from pathlib import Path


def get_unique_destination(file_path: Path) -> Path:

    counter = 1
    new_path = file_path
    while new_path.exists():
        new_path = file_path.with_name(f"{file_path.stem}_copy{counter}{file_path.suffix}")
        counter += 1
    return new_path


def create_extension_folder(base_folder: Path, extension: str) -> Path:

    folder = base_folder / extension
    folder.mkdir(parents=True, exist_ok=True)
    return folder


def copy_and_sort_files(source_folder: Path, destination_folder: Path):

    if not source_folder.exists() or not source_folder.is_dir():
        print(f"❌ Папка {source_folder} не існує або не є директорією.")
        return

    files_processed = 0
    skipped_hidden = 0
    dirs_processed = 0

    for item in source_folder.rglob("*"):
        if item.is_dir():
            dirs_processed += 1
            continue
        if item.name.startswith('.'):
            skipped_hidden += 1
            continue
        if item.is_file():
            extension = item.suffix[1:].lower() if item.suffix else 'no_extension'
            target_dir = create_extension_folder(destination_folder, extension)
            destination_file = get_unique_destination(target_dir / item.name)
            try:
                shutil.copy2(item, destination_file)
                print(f"✅ {item.name} → {destination_file.relative_to(destination_folder)}")
                files_processed += 1
            except Exception as e:
                print(f"⚠️ Не вдалося скопіювати {item}: {e}")

    print("\n📊 Звіт:")
    print(f"📁 Опрацьовано директорій: {dirs_processed}")
    print(f"📄 Скопійовано файлів: {files_processed}")
    print(f"🙈 Пропущено прихованих файлів: {skipped_hidden}")


def main():
    parser = argparse.ArgumentParser(description="Рекурсивне копіювання та сортування файлів за розширенням")
    parser.add_argument("source", help="Шлях до вихідної директорії")
    parser.add_argument("destination", nargs="?", default="dist", help="Шлях до директорії призначення (default: dist)")
    args = parser.parse_args()

    source_path = Path(args.source)
    destination_path = Path(args.destination)

    destination_path.mkdir(parents=True, exist_ok=True)
    print(f"🚀 Починаємо сортування з {source_path} до {destination_path}...\n")
    copy_and_sort_files(source_path, destination_path)
    print("\n✅ Сортування завершено.")


if __name__ == "__main__":
    main()
