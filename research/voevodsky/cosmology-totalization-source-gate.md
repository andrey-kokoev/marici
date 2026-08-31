# Totalization is not an independent source mechanism

## Result

The current sourced complex has no degree-one cell and has the primitive closed degree-two pair `(Xi_log,-sigma123)` with column `(1,1)`.

A mapping cone or homotopy fiber can package and shift existing cochains, maps, and homotopies. It cannot create a nullhomotopy absent from its input. Applied to the current data, totalization either retains zero sourced rank in the incoming horn degree or includes a map whose defining datum is already the missing nullhomotopy.

Fixing the exceptional-face coefficient to one forces the `Xi_log` coefficient to one by the chain condition. This proves uniqueness of a hypothetical comparison coefficient, not existence of the comparison.

## Disposition

The totalization-source leaf is completed negatively. Declaring a mapping cone without an independently constructed geometric map is circular and reproduces abstract `tau_p`.

The next admissible branch is a deformation-to-normal or Rees correspondence with an independently defined specialization/connecting morphism. Its chain-level boundary must be computed from the correspondence and then tested against `(1,1)`; the column may not be stipulated.

## Verification

- `research/voevodsky/check_cosmology_totalization_source_gate.py`
- `research/voevodsky/results/cosmology_totalization_source_gate.json`
