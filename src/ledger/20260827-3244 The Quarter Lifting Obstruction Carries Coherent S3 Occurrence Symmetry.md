# 3244 — The Quarter Lifting Obstruction Carries Coherent S3 Occurrence Symmetry

## Question

Do Entry 3237's reflected transport and Entry 3241's cyclic descent satisfy the generating relation of the full occurrence symmetry group?

## Frozen presentation

Let \(r\) be the site cycle and \(s\) the transposition exchanging sites two and three.  The required presentation is

\[
S_3=\langle r,s\mid r^3=s^2=1,\ srs=r^{-1}\rangle.
\]

On the three residue charts:

- \(r\) cycles \(G_{12}\to G_{23}\to G_{31}\to G_{12}\), fixes the positional retained exponents, and has residue sign \(+1\);
- \(s\) exchanges the \(G_{12}\) and \(G_{31}\) charts, fixes \(G_{23}\), swaps the two retained exponents, and has residue sign \(-1\).

## Exact checks

The relation \(srs=r^{-1}\), together with \(r^3=s^2=1\), was checked on:

1. all three site labels;
2. all six vertex and edge marked-subgraph labels;
3. all 108 signed low-occurrence states
   \[
   (G_{ij},a^mb^n),
   \qquad m+n\leq7.
   \]

The residue signs are part of the state action.  In particular, the two reflection signs in \(srs\) cancel, matching the positive sign of \(r^{-1}\).

The reflected compressed transport has rank 535 at both primes.  Entries 3237 and 3241 already establish its naturality on one reflection edge and around the cyclic atlas.  Conjugating that edge by the cyclic descent therefore supplies the remaining reflected edges without choosing new gauges.

## Result

The finite-field first-normal lifting obstruction carries a coherent \(S_3\) occurrence action.  Both supported fibers are equivariant:

\[
5=2+3
\]

and

\[
7=2+4+1.
\]

Thus the quarter defects are not only fixed-chart filtered torsion.  They are occurrence-covariant coefficient objects over the frozen resolved carrier atlas.

## Scope

This result concerns the algebraic exponent-adapter coefficient object.  It does not provide:

- a characteristic-zero certificate;
- a physical relative-cycle pairing;
- a new Carrier divisor;
- an identification with the cosmological quartic \(\mathcal Q\).

## Updated frontier

The occurrence-covariance branch is closed in the tested finite model.  The highest-information remaining gates are now:

1. exact characteristic-zero promotion of the two quarter supports;
2. source-derived physical pairing with the equivariant defect fibers;
3. comparison with existing Landau, Gram, soft, or endpoint support before assigning physical meaning.

## Evidence

- `research/benincasa/checkers/exponent_adapter_s3_coherence.py`
- `research/benincasa/results/exponent_adapter_s3_coherence.json`
- Entries 3237 and 3241.

Ledger number authority: `seqclaim-cf2365c2e6768f4677baf353`.
