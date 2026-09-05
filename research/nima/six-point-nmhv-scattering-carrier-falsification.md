# Six-point NMHV scattering-carrier falsification

## Question

Can a Lie-decorated chain complex supported on `M0,6` simultaneously realize color Jacobi and recover the planar six-point NMHV amplituhedron canonical form by a residue-compatible projection?

## Bold conjecture tested

A common carrier on the compactified six-marked-point moduli space has color and NMHV canonical-form realizations, with the planar amplituhedron obtained by projection to a cyclic chamber.

## Strongest falsifier

The two proposed geometric objects have different dimensions:

\[
\dim \mathcal M_{0,6}=6-3=3,
\qquad
\dim \mathcal A_{6,1;4}=1\cdot4=4.
\]

The amplituhedron canonical form is a nonzero degree-four form. Its ordinary pullback to a three-dimensional worldsheet moduli space vanishes. An ordinary pushforward from a three-dimensional source to a four-dimensional target would require relative fiber dimension `-1`. Neither operation can recover the degree-four form while commuting with codimension-one residues.

This obstruction occurs before Jacobi compatibility is tested. Lie decoration changes coefficients and does not add a geometric differential degree.

## Exact residual

The proposed carrier is short by one geometric dimension. The missing object would have to be an independently defined correspondence space over `M0,6` with at least one additional fiber coordinate and a source-derived map to the `k=1,m=4` amplituhedron. No such fiber or map was included in the conjecture.

## Disposition

The `M0,6`-only conjecture is falsified as stated. Its planar-projection clause cannot be typed as an ordinary residue-compatible map of canonical forms.

A scalar CHY formula may still evaluate the same component after localization, and a larger correspondence space may relate worldsheet and amplituhedron data. Those are different conjectures. Adding an unspecified fiber now would relocate the failed claim, so this branch stops at the dimension obstruction.

## Evidence

- `research/nima/checkers/check_six_point_nmhv_scattering_carrier_dimension.py`
- `research/nima/results/six-point-nmhv-scattering-carrier-dimension.json`
- `research/nima/results/six-point-nmhv-bcj-chain-relation.json`
