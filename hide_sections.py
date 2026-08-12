import os

dir_path = r"C:\Users\Madhan\.gemini\antigravity\scratch\navisights"
html_path = os.path.join(dir_path, "index.html")

script_to_append = """
    <script>
      setInterval(() => {
        document.querySelectorAll('h1').forEach(h1 => {
          if (h1.textContent.includes("Our Supporting Institutions and Organisations") ||
              h1.textContent.includes("Expert Testimonials")) {
            // Find the main section container (usually 2-3 levels up)
            let el = h1;
            for(let i=0; i<3; i++) {
                if(el.parentElement) el = el.parentElement;
            }
            if(el) el.style.display = 'none';
          }
        });
      }, 500);
    </script>
  </body>
</html>
"""

with open(html_path, 'r', encoding='utf-8') as f:
    html_content = f.read()

# Replace the closing body and html tags with our script
html_content = html_content.replace('</body>', script_to_append.replace('</body>\n</html>', '</body>'))

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(html_content)

print("HTML script appended!")
