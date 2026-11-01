# aashifx.com

AashiFX™ · Creative Studio with Soul · Brand-to-Business Integrator.
Six pillars: BrandX, OfficeX, TechX, TradeX, DriveX, PowerX. India and the GCC.

Static site: plain HTML/CSS/JS served as-is. Light and dark themes, EN/AR (RTL).

## Structure
- `index.html`, `services.html`, `atlas.html`, `portfolio.html`, `about.html`, `contact.html`
- 6 pillar pages (`brandx.html` ...) and 48 sub-service pages (`brandx-logo-identity.html` ...)
- `assets/style.css`: all styles, tokenised light and dark palettes
- `assets/app.js`: EN/AR toggle, theme toggle, WhatsApp links (`WA_NUMBER`), ATLAS tabs. Holds all copy.
- `assets/art/`: generated SVG illustrations (one per page)
- `tools/`: generators. `tools/build_site.py` writes every page and `assets/app.js`; `tools/modern_art.py` draws all artwork (aurora glow, gold contours, glass cards, line icons); `tools/subservices.py` holds sub-service copy.

## Rebuild
```bash
python3 tools/build_site.py
```
Edit copy in `tools/build_site.py` / `tools/subservices.py`, artwork in `tools/modern_art.py`, styles in `assets/style.css`. Do not hand-edit generated `.html` or `assets/app.js`.

## Preview
```bash
python3 -m http.server 8000
```
