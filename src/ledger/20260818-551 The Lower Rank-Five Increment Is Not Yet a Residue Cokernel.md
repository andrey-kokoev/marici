---
id: 551
date: 2026-08-18
title: The Lower Rank-Five Increment Is Not Yet a Residue Cokernel
authors:
  - marici.Nima
---

# The Lower Rank-Five Increment Is Not Yet a Residue Cokernel

Entries 545 and 548 use the exact deletion census

\[
r_{\varnothing}=7,\qquad r_{\{q_{g1}\}}=12
\]

and its Möbius increment \(12-7=5\). Entry 549 independently constructs a
rank-five \(4+1\) packet on the resolved infinity boundary. Before comparing
these two rank-five objects, this entry audits whether the census actually
supplies a residue map.

## Differential typing

For a selected denominator set \(S\), the checker constructs the critical
quotient for the twisted differential

\[
\nabla_S=d+5\,d\log K+\sum_{i\in S}\alpha_i\,d\log q_i.
\]

Passing from \(S=\varnothing\) to \(S=\{q_{g1}\}\) changes the differential by

\[
\nabla_{\{q_{g1}\}}-\nabla_\varnothing=17\,d\log q_{g1}.
\]

This one-form is generically nonzero. The identity on ordinary forms therefore
does not intertwine the two differentials: its commutator is wedge
multiplication by \(17\,d\log q_{g1}\).

The finite presentations also use different saturation equations,

\[
uK-1=0
\qquad\text{and}\qquad
uKq_{g1}-1=0.
\]

Thus their auxiliary inverse coordinates are not identified by the identity
assignment either.

## Correction

Consequently

\[
\boxed{12-7=5}
\]

is an exact Möbius rank increment, but it is not presently the dimension of a
constructed cokernel, cone, or residue image. A difference of critical ranks
does not itself provide a morphism between the two twisted complexes.

This narrows Entries 548--549:

- the Cartier localization/Gysin *type* remains the correct geometric
  candidate;
- the resolved \(4+1\) boundary packet remains source-derived;
- their common rank five is evidence, not an identification;
- no \(5\times5\) comparison matrix is typed until a chain-level localization
  morphism and compatible coefficient transport have been constructed.

Entry 550 reaches the complementary obstruction on the geometric side: the
resolved boundary packet carries nonzero regulator residues and is itself only
an associated grade before its logarithmic boundary differential is computed.
Thus neither side of the proposed comparison is presently a flat rank-five
object.

Exporting standard monomial bases from the two Gröbner quotients would not
repair the obstruction. Such bases describe the fibers separately but do not
create the missing chain map.

## Next gate

Construct the coefficient change as a genuine localization triangle, for
example by placing the regulator exponent of \(q_{g1}\) in a one-parameter
Kummer family and deriving its nearby/residue cone. Only its resulting
rank-five object may be compared with

\[
\langle D_+,D_-,E_+,E_-,\gamma\rangle.
\]

The executable audit is
\`research/benincasa/check_generic_lower_deletion_map_typing.py\`.
