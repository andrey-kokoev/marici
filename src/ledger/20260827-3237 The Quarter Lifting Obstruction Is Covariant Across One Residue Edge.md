# 3237 — The Quarter Lifting Obstruction Is Covariant Across One Residue Edge

## Question

Does Entry 3225's filtered lifting obstruction survive a source-derived occurrence-chart transition, or is it an artifact of the fixed \(G_{12}\) presentation?

## Independent target

Reconstruct the \(G_{31}\) exponent pencil directly from the reflected source data of Entry 756:

\[
(X_1,X_2,X_3)=(2,3,4)
\longmapsto
(2,4,3),
\]

\[
(a,b)\longmapsto(c',a')=(b,a),
\]

with marked-pole order

\[
(g_1,g_2,g_3,g_{23},g_{31})
\longmapsto
(g_1,g_3,g_2,g_{23},g_{12}).
\]

The Poincaré-residue convention forces the transport sign \(-1\).

The target pencil was constructed independently at primes 32003 and 32009.  It was not obtained by conjugating the \(G_{12}\) matrix.

## Quotient transport

The two compressed pencils select different active-coordinate gauges.  Therefore raw coordinate permutation is not typed.  Each source active coordinate was first lifted to its ambient labelled monomial, reflected, reduced through the target's 14933 retained quotient pivots, and only then expressed in the target active basis.

This produces a rank-535 signed transport.

## Checks

At both quarter points and both primes:

1. the mapped \(G_{12}\) source module and the independently constructed \(G_{31}\) source module contain each other through first normal order;
2. both constant and first-normal inclusion failure counts are zero in both directions;
3. all 36 low rows map exactly under
   \[
   a^ib^j\longmapsto-\,c^ja^i;
   \]
4. the target source first-normal residual rank is zero;
5. the target lifting-obstruction ranks and filtrations are
   \[
   5:(0,0,0,0,0,2,5,5)
   \]
   at \(-5/4\), and
   \[
   7:(0,0,0,0,0,2,6,7)
   \]
   at \(-7/4\).

## Result

Entry 3225's first-normal lifting obstruction is natural across the labelled \(G_{12}\to G_{31}\) residue edge.  Its ranks and filtration are not fixed-chart artifacts.

The proof uses the decomposition

\[
\text{source module}
\oplus
\text{signed low rows}.
\]

One must not test the nonflat augmented module by reducing all generators against a special-fiber basis: omitted torsion generators then appear spuriously as first-normal failures.  Source-module dual inclusion plus exact low-row transport is the typed comparison.

## Scope

This proves one reflection edge, not the complete three-chart cocycle.  Full occurrence descent still requires the independently reconstructed \(G_{23}\) edge and signed cyclic composition.

## Evidence

- `research/benincasa/checkers/exponent_adapter_occurrence_covariance.py`
- `research/benincasa/results/exponent_adapter_occurrence_covariance.json`
- the two independent \(G_{31}\) sparse pencils and two signed transport packets in `research/benincasa/results/`.

Ledger number authority: `seqclaim-9b4cdfcc9e635df6dc720f04`.
