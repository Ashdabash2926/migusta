import os
import re

files = [
    'classes.html', 'methodology.html', 'teachers.html',
    'cafe.html', 'about.html', 'accommodation.html', 'faqs.html',
    'blog.html', 'contact.html'
]

base = '/Users/ash/Projects/migusta'

# The tail of the lang-dropdown that closes both lang-dropdown and lang-select
LANG_SELECT_END = '        <div class="lang-option" data-lang="fr"><span class="lang-flag-ic">🇫🇷</span><span class="lang-name">Français</span></div>\n      </div>\n    </div>'

# What to insert after the lang-select closing div
INSERT = '''
      <a href="classes.html" class="nav-cta" data-en="Register Now" data-es="Regístrate" data-fr="S\'inscrire">Register Now</a>
      <button class="nav-burger" id="navBurger" aria-label="Open menu">
        <span></span><span></span><span></span>
      </button>
    </div>
  </nav>'''

for fname in files:
    path = os.path.join(base, fname)
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()

    if LANG_SELECT_END not in content:
        print(f'PATTERN NOT FOUND: {fname}')
        continue

    # Find position right after the lang-select closing </div>
    idx = content.find(LANG_SELECT_END) + len(LANG_SELECT_END)

    # What comes after — strip any </section> or </nav> immediately following
    remainder = content[idx:]
    # Remove a leading </section> or </nav> (with optional whitespace/newline before)
    remainder = re.sub(r'^\s*<\/section>', '', remainder)
    remainder = re.sub(r'^\s*<\/nav>', '', remainder)

    # Rebuild: everything up to end of lang-select + our insert + remainder
    new_content = content[:idx] + INSERT + '\n' + remainder

    with open(path, 'w', encoding='utf-8') as f:
        f.write(new_content)
    print(f'FIXED: {fname}')
