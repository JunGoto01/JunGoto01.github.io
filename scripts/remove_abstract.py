import re

# Read the file
with open('research.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Find and remove the abstract for "Social Media, Discrimination, and Politics"
# This is in the Work in Progress section
pattern = r'(<li class="publication-item">\s*<span class="pub-title">Social Media, Discrimination, and Politics: Online Field Experiments in\s*India</span>)\s*<details>.*?</details>\s*(</li>)'

replacement = r'\1\n                \2'

new_content = re.sub(pattern, replacement, content, flags=re.DOTALL)

# Write back
with open('research.html', 'w', encoding='utf-8') as f:
    f.write(new_content)

print("Abstract removed successfully")
