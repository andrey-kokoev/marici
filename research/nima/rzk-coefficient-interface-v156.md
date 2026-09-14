# v156: relation-lattice localization at 6

The true labelled integral Smith results are now aggregated independently of
the canonical generator presentation.

At D12,16,20,24,28 the full relation-derived Bockstein image has torsion prime
support contained in `{2,3}`. Consequently localization at 6 saturates that
image at every exact cutoff. The beta-rank gains are `8,14,18,22,26`, and the
distinguished transition has index ratio two throughout.

This gives a sharply better coefficient result than the canonical lattice:
there is one stable tested localization, `Z[1/6]`, rather than the growing prime
set forced by canonical generators. It does not authorize changing physical
coefficients and is not an all-degree theorem; an integral road map must still
carry the 2/3-primary derived data.

Evidence is `results/L2-relation-lattice-localization.json` from
`checkers/check_L2_relation_lattice_localization.py`.
`rzk/184-l2-relation-lattice-localization.rzk.md` passes all eight declarations
without assumptions.
