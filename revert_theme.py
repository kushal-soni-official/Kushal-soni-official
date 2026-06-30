import re

# --- README.md Changes ---
with open('README.md', 'r', encoding='utf-8') as f:
    readme = f.read()

# 1. Restore Top Languages
old_languages = """**◈ Most Used Languages**

<p align="center">
  <a href="https://github-profile-summary-cards.vercel.app/api/cards/repos-per-language?username=kushal-soni-official&theme=tokyonight" target="_blank">
    <img src="https://github-profile-summary-cards.vercel.app/api/cards/repos-per-language?username=kushal-soni-official&theme=tokyonight" height="150" alt="Top Languages" />
  </a>
</p>"""

new_languages = """**◈ Most Used Languages**

<p align="center">
  <a href="https://github-readme-stats.vercel.app/api/top-langs/?username=kushal-soni-official&layout=compact&hide_border=true&bg_color=0D1117&title_color=00FF88&text_color=C9D1D9&custom_title=Most+Used+Languages" target="_blank">
    <img src="https://github-readme-stats.vercel.app/api/top-langs/?username=kushal-soni-official&layout=compact&hide_border=true&bg_color=0D1117&title_color=00FF88&text_color=C9D1D9&custom_title=Most+Used+Languages" width="60%" alt="Top Languages" />
  </a>
</p>"""

readme = readme.replace(old_languages, new_languages)

# 2. Revert Colors
# Dividers
readme = readme.replace('color=0:0a0f1e,50:0088ff,100:0a0f1e', 'color=0:050510,50:00ff88,100:050510')

# Typing animation
readme = readme.replace('color=0088FF&center', 'color=00FF88&center')

# Badges Backgrounds
readme = readme.replace('color=0a0f1e&labelColor=0a0f1e', 'color=041a0e&labelColor=041a0e')
readme = readme.replace('Ofc.kusharu@gmail.com-0a0f1e?style', 'Ofc.kusharu@gmail.com-041a0e?style')
readme = readme.replace('labelColor=0a0f1e', 'labelColor=041a0e')
readme = readme.replace('-0a0f1e?style=for-the-badge', '-0d1117?style=for-the-badge')

# Accents (Icons, Rings, Logos)
readme = readme.replace('logoColor=0088ff', 'logoColor=00ff88')
readme = readme.replace('bg_color=0a0f1e&color=0088ff&line=0088ff', 'bg_color=050510&color=00ff88&line=00ff88')
readme = readme.replace('area_color=0a0f1e', 'area_color=041a0e')
readme = readme.replace('ring=0088FF&fire=FF003C&currStreakLabel=0088FF', 'ring=00FF88&fire=FF003C&currStreakLabel=00FF88')
readme = readme.replace('background=0a0f1e&border=0a0f1e', 'background=0D1117&border=0D1117')
readme = readme.replace('title_color=0088FF&icon_color=0088FF&text_color=ffffff&ring_color=0088FF', 'title_color=00FF88&icon_color=00FF88&text_color=C9D1D9&ring_color=00FF88')
readme = readme.replace('title_color=0088FF&text_color=ffffff', 'title_color=00FF88&text_color=C9D1D9')
readme = readme.replace('bg_color=0a0f1e', 'bg_color=0D1117')

with open('README.md', 'w', encoding='utf-8') as f:
    f.write(readme)

# --- SVGs Changes ---
for svg_file in ['header.svg', 'footer.svg']:
    with open(svg_file, 'r', encoding='utf-8') as f:
        svg = f.read()

    # Background
    svg = svg.replace('#0a0f1e', '#050510')
    # Center text
    svg = svg.replace('#00d4ff', '#00ff88')

    with open(svg_file, 'w', encoding='utf-8') as f:
        f.write(svg)
