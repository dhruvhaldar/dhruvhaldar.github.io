<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0"
                xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
                xmlns:sitemap="http://www.sitemaps.org/schemas/sitemap/0.9">
  <xsl:output method="html" version="1.0" encoding="UTF-8" indent="yes"/>
  
  <xsl:template match="/">
    <html xmlns="http://www.w3.org/1999/xhtml" lang="en">
      <head>
        <title>XML Sitemap</title>
        <meta content="width=device-width, initial-scale=1.0" name="viewport"/>
        <link rel="icon" href="data:;base64,iVBORw0KGgo="/>
        <!-- Security: Strict CSP to prevent XSS. -->
        <meta http-equiv="Content-Security-Policy" content="default-src 'none'; style-src 'sha256-kzNo/DzEZFkMvvzMOh5ptHsR9AelbnTEG659xsI9QU8='; script-src 'none'; img-src 'self' data:; font-src 'self'; connect-src 'self'; base-uri 'self'; form-action 'self';"/>
        <!-- Security: Control referrer information to preserve privacy. -->
        <meta name="referrer" content="strict-origin-when-cross-origin"/>
                <link href="https://dhruvhaldar.vercel.app" rel="preconnect"/>
        <link href="https://dhruvhaldar.vercel.app" rel="dns-prefetch"/>
        <style type="text/css">
          body {
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Oxygen-Sans, Ubuntu, Cantarell, "Helvetica Neue", sans-serif;
            color: #333;
            max-width: 75rem;
            margin: 0 auto;
            padding: 2rem;
          }
          h1 {
            color: #1a73e8;
            font-size: 2rem;
            margin-bottom: 1rem;
          }
          table {
            border-collapse: collapse;
            width: 100%;
            background: white;
            margin: 2rem 0;
            box-shadow: 0 1px 3px rgba(0,0,0,0.2);
          }
          th {
            background: #f8f9fa;
            padding: 1rem;
            text-align: left;
            font-weight: 600;
            border-bottom: 2px solid #dee2e6;
          }
          td {
            padding: 0.75rem 1rem;
            border-bottom: 1px solid #dee2e6;
            word-break: break-all;
          }
          tr:hover {
            background: #f8f9fa;
          }
          .url-count {
            color: #666;
            margin-bottom: 2rem;
          }
          .url {
            color: #0051d8;
            text-decoration: none;
          }
          .url:hover {
            text-decoration: underline;
          }
          .url:focus {
            outline: 2px solid #1a73e8;
            outline-offset: 2px;
            border-radius: 2px;
          }
          .nav-header {
            margin-bottom: 1rem;
          }
          .back-link {
            display: inline-block;
            color: #666;
            text-decoration: none;
            font-size: 0.9rem;
          }
          .back-link:hover {
            text-decoration: underline;
            color: #1a73e8;
          }
          .back-link:focus {
            outline: 2px solid #1a73e8;
            outline-offset: 2px;
            border-radius: 2px;
          }

          @media (prefers-color-scheme: dark) {
            body {
              background-color: #1a1a1a;
              color: #e0e0e0;
            }
            h1 {
              color: #4da3ff;
            }
            .back-link {
              color: #aaa;
            }
            .back-link:hover {
              color: #4da3ff;
            }
            .back-link:focus {
              outline-color: #4da3ff;
            }
            table {
              background: #2d2d2d;
              color: #e0e0e0;
            }
            th {
              background: #333;
              border-bottom-color: #444;
              color: #fff;
            }
            td {
              border-bottom-color: #444;
            }
            tr:hover {
              background: #333;
            }
            .url-count {
              color: #aaa;
            }
            .url {
              color: #4da3ff;
            }
            .url:focus {
              outline-color: #4da3ff;
            }
          }
        </style>
      </head>
      <body>
        <div class="nav-header">
          <a class="back-link" href="https://dhruvhaldar.vercel.app">← Back to Portfolio</a>
        </div>
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
                <a class="url" href="{sitemap:loc}">
                  <xsl:value-of select="sitemap:loc"/>
                </a>
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