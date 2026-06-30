import re

with open('README.md', 'r', encoding='utf-8') as f:
    content = f.read()

original = content

# -- TYPING ANIMATION: green -> blue --
content = content.replace('color=00FF88&center', 'color=0088FF&center')
content = content.replace('color=00ff88&center', 'color=0088FF&center')

# -- DIVIDERS: green -> blue --
content = content.replace('color=0:050510,50:00ff88,100:050510', 'color=0:0a0f1e,50:0088ff,100:0a0f1e')
content = content.replace('color=0:050510,50:00FF88,100:050510', 'color=0:0a0f1e,50:0088ff,100:0a0f1e')

# -- BADGE BACKGROUNDS: old dark green -> electric blue dark --
content = content.replace('-041a0e?style=for-the-badge', '-0a0f1e?style=for-the-badge')
content = content.replace('color=041a0e&labelColor=041a0e', 'color=0a0f1e&labelColor=0a0f1e')
content = content.replace('labelColor=041a0e', 'labelColor=0a0f1e')
content = content.replace('-0d1117?style=for-the-badge', '-0a0f1e?style=for-the-badge')

# -- LOGO COLORS: nav/UI green -> blue (NOT tool logos like PyTorch, Kali etc.) --
# Followers button logo
content = content.replace('logoColor=00ff88" alt="GitHub Followers', 'logoColor=0088ff" alt="GitHub Followers')
# View Repo buttons
content = content.replace('logoColor=00ff88" alt="View ', 'logoColor=0088ff" alt="View ')
# View All Projects button
content = content.replace('logoColor=00ff88" alt="View all', 'logoColor=0088ff" alt="View all')
# Nmap badge keeps 00ff88 as it is tool-specific accent - actually let's change it too for consistency
content = content.replace('Nmap-0a0f1e?style=for-the-badge&logo=gnubash&logoColor=00ff88', 'Nmap-0a0f1e?style=for-the-badge&logo=gnubash&logoColor=0088ff')

# -- ACTIVITY GRAPH: green -> blue --
content = content.replace('bg_color=050510&color=00ff88&line=00ff88', 'bg_color=0a0f1e&color=0088ff&line=0088ff')
content = content.replace('area_color=041a0e', 'area_color=0a0f1e')

# -- STREAK STATS: green ring/label -> blue, keep red fire --
content = content.replace('ring=00FF88&fire=FF003C&currStreakLabel=00FF88', 'ring=0088FF&fire=FF003C&currStreakLabel=0088FF')
content = content.replace('background=0D1117&border=0D1117', 'background=0a0f1e&border=0a0f1e')

# -- GITHUB STATS CARDS: green -> blue --
content = content.replace('title_color=00FF88&icon_color=00FF88&text_color=C9D1D9&ring_color=00FF88', 'title_color=0088FF&icon_color=0088FF&text_color=ffffff&ring_color=0088FF')
content = content.replace('title_color=00FF88&text_color=C9D1D9', 'title_color=0088FF&text_color=ffffff')
content = content.replace('bg_color=0D1117', 'bg_color=0a0f1e')

count = content.count('0088ff') + content.count('0088FF')
remaining_green = content.count('00ff88') + content.count('00FF88')

with open('README.md', 'w', encoding='utf-8') as f:
    f.write(content)

print('[OK] Blue replacements applied:', count)
print('[INFO] Remaining green instances (tool-specific):', remaining_green)
