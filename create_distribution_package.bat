@echo off
echo ========================================
echo    CREATING DISTRIBUTION PACKAGE
echo ========================================
echo.

REM Create distribution folder
if not exist "UltimateGamingApp_Distribution" mkdir "UltimateGamingApp_Distribution"

REM Copy executable
copy "dist\UltimateGamingApp.exe" "UltimateGamingApp_Distribution\"

REM Copy installer
copy "install_ultimate_gaming_app.bat" "UltimateGamingApp_Distribution\"

REM Copy README
copy "README_UltimateGamingApp.txt" "UltimateGamingApp_Distribution\"

echo.
echo ========================================
echo    PACKAGE CREATED SUCCESSFULLY!
echo ========================================
echo.
echo Distribution package created in:
echo UltimateGamingApp_Distribution\
echo.
echo Files included:
echo - UltimateGamingApp.exe (Standalone executable)
echo - install_ultimate_gaming_app.bat (Installer script)
echo - README_UltimateGamingApp.txt (Installation guide)
echo.
echo Ready for distribution to Windows users!
echo.
pause 