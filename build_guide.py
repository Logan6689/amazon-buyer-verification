#!/usr/bin/env python3
"""Add Valivy Guide modal to Cash Rush UK landing page."""

import re

with open(r"C:\Users\Administrator.WIN-0V19CGJAQ3O\.qclaw\workspace-agent-e2d75f0a\landing-page\index.html", "r", encoding="utf-8") as f:
    html = f.read()

# ── 1. Insert modal CSS before </style> ──
modal_css = """
  /* ===== Valivy Guide Modal ===== */
  .guide-overlay { position: fixed; inset: 0; z-index: 9999; background: rgba(0,0,0,0.5); display: none; align-items: flex-start; justify-content: center; overflow-y: auto; padding: 20px; }
  .guide-overlay.open { display: flex; }
  .guide-modal { background: #fff; border-radius: 24px; width: 100%; max-width: 780px; margin: 40px auto; box-shadow: 0 20px 60px rgba(0,0,0,0.25); position: relative; overflow: hidden; }
  .guide-modal-close { position: absolute; top: 16px; right: 20px; width: 44px; height: 44px; border-radius: 50%; background: rgba(0,0,0,0.06); border: none; cursor: pointer; display: flex; align-items: center; justify-content: center; font-size: 22px; color: #555; z-index: 10; transition: all 0.2s; }
  .guide-modal-close:hover { background: rgba(0,0,0,0.12); color: #111; }
  .guide-header { background: linear-gradient(135deg, #FF6B35 0%, #FF8C5A 100%); color: #fff; text-align: center; padding: 50px 32px 40px; }
  .guide-header h1 { font-size: 32px; font-weight: 800; margin-bottom: 6px; }
  .guide-header p { font-size: 15px; opacity: 0.92; }
  .guide-body { padding: 36px 32px; }
  .guide-sec { margin-bottom: 40px; }
  .guide-sec:last-child { margin-bottom: 0; }
  .guide-sec-title { font-size: 22px; font-weight: 700; color: #1a1a2e; margin-bottom: 18px; display: flex; align-items: center; gap: 12px; }
  .guide-sec-num { background: #FF6B35; color: #fff; min-width: 36px; height: 36px; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-size: 17px; font-weight: 700; }
  .guide-desc { font-size: 14px; color: #555; line-height: 1.7; margin-bottom: 16px; }
  .guide-highlight { background: #fff3ed; border-left: 4px solid #FF6B35; padding: 14px 18px; border-radius: 6px; font-size: 13px; color: #333; margin: 14px 0; line-height: 1.6; }
  .guide-highlight strong { color: #FF6B35; }
  .guide-money-card { background: linear-gradient(135deg, #6B4EFF 0%, #8B6FFF 100%); border-radius: 16px; padding: 26px 24px; color: #fff; display: flex; gap: 16px; margin: 18px 0; box-shadow: 0 4px 20px rgba(107,78,255,0.2); }
  .guide-money-half { flex: 1; text-align: center; }
  .guide-money-label { font-size: 11px; opacity: 0.85; margin-bottom: 4px; text-transform: uppercase; letter-spacing: 0.5px; }
  .guide-money-value { font-size: 28px; font-weight: 800; margin-bottom: 2px; }
  .guide-money-sub { font-size: 10px; opacity: 0.8; }
  .guide-money-divider { width: 1px; background: rgba(255,255,255,0.3); }
  .guide-gray-box { background: #f8f8fb; border-radius: 10px; padding: 14px 16px; font-size: 13px; color: #555; line-height: 1.7; margin: 12px 0; }
  .guide-ways { margin: 16px 0; }
  .guide-way { background: #fff; border: 2px solid #f0f0f5; border-radius: 14px; padding: 18px; margin-bottom: 12px; display: flex; gap: 14px; align-items: flex-start; }
  .guide-way-num { background: #FF6B35; color: #fff; min-width: 32px; height: 32px; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-weight: 700; font-size: 15px; }
  .guide-way-content h4 { font-size: 14px; font-weight: 700; color: #1a1a2e; margin-bottom: 4px; }
  .guide-way-content p { font-size: 13px; color: #666; line-height: 1.5; }
  .guide-steps { margin: 16px 0; }
  .guide-step { display: flex; gap: 14px; margin-bottom: 14px; align-items: flex-start; }
  .guide-step-num { background: #FF6B35; color: #fff; min-width: 28px; height: 28px; border-radius: 8px; display: flex; align-items: center; justify-content: center; font-weight: 700; font-size: 13px; flex-shrink: 0; }
  .guide-step-text { flex: 1; font-size: 14px; color: #333; line-height: 1.5; padding-top: 3px; }
  .guide-step-text strong { color: #FF6B35; }
  .guide-order-tabs { display: grid; grid-template-columns: repeat(4, 1fr); gap: 10px; margin: 16px 0; }
  .guide-order-tab { background: #fff; border: 2px solid #eee; border-radius: 12px; padding: 16px 8px; text-align: center; }
  .guide-order-tab .icon { font-size: 26px; margin-bottom: 4px; }
  .guide-order-tab .name { font-size: 12px; font-weight: 600; color: #1a1a2e; }
  .guide-order-tab .count { font-size: 10px; color: #888; margin-top: 2px; }
  .guide-order-card { background: #fff; border: 1.5px solid #eee; border-radius: 12px; padding: 16px; margin: 12px 0; }
  .guide-order-head { display: flex; justify-content: space-between; align-items: center; margin-bottom: 10px; padding-bottom: 8px; border-bottom: 1px solid #f0f0f5; }
  .guide-order-status { font-size: 11px; color: #888; font-weight: 600; }
  .guide-order-price { font-size: 13px; font-weight: 700; color: #1a1a2e; }
  .guide-order-body { display: flex; gap: 10px; align-items: center; margin-bottom: 10px; }
  .guide-order-thumb { width: 54px; height: 54px; background: #f8f8fb; border-radius: 8px; display: flex; align-items: center; justify-content: center; font-size: 18px; flex-shrink: 0; }
  .guide-order-info { flex: 1; font-size: 12px; color: #333; }
  .guide-order-info .qty { color: #888; font-size: 11px; margin-top: 2px; }
  .guide-auto-tip { font-size: 11px; color: #FF6B35; margin-top: 6px; }
  .guide-btn-confirm { background: #FF6B35; color: #fff; padding: 7px 16px; border-radius: 8px; font-size: 12px; font-weight: 600; display: inline-block; }
  .guide-arrow-note { display: flex; align-items: center; gap: 10px; background: #fff3ed; border-radius: 8px; padding: 10px 14px; margin: 12px 0; font-size: 13px; color: #333; }
  .guide-arrow-note .arrow { color: #FF6B35; font-size: 16px; font-weight: 700; }
  .guide-red-mark { display: inline-block; background: #ff3b30; color: #fff; font-size: 10px; padding: 2px 6px; border-radius: 3px; margin-left: 6px; }
  .guide-cta-section { background: linear-gradient(135deg, #1a1a2e 0%, #2d2d4a 100%); color: #fff; text-align: center; padding: 48px 32px; border-radius: 0; }
  .guide-cta-section h2 { font-size: 26px; font-weight: 800; margin-bottom: 10px; }
  .guide-cta-section .sub { font-size: 14px; opacity: 0.9; margin-bottom: 24px; }
  .guide-cta-btn { display: inline-block; background: #FF6B35; color: #fff; padding: 16px 44px; border-radius: 50px; font-size: 16px; font-weight: 700; text-decoration: none; box-shadow: 0 8px 30px rgba(255,107,53,0.4); margin-bottom: 12px; }
  .guide-cta-note { font-size: 11px; opacity: 0.7; }
  .guide-proxy-card { background: linear-gradient(135deg, #1a1a2e, #2d2d4a); color: #fff; border-radius: 14px; padding: 22px; text-align: center; margin-bottom: 18px; }
  .guide-proxy-card .tag-row { display: flex; gap: 8px; justify-content: center; margin-top: 12px; flex-wrap: wrap; }
  .guide-proxy-card .tag { background: rgba(255,107,53,0.2); border: 1px solid #FF6B35; padding: 5px 12px; border-radius: 14px; font-size: 11px; }
  .guide-proxy-card .tag2 { background: rgba(255,255,255,0.1); padding: 5px 12px; border-radius: 14px; font-size: 11px; }
  @media (max-width: 768px) {
    .guide-modal { border-radius: 16px; margin: 20px auto; }
    .guide-header { padding: 36px 20px 30px; }
    .guide-header h1 { font-size: 24px; }
    .guide-body { padding: 24px 20px; }
    .guide-order-tabs { grid-template-columns: repeat(2, 1fr); }
    .guide-money-card { flex-direction: column; gap: 12px; }
    .guide-money-divider { width: 100%; height: 1px; }
    .guide-sec-title { font-size: 18px; }
  }
"""
html = html.replace("</style>", modal_css + "\n</style>")

# ── 2. Add "Valivy Guide" link in nav (between nav-links) ──
# Replace the closing of nav-links div to add guide link
old_nav_close = """    <a href="#invite-faq" style="color: #555; text-decoration: none;">Invite & FAQ</a>
  </div>
</nav>"""
new_nav_close = """    <a href="#invite-faq" style="color: #555; text-decoration: none;">Invite & FAQ</a>
    <a href="javascript:void(0)" onclick="openGuide()" style="background: linear-gradient(135deg, #FF6B35, #FF8C5A); color: #fff; padding: 8px 20px; border-radius: 9999px; font-weight: 700; font-size: 13px; text-decoration: none; transition: all 0.2s;" onmouseover="this.style.boxShadow='0 4px 16px rgba(255,107,53,0.35)'" onmouseout="this.style.boxShadow='none'">Valivy Guide</a>
  </div>
</nav>"""
html = html.replace(old_nav_close, new_nav_close)

# ── 3. Build the modal HTML ──
modal_html = """
<!-- ===== Valivy Guide Modal ===== -->
<div class="guide-overlay" id="guideOverlay" onclick="if(event.target===this) closeGuide()">
  <div class="guide-modal" id="guideModal">
    <button class="guide-modal-close" onclick="closeGuide()" aria-label="Close">×</button>

    <!-- Header -->
    <div class="guide-header">
      <h1>Your Valivy Guide</h1>
      <p>Everything you need to know — in one page</p>
    </div>

    <div class="guide-body">

      <!-- 1. Your Account -->
      <div class="guide-sec">
        <div class="guide-sec-title"><span class="guide-sec-num">1</span> Your Account</div>
        <div style="background:#fff; border:1px solid #eee; border-radius:14px; padding:20px;">
          <div style="display:flex; align-items:center; gap:14px; padding-bottom:16px; border-bottom:1px solid #f0f0f5;">
            <div style="width:52px; height:52px; background:linear-gradient(135deg,#FF6B35,#FF8C5A); border-radius:50%; display:flex; align-items:center; justify-content:center; color:#fff; font-size:22px; font-weight:700;">L</div>
            <div style="flex:1;">
              <div style="font-size:16px; font-weight:700; color:#1a1a2e;">Your Profile</div>
              <div style="display:flex; align-items:center; gap:8px; margin-top:4px;">
                <span style="font-size:13px; color:#FF6B35; font-weight:600; border:2px dashed #FF6B35; padding:2px 10px; border-radius:6px;">@YourID</span>
                <span style="background:#1a1a2e; color:#fff; font-size:10px; padding:3px 8px; border-radius:10px;">Member</span>
              </div>
            </div>
          </div>
          <div class="guide-arrow-note">
            <span class="arrow">←</span>
            <span><strong>This is your unique ID</strong> — share with customer service</span>
          </div>
        </div>
      </div>

      <!-- 2. Two Types of Money -->
      <div class="guide-sec">
        <div class="guide-sec-title"><span class="guide-sec-num">2</span> Two Types of Money</div>
        <p class="guide-desc">Your account has two balances. Here's the difference:</p>
        <div class="guide-money-card">
          <div class="guide-money-half">
            <div class="guide-money-label">Available Balance</div>
            <div class="guide-money-value">£94.00</div>
            <div class="guide-money-sub">✓ Spend &nbsp; ✓ Withdraw</div>
          </div>
          <div class="guide-money-divider"></div>
          <div class="guide-money-half">
            <div class="guide-money-label">Points</div>
            <div class="guide-money-value">145,806</div>
            <div class="guide-money-sub">✓ Spend &nbsp; ✗ No withdraw</div>
          </div>
        </div>
        <div class="guide-gray-box">
          <strong>💡 How to get each:</strong><br><br>
          <strong>Balance:</strong> Earn via eBay business · Top up via PayPal<br>
          <strong>Points:</strong> Submit Amazon orders · Invite friends · Channel events<br>
          <strong style="color:#FF6B35;">100 Points = £1</strong>
        </div>
      </div>

      <!-- 3. Track Your Orders -->
      <div class="guide-sec">
        <div class="guide-sec-title"><span class="guide-sec-num">3</span> Track Your Orders</div>
        <p class="guide-desc">Four status tabs to keep you in the loop:</p>
        <div class="guide-order-tabs">
          <div class="guide-order-tab"><div class="icon">⏱️</div><div class="name">Unpaid</div></div>
          <div class="guide-order-tab" style="border-color:#FF6B35;"><div class="icon">🚚</div><div class="name">In progress</div><div class="count">2 active</div></div>
          <div class="guide-order-tab"><div class="icon">📦</div><div class="name">Completed</div></div>
          <div class="guide-order-tab"><div class="icon">⭐</div><div class="name">Review</div></div>
        </div>
      </div>

      <!-- 4. Earn Points - 3 Ways -->
      <div class="guide-sec">
        <div class="guide-sec-title"><span class="guide-sec-num">4</span> Earn Points — 3 Ways</div>
        <div class="guide-ways">
          <div class="guide-way">
            <div class="guide-way-num">1</div>
            <div class="guide-way-content">
              <h4>Submit Amazon Orders</h4>
              <p>Have an Amazon UK order number? Send it to customer service on Telegram. Earn points per valid order.</p>
            </div>
          </div>
          <div class="guide-way">
            <div class="guide-way-num">2</div>
            <div class="guide-way-content">
              <h4>Invite Friends</h4>
              <p>When your invited friends submit their valid Amazon orders, you earn points for each one.</p>
            </div>
          </div>
          <div class="guide-way">
            <div class="guide-way-num">3</div>
            <div class="guide-way-content">
              <h4>Weekly Channel Giveaways</h4>
              <p>Every Wednesday we drop free points. Plus bonus events throughout the week. Don't miss out!</p>
            </div>
          </div>
        </div>
      </div>

      <!-- 5. 20% Off Proxy Shopping -->
      <div class="guide-sec">
        <div class="guide-sec-title"><span class="guide-sec-num">5</span> Amazon UK — 20% Off Proxy Shopping</div>
        <div class="guide-proxy-card">
          <div style="font-size:12px; opacity:0.8; letter-spacing:1px;">UK PROXY SHOPPING</div>
          <div style="font-size:26px; font-weight:800; margin:6px 0;">Amazon UK</div>
          <div style="font-size:12px; opacity:0.9;">Buy & Ship Worldwide</div>
          <div class="tag-row">
            <span class="tag">20% Off</span>
            <span class="tag2">Direct Shipping</span>
            <span class="tag2">Duty Support</span>
          </div>
        </div>
        <div class="guide-steps">
          <div class="guide-step"><div class="guide-step-num">1</div><div class="guide-step-text">Submit the <strong>product link</strong> on Valivy.com</div></div>
          <div class="guide-step"><div class="guide-step-num">2</div><div class="guide-step-text">We place the order via <strong>Amazon UK</strong> for you</div></div>
          <div class="guide-step"><div class="guide-step-num">3</div><div class="guide-step-text">You pay <strong>80% of the listed price</strong> — that's it. No shipping, no duty (we cover those)</div></div>
          <div class="guide-step"><div class="guide-step-num">4</div><div class="guide-step-text">Pay with <strong>Points</strong> or <strong>Balance</strong> — use Points on the payment page to offset your total (100 points = £1)</div></div>
          <div class="guide-step"><div class="guide-step-num">5</div><div class="guide-step-text">Parcel arrives within <strong>72 hours</strong></div></div>
        </div>
      </div>

      <!-- 6. Track Your Order - Details -->
      <div class="guide-sec">
        <div class="guide-sec-title"><span class="guide-sec-num">6</span> Track Your Order</div>
        <p class="guide-desc">All your orders live here. Find "My orders" in the app.</p>
        <div style="background:#1a1a2e; color:#fff; padding:12px 18px; font-weight:600; font-size:15px; border-radius:10px 10px 0 0;">My orders</div>
        <div style="display:flex; gap:0; background:#f8f8fb; padding:0 18px; border:1px solid #eee; border-top:none;">
          <div style="padding:12px 6px; font-size:11px; color:#888;">Pending payment</div>
          <div style="padding:12px 6px; font-size:11px; color:#888;">Pending shipment</div>
          <div style="padding:12px 6px; font-size:11px; color:#FF6B35; font-weight:700; border-bottom:2px solid #FF6B35;">Pending receipt</div>
          <div style="padding:12px 6px; font-size:11px; color:#888;">To review</div>
        </div>
        <div class="guide-order-card" style="border-top:none;">
          <div class="guide-order-head">
            <div class="guide-order-status">Processing, shipped</div>
            <div class="guide-order-price">Total 1 item(s): <span style="color:#FF6B35;">£0.00</span></div>
          </div>
          <div class="guide-order-body">
            <div class="guide-order-thumb">📦</div>
            <div class="guide-order-info"><div style="font-weight:600;">Amazon Order Placement</div><div class="qty">× 5</div></div>
          </div>
          <div class="guide-auto-tip">Order will be auto-confirmed in 4 day(s)</div>
          <div style="text-align:right; margin-top:8px;"><span class="guide-btn-confirm">Confirm receipt</span></div>
        </div>
        <div class="guide-order-card">
          <div class="guide-order-head">
            <div class="guide-order-status">Processing, shipped</div>
            <div class="guide-order-price">Total 1 item(s): <span style="color:#FF6B35;">£3.00</span></div>
          </div>
          <div class="guide-order-body">
            <div class="guide-order-thumb">🎁</div>
            <div class="guide-order-info"><div style="font-weight:600;">£1 Amazon Shopping Credit</div><div class="qty">× 3</div></div>
          </div>
          <div style="text-align:right; margin-top:8px;"><span class="guide-btn-confirm">Confirm receipt</span></div>
        </div>
      </div>

      <!-- 7. Need Help? -->
      <div class="guide-sec">
        <div class="guide-sec-title"><span class="guide-sec-num">7</span> Need Help?</div>
        <div class="guide-highlight">
          <strong>⚠️ Any issues with your order?</strong><br>
          Send your <strong>order number</strong> to customer service on Telegram <strong>@amazonclub16</strong>. We'll check it for you.
        </div>
        <div class="guide-gray-box">
          💡 <strong>Tip:</strong> Orders auto-confirm in 4 days. Tap "Confirm receipt" right after you receive your parcel.
        </div>
      </div>

    </div>

    <!-- CTA -->
    <div class="guide-cta-section">
      <h2>Ready to Start?</h2>
      <p class="sub">Register now and get 500 FREE welcome points</p>
      <a href="https://www.valivy.com/" class="guide-cta-btn" target="_blank">Register Now → valivy.com</a>
      <div class="guide-cta-note">After sign-up, message @amazonclub16 your username to claim your 500 points</div>
    </div>

  </div>
</div>
"""
# Insert before </footer> or </body>
html = html.replace("</footer>", "</footer>" + modal_html)

# ── 4. Add JS functions for open/close ──
modal_js = """
function openGuide() {
  document.getElementById('guideOverlay').classList.add('open');
  document.body.style.overflow = 'hidden';
}
function closeGuide() {
  document.getElementById('guideOverlay').classList.remove('open');
  document.body.style.overflow = '';
}
// Close on Esc
document.addEventListener('keydown', function(e) {
  if (e.key === 'Escape') closeGuide();
});
"""
html = html.replace("</script>", "\n" + modal_js + "\n</script>")

# Write
with open(r"C:\Users\Administrator.WIN-0V19CGJAQ3O\.qclaw\workspace-agent-e2d75f0a\landing-page\index.html", "w", encoding="utf-8") as f:
    f.write(html)

print("Done. Guide modal added to index.html")
print(f"File size: {len(html)} bytes")
