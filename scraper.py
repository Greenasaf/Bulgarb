#!/usr/bin/env python3
"""
TV Kanal Scraper - M3U Oluşturucu (v3)
bg-gledai.video, gledaitv.fan ve rotana.net kanallarını çeker.
"""

import requests
from bs4 import BeautifulSoup
import re
import time
import json
import base64
from datetime import datetime

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Android 13; Mobile; rv:109.0) Gecko/109.0 Firefox/115.0",
    "Accept-Language": "bg,en;q=0.9",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
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


def extract_stream_url(html):
    yt = re.search(r'youtube\.com/embed/([A-Za-z0-9_\-]{11})', html)
    if yt:
        return f"https://www.youtube.com/watch?v={yt.group(1)}"
    m3u8 = re.search(r'(https?://[^\s"\'<>]+\.m3u8[^\s"\'<>]*)', html)
    if m3u8:
        return m3u8.group(1)
    mp4 = re.search(r'(https?://[^\s"\'<>]+\.mp4[^\s"\'<>]*)', html)
    if mp4:
        return mp4.group(1)
    dm = re.search(r'dailymotion\.com/embed/video/([A-Za-z0-9]+)', html)
    if dm:
        return f"https://www.dailymotion.com/video/{dm.group(1)}"
    tw = re.search(r'player\.twitch\.tv/\?channel=([A-Za-z0-9_]+)', html)
    if tw:
        return f"https://www.twitch.tv/{tw.group(1)}"
    return None


# ─────────────────────────────────────────────
# 1. bg-gledai.video
# ─────────────────────────────────────────────

BG_BASE = "https://www.bg-gledai.video"

def scrape_bg_gledai():
    channels = []
    page = 1
    print("[bg-gledai.video] Kanallar taranıyor...")

    while True:
        url = f"{BG_BASE}/page/{page}" if page > 1 else BG_BASE
        html = fetch(url)
        if not html:
            break

        soup = BeautifulSoup(html, "html.parser")
        cards = soup.select("a[href$='-online']")
        if not cards:
            break

        new_found = 0
        for card in cards:
            href = card.get("href", "")
            if not href or href.startswith("http"):
                continue
            img = card.find("img")
            if not img:
                continue
            alt = img.get("alt", "")
            name = alt.replace(" Online", "").strip()
            logo = img.get("src", "")
            if logo.startswith("/"):
                logo = BG_BASE + logo

            page_url = BG_BASE + href if href.startswith("/") else href
            ch_html = fetch(page_url)
            stream_url = extract_stream_url(ch_html) if ch_html else None

            if name and stream_url:
                channels.append({"name": name, "logo": logo, "url": stream_url, "group": "BG-Gledai"})
                print(f"  ✓ {name} -> {stream_url[:60]}")
                new_found += 1
            elif name:
                print(f"  ✗ {name} -> stream bulunamadı, atlandı")
            time.sleep(0.7)

        if new_found == 0:
            break
        if not soup.select_one("a.next.page-numbers"):
            break
        page += 1
        time.sleep(1)

    print(f"  -> Toplam {len(channels)} kanal eklendi")
    return channels


# ─────────────────────────────────────────────
# 2. gledaitv.fan
# ─────────────────────────────────────────────

FAN_BASE = "https://www.gledaitv.fan"

def scrape_gledaitv_fan():
    channels = []
    print("[gledaitv.fan] Sitemap taranıyor...")

    sitemap = fetch(f"{FAN_BASE}/sitemap.xml")
    if sitemap:
        live_urls = re.findall(r'<loc>(https://www\.gledaitv\.fan/[^<]+-live-tv\.html)</loc>', sitemap)
        live_urls = [u for u in live_urls if "-hd-live" not in u and "-alternative-" not in u]
    else:
        html = fetch(f"{FAN_BASE}/all-channels.html")
        if not html:
            return channels
        soup = BeautifulSoup(html, "html.parser")
        live_urls = []
        for a in soup.select("a[href*='-live-tv.html']"):
            href = a.get("href", "")
            if "-hd-live" not in href and "-alternative-" not in href:
                live_urls.append(href if href.startswith("http") else FAN_BASE + href)

    print(f"  -> {len(live_urls)} kanal sayfası bulundu")

    for url in live_urls:
        html = fetch(url)
        if not html:
            continue
        soup = BeautifulSoup(html, "html.parser")
        h1 = soup.find("h1")
        name = h1.get_text(strip=True) if h1 else ""
        logo_img = soup.select_one("img[src*='/upload/tv/']")
        logo = ""
        if logo_img:
            logo = logo_img.get("src", "")
            if not logo.startswith("http"):
                logo = FAN_BASE + logo
        cat_a = soup.select_one("a[href*='-channels.html']")
        group = cat_a.get_text(strip=True) if cat_a else "GledaiTV Fan"

        iframe = soup.find("iframe")
        iframe_src = iframe.get("src", "") if iframe else ""
        stream_url = None

        if iframe_src:
            if "youtube.com" in iframe_src:
                yt = re.search(r'embed/([A-Za-z0-9_\-]{11})', iframe_src)
                if yt:
                    stream_url = f"https://www.youtube.com/watch?v={yt.group(1)}"
            elif "gledaitv.fan/live/" in iframe_src or iframe_src.endswith(".html"):
                if not iframe_src.startswith("http"):
                    iframe_src = FAN_BASE + iframe_src
                inner_html = fetch(iframe_src)
                if inner_html:
                    stream_url = extract_stream_url(inner_html)
            else:
                stream_url = extract_stream_url(iframe_src)

        if not stream_url:
            stream_url = extract_stream_url(html)

        if name and stream_url:
            channels.append({"name": name, "logo": logo, "url": stream_url, "group": group})
            print(f"  ✓ {name} -> {stream_url[:60]}")
        elif name:
            print(f"  ✗ {name} -> stream bulunamadı, atlandı")
        time.sleep(0.7)

    print(f"  -> Toplam {len(channels)} kanal eklendi")
    return channels


# ─────────────────────────────────────────────
# 3. rotana.net  —  hibridcdn API ile token al
# ─────────────────────────────────────────────

ROTANA_CHANNELS = [
    {"slug": "rotana-classical",  "name": "Rotana Classic",    "logo": "https://rotana.net/assets/themes/TriTheme/images/channels/classic.png"},
    {"slug": "rotana-cinema",     "name": "Rotana Cinema",     "logo": "https://rotana.net/assets/themes/TriTheme/images/channels/cinema.png"},
    {"slug": "rotana-drama",      "name": "Rotana Drama",      "logo": "https://rotana.net/assets/themes/TriTheme/images/channels/drama.png"},
    {"slug": "rotana-khaleejiya", "name": "Rotana Khalijia",   "logo": "https://rotana.net/assets/themes/TriTheme/images/channels/khaleejiya.png"},
    {"slug": "rotana-music",      "name": "Rotana Music",      "logo": "https://rotana.net/assets/themes/TriTheme/images/channels/music.png"},
    {"slug": "rotana-clip",       "name": "Rotana Clip",       "logo": "https://rotana.net/assets/themes/TriTheme/images/channels/clip.png"},
    {"slug": "rotana-aflam",      "name": "Rotana Aflam",      "logo": "https://rotana.net/assets/themes/TriTheme/images/channels/aflam.png"},
    {"slug": "rotana-comedy",     "name": "Rotana Comedy",     "logo": "https://rotana.net/assets/themes/TriTheme/images/channels/comedy.png"},
    {"slug": "rotana-kids",       "name": "Rotana Kids",       "logo": "https://rotana.net/assets/themes/TriTheme/images/channels/kids.png"},
]

def get_rotana_stream(slug):
    """
    hibridcdn API'sinden token'lı m3u8 URL'si alır.
    API yanıtı base64 kodlu JS parçaları içeriyor; decode edince JSON geliyor.
    """
    ts = int(time.time() * 1000)
    api_url = f"https://hiplayer.hibridcdn.net/l/{slug}?_={ts}"
    try:
        r = SESSION.get(api_url, timeout=15,
                        headers={"Referer": "https://rotana.net/", "Origin": "https://rotana.net"})
        text = r.text

        # base64 parçalarını bul (uzun eYJ... ile başlayan)
        segments = re.findall(r"['\"]([A-Za-z0-9+/=]{40,})['\"]", text)
        for seg in segments:
            # padding düzelt
            padding = 4 - len(seg) % 4
            if padding != 4:
                seg += "=" * padding
            try:
                decoded = base64.b64decode(seg).decode("utf-8", errors="ignore")
                if "streamUrl" in decoded:
                    data = json.loads(decoded)
                    return data.get("streamUrl") or data.get("stream_url")
            except Exception:
                continue

        # Doğrudan m3u8 ara
        m3u8 = re.search(r'(https?://[^\s"\'<>]+\.m3u8[^\s"\'<>]*)', text)
        if m3u8:
            return m3u8.group(1)

    except Exception as e:
        print(f"    [HATA] {slug}: {e}")
    return None


def scrape_rotana():
    channels = []
    print("[rotana.net] Kanallar alınıyor (hibridcdn API)...")

    for ch in ROTANA_CHANNELS:
        stream_url = get_rotana_stream(ch["slug"])
        if stream_url:
            channels.append({
                "name": ch["name"],
                "logo": ch["logo"],
                "url": stream_url,
                "group": "Rotana",
            })
            print(f"  ✓ {ch['name']} -> {stream_url[:60]}")
        else:
            print(f"  ✗ {ch['name']} -> stream alınamadı, atlandı")
        time.sleep(1)

    print(f"  -> Toplam {len(channels)} Rotana kanalı eklendi")
    return channels


# ─────────────────────────────────────────────
# M3U Oluştur
# ─────────────────────────────────────────────

def build_m3u(channels):
    lines = ["#EXTM3U"]
    for ch in channels:
        name  = ch.get("name", "Kanal")
        logo  = ch.get("logo", "")
        group = ch.get("group", "Genel")
        url   = ch.get("url", "")
        if not url:
            continue
        lines.append(f'#EXTINF:-1 tvg-logo="{logo}" group-title="{group}",{name}')
        lines.append(url)
    return "\n".join(lines)


# ─────────────────────────────────────────────
# Ana
# ─────────────────────────────────────────────

def main():
    print("=" * 55)
    print("TV Kanal Scraper v3 başlatılıyor...")
    print(f"Tarih: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("=" * 55)

    all_channels = []

    try:
        all_channels += scrape_bg_gledai()
    except Exception as e:
        print(f"[bg-gledai] Genel hata: {e}")

    try:
        all_channels += scrape_gledaitv_fan()
    except Exception as e:
        print(f"[gledaitv.fan] Genel hata: {e}")

    try:
        all_channels += scrape_rotana()
    except Exception as e:
        print(f"[rotana] Genel hata: {e}")

    # Tekrar temizle
    seen = set()
    unique = []
    for ch in all_channels:
        key = ch["url"]
        if key not in seen:
            seen.add(key)
            unique.append(ch)

    print(f"\n{'='*55}")
    print(f"Toplam: {len(unique)} benzersiz oynatılabilir kanal")

    with open("channels.m3u", "w", encoding="utf-8") as f:
        f.write(build_m3u(unique))

    with open("channels.json", "w", encoding="utf-8") as f:
        json.dump(unique, f, ensure_ascii=False, indent=2)

    print("channels.m3u oluşturuldu ✓")
    print("channels.json oluşturuldu ✓")

    from collections import Counter
    groups = Counter(ch["group"] for ch in unique)
    print("\nGrup özeti:")
    for g, c in sorted(groups.items()):
        print(f"  {g}: {c} kanal")


if __name__ == "__main__":
    main()
