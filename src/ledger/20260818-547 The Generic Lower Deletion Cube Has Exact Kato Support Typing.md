---
id: 547
date: 2026-08-18
title: The Generic Lower Deletion Cube Has Exact Kato Support Typing
authors:
  - marici.Nima
---

# The Generic Lower Deletion Cube Has Exact Kato Support Typing

Entries 545--546 compute the complete rank-34 denominator-deletion cube and
the single-wall boundary geometry. This entry
performs the first cross-sector test suggested by Entry 544: compare every
nonzero proper grade with the source-defined logarithmic incidence strata,
without yet identifying coefficient objects of equal rank.

In coordinates ((c,a,b)), the four pole normals are

\[
n_1=(1,0,1),quad
n_2=(1,1,0),quad
n_3=(0,1,1),quad
n_{23}=(1,0,1).
\]

Thus (q_{g_1}) and (q_{g_{23}}) are the unique parallel pair.  At generic
kinematics their constants differ by

\[
X_1-X_2-X_3,
\]

so their intersection is empty away from the already frozen coincidence
divisor.  Every support containing this pair is likewise empty.  These are
exactly the masks

\[
1001,quad1011,quad1101,quad1111,
\]

and Entry 545 assigns proper grade zero to all four.

All five other pairs are transverse affine lines.  Exactly two triples are
transverse points:

\[
q_{g_1}q_{g_2}q_{g_3},qquad
q_{g_2}q_{g_3}q_{g_{23}}.
\]

Their support census agrees exactly with the Möbius grades:

\[
\begin{array}{c|c|c}
\text{support type}&\text{number}&\text{proper rank}\\ \hline
\text{single plane}&4&5\\
\text{finite transverse pair}&5&1\\
\text{parallel pair}&1&0\\
\text{transverse triple}&2&1\\
\text{empty triple}&2&0\\
\text{fourfold}&1&0.
\end{array}
\]

The oriented Boolean localization cube supplies the canonical residue/Gysin
incidence signs.  All eleven nonempty two-step squares anticommute.  No fitted
sign, extra support, or new carrier stratum is needed.

Therefore

\[
\boxed{\text{the generic lower deletion cube passes Entry 544's Kato
support-typing test}.}
\]

This is not yet a coefficient-kernel theorem.  The rank-five single-pole
objects have not been constructed geometrically, and no actual morphism from
one of them to a rank-one pair or triple grade has been computed.  Rank and
support agreement alone cannot establish H2.

The next test is to realize a single-pole grade as the relative cohomology of
the frozen Cayley--Menger surface cut by one pole plane, derive its residue to
each finite pair line, and verify that the two iterated residues land on the
two source-defined triple points with the Boolean signs above.  The parallel
residue must vanish because its fiber product is empty, not because a matrix
entry is set to zero.

The executable audit is
`research/benincasa/check_generic_lower_kato_incidence.py`.
