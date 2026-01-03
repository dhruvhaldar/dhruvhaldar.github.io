import re

def prepare():
    with open('index.html', 'r') as f:
        content = f.read()

    # Remove the redirect script
    # Matches <script>window.location.replace...</script>
    # The script content is fixed in this repo.
    content = re.sub(r'<script>window\.location\.replace.*?</script>', '', content)

    # Remove the meta refresh
    content = re.sub(r'<meta content="0; URL=.*?" http-equiv="refresh"/>', '', content)

    with open('verification/test.html', 'w') as f:
        f.write(content)

    print("verification/test.html created without redirects.")

if __name__ == "__main__":
    prepare()
