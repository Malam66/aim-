@echo off
echo ========================================
echo    ULTIMATE GAMING APP INSTALLER
echo ========================================
echo.
echo Installing Ultimate Gaming App...
echo.

REM Create installation directory
if not exist "%PROGRAMFILES%\UltimateGamingApp" mkdir "%PROGRAMFILES%\UltimateGamingApp"

REM Copy executable
copy "dist\UltimateGamingApp.exe" "%PROGRAMFILES%\UltimateGamingApp\"

REM Create desktop shortcut
echo Creating desktop shortcut...
powershell "$WshShell = New-Object -comObject WScript.Shell; $Shortcut = $WshShell.CreateShortcut('%USERPROFILE%\Desktop\Ultimate Gaming App.lnk'); $Shortcut.TargetPath = '%PROGRAMFILES%\UltimateGamingApp\UltimateGamingApp.exe'; $Shortcut.Save()"

echo.
echo ========================================
echo    INSTALLATION COMPLETE!
echo ========================================
echo.
echo The Ultimate Gaming App has been installed to:
echo %PROGRAMFILES%\UltimateGamingApp\
echo.
echo A desktop shortcut has been created.
echo.
echo Press any key to exit...
pause >nul 