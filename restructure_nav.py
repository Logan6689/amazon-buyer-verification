#!/usr/bin/env python3
import sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

path = r"C:\Users\Administrator.WIN-0V19CGJAQ3O\.qclaw\workspace-agent-e2d75f0a\landing-page\index.html"
h = open(path, encoding='utf-8').read()

old = '''  <div class="nav-links" style="display: flex; gap: 28px; font-size: 14px; font-weight: 500;">
    <a href="#how" style="color: #555; text-decoration: none;">Activities</a>
    <a href="#agent" style="color: #555; text-decoration: none;">Purchase Agent</a>
    <a href="#invite-faq" style="color: #555; text-decoration: none;">Invite & FAQ</a>
    <a href="javascript:void(0)" onclick="openGuide()" style="background: linear-gradient(135deg, #FF6B35, #FF8C5A); color: #fff; padding: 8px 20px; border-radius: 9999px; font-weight: 700; font-size: 13px; text-decoration: none; transition: all 0.2s;" onmouseover="this.style.boxShadow='0 4px 16px rgba(255,107,53,0.35)'" onmouseout="this.style.boxShadow='none'">Valivy Guide</a>
  </div>
</nav>'''

new = '''  <div class="nav-links" style="display: flex; gap: 28px; font-size: 14px; font-weight: 500; justify-content: center;">
    <a href="#how" style="color: #555; text-decoration: none;">Activities</a>
    <a href="#agent" style="color: #555; text-decoration: none;">Purchase Agent</a>
    <a href="#invite-faq" style="color: #555; text-decoration: none;">Invite & FAQ</a>
  </div>
  <div class="nav-right" style="display: flex; justify-content: flex-end; align-items: center;">
    <a href="javascript:void(0)" onclick="openGuide()" class="nav-guide-btn" style="background: linear-gradient(135deg, #FF6B35, #FF8C5A); color: #fff; padding: 8px 20px; border-radius: 9999px; font-weight: 700; font-size: 13px; text-decoration: none; transition: all 0.2s; white-space: nowrap;" onmouseover="this.style.boxShadow='0 4px 16px rgba(255,107,53,0.35)'" onmouseout="this.style.boxShadow='none'">Valivy Guide</a>
  </div>
</nav>'''

if old not in h:
    print("ERROR: old block not found")
    sys.exit(1)

h = h.replace(old, new)

# Also change the parent nav to grid
h = h.replace(
    'display: flex; align-items: center; justify-content: space-between; padding: 10px 36px;"', 
    'display: grid; grid-template-columns: 1fr auto 1fr; align-items: center; padding: 10px 36px; gap: 24px;"', 1)

# Add justify-content: flex-start to nav-left if not present
h = h.replace(
    '<div class="nav-left" style="display: flex; align-items: center; gap: 14px;">',
    '<div class="nav-left" style="display: flex; align-items: center; gap: 14px; justify-content: flex-start;">', 1)

open(path, "w", encoding="utf-8").write(h)
print(f"Done. size: {len(h)} bytes")
