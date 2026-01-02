import lxml.etree as ET

def transform_sitemap():
    dom = ET.parse('sitemap.xml')
    xslt = ET.parse('stylemap.xsl')
    transform = ET.XSLT(xslt)
    newdom = transform(dom)
    output = str(newdom)
    with open('verification/sitemap_output.html', 'w') as f:
        f.write(output)
    print("Transformation complete. Output written to verification/sitemap_output.html")
    return output

if __name__ == "__main__":
    transform_sitemap()
