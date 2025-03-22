python3 -m venv .venv
.venv\Scripts\Activate

pip install --upgrade pip
pip install -r requirements.txt

Remove-Item -Recurse -Force public
reflex init
reflex export --frontend-only

Remove-Item -Recurse -Force public
Expand-Archive -Path frontend.zip -DestinationPath public
Remove-Item frontend.zip

deactivate
