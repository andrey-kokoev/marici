# 3241 — The Quarter Obstruction Descends Around the Cyclic Residue Atlas

## Question

Complete Entry 3237's one-edge test by constructing the \(G_{23}\) and cyclic \(G_{31}\) charts from source formulas and checking the signed three-chart composition.

## Site cycle

Use

\[
(X_1,X_2,X_3)\longmapsto(X_3,X_1,X_2)
\]

and

\[
(c,a,b)\longmapsto(b,c,a).
\]

The retained coordinates therefore map as

\[
(a,b)_{G_{12}}
\longmapsto
(b',c')_{G_{23}}=(a,b),
\]

and after a second cycle as

\[
(c'',a'')_{G_{31}}=(a,b).
\]

With the ambient orientation \(dc\wedge da\wedge db\), the three cyclic Poincaré-residue transitions have signs

\[
(+1,+1,+1).
\]

## Source-level reconstruction

The one-cycle mark map is

\[
(g_1,g_2,g_3,g_{23},g_{31})
\longmapsto
(g_2,g_3,g_1,g_{31},g_{12}).
\]

The two-cycle chart has ordered marks

\[
(g_3,g_1,g_2,g_{12},g_{23}).
\]

After substituting the cyclicly permuted external parameters and retaining these positional labels, the complete Cayley–Menger polynomial and all five marked linear forms are coefficientwise identical to the \(G_{12}\) packet.  This was checked at three independent integer kinematic points over both primes 32003 and 32009.

The result is structural rather than accidental: the target constructions call the canonical polynomial with argument orders

\[
(Y,Z,X)_{G_{23}}
\]

and

\[
(Z,X,Y)_{G_{31}},
\]

which return the original ordered arguments after the corresponding site permutation.

## Composition

The three explicit mark maps compose to identity.  Since the retained fiber coordinates are positional identities and all three orientation signs are positive, the full signed cyclic transport is also identity.

Consequently each cyclic chart carries the same first-normal lifting obstruction:

\[
5=2+3
\]

at \(-5/4\), and

\[
7=2+4+1
\]

at \(-7/4\).

## Conclusion

The quarter-supported lifting obstruction descends around the complete \(C_3\) residue atlas.  Together with Entry 3237's reflected edge, this supplies cyclic descent plus one nontrivial reflection edge for the frozen occurrence packet.

This establishes occurrence covariance of the finite-field obstruction mechanism.  It does not identify a physical cycle pairing or promote the quarter supports to characteristic zero.

## Next falsifier

Test the reflection–cycle compatibility relation generating the full \(S_3\) action on the obstruction complex.  The required relation is not merely equality of ranks: the reflected transport must conjugate the cyclic generator to its inverse, including the Poincaré-residue sign.

## Evidence

- `research/benincasa/checkers/exponent_adapter_cyclic_occurrence_descent.py`
- `research/benincasa/results/exponent_adapter_cyclic_occurrence_descent.json`
- Entry 3237's independently reconstructed reflection packet.

Ledger number authority: `seqclaim-debfd2fd80ba1661f81c130b`.
