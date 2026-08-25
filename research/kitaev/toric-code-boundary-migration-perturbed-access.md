# Toric-code boundary migration and perturbed constructor access

Status: exact finite migration for annular circumferences `3 <= L <= 6` and
the frozen single-edge perturbation.  This packet covers WP14--WP15.

## Absolute-to-relative migration

Let `R` contain the rough inner-boundary vertices and edges.  The migration
maps are the quotient projections

\[
q_2=1:C_2(K)\to C_2(K,R),\quad
q_1:C_1(K)\to C_1(K)/C_1(R),\quad
q_0:C_0(K)\to C_0(K)/C_0(R).
\]

The checker verifies both chain squares

\[
q_0d_1=d_1^{rel}q_1,\qquad
q_1d_2=d_2^{rel}q_2,
\]

and hence the induced map on homology.  The absolute annulus has `dim H1=1`;
the rough-relative successor has `dim H1=0`.  The outer `gamma` maps to the
relative sum of faces.

The old seam Wilson functional paired to `gamma` does not descend to the
successor: after removing the rough edge, it evaluates to one on a projected
face boundary.  This is an exact view invalidation, not missing data.  Cached
claims “`gamma` is nontrivial” and “the old Wilson functional descends” become
false.  Cell labels, bulk incidence away from the changed support, and the
coefficient prime remain unchanged.

## Repetition under the bounded perturbation

Choose the admitted term `-X_e0` on the middle circumference, disjoint from
the outer `Z(gamma)` support.  It anticommutes with exactly two adjacent
plaquette terms and retains the local block polynomial `lambda^2-5` at unit
couplings.  Because it is disjoint from `gamma`, the admitted controlled
`Z(gamma)` measurement remains QND with respect to this perturbation.

The three mechanisms remain distinct:

- access denial still removes the constructor while the perturbed
  Hamiltonian and absolute class remain;
- projection loss still retains the constructor/class and kills only its
  classical record;
- rough-boundary migration still kills the relative class and invalidates
  the old Wilson functional, while also changing boundary Hamiltonian terms.

The cellular migration maps are unaffected by the coefficient perturbation.
The spectral response is therefore an independent column, not evidence that
the three disappearances coincide.  No generic stability theorem follows
from the disjoint integrable choice.

## Falsifiers and unresolved typing

Falsifiers are a noncommuting chain square, survival of `gamma` outside the
relative repair span, descent of the old Wilson functional despite its
nonzero value on a new repair, or perturbation support intersecting the
declared `gamma` while the protocol is still called QND.

Unresolved: noisy ancilla histories, cat-state preparation depth under a
specific geometry, completely positive instrument equivalence, and generic
quasi-adiabatic dressing of the Wilson constructor.  The perturbation also
does not derive a recovery cost, logical objective, tie-break, or concrete
instrument; those remain independent source data.
