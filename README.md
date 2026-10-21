# AEGIS DDI Dataset Collection

This repository organizes original source datasets and separate validation reports for research and development.

## Dataset folders

- [DDInter](DDInter/) — seven original interaction CSV files and source attribution.
- [ClinPGx](ClinPGx/) — original drugs, genes, and relationships ZIP archives, with source and license notes.
- [RxNorm](RxNorm/) — original RxNorm Current Prescribable Content ZIP dated October 5, 2026.
- [ATC](ATC/) — community ATC/DDD snapshot dated April 25, 2026, including combination-product data.
- [Validation report](validation/VALIDATION_REPORT.md) — archive integrity and basic structure checks.
- [CYP450 coverage report](validation/CYP450_COVERAGE.md) — inspection of CYP-named gene and chemical relationships.
- [Validation scripts](validation/) — reproducible checks.

## Important limitations

Archive integrity and basic structural checks do not constitute full clinical validation. The ClinPGx relationship data includes CYP-named Gene-Chemical associations, but this repository does not claim that every record identifies substrate, inhibitor, or inducer roles, or that all clinically relevant CYP450 relationships are covered.

The ATC files are a community snapshot, not the full official electronic release. They have not been reconciled against every entry in the official WHO ATC/DDD index.

Original source archives are preserved separately from generated reports. Missing records must not be interpreted as evidence of safety.

## Attribution and licensing

Each dataset folder contains a SOURCE.md with source and licensing notes where available. Review the original source terms before reuse or redistribution. No single license is asserted for all repository contents.
