# Dataset Validation Report

Validation date: 2026-10-21

This report checks file integrity and basic structure. It does not
claim complete clinical coverage or full equivalence to official indexes.

## 1. Archive integrity
- **ClinPGx/original/genes.zip:** PASS
- **ClinPGx/original/drugs.zip:** PASS
- **ClinPGx/original/relationships.zip:** PASS
- **RxNorm/original/RxNorm_full_prescribe_10052026.zip:** PASS

## 2. DDInter CSV checks

- **ddinter_B.csv:** 15140 data rows; 0 repeated ordered pairs; 0 reverse-pair occurrences; levels: {'Major': 2739, 'Moderate': 7359, 'Minor': 800, 'Unknown': 4242}.
- **ddinter_D.csv:** 25681 data rows; 0 repeated ordered pairs; 0 reverse-pair occurrences; levels: {'Minor': 2015, 'Major': 2314, 'Moderate': 13519, 'Unknown': 7833}.
- **ddinter_H.csv:** 11727 data rows; 0 repeated ordered pairs; 0 reverse-pair occurrences; levels: {'Minor': 707, 'Moderate': 7051, 'Major': 1203, 'Unknown': 2766}.
- **ddinter_L.csv:** 65389 data rows; 0 repeated ordered pairs; 0 reverse-pair occurrences; levels: {'Moderate': 39985, 'Major': 15915, 'Minor': 2076, 'Unknown': 7413}.
- **ddinter_P.csv:** 5492 data rows; 0 repeated ordered pairs; 0 reverse-pair occurrences; levels: {'Minor': 278, 'Moderate': 3270, 'Major': 1278, 'Unknown': 666}.
- **ddinter_R.csv:** 30563 data rows; 0 repeated ordered pairs; 0 reverse-pair occurrences; levels: {'Minor': 1138, 'Moderate': 19675, 'Major': 2617, 'Unknown': 7133}.
- **ddinter_V.csv:** 12024 data rows; 0 repeated ordered pairs; 0 reverse-pair occurrences; levels: {'Moderate': 6451, 'Minor': 287, 'Major': 2924, 'Unknown': 2362}.

Note: repeated/reverse pairs are flagged for review, not automatically removed.

## 3. ATC community snapshot
- **WHO_ATC-DDD-combinations_2026-04-25.csv:** 244 data rows; columns: atc_code, brand_name, dosage_form, ingredients, ddd_comb.
- **WHO_ATC-DDD_2026-04-25.csv:** 7536 data rows; columns: atc_code, atc_name, ddd, uom, adm_r, note.

The ATC files are a community snapshot dated 2026-04-25. They have not
been fully reconciled against every entry in the official WHO ATC/DDD index.

## 4. ClinPGx CYP450 relationship coverage
- Relationship TSV: `relationships.tsv`; 246714 total rows.
- Rows mentioning CYP in entity names/types: 25342.
- Available columns: Entity1_id, Entity1_name, Entity1_type, Entity2_id, Entity2_name, Entity2_type, Evidence, Association, PK, PD, PMIDs.
- CYP-mentioned rows with a drug entity type: 0.
- This is a keyword-based coverage check, not a clinical completeness assessment.
- Verify whether enzyme substrate/inhibitor/inducer roles and evidence fields meet the project schema.

## 5. RxNorm
- Original RxNorm Full Prescribable Content archive is retained unchanged.
- Its embedded README identifies the October 5, 2026 release and 2020AA UMLS consistency.
- No full semantic validation of every RxNorm record was performed by this script.

## Overall status
- File-level archive checks and basic tabular checks are recorded above.
- Original datasets were not modified by this validation script.
- CYP450 completeness and ATC equivalence to the official index remain unverified.
