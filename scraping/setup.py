from cx_Freeze import setup, Executable

base = None

executables = [Executable("scrapping_mayeen.py", base=base)]

packages = ["idna", "os", "sys"]
options = {
    'build_exe': {
        'packages': packages,
    },
}

setup(
    name="Album Downloader",
    options=options,
    version="1.1.0",
    description='Downloads image from apple site.',
    executables=executables
)
