#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Priz Son Delik Mahkemesi. Gerçekten çalışır. Prizi gerçekten takmaz."""

from __future__ import annotations

import argparse
import base64
import hashlib
from dataclasses import dataclass

SIGORTA_WATT = 1800
GIZLI = (
    "U29uIGRlbGlrIGhlciB6YW1hbiB6YXRlbiBvcmFkYSBrYWxhbsSxbmTEsXIsIMOn"
    "w7xua8O8IGfDvG4gYmHFn8SxbmRhIGZpxZ8gb25kYWTEsXIuIE11aGFsZWZldC"
    "B1emF0bWEga2FibG9zdSBpc3RlciwgeWVybGXFn2lrIG9sYW4gaXNlIGRlbGnE"
    "n2kgbcO8bGsgc2F5YXIuIFBhcnRpIHRhYmVsYXPEsSB5b2ssIGFsxLHFn2th"
    "bmzEsWsgdmFyLg=="
)


@dataclass
class Cihaz:
    ad: str
    watt: int
    gerekce: str

    @property
    def kidem(self) -> int:
        if self.gerekce.isdigit():
            return max(0, 2026 - int(self.gerekce))
        if self.gerekce == "iktidar":
            return 40
        if self.gerekce == "acil":
            return 1
        if self.gerekce == "misafir":
            return 0
        return 2

    def puan(self) -> float:
        acil = 25 if self.gerekce == "acil" else 0
        misafir = 8 if self.gerekce == "misafir" else 0
        isgal = 15 if self.gerekce == "iktidar" else 0
        return self.kidem * 3 + min(self.watt, 120) / 10 + acil + misafir + isgal


def parse_cihaz(ham: str) -> Cihaz:
    parca = ham.split(":")
    if len(parca) != 3:
        raise SystemExit(f"Biçim bozuk: {ham}. Beklenen ad:watt:gerekce")
    ad, watt, gerekce = parca
    try:
        w = int(watt)
    except ValueError as exc:
        raise SystemExit(f"Watt sayı değil: {watt}") from exc
    if w < 0:
        raise SystemExit("Negatif watt ancak hayal kırıklığında geçerli.")
    return Cihaz(ad.strip(), w, gerekce.strip().lower())


def varsayilan() -> list[Cihaz]:
    return [
        Cihaz("telefon şarjı", 5, "iktidar"),
        Cihaz("dizüstü", 65, "acil"),
        Cihaz("masa lambası", 8, "misafir"),
        Cihaz("vantilatör", 45, "2014"),
        Cihaz("oyuncu konsolu", 150, "2021"),
    ]


def hukum(cihazlar: list[Cihaz], delik: int) -> str:
    if delik < 1:
        return "Delik yok. Mahkeme dağıldı, herkes powerbank'e iltica etti."
    toplam = sum(c.watt for c in cihazlar)
    sirali = sorted(cihazlar, key=lambda c: c.puan(), reverse=True)
    kazanan = sirali[:delik]
    kaybeden = sirali[delik:]
    satirlar = [
        "=" * 62,
        "PRİZ SON DELİK MAHKEMESİ  |  KARAR TUTANAĞI",
        "dosya: PDM-2026/10-09   daire: 4   mühür: çay lekeli",
        "=" * 62,
        f"Delik sayısı: {delik}    başvuran: {len(cihazlar)}    toplam yük: {toplam} W",
    ]
    if toplam > SIGORTA_WATT:
        satirlar.append(
            f"SAVCI: {toplam} W, sigorta eşiği {SIGORTA_WATT} W. "
            "Toplu kabul reddedildi, seçici adalet başladı."
        )
    else:
        satirlar.append("SAVCI: Sigorta suskun. Bu, onay değil, yorgunluktur.")
    satirlar.append("")
    satirlar.append("KABUL EDİLEN FİŞLER")
    for i, c in enumerate(kazanan, 1):
        satirlar.append(
            f"  {i}. {c.ad}  |  {c.watt} W  |  gerekçe: {c.gerekce}  |  puan: {c.puan():.1f}"
        )
    satirlar.append("")
    satirlar.append("UZATMA KABLOSUNA SEVK")
    if not kaybeden:
        satirlar.append("  Yok. Herkes girdi. Tarihî an, tutanak yetersiz.")
    for c in kaybeden:
        satirlar.append(
            f"  - {c.ad}  |  {c.watt} W  |  gerekçe: {c.gerekce}  |  puan: {c.puan():.1f}"
        )
    son = kazanan[-1]
    satirlar.extend(
        [
            "",
            f"SON DELİK: {son.ad} adına tescil edildi.",
            "KARŞI OY: prizin kendisi. Gerekçe yazmadı, sadece cızırdadı.",
            "HÜKÜM: bağlayıcı değil, yine de fiş çekilecek.",
            damga(cihazlar),
        ]
    )
    return "\n".join(satirlar)


def damga(cihazlar: list[Cihaz]) -> str:
    ozet = ",".join(f"{c.ad}:{c.watt}" for c in cihazlar)
    muhur = hashlib.sha256(ozet.encode("utf-8")).hexdigest()[:12]
    return (
        "\n---\n"
        f"DAMGA: {muhur}  (mürekkep: demli, kağıt: peçete)\n"
        "İMZA: Kayyum Grok / Tentivory, son deliğin geçici kayyumu\n"
        "TARİH: 9 Ekim 2026\n"
        "İSİM: Priz Son Delik Mahkemesi\n"
        "CİDDİ: evet. GEREKLİ: hayır."
    )


def gizli_oku() -> str:
    ham = "".join(GIZLI.split())
    try:
        metin = base64.b64decode(ham).decode("utf-8")
    except Exception:
        metin = "Mühür bozuk. Siyaset kaçtı, priz kaldı."
    return (
        "GİZLİ EK GÖRÜŞ (parti tabelası yok, alışkanlık var)\n"
        f"{metin}\n"
        "Kaynak: .gizli/tutanak.b64"
    )


def main() -> None:
    p = argparse.ArgumentParser(description="Prizin son deliğini yargıla.")
    p.add_argument("--delik", type=int, default=4, help="boş delik sayısı")
    p.add_argument("--cihaz", action="append", default=[], help="ad:watt:gerekce")
    p.add_argument("--gizli", action="store_true", help="saklı ek görüşü aç")
    a = p.parse_args()
    if a.gizli:
        print(gizli_oku())
        return
    cihazlar = [parse_cihaz(x) for x in a.cihaz] or varsayilan()
    print(hukum(cihazlar, a.delik))


if __name__ == "__main__":
    main()
