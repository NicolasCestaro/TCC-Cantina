# PowerShell setup script for Windows
# Usage: open PowerShell in this folder (containing manage.py) and run:
#   .\setup.ps1

Write-Host "== Setup script for TCC-Cantina (Windows) =="

# 1) Create virtualenv if not exists
if (-not (Test-Path -Path .\venv)) {
    Write-Host "Creating virtual environment..."
    python -m venv venv
} else {
    Write-Host "Virtual environment already exists."
}

Write-Host "To activate the venv run: .\venv\Scripts\Activate.ps1"
Write-Host "Then run the remaining commands below (or run them now if you activated this shell)."

Write-Host "Installing dependencies..."
pip install -r requirements.txt

Write-Host "Showing migrations status (before):"
python manage.py showmigrations

Write-Host "Applying migrations..."
python manage.py migrate

Write-Host "Showing migrations status (after):"
python manage.py showmigrations

Write-Host "Populating initial data (optional but recommended):"
python ..\scripts\populate_foods.py 2>$null
if ($LASTEXITCODE -ne 0) {
    Write-Host "Primary populate script failed; trying repository script path..."
    python ..\..\scripts\populate_foods.py 2>$null
}

Write-Host "Done. Start server with: python manage.py runserver"
