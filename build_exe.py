#!/usr/bin/env python3
"""
Build Script for Ultimate Gaming App
Creates a standalone executable for Windows
"""

import os
import sys
import subprocess
import shutil

def install_requirements():
    """Install required packages"""
    print("📦 Installing required packages...")
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
        print("✅ Packages installed successfully!")
    except subprocess.CalledProcessError as e:
        print(f"❌ Error installing packages: {e}")
        return False
    return True

def get_pyinstaller_path():
    """Get the full path to PyInstaller"""
    try:
        # Try to find pyinstaller in the scripts directory
        scripts_dir = os.path.join(os.path.dirname(sys.executable), "Scripts")
        pyinstaller_path = os.path.join(scripts_dir, "pyinstaller.exe")
        
        if os.path.exists(pyinstaller_path):
            return [pyinstaller_path]
        
        # Try using python -m pyinstaller
        return [sys.executable, "-m", "pyinstaller"]
    except:
        return [sys.executable, "-m", "pyinstaller"]

def create_executable():
    """Create standalone executable using PyInstaller"""
    print("🔨 Creating standalone executable...")
    
    # Get PyInstaller path
    pyinstaller_cmd = get_pyinstaller_path()
    
    # PyInstaller command with optimized settings
    cmd = pyinstaller_cmd + [
        "--onefile",                    # Single executable file
        "--windowed",                   # No console window
        "--name=UltimateGamingApp",     # Executable name
        "--hidden-import=PIL._tkinter_finder",  # Fix PIL import issues
        "--hidden-import=pynput.keyboard._win32",  # Fix pynput imports
        "--hidden-import=pynput.mouse._win32",
        "--hidden-import=keyboard",
        "--hidden-import=mouse",
        "--hidden-import=ctypes",
        "--hidden-import=threading",
        "--hidden-import=json",
        "--hidden-import=math",
        "--hidden-import=random",
        "--hidden-import=time",
        "--hidden-import=subprocess",
        "--hidden-import=os",
        "--hidden-import=sys",
        "--clean",                      # Clean cache
        "--noconfirm",                  # Don't ask for confirmation
        "new_ultimate_app.py"
    ]
    
    # Add icon if available
    if os.path.exists("app_icon.ico"):
        cmd.insert(-1, "--icon=app_icon.ico")
    
    try:
        subprocess.check_call(cmd)
        print("✅ Executable created successfully!")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Error creating executable: {e}")
        return False

def create_installer():
    """Create a simple installer script"""
    print("📋 Creating installer...")
    
    installer_content = '''@echo off
echo ========================================
echo    ULTIMATE GAMING APP INSTALLER
echo ========================================
echo.
echo Installing Ultimate Gaming App...
echo.

REM Create installation directory
if not exist "%PROGRAMFILES%\\UltimateGamingApp" mkdir "%PROGRAMFILES%\\UltimateGamingApp"

REM Copy executable
copy "UltimateGamingApp.exe" "%PROGRAMFILES%\\UltimateGamingApp\\"

REM Create desktop shortcut
echo Creating desktop shortcut...
powershell "$WshShell = New-Object -comObject WScript.Shell; $Shortcut = $WshShell.CreateShortcut('%USERPROFILE%\\Desktop\\Ultimate Gaming App.lnk'); $Shortcut.TargetPath = '%PROGRAMFILES%\\UltimateGamingApp\\UltimateGamingApp.exe'; $Shortcut.Save()"

echo.
echo ========================================
echo    INSTALLATION COMPLETE!
echo ========================================
echo.
echo The Ultimate Gaming App has been installed to:
echo %PROGRAMFILES%\\UltimateGamingApp\\
echo.
echo A desktop shortcut has been created.
echo.
echo Press any key to exit...
pause >nul
'''
    
    try:
        with open("install_ultimate_gaming_app.bat", "w") as f:
            f.write(installer_content)
        print("✅ Installer created: install_ultimate_gaming_app.bat")
        return True
    except Exception as e:
        print(f"❌ Error creating installer: {e}")
        return False

def create_readme():
    """Create a README file with installation instructions"""
    print("📖 Creating README...")
    
    readme_content = '''# 🎯 Ultimate Gaming App

## 📦 Installation Instructions

### Option 1: Quick Install (Recommended)
1. Download `UltimateGamingApp.exe`
2. Double-click to run immediately
3. No installation required - it's a standalone executable!

### Option 2: Full Installation
1. Download `UltimateGamingApp.exe` and `install_ultimate_gaming_app.bat`
2. Right-click `install_ultimate_gaming_app.bat` and "Run as Administrator"
3. The app will be installed to Program Files with desktop shortcut

## 🚀 Features
- **Anti-Recoil System**: Advanced recoil compensation
- **Aim Assist**: Intelligent target detection and assistance
- **Mouse Control**: Precise mouse movement and control
- **Customizable Settings**: Adjust sensitivity, strength, and behavior
- **Anti-Detection**: Built-in protection mechanisms
- **Emergency Stop**: F1 key for instant emergency stop

## 🎮 Controls
- **Insert**: Toggle main script
- **F4**: Toggle aim assist
- **F1**: Emergency stop
- **Caps Lock**: Master switch

## ⚠️ Important Notes
- Run as Administrator for full functionality
- Windows 10/11 compatible
- Requires no additional software installation
- Standalone executable - no Python required

## 🔧 Troubleshooting
If the app doesn't start:
1. Right-click and "Run as Administrator"
2. Check Windows Defender isn't blocking it
3. Add to antivirus exceptions if needed

## 📞 Support
For issues or questions, check the app's built-in help system.

---
**Version**: 1.0
**Platform**: Windows 10/11
**Size**: ~50MB (standalone)
'''
    
    try:
        with open("README_UltimateGamingApp.txt", "w") as f:
            f.write(readme_content)
        print("✅ README created: README_UltimateGamingApp.txt")
        return True
    except Exception as e:
        print(f"❌ Error creating README: {e}")
        return False

def main():
    """Main build process"""
    print("🎯 ULTIMATE GAMING APP - EXECUTABLE BUILDER")
    print("=" * 50)
    
    # Step 1: Install requirements
    if not install_requirements():
        print("❌ Failed to install requirements. Exiting.")
        return
    
    # Step 2: Create executable
    if not create_executable():
        print("❌ Failed to create executable. Exiting.")
        return
    
    # Step 3: Create installer
    create_installer()
    
    # Step 4: Create README
    create_readme()
    
    # Step 5: Show results
    print("\n" + "=" * 50)
    print("🎉 BUILD COMPLETE!")
    print("=" * 50)
    print("\n📁 Generated Files:")
    
    if os.path.exists("dist/UltimateGamingApp.exe"):
        print("✅ UltimateGamingApp.exe - Standalone executable")
        size = os.path.getsize("dist/UltimateGamingApp.exe") / (1024 * 1024)
        print(f"   Size: {size:.1f} MB")
    
    if os.path.exists("install_ultimate_gaming_app.bat"):
        print("✅ install_ultimate_gaming_app.bat - Installer script")
    
    if os.path.exists("README_UltimateGamingApp.txt"):
        print("✅ README_UltimateGamingApp.txt - Installation guide")
    
    print("\n🚀 Ready for distribution!")
    print("Users can now install and run your Ultimate Gaming App on any Windows device!")

if __name__ == "__main__":
    main() 