<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0"
                xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
                xmlns:sitemap="http://www.sitemaps.org/schemas/sitemap/0.9">
  <xsl:output method="html" version="1.0" encoding="UTF-8" indent="yes"/>
  
  <xsl:template match="/">
    <html xmlns="http://www.w3.org/1999/xhtml" lang="en">
      <head>
        <meta charset="utf-8"/>
        <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
        <title>XML Sitemap</title>
        <link rel="icon" href="data:;base64,iVBORw0KGgo="/>
        <!-- Security: Strict CSP to prevent XSS. -->
        <meta http-equiv="Content-Security-Policy" content="default-src 'none'; object-src 'none'; style-src 'sha256-XdWac56BCqyPcPHIPDlSXxa6GkG0nwTOYFFG1lj/6a0='; script-src 'none'; img-src 'self' data:; font-src 'self'; connect-src 'self'; base-uri 'none'; form-action 'none';"/>
        <!-- Security: Control referrer information to preserve privacy. -->
        <meta name="referrer" content="strict-origin-when-cross-origin"/>
        <link href="https://dhruvhaldar.vercel.app" rel="preconnect"/>
        <link href="https://dhruvhaldar.vercel.app" rel="dns-prefetch"/>
        <style type="text/css">body{font-family:-apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,Oxygen-Sans,Ubuntu,Cantarell,"Helvetica Neue",sans-serif;color:#333;max-width:75rem;margin:0 auto;padding:2rem} h1{color:#1a73e8;font-size:2rem;margin-bottom:1rem} table{border-collapse:collapse;width:100%;background:white;margin:2rem 0;box-shadow:0 1px 3px rgba(0,0,0,0.2)} th{background:#f8f9fa;padding:1rem;text-align:left;font-weight:600;border-bottom:2px solid #dee2e6} td{padding:0.75rem 1rem;border-bottom:1px solid #dee2e6;word-break:break-all} tr:hover{background:#f8f9fa} .url-count{color:#666;margin-bottom:2rem} .url{color:#0051d8;text-decoration:none} .url:hover{text-decoration:underline} .url:focus{outline:2px solid #1a73e8;outline-offset:2px;border-radius:2px} @media (prefers-color-scheme:dark){body{background-color:#1a1a1a;color:#e0e0e0} h1{color:#4da3ff} table{background:#2d2d2d;color:#e0e0e0} th{background:#333;border-bottom-color:#444;color:#fff} td{border-bottom-color:#444} tr:hover{background:#333} .url-count{color:#aaa} .url{color:#4da3ff} .url:focus{outline-color:#4da3ff} }</style>
      </head>
      <body>
        <h1>XML Sitemap</h1>
        <div class="url-count">
          Number of URLs: <xsl:value-of select="count(sitemap:urlset/sitemap:url)"/>
        </div>
        <table>
          <caption>Sitemap URLs</caption>
          <tr>
            <th scope="col">URL</th>
            <th scope="col">Path</th>
          </tr>
          <xsl:for-each select="sitemap:urlset/sitemap:url">
            <tr>
              <td>
                <xsl:choose>
                  <xsl:when test="starts-with(sitemap:loc, 'http')">
                    <a class="url" href="{sitemap:loc}">
                      <xsl:value-of select="sitemap:loc"/>
                    </a>
                  </xsl:when>
                  <xsl:otherwise>
                    <xsl:value-of select="sitemap:loc"/>
                  </xsl:otherwise>
                </xsl:choose>
              </td>
              <td>
                <xsl:value-of select="substring-after(sitemap:loc, 'dhruvhaldar.vercel.app')"/>
              </td>
            </tr>
          </xsl:for-each>
        </table>
      </body>
    </html>
  </xsl:template>
</xsl:stylesheet>