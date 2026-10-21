import csv, io, zipfile
from pathlib import Path
from collections import Counter

archive = Path("ClinPGx/original/relationships.zip")
out = Path("validation/CYP450_COVERAGE.md")

with zipfile.ZipFile(archive) as z:
    tsv = next(n for n in z.namelist()
               if n.lower().endswith("relationships.tsv"))
    with z.open(tsv) as raw:
        reader = csv.DictReader(io.TextIOWrapper(raw, encoding="utf-8-sig"),
                                delimiter="\t")
        rows = list(reader)

def val(row, key):
    return (row.get(key) or "").strip()

def entity(row, n):
    return val(row, f"Entity{n}_name"), val(row, f"Entity{n}_type")

cyp_rows = []
cyp_gene_chemical = []
type_pairs = Counter()

for r in rows:
    n1, t1 = entity(r, 1)
    n2, t2 = entity(r, 2)
    if "CYP" in (n1 + " " + n2).upper():
        cyp_rows.append(r)
        type_pairs[tuple(sorted((t1, t2)))] += 1

    gene1 = "CYP" in n1.upper() and "GENE" in t1.upper()
    gene2 = "CYP" in n2.upper() and "GENE" in t2.upper()
    chem1 = "CHEMICAL" in t1.upper()
    chem2 = "CHEMICAL" in t2.upper()

    if (gene1 and chem2) or (gene2 and chem1):
        cyp_gene_chemical.append(r)

lines = [
    "# CYP450 Relationship Coverage Check",
    "",
    "Source: ClinPGx `relationships.tsv` inside the preserved original archive.",
    "",
    "## Counts",
    f"- Total relationship rows: {len(rows)}",
    f"- Rows with CYP in either entity name: {len(cyp_rows)}",
    f"- Rows linking a CYP-named Gene entity with a Chemical entity: {len(cyp_gene_chemical)}",
    "",
    "## Entity-type pairs among CYP-mentioned rows",
]
for pair, count in type_pairs.most_common():
    lines.append(f"- `{pair[0]}` + `{pair[1]}`: {count}")

lines += [
    "",
    "## Evidence-field availability for CYP Gene–Chemical rows",
]
for field in ("Association", "PK", "PD", "Evidence", "PMIDs"):
    populated = sum(bool(val(r, field)) for r in cyp_gene_chemical)
    lines.append(f"- `{field}` populated: {populated}/{len(cyp_gene_chemical)}")

lines += ["", "## Sample relationships (up to 15)", ""]
lines.append("| Entity 1 | Type 1 | Entity 2 | Type 2 | Association | PK | PD | Evidence | PMIDs |")
lines.append("|---|---|---|---|---|---|---|---|---|")
for r in cyp_gene_chemical[:15]:
    cells = [
        val(r, "Entity1_name"), val(r, "Entity1_type"),
        val(r, "Entity2_name"), val(r, "Entity2_type"),
        val(r, "Association"), val(r, "PK"), val(r, "PD"),
        val(r, "Evidence"), val(r, "PMIDs")
    ]
    lines.append("| " + " | ".join(c.replace("|", "\\|").replace("\n", " ") for c in cells) + " |")

lines += [
    "",
    "## Interpretation and limitations",
    "- Entity types are interpreted as supplied by ClinPGx; they are not renamed.",
    "- This keyword-based analysis is a coverage check, not proof that all clinically relevant CYP450 interactions are represented.",
    "- It does not establish whether every relationship identifies substrate, inhibitor, or inducer roles.",
    "- The original ClinPGx archive was not modified.",
    "",
]
out.write_text("\n".join(lines), encoding="utf-8")
print(out.read_text())
