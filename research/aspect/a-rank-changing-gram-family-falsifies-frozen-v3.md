# A rank-changing Gram family falsifies frozen v3

## Target

Frozen v3 admits only nondegenerate metric route spaces. It says singular Gramians require a separate stratum, but it defines no degenerate route object, specialization arrow, radical quotient, or gluing cell.

That omission is fatal for even the smallest rank-changing family.

## Hostile packet

Let

\[
G(t)=
\begin{pmatrix}1&0\\0&t\end{pmatrix},
\qquad
F(t)=I.
\]

The metric relation holds identically:

\[
F(t)^*G(t)F(t)=G(t).
\]

For \(t>0\), the metric is positive definite. For \(t<0\), it has signature \((1,1)\). At \(t=0\), its rank drops from two to one and its radical is

\[
\operatorname{rad}G(0)=\operatorname{span}(e_2).
\]

The determinant crosses zero simply:

\[
\det G(t)=t.
\]

This is one coherent family, not three unrelated packets. Its invariant content includes the generic metrics, the central radical, the quotient metric on \(V/\operatorname{rad}G(0)\), and the normal first jet recording how the null direction re-enters.

## Decision

Frozen v3 cannot type the family over a base containing \(t=0\):

- its route object requires nondegeneracy;
- its metric dagger requires an inverse Gramian;
- its signature field cannot remain constant through the crossing;
- no specialization arrow relates generic fibers to the singular fiber;
- no cell records radical, quotient, or normal jet.

Therefore v3 is falsified.

Deleting \(t=0\) is not a repair. It destroys the comparison that identifies the two nondegenerate regions as parts of one packet and erases the rank-change event the apparatus is meant to resolve.

## Required future repair

A future v4 would need a stratified metric route object containing:

1. a base stratification by constant rank and signature;
2. the radical subspace on every singular stratum;
3. the induced nondegenerate quotient metric;
4. specialization and generization arrows;
5. a normal jet or crossing form;
6. gluing laws for associators, exchanges, and exposure maps across strata;
7. a rule distinguishing transverse crossings from higher-order tangencies.

The natural local invariant at a simple crossing is the form induced by \(G'(0)\) on the radical. Here it is the positive scalar one. That scalar orients the crossing without inventing a privileged inverse at the singular point.

## Optical meaning

Dark ports, exceptional points, polarization zeros, threshold collisions, and determinant divisors are rank-changing Gram phenomena. An instrument grammar that works only on nondegenerate fibers omits the very loci where network topology changes.

This is also why a 3+2+1 architecture cannot be inferred independently on each open stratum. The gluing data determine whether channels merge, split, or acquire defect memory at the singular locus.

## Verification

```text
uv run --with sympy python research/aspect/checkers/check_v3_rank_change_stratum_falsifier.py
```
