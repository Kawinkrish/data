import csv, json, zipfile
from pathlib import Path
from collections import Counter

root = Path(".")
report = [
    "# Dataset Validation Report",
    "",
    "Validation date: 2026-10-21",
    "",
    "This report checks file integrity and basic structure. It does not",
    "claim complete clinical coverage or full equivalence to official indexes.",
    "",
    "## 1. Archive integrity",
]
archives = list(root.glob("ClinPGx/original/*.zip")) + list(root.glob("RxNorm/original/*.zip"))
for p in archives:
    try:
        with zipfile.ZipFile(p) as z:
            bad = z.testzip()
        report.append(f"- **{p}:** {'PASS' if bad is None else 'FAIL: ' + bad}")
    except Exception as e:
        report.append(f"- **{p}: FAIL** — {e}")

report += ["", "## 2. DDInter CSV checks", ""]
for p in sorted((root / "DDInter/original").glob("*.csv")):
    with p.open(encoding="utf-8-sig", newline="") as f:
        rows = list(csv.DictReader(f))
    pairs, reverse_pairs, levels = set(), 0, Counter()
    exact_dupes = 0
    for row in rows:
        a = (row.get("Drug_A") or "").strip().casefold()
        b = (row.get("Drug_B") or "").strip().casefold()
        pair = (a, b)
        if pair in pairs:
            exact_dupes += 1
        if (b, a) in pairs and a != b:
            reverse_pairs += 1
        pairs.add(pair)
        levels[(row.get("Level") or "").strip()] += 1
    report.append(
        f"- **{p.name}:** {len(rows)} data rows; "
        f"{exact_dupes} repeated ordered pairs; "
        f"{reverse_pairs} reverse-pair occurrences; "
        f"levels: {dict(levels)}."
    )
report += [
    "",
    "Note: repeated/reverse pairs are flagged for review, not automatically removed.",
    "",
    "## 3. ATC community snapshot",
]
for p in sorted((root / "ATC/original").glob("*.csv")):
    with p.open(encoding="utf-8-sig", newline="") as f:
        reader = csv.DictReader(f)
        headers = reader.fieldnames or []
        rows = list(reader)
    report.append(f"- **{p.name}:** {len(rows)} data rows; columns: {', '.join(headers)}.")
report += [
    "",
    "The ATC files are a community snapshot dated 2026-04-25. They have not",
    "been fully reconciled against every entry in the official WHO ATC/DDD index.",
    "",
    "## 4. ClinPGx CYP450 relationship coverage",
]
rel_zip = root / "ClinPGx/original/relationships.zip"
cyp_rows, rel_rows, rel_header = [], 0, []
try:
    with zipfile.ZipFile(rel_zip) as z:
        candidates = [n for n in z.namelist() if n.lower().endswith(".tsv")]
        rel_name = next((n for n in candidates if "relationship" in n.lower()), None)
        if rel_name is None:
            rel_name = next((n for n in candidates if n.lower().endswith(".tsv")), None)
        if rel_name:
            with z.open(rel_name) as raw:
                import io
                reader = csv.DictReader(io.TextIOWrapper(raw, encoding="utf-8-sig"), delimiter="\t")
                rel_header = reader.fieldnames or []
                for row in reader:
                    rel_rows += 1
                    e1 = " ".join(str(row.get(k, "")) for k in ("Entity1_name", "Entity1_type"))
                    e2 = " ".join(str(row.get(k, "")) for k in ("Entity2_name", "Entity2_type"))
                    if "CYP" in (e1 + " " + e2).upper():
                        cyp_rows.append(row)
            report.append(f"- Relationship TSV: `{rel_name}`; {rel_rows} total rows.")
            report.append(f"- Rows mentioning CYP in entity names/types: {len(cyp_rows)}.")
            report.append(f"- Available columns: {', '.join(rel_header)}.")
            gene_chemical_links = [
                r for r in cyp_rows
                if (
                    ("CYP" in str(r.get("Entity1_name", "")).upper()
                     and "GENE" in str(r.get("Entity1_type", "")).upper()
                     and "CHEMICAL" in str(r.get("Entity2_type", "")).upper())
                    or
                    ("CYP" in str(r.get("Entity2_name", "")).upper()
                     and "GENE" in str(r.get("Entity2_type", "")).upper()
                     and "CHEMICAL" in str(r.get("Entity1_type", "")).upper())
                )
            ]
            report.append(f"- CYP-named Gene-Chemical relationship rows: {len(gene_chemical_links)}.")
            report.append("- ClinPGx records associations and evidence; it may not fully specify substrate, inhibitor, or inducer roles.")
            report.append("- This is a keyword-based coverage check, not a clinical completeness assessment.")
        else:
            report.append("- No TSV file found in relationships.zip; manual schema review required.")
except Exception as e:
    report.append(f"- Could not inspect relationships archive: {e}")

report += [
    "",
    "## 5. RxNorm",
    "- Original RxNorm Full Prescribable Content archive is retained unchanged.",
    "- Its embedded README identifies the October 5, 2026 release and 2020AA UMLS consistency.",
    "- No full semantic validation of every RxNorm record was performed by this script.",
    "",
    "## Overall status",
    "- File-level archive checks and basic tabular checks are recorded above.",
    "- Original datasets were not modified by this validation script.",
    "- CYP450 completeness and ATC equivalence to the official index remain unverified.",
]
out = root / "validation/VALIDATION_REPORT.md"
out.write_text("\n".join(report) + "\n", encoding="utf-8")
print(out.read_text())
