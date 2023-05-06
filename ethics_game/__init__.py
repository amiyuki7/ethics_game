import sys
import os


# To support image files when compiling into a binary with pyinstaller
def resource_path(rel_path):
    try:
        base_path = sys._MEIPASS  # type: ignore
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, rel_path)
