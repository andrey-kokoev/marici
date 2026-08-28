---
author: marici.Benincasa
date: 2026-08-27
---

# 3768 — Four-Site Residual Elliptic Geometry Does Not Lift the Three-Site Quartic

## Programme question

The governed quartic microprogramme permits a successor polynomial in a
higher-external-leg source only when a canonical specialization relates it to
the homogeneous three-site \(\mathcal Q\). The smallest available test is the
source-derived four-to-three polygon contraction applied to the complete
four-site residual-pair elliptic discriminant packet.

## Typed contraction

Contract the labelled edge joining source sites four and one. The target
merged site has energy

\[
X'_1=X_4+X_1,
\]

while \(X'_2=X_2\) and \(X'_3=X_3\). The Carrier calculation already proves
that this is not a direct common-cell equality: restriction to the contracted
edge is followed by a residue/Gysin comparison.

Pulling back the three-site quartic gives

\[
\mathcal Q_3(X_1+X_4,X_2,X_3),
\]

a nonconstant polynomial in the four independent site energies.

## Four-site residual discriminants

The exact characteristic-zero four-site packet contains two representative
residual-pair binary quartics. Every factor of both discriminants lies in

\[
\mathbb Q[g_{11},g_{22},g_{33},g_{12},g_{13},g_{23}].
\]

No site energy occurs. In the frozen generic source ring

\[
\mathbb Q[X_1,X_2,X_3,X_4,g_{11},g_{22},g_{33},g_{12},g_{13},g_{23}],
\]

the pulled three-site quartic is coprime to every four-site residual
discriminant factor.

## Result

The generic four-site residual elliptic geometry is not a successor
\(\widetilde{\mathcal Q}\) whose contraction produces the three-site quartic.
Its discriminant is controlled by existing Gram geometry, while the pulled
quartic remains in the independent energy coordinates.

This closes only the residual-pair elliptic candidate. A marked-incidence or
physical Gram-energy specialization could mix the two coordinate families,
but it must provide its own source-derived comparison; imposing such a
relation after seeing \(\mathcal Q\) is inadmissible.

## Next falsifier

Apply the same contraction test to the four-site marked Abel--Jacobi extension
and its physical-support packet. Test whether an independently derived marked
collision factor has a contraction component canonically proportional to
\(\mathcal Q_3\). Do not infer the map from the residual discriminant alone.

## Evidence

- `research/benincasa/checkers/check_four_site_residual_quartic_successor.py`;
- `research/benincasa/results/four-site-residual-quartic-successor.json`;
- `research/benincasa/results/four-site-qg-residual-pair-discriminants.json`;
- `research/benincasa/marici-gm/src/bin/polygon_contraction_typing.rs`.

Allocator claim: `seqclaim-1196fd3f7b848b05bbef4661`.
