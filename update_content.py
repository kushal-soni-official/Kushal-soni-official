import re

# --- README.md Changes ---
with open('README.md', 'r', encoding='utf-8') as f:
    readme = f.read()

# 1. Remove Education section
# From: ## `▸` Education
# To: the divider before ## `▸` Certifications &amp; Achievements
readme = re.sub(r'## `▸` Education.*?<img width="100%" src="https://capsule-render\.vercel\.app/api\?type=rect&color=0:0a0f1e,50:0088ff,100:0a0f1e&height=2&section=header" alt="section divider" />\n\n', '', readme, flags=re.DOTALL)

# 2. Remove Language Proficiencies section
# From: ## `▸` Language Proficiencies
# To: the divider before ## `▸` Contribution Activity
readme = re.sub(r'## `▸` Language Proficiencies.*?<img width="100%" src="https://capsule-render\.vercel\.app/api\?type=rect&color=0:0a0f1e,50:0088ff,100:0a0f1e&height=2&section=header" alt="section divider" />\n\n', '', readme, flags=re.DOTALL)

# 3. GitHub Stats - Keep only Streak and Top Languages
# Remove:
# **◈ Overall GitHub Activity Snapshot**
# <p align="center"> ... </p>
readme = re.sub(r'\*\*◈ Overall GitHub Activity Snapshot\*\*.*?</p>\n\n', '', readme, flags=re.DOTALL)

# 4. Remove specific rows from Certifications table
# Remove: 10 Day AI Bootcamp, Ranked #2 in City, Certificate of Excellence, Build Reliable Agent Applications
cert_lines = readme.split('\n')
new_cert_lines = []
for line in cert_lines:
    if '10-Day AI Bootcamp' in line or 'Ranked #2 in City' in line or 'Certificate of Excellence' in line or 'Build Reliable Agentic AI Applications' in line:
        continue
    new_cert_lines.append(line)
readme = '\n'.join(new_cert_lines)

# 5. Enhance Technical Stack
old_tech_stack = """<p align="center"><b>◈ Languages &amp; Core</b></p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-0a0f1e?style=for-the-badge&logo=python&logoColor=3776AB" alt="Python" />
  <img src="https://img.shields.io/badge/JavaScript-0a0f1e?style=for-the-badge&logo=javascript&logoColor=F7DF1E" alt="JavaScript" />
  <img src="https://img.shields.io/badge/HTML5-0a0f1e?style=for-the-badge&logo=html5&logoColor=E34F26" alt="HTML5" />
  <img src="https://img.shields.io/badge/CSS3-0a0f1e?style=for-the-badge&logo=css3&logoColor=1572B6" alt="CSS3" />
</p>

<br/>

<p align="center"><b>◈ Cybersecurity &amp; Offensive Tools</b></p>

<p align="center">
  <img src="https://img.shields.io/badge/Kali_Linux-0a0f1e?style=for-the-badge&logo=kalilinux&logoColor=557C94" alt="Kali Linux" />
  <img src="https://img.shields.io/badge/Linux-0a0f1e?style=for-the-badge&logo=linux&logoColor=FCC624" alt="Linux" />
  <img src="https://img.shields.io/badge/Wireshark-0a0f1e?style=for-the-badge&logo=wireshark&logoColor=1679A7" alt="Wireshark" />
  <img src="https://img.shields.io/badge/Nmap-0a0f1e?style=for-the-badge&logo=gnubash&logoColor=0088ff" alt="Nmap" />
  <img src="https://img.shields.io/badge/SHA--256_Cryptography-0a0f1e?style=for-the-badge&logo=letsencrypt&logoColor=3C8CA3" alt="SHA-256" />
  <img src="https://img.shields.io/badge/Windows_Registry_API-0a0f1e?style=for-the-badge&logo=windows&logoColor=0078D6" alt="Windows Registry API" />
</p>

<br/>

<p align="center"><b>◈ AI, ML &amp; Security Intelligence</b></p>

<p align="center">
  <img src="https://img.shields.io/badge/PyTorch-0a0f1e?style=for-the-badge&logo=pytorch&logoColor=EE4C2C" alt="PyTorch" />
  <img src="https://img.shields.io/badge/scikit--learn-0a0f1e?style=for-the-badge&logo=scikitlearn&logoColor=F7931E" alt="scikit-learn" />
  <img src="https://img.shields.io/badge/TF--IDF_NLP-0a0f1e?style=for-the-badge&logo=spacy&logoColor=09A3D5" alt="TF-IDF NLP" />
  <img src="https://img.shields.io/badge/Google_ADK-0a0f1e?style=for-the-badge&logo=google&logoColor=4285F4" alt="Google ADK" />
  <img src="https://img.shields.io/badge/Gemini_API-0a0f1e?style=for-the-badge&logo=googlegemini&logoColor=8E75B2" alt="Gemini API" />
  <img src="https://img.shields.io/badge/Groq_API-0a0f1e?style=for-the-badge&logo=groq&logoColor=F55036" alt="Groq API" />
</p>

<br/>

<p align="center"><b>◈ Web, API &amp; Data</b></p>

<p align="center">
  <img src="https://img.shields.io/badge/FastAPI-0a0f1e?style=for-the-badge&logo=fastapi&logoColor=009688" alt="FastAPI" />
  <img src="https://img.shields.io/badge/REST_APIs-0a0f1e?style=for-the-badge&logo=postman&logoColor=FF6C37" alt="REST APIs" />
  <img src="https://img.shields.io/badge/SQLite-0a0f1e?style=for-the-badge&logo=sqlite&logoColor=4ea4d4" alt="SQLite" />
  <img src="https://img.shields.io/badge/Power_BI-0a0f1e?style=for-the-badge&logo=powerbi&logoColor=F2C811" alt="Power BI" />
  <img src="https://img.shields.io/badge/DAX-0a0f1e?style=for-the-badge&logo=powerbi&logoColor=F2C811" alt="DAX" />
</p>

<br/>

<p align="center"><b>◈ DevOps &amp; Tools</b></p>

<p align="center">
  <img src="https://img.shields.io/badge/Git-0a0f1e?style=for-the-badge&logo=git&logoColor=F05032" alt="Git" />
  <img src="https://img.shields.io/badge/GitHub-0a0f1e?style=for-the-badge&logo=github&logoColor=ffffff" alt="GitHub" />
  <img src="https://img.shields.io/badge/Antigravity_CLI-0a0f1e?style=for-the-badge&logo=google&logoColor=4285F4" alt="Google Antigravity CLI" />
</p>"""

new_tech_stack = """<p align="center"><b>⚡ Core Languages &amp; Scripting</b></p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-0a0f1e?style=for-the-badge&logo=python&logoColor=3776AB" alt="Python" />
  <img src="https://img.shields.io/badge/JavaScript-0a0f1e?style=for-the-badge&logo=javascript&logoColor=F7DF1E" alt="JavaScript" />
  <img src="https://img.shields.io/badge/HTML5-0a0f1e?style=for-the-badge&logo=html5&logoColor=E34F26" alt="HTML5" />
  <img src="https://img.shields.io/badge/CSS3-0a0f1e?style=for-the-badge&logo=css3&logoColor=1572B6" alt="CSS3" />
</p>

<br/>

<p align="center"><b>🛡️ Offensive Security &amp; Penetration Testing</b></p>

<p align="center">
  <img src="https://img.shields.io/badge/Kali_Linux-0a0f1e?style=for-the-badge&logo=kalilinux&logoColor=557C94" alt="Kali Linux" />
  <img src="https://img.shields.io/badge/Linux-0a0f1e?style=for-the-badge&logo=linux&logoColor=FCC624" alt="Linux" />
  <img src="https://img.shields.io/badge/Wireshark-0a0f1e?style=for-the-badge&logo=wireshark&logoColor=1679A7" alt="Wireshark" />
  <img src="https://img.shields.io/badge/Nmap-0a0f1e?style=for-the-badge&logo=gnubash&logoColor=0088ff" alt="Nmap" />
  <img src="https://img.shields.io/badge/SHA--256_Cryptography-0a0f1e?style=for-the-badge&logo=letsencrypt&logoColor=3C8CA3" alt="SHA-256" />
  <img src="https://img.shields.io/badge/Windows_Registry_API-0a0f1e?style=for-the-badge&logo=windows&logoColor=0078D6" alt="Windows Registry API" />
</p>

<br/>

<p align="center"><b>🧠 AI, Machine Learning &amp; Defense Engineering</b></p>

<p align="center">
  <img src="https://img.shields.io/badge/PyTorch-0a0f1e?style=for-the-badge&logo=pytorch&logoColor=EE4C2C" alt="PyTorch" />
  <img src="https://img.shields.io/badge/scikit--learn-0a0f1e?style=for-the-badge&logo=scikitlearn&logoColor=F7931E" alt="scikit-learn" />
  <img src="https://img.shields.io/badge/TF--IDF_NLP-0a0f1e?style=for-the-badge&logo=spacy&logoColor=09A3D5" alt="TF-IDF NLP" />
  <img src="https://img.shields.io/badge/Google_ADK-0a0f1e?style=for-the-badge&logo=google&logoColor=4285F4" alt="Google ADK" />
  <img src="https://img.shields.io/badge/Gemini_API-0a0f1e?style=for-the-badge&logo=googlegemini&logoColor=8E75B2" alt="Gemini API" />
  <img src="https://img.shields.io/badge/Groq_API-0a0f1e?style=for-the-badge&logo=groq&logoColor=F55036" alt="Groq API" />
</p>

<br/>

<p align="center"><b>⚙️ Web, API &amp; Data</b></p>

<p align="center">
  <img src="https://img.shields.io/badge/FastAPI-0a0f1e?style=for-the-badge&logo=fastapi&logoColor=009688" alt="FastAPI" />
  <img src="https://img.shields.io/badge/REST_APIs-0a0f1e?style=for-the-badge&logo=postman&logoColor=FF6C37" alt="REST APIs" />
  <img src="https://img.shields.io/badge/SQLite-0a0f1e?style=for-the-badge&logo=sqlite&logoColor=4ea4d4" alt="SQLite" />
  <img src="https://img.shields.io/badge/Power_BI-0a0f1e?style=for-the-badge&logo=powerbi&logoColor=F2C811" alt="Power BI" />
  <img src="https://img.shields.io/badge/DAX-0a0f1e?style=for-the-badge&logo=powerbi&logoColor=F2C811" alt="DAX" />
</p>

<br/>

<p align="center"><b>🛠️ DevOps &amp; Development Tools</b></p>

<p align="center">
  <img src="https://img.shields.io/badge/Git-0a0f1e?style=for-the-badge&logo=git&logoColor=F05032" alt="Git" />
  <img src="https://img.shields.io/badge/GitHub-0a0f1e?style=for-the-badge&logo=github&logoColor=ffffff" alt="GitHub" />
  <img src="https://img.shields.io/badge/Antigravity_CLI-0a0f1e?style=for-the-badge&logo=google&logoColor=4285F4" alt="Google Antigravity CLI" />
</p>"""

readme = readme.replace(old_tech_stack, new_tech_stack)

with open('README.md', 'w', encoding='utf-8') as f:
    f.write(readme)
print("Updated README.md")

# --- SVG Changes ---
for svg_file in ['header.svg', 'footer.svg']:
    with open(svg_file, 'r', encoding='utf-8') as f:
        svg = f.read()
    
    # Theme colors update
    svg = svg.replace('#050510', '#0a0f1e') # Background
    svg = svg.replace('#00ff88', '#0088ff') # Matrix rain & lines
    
    with open(svg_file, 'w', encoding='utf-8') as f:
        f.write(svg)
    print(f"Updated {svg_file}")
