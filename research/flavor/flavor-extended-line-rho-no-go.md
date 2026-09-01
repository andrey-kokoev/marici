# Extended-line \(\rho\) no-go: WP1114

## Question

Can tensoring the determinant reciprocal by the matched-holonomy or Wilson
line construct an independent \(\rho\)?

## Flat-line alternative

Matched holonomy supplies a rank-one space of flat sections whose nonzero
generators form a \(\mathbb C^\times\)-torsor, with no preferred generator.
If the flat extension is trivial and has a nonzero flat section \(c\), the
candidate is

\[
\rho_c=\frac{c}{D},
\]

a constant nonzero multiple of the tautological reciprocal \(1/D\). It has the
same weight and ray, so it is not independent.

If the extension is nontrivial torsion, it has no global nonzero flat section,
so it supplies no \(\rho\) at all.

## Classification

Negative gate. Wilson holonomy, a \(\mathbb C^\times\)-torsor generator, or
\(c/D\) cannot be promoted to independent \(\rho\).

Checker: `research/flavor/checkers/wp1114_extended_line_rho_no_go.py`

Result: `results/wp1114_extended_line_rho_no_go.json`
