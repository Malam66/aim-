@echo off
echo ========================================
echo    DEPLOYING TO GITHUB
echo ========================================
echo.

echo Step 1: Checking Git status...
git status

echo.
echo Step 2: Adding all files...
git add .

echo.
echo Step 3: Committing changes...
git commit -m "Deploy Ultimate Gaming App v1.0 to GitHub"

echo.
echo Step 4: Ready to push to GitHub!
echo.
echo ========================================
echo    NEXT STEPS:
echo ========================================
echo.
echo 1. Create a new repository on GitHub:
echo    - Go to https://github.com
echo    - Click "New repository"
echo    - Name: ultimate-gaming-app
echo    - Make it PUBLIC (for GitHub Pages)
echo    - DON'T initialize with README (we have one)
echo.
echo 2. After creating the repository, run:
echo    git remote add origin https://github.com/YOUR_USERNAME/ultimate-gaming-app.git
echo    git branch -M main
echo    git push -u origin main
echo.
echo 3. Enable GitHub Pages:
echo    - Go to repository Settings
echo    - Scroll to "Pages" section
echo    - Source: "Deploy from a branch"
echo    - Branch: "main" / "/ (root)"
echo    - Save
echo.
echo 4. Create a Release:
echo    - Go to "Releases" tab
echo    - "Create a new release"
echo    - Tag: v1.0
echo    - Title: "Ultimate Gaming App v1.0"
echo    - Upload UltimateGamingApp.exe
echo    - Publish release
echo.
echo Your app will be available at:
echo - Repository: https://github.com/YOUR_USERNAME/ultimate-gaming-app
echo - Web Page: https://YOUR_USERNAME.github.io/ultimate-gaming-app/
echo - Direct Download: https://github.com/YOUR_USERNAME/ultimate-gaming-app/releases/latest/download/UltimateGamingApp.exe
echo.
pause 