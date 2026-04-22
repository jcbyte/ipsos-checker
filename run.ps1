# Execute `main.py`, creating an environment if one does not already exist

$VenvPath = "$PSScriptRoot/.venv"
$VenvPython = "$VenvPath/Scripts/python.exe"
$PyScript = "$PSScriptRoot/main.py"

# If the environment doesn't exist then create it
if (-not (Test-Path $VenvPath)) {
  # Create virtual environment
  python -m venv $VenvPath

  # Install packages
  & $VenvPython -m pip install -r "$PSScriptRoot/requirements.txt"

  # Install playwright browsers are installed
  $VenvPlaywright = "$VenvPath/Scripts/playwright.exe"
  & $VenvPlaywright install chromium

  Write-Host "-----`n" -ForegroundColor Gray
}

# Execute the python script using the environment
& $VenvPython $PyScript

Write-Host "[Press any key to exit]" -ForegroundColor DarkGray -NoNewline
[Console]::ReadKey($true) | Out-Null
