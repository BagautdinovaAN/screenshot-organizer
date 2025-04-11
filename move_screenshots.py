import os
import shutil

def main():
    desktop_path = os.path.expanduser("~/Desktop")
    screenshots_folder = os.path.join(desktop_path, "Screenshots")
    screenshots = []

    if not os.path.exists(screenshots_folder):
        os.makedirs(screenshots_folder)
        print(f"Создана папка: {screenshots_folder}")
    else:
        print(f"Папка уже существует: {screenshots_folder}")

    for file in os.listdir(desktop_path):
        if file.startswith("Screenshot") and file.endswith(".png"):
            screenshots.append(file)
    if screenshots:
        for file in screenshots:
            shutil.move(os.path.join(desktop_path, file), screenshots_folder)
    else:
        print("Скриншоты на рабочем столе не найдены")

if __name__ == "__main__":
    main()
