import os
import re
import hashlib
import base64
import glob

def calculate_hash(content):
    return base64.b64encode(hashlib.sha256(content.encode('utf-8')).digest()).decode('utf-8')

# Find all index.html files
files = []
for root, dirs, filenames in os.walk("."):
    for filename in filenames:
        if filename == "index.html":
            files.append(os.path.join(root, filename))

NEW_CSS_BLOCK = """

        @media (prefers-reduced-motion: reduce) {
            .spinner {
                animation: none;
            }
        }"""

for filepath in files:
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        # Find the style tag content
        style_match = re.search(r'<style>(.*?)</style>', content, re.DOTALL)
        if not style_match:
            print(f"No style tag found in {filepath}")
            continue

        original_style_content = style_match.group(1)

        # Check if already added (idempotency)
        if "prefers-reduced-motion" in original_style_content:
             print(f"Already updated {filepath}")
             continue

        new_style_content = original_style_content + NEW_CSS_BLOCK
        new_style_hash = calculate_hash(new_style_content)

        # Replace style content
        new_content = content.replace(f"<style>{original_style_content}</style>", f"<style>{new_style_content}</style>")

        # Update CSP hash
        # Look for style-src 'sha256-...'
        csp_pattern = r"style-src 'sha256-[^']+'"
        new_csp_part = f"style-src 'sha256-{new_style_hash}'"

        if re.search(csp_pattern, new_content):
            new_content = re.sub(csp_pattern, new_csp_part, new_content)

            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"Updated {filepath} with hash {new_style_hash}")
        else:
            print(f"CSP style-src not found in {filepath}")

    except Exception as e:
        print(f"Error processing {filepath}: {e}")
