import re

# --- 1. SVGs ---
for svg_file in ['header.svg', 'footer.svg']:
    with open(svg_file, 'r', encoding='utf-8') as f:
        svg = f.read()

    # Step A: First revert all the previous #0088ff (blue) back to green #00ff88
    # Since I did a blanket replace earlier, everything is #0088ff.
    svg = svg.replace('#0088ff', '#00ff88')
    
    # Step B: Make the matrix rain letters clearer
    # Replace low opacities with higher opacities for better readability
    svg = svg.replace('opacity="0.08"', 'opacity="0.5"')
    svg = svg.replace('opacity="0.07"', 'opacity="0.5"')
    svg = svg.replace('opacity="0.04"', 'opacity="0.1"')
    svg = svg.replace('opacity="0.06"', 'opacity="0.2"')

    # Step C: Turn "KUSHAL SONI" and the subtitle tags to a bright glowing blue
    # For header.svg, the text KUSHAL SONI is surrounded by text tags.
    # The subtitle is "​[ AI · CYBERSECURITY · ETHICAL HACKING ]"
    # For footer.svg, the text is "THINK LIKE AN ATTACKER  ·  DEFEND LIKE A GUARDIAN"
    
    # Header: find text blocks containing KUSHAL SONI or the tags and change fill
    # Actually, we can use regex to target exactly those texts.
    if svg_file == 'header.svg':
        # Name
        svg = re.sub(r'(fill="#00ff88")([^>]*>KUSHAL SONI</text>)', r'fill="#00d4ff"\2', svg)
        # Subtitle
        svg = re.sub(r'(fill="#00ff88")([^>]*>\s*​\[ AI · CYBERSECURITY · ETHICAL HACKING \]\s*<)', r'fill="#00d4ff"\2', svg)
    elif svg_file == 'footer.svg':
        # Name / Tagline
        svg = re.sub(r'(fill="#00ff88")([^>]*>.*THINK LIKE AN ATTACKER.*</text>)', r'fill="#00d4ff"\2', svg)

    with open(svg_file, 'w', encoding='utf-8') as f:
        f.write(svg)

# --- 2. README.md ---
with open('README.md', 'r', encoding='utf-8') as f:
    readme = f.read()

# Replace Technical Stack with the exact clean version from Exp-readme
old_stack = re.search(r'## `▸` Technical Stack.*?<img width="100%" src="https://capsule-render', readme, flags=re.DOTALL).group(0)

new_stack = """## `▸` Technical Stack

<p align="center"><b>⚡ Core Languages &amp; Scripting</b></p>
<p align="center">
  <img src="https://img.shields.io/badge/Python-0a0f1e?style=for-the-badge&logo=python&logoColor=3776AB" alt="Python" />
  <img src="https://img.shields.io/badge/JavaScript-0a0f1e?style=for-the-badge&logo=javascript&logoColor=F7DF1E" alt="JavaScript" />
  <img src="https://img.shields.io/badge/HTML5-0a0f1e?style=for-the-badge&logo=html5&logoColor=E34F26" alt="HTML5" />
  <img src="https://img.shields.io/badge/SQL-0a0f1e?style=for-the-badge&logo=sqlite&logoColor=0088ff" alt="SQL" />
</p>

<p align="center"><b>🛡️ Offensive Security &amp; Penetration Testing</b></p>
<p align="center">
  <img src="https://img.shields.io/badge/Kali_Linux-0a0f1e?style=for-the-badge&logo=kalilinux&logoColor=557C94" alt="Kali Linux" />
  <img src="https://img.shields.io/badge/Wireshark-0a0f1e?style=for-the-badge&logo=wireshark&logoColor=1679A7" alt="Wireshark" />
  <img src="https://img.shields.io/badge/Nmap-0a0f1e?style=for-the-badge&logo=gnubash&logoColor=00ff88" alt="Nmap" />
  <img src="https://img.shields.io/badge/Burp_Suite-0a0f1e?style=for-the-badge&logo=burpsuite&logoColor=FF6633" alt="Burp Suite" />
  <img src="https://img.shields.io/badge/AES--256_Cryptography-0a0f1e?style=for-the-badge&logo=letsencrypt&logoColor=FFD700" alt="AES-256" />
</p>

<p align="center"><b>🧠 AI, ML &amp; Defense Engineering</b></p>
<p align="center">
  <img src="https://img.shields.io/badge/PyTorch-0a0f1e?style=for-the-badge&logo=pytorch&logoColor=EE4C2C" alt="PyTorch" />
  <img src="https://img.shields.io/badge/scikit--learn-0a0f1e?style=for-the-badge&logo=scikitlearn&logoColor=F7931E" alt="scikit-learn" />
  <img src="https://img.shields.io/badge/Google_ADK-0a0f1e?style=for-the-badge&logo=google&logoColor=4285F4" alt="Google ADK" />
  <img src="https://img.shields.io/badge/Gemini_API-0a0f1e?style=for-the-badge&logo=googlegemini&logoColor=0088ff" alt="Gemini API" />
  <img src="https://img.shields.io/badge/FastAPI-0a0f1e?style=for-the-badge&logo=fastapi&logoColor=00ff88" alt="FastAPI" />
  <img src="https://img.shields.io/badge/Flask-0a0f1e?style=for-the-badge&logo=flask&logoColor=ffffff" alt="Flask" />
</p>

<p align="center"><b>⚙️ Platforms &amp; Data</b></p>
<p align="center">
  <img src="https://img.shields.io/badge/Linux-0a0f1e?style=for-the-badge&logo=linux&logoColor=FCC624" alt="Linux" />
  <img src="https://img.shields.io/badge/Power_BI-0a0f1e?style=for-the-badge&logo=powerbi&logoColor=FFD700" alt="Power BI" />
  <img src="https://img.shields.io/badge/Azure_(Learning)-0a0f1e?style=for-the-badge&logo=microsoftazure&logoColor=0088ff" alt="Azure" />
</p>

<img width="100%" src="https://capsule-render.vercel.app"""

readme = readme.replace(old_stack, new_stack)

# Fix Top Languages (Replace the whole section for Top Languages)
old_languages = """**◈ Most Used Languages**

<p align="center">
  <a href="https://github-readme-stats.vercel.app/api/top-langs/?username=kushal-soni-official&layout=compact&hide_border=true&bg_color=0a0f1e&title_color=0088FF&text_color=ffffff&custom_title=Most+Used+Languages" target="_blank">
    <img src="https://github-readme-stats.vercel.app/api/top-langs/?username=kushal-soni-official&layout=compact&hide_border=true&bg_color=0a0f1e&title_color=0088FF&text_color=ffffff&custom_title=Most+Used+Languages" width="60%" alt="Top Languages" />
  </a>
</p>"""

new_languages = """**◈ Most Used Languages**

<p align="center">
  <a href="https://github-profile-summary-cards.vercel.app/api/cards/repos-per-language?username=kushal-soni-official&theme=tokyonight" target="_blank">
    <img src="https://github-profile-summary-cards.vercel.app/api/cards/repos-per-language?username=kushal-soni-official&theme=tokyonight" height="150" alt="Top Languages" />
  </a>
</p>"""

readme = readme.replace(old_languages, new_languages)

with open('README.md', 'w', encoding='utf-8') as f:
    f.write(readme)
