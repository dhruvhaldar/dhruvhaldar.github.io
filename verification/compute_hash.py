import hashlib
import re

def compute_hash():
    with open('stylemap.xsl', 'r') as f:
        content = f.read()

    # Extract content between <style type="text/css"> and </style>
    match = re.search(r'<style type="text/css">(.*?)</style>', content, re.DOTALL)
    if match:
        style_content = match.group(1)
        # Calculate SHA256 hash
        sha256_hash = hashlib.sha256(style_content.encode('utf-8')).digest()
        import base64
        base64_hash = base64.b64encode(sha256_hash).decode('utf-8')
        print(f"sha256-{base64_hash}")
        return f"sha256-{base64_hash}"
    else:
        print("Style tag not found")
        return None

if __name__ == "__main__":
    compute_hash()
