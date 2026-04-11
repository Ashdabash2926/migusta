import os

files = [
    'index.html', 'classes.html', 'methodology.html', 'teachers.html',
    'cafe.html', 'about.html', 'accommodation.html', 'faqs.html',
    'blog.html', 'contact.html'
]

# The broken pattern currently in all pages
old = '''    <div class="nav-right">
      <div class="lang-select" id="langSelect">
      <div class="lang-selected" id="langSelected">
        <span class="lang-flag-ic" id="langFlag">🇬🇧</span>
        <span class="lang-code-lbl" id="langCode">EN</span>
        <span class="lang-caret">&#9660;</span>
      </div>
      <div class="lang-dropdown" id="langDropdown">
        <div class="lang-option active" data-lang="en"><span class="lang-flag-ic">🇬🇧</span><span class="lang-name">English</span></div>
        <div class="lang-option" data-lang="es"><span class="lang-flag-ic">🇪🇸</span><span class="lang-name">Español</span></div>
        <div class="lang-option" data-lang="fr"><span class="lang-flag-ic">🇫🇷</span><span class="lang-name">Français</span></div>
      </div>
    </div>
  </section>'''

# The correct replacement
new = '''    <div class="nav-right">
      <div class="lang-select" id="langSelect">
        <div class="lang-selected" id="langSelected">
          <span class="lang-flag-ic" id="langFlag">🇬🇧</span>
          <span class="lang-code-lbl" id="langCode">EN</span>
          <span class="lang-caret">&#9660;</span>
        </div>
        <div class="lang-dropdown" id="langDropdown">
          <div class="lang-option active" data-lang="en"><span class="lang-flag-ic">🇬🇧</span><span class="lang-name">English</span></div>
          <div class="lang-option" data-lang="es"><span class="lang-flag-ic">🇪🇸</span><span class="lang-name">Español</span></div>
          <div class="lang-option" data-lang="fr"><span class="lang-flag-ic">🇫🇷</span><span class="lang-name">Français</span></div>
        </div>
      </div>
      <a href="classes.html" class="nav-cta" data-en="Register Now" data-es="Regístrate" data-fr="S\'inscrire">Register Now</a>
      <button class="nav-burger" id="navBurger" aria-label="Open menu">
        <span></span><span></span><span></span>
      </button>
    </div>
  </nav>'''

base = '/Users/ash/Projects/migusta'

for fname in files:
    path = os.path.join(base, fname)
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
    if old in content:
        content = content.replace(old, new)
        with open(path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f'FIXED: {fname}')
    else:
        print(f'PATTERN NOT FOUND: {fname}')
