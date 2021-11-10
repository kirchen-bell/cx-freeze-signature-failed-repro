import sys
from cx_Freeze import setup, Executable

base = None
if sys.platform == "win32":
    base = "Win32GUI"

executables = [
    Executable(
        "run.py",
        target_name="TestApp",
        base=base
    )
]

options = {
    "bdist_mac": {
        "bundle_name": "TestApp"
    }
}

setup(
    name="TestApp",
    version="1.0.0",
    executables=executables,
    options=options
)
