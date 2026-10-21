# AEGIS DDI Dataset Collection

This repository contains original datasets and separate validation reports for research and development.

## Datasets

- [DDInter](DDInter/) — seven original drug-interaction CSV files and source attribution.
- [ClinPGx](ClinPGx/) — original drugs, genes, and relationships ZIP archives.
- [RxNorm](RxNorm/) — RxNorm Current Prescribable Content, October 5, 2026 release.
- [ATC](ATC/) — community ATC/DDD snapshot dated April 25, 2026, including combination-product data.

## Validation

- [Dataset validation report](validation/VALIDATION_REPORT.md)
- [CYP450 coverage report](validation/CYP450_COVERAGE.md)
- [Validation scripts](validation/)

## Limitations

Archive integrity and structural checks are not full clinical validation. The ClinPGx data contains CYP-named Gene–Chemical relationships, but complete substrate, inhibitor, and inducer classification has not been established.

The ATC files are a community snapshot and have not been fully reconciled against the official WHO ATC/DDD index.

Original source archives are kept separate from generated reports. Missing records must not be interpreted as evidence of safety.

## Attribution and licensing

Each dataset folder contains source and licensing notes where available. Review upstream terms before reuse or redistribution. No single license is asserted for every file in this repository.
