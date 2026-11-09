#!/usr/bin/env python3
"""Writes reports/_facts/YYYY.md, the facts and figures for each year, from the data of the centre website.

    python3 tools/facts.py            # expects ../mishmash-web next to this repository
    MISHMASH_WEB=/path/to/mishmash-web python3 tools/facts.py

Numbers come only from the website's data: results registered in NVA (site/_data/mishmash_results.yml),
events (site/_events, only those held before the day of the run), news (site/_news), people in the
directory and partners (site/_directory, site/_data/partners.yml). Run it again before a chapter is
published; the date of the count is written under each table.
"""
import collections, datetime, os, re
from pathlib import Path
import yaml

ROOT = Path(__file__).resolve().parent.parent
WEB = Path(os.environ.get("MISHMASH_WEB", ROOT.parent / "mishmash-web")) / "site"
OUT = ROOT / "reports" / "_facts"
TODAY = datetime.date.today()
YEARS = range(2024, 2031)


def dated(folder):
    """(date, name) for every entry in a Jekyll collection named YYYY-MM-DD-..."""
    out = []
    for p in (WEB / folder).iterdir():
        m = re.match(r"(\d{4})-(\d{2})-(\d{2})-(.*?)(\.md)?$", p.name)
        if m:
            out.append((datetime.date(int(m[1]), int(m[2]), int(m[3])), m[4]))
    return out


def main():
    results = yaml.safe_load(open(WEB / "_data" / "mishmash_results.yml", encoding="utf8"))
    synced = str(results.get("synced_at", ""))[:10]
    by_year = collections.defaultdict(collections.Counter)
    for r in results["results"]:
        by_year[str(r.get("year"))][r.get("group_type") or r.get("type_label") or "Other"] += 1
    events = [(d, n) for d, n in dated("_events") if d < TODAY]
    news = [d for d, _ in dated("_news") if d <= TODAY]
    people = sum(1 for p in (WEB / "_directory" / "people").iterdir() if p.is_dir() or p.suffix == ".md")
    partners = yaml.safe_load(open(WEB / "_data" / "partners.yml", encoding="utf8"))
    partner_counts = {g.get("key"): len(g.get("entries", [])) for g in partners}
    OUT.mkdir(parents=True, exist_ok=True)
    for y in YEARS:
        lines = []
        res = by_year.get(str(y), collections.Counter())
        ev = [n for d, n in events if d.year == y]
        meshups = sum(1 for n in ev if n.startswith("meshup"))
        nws = sum(1 for d in news if d.year == y)
        if not res and not ev and not nws:
            lines.append("Not yet: the numbers are added when the year has begun." if y >= TODAY.year else
                         "The website has no results, events or news registered for this year; the centre had not started yet.")
        else:
            lines += ["| Measure | Number |", "| --- | --- |"]
            lines.append(f"| Results registered in NVA | {sum(res.values())} |")
            for kind, n in res.most_common():
                lines.append(f"| {kind} | {n} |")
            lines.append(f"| MeshUps held | {meshups} |")
            lines.append(f"| Other events on the website | {len(ev) - meshups} |")
            lines.append(f"| News stories | {nws} |")
            if y == TODAY.year:
                lines.append(f"| People in the directory | {people} |")
                for key, n in partner_counts.items():
                    lines.append(f"| Partners, {key} | {n} |")
            lines.append("")
            lines.append(f"Counted on {TODAY.isoformat()} from the data of mishmash.no; NVA results as synced on {synced}. "
                         "A result is counted in the year NVA gives it.")
        (OUT / f"{y}.md").write_text("\n".join(lines) + "\n", encoding="utf8")
        print(y, sum(res.values()), len(ev), nws)


if __name__ == "__main__":
    main()
