@echo off
REM Step 1: Remove any existing build, dist, and spec files if they exist
echo Cleaning up previous builds...

IF EXIST build (
    rmdir /S /Q build
)

IF EXIST dist (
    rmdir /S /Q dist
)

IF EXIST main.spec (
    del main.spec
)

REM Step 2: Run PyInstaller to create the executable
echo Building the executable with PyInstaller...
pyinstaller --onefile --add-data "config.py;." --add-data "search_string.txt;." main.py

REM Step 3: Copy the config.py and search_string.txt files to the dist directory
echo Copying config.py and search_string.txt to the dist folder...

IF EXIST config.py (
    copy config.py dist\config.py
) ELSE (
    echo config.py not found, skipping copy...
)

IF EXIST search_string.txt (
    copy search_string.txt dist\search_string.txt
) ELSE (
    echo search_string.txt not found, skipping copy...
)

REM Step 4: Clean up unnecessary files (e.g., build directory, spec file)
echo Cleaning up unnecessary files...

IF EXIST build (
    rmdir /S /Q build
)

IF EXIST main.spec (
    del main.spec
)

REM Step 5: Notify the user and exit
echo Build complete. Executable and config files are in the dist folder.
pause
