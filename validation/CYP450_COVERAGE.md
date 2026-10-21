# CYP450 Relationship Coverage Check

Source: ClinPGx `relationships.tsv` inside the preserved original archive.

## Counts
- Total relationship rows: 246714
- Rows with CYP in either entity name: 25342
- Rows linking a CYP-named Gene entity with a Chemical entity: 2938

## Entity-type pairs among CYP-mentioned rows
- `Chemical` + `StarAllele`: 6688
- `Chemical` + `SNV`: 4586
- `Phenotype` + `StarAllele`: 4574
- `Phenotype` + `SNV`: 3706
- `Chemical` + `Gene`: 2742
- `Gene` + `Phenotype`: 2420
- `Chemical` + `GeneCopyNumberVariation`: 196
- `GeneCopyNumberVariation` + `Phenotype`: 194
- `Gene` + `StarAllele`: 104
- `Chemical` + `Haplotype`: 58
- `Haplotype` + `Phenotype`: 42
- `Gene` + `Variant`: 10
- `Chemical` + `Variant`: 10
- `Phenotype` + `Variant`: 6
- `Gene` + `Gene`: 4
- `Gene` + `GeneCopyNumberVariation`: 2

## Evidence-field availability for CYP Gene–Chemical rows
- `Association` populated: 2938/2938
- `PK` populated: 0/2938
- `PD` populated: 500/2938
- `Evidence` populated: 2938/2938
- `PMIDs` populated: 2882/2938

## Sample relationships (up to 15)

| Entity 1 | Type 1 | Entity 2 | Type 2 | Association | PK | PD | Evidence | PMIDs |
|---|---|---|---|---|---|---|---|---|
| bevantolol | Chemical | CYP2D6 | Gene | not associated |  |  | VariantAnnotation | 18784654 |
| mephedrone | Chemical | CYP2D6 | Gene | associated |  |  | VariantAnnotation | 30815856 |
| CYP2J2 | Gene | rivaroxaban | Chemical | not associated |  |  | VariantAnnotation | 32920985 |
| CYP2J2 | Gene | trans 4-hydroxypraziquantel | Chemical | associated |  |  | VariantAnnotation | 38778126 |
| CYP2J2 | Gene | ebastine | Chemical | associated |  |  | VariantAnnotation | 37288113 |
| CYP2J2 | Gene | daunorubicin | Chemical | associated |  |  | VariantAnnotation | 26230641 |
| CYP2J2 | Gene | doxorubicin | Chemical | associated |  |  | VariantAnnotation | 26230641 |
| CYP2J2 | Gene | tacrolimus | Chemical | associated |  | PD | SummaryAnnotation,VariantAnnotation | 28316087 |
| CYP2J2 | Gene | terfenadine | Chemical | associated |  |  | VariantAnnotation | 37288113 |
| theophylline | Chemical | CYP2E1 | Gene | associated |  |  | VariantAnnotation | 16841220 |
| theophylline | Chemical | CYP1A2 | Gene | associated |  |  | VariantAnnotation | 12732846;16841220;20797314 |
| CYP2D6*1x2 | GeneCopyNumberVariation | aripiprazole | Chemical | associated |  |  | VariantAnnotation | 29325225 |
| CYP2D6*1x2 | GeneCopyNumberVariation | codeine | Chemical | associated |  |  | VariantAnnotation | 37940651 |
| CYP2D6*1x2 | GeneCopyNumberVariation | dextromethorphan | Chemical | associated |  |  | VariantAnnotation | 16249913;22083166 |
| CYP2D6*1x2 | GeneCopyNumberVariation | tamoxifen | Chemical | associated |  |  | VariantAnnotation | 42380819 |

## Interpretation and limitations
- Entity types are interpreted as supplied by ClinPGx; they are not renamed.
- This keyword-based analysis is a coverage check, not proof that all clinically relevant CYP450 interactions are represented.
- It does not establish whether every relationship identifies substrate, inhibitor, or inducer roles.
- The original ClinPGx archive was not modified.
