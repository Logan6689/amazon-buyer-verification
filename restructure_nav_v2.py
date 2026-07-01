#!/usr/bin/env python3
import sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

path = r"C:\Users\Administrator.WIN-0V19CGJAQ3O\.qclaw\workspace-agent-e2d75f0a\landing-page\index.html"
h = open(path, encoding='utf-8').read()

old = '''<nav class="top-nav" style="position: fixed; top: 0; left: 0; right: 0; z-index: 1000; background: rgba(255,255,255,0.97); backdrop-filter: blur(16px); border-bottom: 1px solid #f0f0f0; display: grid; grid-template-columns: 1fr auto 1fr; align-items: center; padding: 10px 36px; gap: 24px;">
  <div class="nav-left" style="display: flex; align-items: center; gap: 14px; justify-content: flex-start;">
    <svg viewBox="0 0 24 24" width="48" height="48" fill="#f59e0b" style="flex-shrink: 0; filter: drop-shadow(0 2px 4px rgba(245,158,11,0.3));"><circle cx="12" cy="12" r="10" fill="url(#coinGrad)"/><defs><linearGradient id="coinGrad" x1="0%" y1="0%" x2="100%" y2="100%"><stop offset="0%" style="stop-color:#fbbf24"/><stop offset="100%" style="stop-color:#f59e0b"/></linearGradient></defs><text x="12" y="16" text-anchor="middle" fill="#fff" font-size="12" font-weight="bold">£</text></svg>
    <span style="font-size: 18px; color: #111; font-weight: 700;">Cash Rush UK</span>
  </div>
  <div class="nav-links" style="display: flex; gap: 28px; font-size: 14px; font-weight: 500; justify-content: center;">
    <a href="#how" style="color: #555; text-decoration: none;">Activities</a>
    <a href="#agent" style="color: #555; text-decoration: none;">Purchase Agent</a>
    <a href="#invite-faq" style="color: #555; text-decoration: none;">Invite & FAQ</a>
  </div>
  <div class="nav-right" style="display: flex; justify-content: flex-end; align-items: center;">
    <a href="javascript:void(0)" onclick="openGuide()" class="nav-guide-btn" style="background: linear-gradient(135deg, #FF6B35, #FF8C5A); color: #fff; padding: 8px 20px; border-radius: 9999px; font-weight: 700; font-size: 13px; text-decoration: none; transition: all 0.2s; white-space: nowrap;" onmouseover="this.style.boxShadow='0 4px 16px rgba(255,107,53,0.35)'" onmouseout="this.style.boxShadow='none'">Valivy Guide</a>
  </div>
</nav>'''

new = '''<nav class="top-nav" style="position: fixed; top: 0; left: 0; right: 0; z-index: 1000; background: rgba(255,255,255,0.97); backdrop-filter: blur(16px); border-bottom: 1px solid #f0f0f0; padding: 10px 36px;">
  <div class="nav-top-row" style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 8px;">
    <div class="nav-left" style="display: flex; align-items: center; gap: 14px;">
      <svg viewBox="0 0 24 24" width="48" height="48" fill="#f59e0b" style="flex-shrink: 0; filter: drop-shadow(0 2px 4px rgba(245,158,11,0.3));"><circle cx="12" cy="12" r="10" fill="url(#coinGrad)"/><defs><linearGradient id="coinGrad" x1="0%" y1="0%" x2="100%" y2="100%"><stop offset="0%" style="stop-color:#fbbf24"/><stop offset="100%" style="stop-color:#f59e0b"/></linearGradient></defs><text x="12" y="16" text-anchor="middle" fill="#fff" font-size="12" font-weight="bold">£</text></svg>
      <span style="font-size: 18px; color: #111; font-weight: 700;">Cash Rush UK</span>
    </div>
    <div class="nav-right">
      <a href="javascript:void(0)" onclick="openGuide()" class="nav-guide-btn" style="background: linear-gradient(135deg, #FF6B35, #FF8C5A); color: #fff; padding: 8px 20px; border-radius: 9999px; font-weight: 700; font-size: 13px; text-decoration: none; transition: all 0.2s; white-space: nowrap;" onmouseover="this.style.boxShadow='0 4px 16px rgba(255,107,53,0.35)'" onmouseout="this.style.boxShadow='none'">Valivy Guide</a>
    </div>
  </div>
  <div class="nav-links" style="display: flex; gap: 28px; font-size: 14px; font-weight: 500; justify-content: center; padding-top: 6px; border-top: 1px solid #f0f0f0;">
    <a href="#how" style="color: #555; text-decoration: none;">Activities</a>
    <a href="#agent" style="color: #555; text-decoration: none;">Purchase Agent</a>
    <a href="#invite-faq" style="color: #555; text-decoration: none;">Invite & FAQ</a>
  </div>
</nav>'''

if old not in h:
    print("ERROR: old nav not found")
    sys.exit(1)

h = h.replace(old, new)
open(path, "w", encoding="utf-8").write(h)
print(f"Done. size: {len(h)} bytes")
