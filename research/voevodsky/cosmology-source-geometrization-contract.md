# Source-geometrization contract

## Evidence revision

The original descriptor-sufficiency conjecture remains rejected, but exact certificate recovery and transport repair now populate four of eight required fields:

- canonical algebraic generator IDs;
- normalized algebraic source words;
- coherent all-even squared-axis transport;
- generator and checker provenance.

Evidence comprises 1,224 exact A12 certificates, 524,224 generator-row transport tests, 2,448 A14 certificate squares, 4,896 A16 path equations, and symbolic all-even descriptor induction.

Four geometric fields remain absent:

- a source-derived geometric support for every labelled generator;
- a source differential with a checked square;
- DNC filtration data;
- exceptional specialization to a named supported target complex.

Assigning an arbitrary support label still fails the contract because the differential, filtration, and specialization remain absent and the label has no constructor-derived map.

## Disposition

Retain the coherent all-even algebraic source presentation. Withhold geometrization and every supported DNC or horn consequence.

The first missing typed object is a map from each labelled `T`, `S_K`, and `Q` descriptor to a geometric support locus derived from its denominator or relation constructor. Acceptance requires complete family coverage, squared-axis preservation, and rejection of fabricated descriptor-only supports.

## Verification

- `research/voevodsky/check_cosmology_source_geometrization_contract.py` — exit 0
- `research/voevodsky/results/cosmology_source_geometrization_contract.json` — four populated, four missing
