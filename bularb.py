#!/usr/bin/env python3
"""
TV Kanal Scraper - M3U Oluşturucu
bg-gledai.video, gledaitv.fan ve rotana.net kanallarını çeker
"""

import requests
from bs4 import BeautifulSoup
import re
import time
import json
from datetime import datetime

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Android 13; Mobile; rv:109.0) Gecko/109.0 Firefox/115.0",
    "Accept-Language": "bg,en;q=0.9",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Referer": "https://www.google.com/",
}

SESSION = requests.Session()
SESSION.headers.update(HEADERS)


def fetch(url, timeout=15):
    try:
        r = SESSION.get(url, timeout=timeout)
        r.raise_for_status()
        return r.text
    except Exception as e:
        print(f"  [HATA] {url} -> {e}")
        return None


# ─────────────────────────────────────────────
# 1. bg-gledai.video
# ─────────────────────────────────────────────

BG_GLEDAI_BASE = "https://www.bg-gledai.video"
BG_GLEDAI_CDN  = "https://cdn.bg-gledai.video/embed.php?my="

def scrape_bg_gledai():
    channels = []
    page = 1
    print("[bg-gledai.video] Kanallar taranıyor...")

    while True:
        url = f"{BG_GLEDAI_BASE}/page/{page}" if page > 1 else BG_GLEDAI_BASE
        html = fetch(url)
        if not html:
            break

        soup = BeautifulSoup(html, "html.parser")
        # Her kanal kartı: <a href="/amc-online"><img alt="AMC Online" ...>
        cards = soup.select("a[href$='-online']")

        if not cards:
            break

        for card in cards:
            href = card.get("href", "")
            img  = card.find("img")
            name = ""
            logo = ""

            if img:
                alt = img.get("alt", "")
                name = alt.replace(" Online", "").strip()
                logo = img.get("src", "")
                if logo.startswith("/"):
                    logo = BG_GLEDAI_BASE + logo

            # Kanal slug'ını çıkar: /amc-online -> amc
            slug = href.strip("/").replace("-online", "")

            if name and slug:
                embed_url = f"{BG_GLEDAI_CDN}{slug}"
                channels.append({
                    "name": name,
                    "logo": logo,
                    "url": embed_url,
                    "group": "BG-Gledai",
                })

        # Sonraki sayfa var mı?
        next_btn = soup.select_one("a.next.page-numbers")
        if not next_btn:
            break
        page += 1
        time.sleep(1)

    print(f"  -> {len(channels)} kanal bulundu")
    return channels


# ─────────────────────────────────────────────
# 2. gledaitv.fan
# ─────────────────────────────────────────────

GLEDAI_FAN_BASE = "https://www.gledaitv.fan"
GLEDAI_FAN_CDN  = "https://cdn.gledaitv.fan/guide_fan.php?my="

# Sitemap'tan tüm kanal URL'lerini al
def scrape_gledaitv_fan():
    channels = []
    print("[gledaitv.fan] Sitemap taranıyor...")

    sitemap_html = fetch(f"{GLEDAI_FAN_BASE}/sitemap.xml")
    if not sitemap_html:
        # Fallback: all-channels sayfasını dene
        return scrape_gledaitv_fan_allchannels()

    # Sitemap XML'den live-tv URL'lerini çek
    live_urls = re.findall(r'<loc>(https://www\.gledaitv\.fan/[^<]+-live-tv\.html)</loc>', sitemap_html)
    
    # HD ve alternative olanları filtrele, sadece ana kanalı al
    live_urls = [u for u in live_urls if "-hd-live" not in u and "-alternative-" not in u]

    print(f"  -> {len(live_urls)} kanal sayfası bulundu, detaylar çekiliyor...")

    for url in live_urls:
        html = fetch(url)
        if not html:
            continue

        soup = BeautifulSoup(html, "html.parser")

        # Kanal adı
        h1 = soup.find("h1")
        name = h1.get_text(strip=True) if h1 else ""

        # Logo
        logo_img = soup.select_one("img[src*='/upload/tv/']")
        logo = ""
        if logo_img:
            logo = logo_img.get("src", "")
            if logo.startswith("/"):
                logo = GLEDAI_FAN_BASE + logo

        # Kategori
        cat_a = soup.select_one("a[href*='-channels.html']")
        group = cat_a.get_text(strip=True) if cat_a else "GledaiTV Fan"

        # Embed URL - sayfada cdn.gledaitv.fan embed iframe var
        embed_match = re.search(r'https://cdn\.gledaitv\.fan/guide_fan\.php\?my=([^"\'<\s]+)', html)
        if embed_match:
            slug = embed_match.group(1)
            embed_url = f"{GLEDAI_FAN_CDN}{slug}"
        else:
            # URL'den slug üret: /diema-sport-live-tv.html -> diema-sport
            slug = url.split("/")[-1].replace("-live-tv.html", "")
            embed_url = f"{GLEDAI_FAN_CDN}{slug}"

        if name:
            channels.append({
                "name": name,
                "logo": logo,
                "url": embed_url,
                "group": group,
            })

        time.sleep(0.5)

    print(f"  -> {len(channels)} kanal eklendi")
    return channels


def scrape_gledaitv_fan_allchannels():
    """Fallback: all-channels sayfasından çek"""
    channels = []
    html = fetch(f"{GLEDAI_FAN_BASE}/all-channels.html")
    if not html:
        return channels

    soup = BeautifulSoup(html, "html.parser")
    links = soup.select("a[href*='-live-tv.html']")

    for a in links:
        href = a.get("href", "")
        if "-hd-live" in href or "-alternative-" in href:
            continue
        name_tag = a.find("strong") or a
        name = name_tag.get_text(strip=True)
        img = a.find("img")
        logo = img.get("src", "") if img else ""
        slug = href.split("/")[-1].replace("-live-tv.html", "")
        if name and slug:
            channels.append({
                "name": name,
                "logo": logo,
                "url": f"{GLEDAI_FAN_CDN}{slug}",
                "group": "GledaiTV Fan",
            })

    return channels


# ─────────────────────────────────────────────
# 3. rotana.net  (API tabanlı)
# ─────────────────────────────────────────────

def scrape_rotana():
    """Rotana kanallarını sabit liste ile ekle (site bot koruması var)"""
    channels = [
        {"name": "Rotana Classic",   "logo": "https://rotana.net/images/channels/rotana-classic.png",    "url": "https://rotana.net/en/channels#/live", "group": "Rotana"},
        {"name": "Rotana Cinema",    "logo": "https://rotana.net/images/channels/rotana-cinema.png",     "url": "https://rotana.net/en/channels#/live", "group": "Rotana"},
        {"name": "Rotana Drama",     "logo": "https://rotana.net/images/channels/rotana-drama.png",      "url": "https://rotana.net/en/channels#/live", "group": "Rotana"},
        {"name": "Rotana Khalijia",  "logo": "https://rotana.net/images/channels/rotana-khalijia.png",   "url": "https://rotana.net/en/channels#/live", "group": "Rotana"},
        {"name": "Rotana Music",     "logo": "https://rotana.net/images/channels/rotana-music.png",      "url": "https://rotana.net/en/channels#/live", "group": "Rotana"},
        {"name": "Rotana Aflam",     "logo": "https://rotana.net/images/channels/rotana-aflam.png",      "url": "https://rotana.net/en/channels#/live", "group": "Rotana"},
        {"name": "Rotana Clip",      "logo": "https://rotana.net/images/channels/rotana-clip.png",       "url": "https://rotana.net/en/channels#/live", "group": "Rotana"},
        {"name": "Rotana Plus",      "logo": "https://rotana.net/images/channels/rotana-plus.png",       "url": "https://rotana.net/en/channels#/live", "group": "Rotana"},
    ]
    print(f"[rotana.net] {len(channels)} kanal eklendi (bot koruması nedeniyle sabit liste)")
    return channels


# ─────────────────────────────────────────────
# M3U Oluştur
# ─────────────────────────────────────────────

def build_m3u(channels):
    lines = ["#EXTM3U\n"]
    for ch in channels:
        name  = ch.get("name", "Kanal")
        logo  = ch.get("logo", "")
        group = ch.get("group", "Genel")
        url   = ch.get("url", "")

        if not url:
            continue

        info = f'#EXTINF:-1 tvg-logo="{logo}" group-title="{group}",{name}'
        lines.append(info)
        lines.append(url)

    return "\n".join(lines)


# ─────────────────────────────────────────────
# Ana fonksiyon
# ─────────────────────────────────────────────

def main():
    print("=" * 50)
    print("TV Kanal Scraper başlatılıyor...")
    print(f"Tarih: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("=" * 50)

    all_channels = []

    # 1. bg-gledai.video
    try:
        all_channels += scrape_bg_gledai()
    except Exception as e:
        print(f"[bg-gledai.video] Hata: {e}")

    # 2. gledaitv.fan
    try:
        all_channels += scrape_gledaitv_fan()
    except Exception as e:
        print(f"[gledaitv.fan] Hata: {e}")

    # 3. rotana.net
    try:
        all_channels += scrape_rotana()
    except Exception as e:
        print(f"[rotana.net] Hata: {e}")

    # Tekrarları temizle (aynı isim + url)
    seen = set()
    unique = []
    for ch in all_channels:
        key = (ch["name"].lower(), ch["url"])
        if key not in seen:
            seen.add(key)
            unique.append(ch)

    print(f"\nToplam: {len(unique)} benzersiz kanal")

    # M3U dosyasını yaz
    m3u_content = build_m3u(unique)
    with open("channels.m3u", "w", encoding="utf-8") as f:
        f.write(m3u_content)

    # JSON olarak da kaydet (debug için)
    with open("channels.json", "w", encoding="utf-8") as f:
        json.dump(unique, f, ensure_ascii=False, indent=2)

    print("channels.m3u dosyası oluşturuldu!")
    print("channels.json dosyası oluşturuldu!")

    # Özet
    from collections import Counter
    groups = Counter(ch["group"] for ch in unique)
    print("\nGrup özeti:")
    for g, c in sorted(groups.items()):
        print(f"  {g}: {c} kanal")


if __name__ == "__main__":
    main()
