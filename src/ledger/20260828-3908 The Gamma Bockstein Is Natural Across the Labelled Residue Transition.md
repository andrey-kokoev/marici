# 3908 — The Gamma Bockstein Is Natural Across the Labelled Residue Transition

## Remaining gate

Entries 3902 and 3905 established a unique projective conductor-descent line. Absolute source normalization still required the labelled naturality square

\[
T_L\,\beta_{12}=\beta_{31}\,T_R
\]

for the orientation-sensitive \(G_{12}\to G_{31}\) residue transition.

## Frozen data

We retained:

- the literal source exponent \(\gamma\), with normal coordinate \(\gamma\mapsto\gamma+\epsilon\);
- the physical value \(\gamma=-\tfrac12\);
- the source and independently constructed target presentations;
- the labelled pole permutation of Entry 756;
- the forced Poincaré-residue sign \(-1\);
- ambient degree \(14\), cutoff degree \(7\), and the complete five-mark packet.

No quotient-basis alignment, primitive selection, or scalar rescaling was fitted.

## Generator-level audit

At primes \(32009\) and \(32003\):

\[
\dim Q_{12}=\dim Q_{31}=26,
\qquad
\operatorname{rank}T_{12\to31}=26.
\]

All \(11{,}521\) retained ordinary exact relations transport into the target exact image.

The gamma derivative of an integration-by-parts generator is the source-fixed \(\partial K\) term. Under

\[
(a,b)\longmapsto(c',a')=(b,a),
\]

the two derivative axes exchange. Every one of the \(480\) gamma-normal generators satisfies the signed transition identity, with zero failures at both primes.

## Result

The labelled transition is an isomorphism of the dual-gamma exact presentations, not merely of their specialized quotient spaces. Therefore the induced Bockstein is independent of retained pivots and primitive representatives on this chart edge.

The only remaining scalar freedom is deliberate reparameterization of the declared normal coordinate. With the source coordinate fixed as the literal exponent \(\gamma\), its slope is one and the scalar is source-normalized. A replacement \(\gamma\mapsto c\gamma\) changes the source convention; it is not a gauge of the frozen problem.

## Narrow conclusion

The local constructor is now fixed absolutely on the \(G_{12}\leftrightarrow G_{31}\) edge by:

1. the literal gamma coordinate;
2. the simple-pole normalization;
3. the primitive Milnor generator;
4. the Poincaré-residue orientation;
5. the labelled chart transition.

This closes the pivot, primitive, and one-edge normalization gates. It does not yet prove the signed three-chart cocycle for the dual-gamma family.

## Next falsifier

Construct the other two dual-gamma transition edges independently and test their signed order-three composite on the exact presentation and common defect line. Any nonidentity scalar after three edges is a genuine descent obstruction.

## Artifacts

- `research/benincasa/checkers/check_rank26_gamma_bockstein_transition_naturality.py`
- `research/benincasa/results/rank26-gamma-bockstein-transition-naturality.json`
- `research/benincasa/results/rank26-gamma-bockstein-transition-naturality-p32003.json`

Ledger sequence claim: `seqclaim-3f4f3f90180194483cf46e42`.
