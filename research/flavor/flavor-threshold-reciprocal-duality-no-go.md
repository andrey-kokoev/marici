# Reciprocal duality does not select the reconstructed threshold ratio: WP1026

## Question

Can the coefficient-free reciprocal selector of WP309 independently choose the
threshold ratio reconstructed in WP1025?

## Admitted domain and operation

The coordinate is the positive weak-basis-singlet ratio \(r=f/M\), restricted
to \(0<r\leq1/4\). The scaled reciprocal involution is

\[
r\longmapsto\frac{\kappa^2}{r}.
\]

Its invariant potential \(V_\kappa=(r-\kappa^2/r)^2\) has unique positive
stationary point \(r=\kappa\), Hessian eight, and response
\(dr_*/d\kappa=1\).

## Exact hostile test

Canonical normalization gives \(r=1\), outside the EFT branch. Rewriting the
coordinate as \(q=4r\) and declaring \(q\mapsto1/q\) gives \(r=1/4\),
but this is exactly the hidden choice \(\kappa=1/4\).

WP1025 proved strict monotonicity and the exact fitted bound

\[
\frac{1061950037427}{4398046511104}\leq r_{\rm fit}\leq
\frac{539770202345}{2199023255552}<\frac14 .
\]

Thus the quarter fixed point predicts
\(J^2(1/4)=400/369161163681\), strictly above every fitted sheet. All 1,210
sheets reject it.

## Instrument and classification

The CKM/Jarlskog instrument falsifies the quarter prediction conditional on the
WP90 threshold map. No executable reciprocal source operation on \(f/M\) is
admitted. Canonical duality is incompatible; quarter duality is a hidden
normalization followed by a false prediction. It is neither a viable selector
nor a repair of WP1025.

The smallest exact falsifier is the fitted upper bracket being below \(1/4\).
The authority falsifier is the unit response to \(\kappa\).

## Claim boundary

This closes reciprocal-duality selection on \(r\), including \(q=4r\). It
does not close independently derived non-duality source equations.

## Disposition

Negative but useful. A successor must derive a value inside the reconstructed
interval without choosing its normalization from CKM.

Verification: uv run --with sympy python
research/flavor/checkers/wp1026_threshold_reciprocal_duality_no_go.py
