import glob
import os
from os.path import dirname, isfile, relpath


def __list_all_modules():
    work_dir = dirname(__file__)
    mod_paths = glob.glob(os.path.join(work_dir, "*", "*.py"))

    all_modules = [
        relpath(f, work_dir)  # Ambil relative path dari file
        .replace(os.sep, ".")  # Ganti \ atau / dengan .
        .rsplit(".", 1)[0]  # Hapus .py
        for f in mod_paths
        if isfile(f)
        and f.endswith(".py")
        and not f.endswith("__init__.py")
    ]

    return all_modules


ALL_MODULES = sorted(__list_all_modules())
__all__ = ALL_MODULES + ["ALL_MODULES"]
