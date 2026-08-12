"""Generate QR code image for session."""
import json, sys
import urllib.request

BASE = "http://localhost:8005"

# Create session
req = urllib.request.Request(
    f"{BASE}/api/session",
    data=json.dumps({"master_name": sys.argv[1] if len(sys.argv) > 1 else ""}).encode(),
    headers={"Content-Type": "application/json"}
)
r = urllib.request.urlopen(req)
data = json.loads(r.read())

print(f"Session ID: {data['session_id']}")
print(f"QR URL: {data['qr_data']}")
print(f"Expires: {data['expires_at']}")
print(f"\nShare this URL with candidate: {data['qr_data']}")
