# A projective torus transport falsifies frozen v12

## Result

Version 12 is falsified. A coherent projective transport need not admit the honest (U(r)) path-groupoid representation required by v12.

## Hostile packet

Take the group

\[
G=\mathbb Z_2\times\mathbb Z_2
\]

and define

\[
\rho(a,b)=X^aZ^b.
\]

The product law is projective:

\[
\rho(a,b)\rho(c,d)
=
(-1)^{bc}\rho(a+c,b+d).
\]

The multiplier

\[
\omega((a,b),(c,d))=(-1)^{bc}
\]

satisfies the 2-cocycle law exactly.

## Decisive obstruction

The two generators commute in (PU(2)), because their discrepancy is central. Their (U(2)) lifts obey

\[
XZ=-ZX,
\qquad
XZX^{-1}Z^{-1}=-I.
\]

Multiplying either lift by any scalar phase leaves this commutator unchanged. Therefore no rephasing turns these projective loop transports into commuting matrices.

The packet is coherent projective transport on the torus, but it is not an honest (U(2)) representation of the torus group.

## Exact defect in v12

v12 demands that all path-groupoid relations hold as matrix equalities. It consequently rejects this valid projective packet. It has no object for the multiplier, central extension, projective bundle, or gerbe class.

For coherent optical modes, the central commutator can be read by a phase-referenced composition interferometer even though rays and projective transformations close.

## Required successor

A successor must retain:

- a (PU(r)) transport bundle;
- local (U(r)) lifts;
- their (U(1)) multiplier 2-cocycle;
- coboundary gauge transformations between lifts;
- the corresponding central extension or bundle gerbe;
- gerbe-compatible specialization and completed sewing.

An honest (U(r)) representation is then a trivialization of this obstruction, not a prerequisite for admission.

## Verification

```text
uv run --with sympy python research/aspect/checkers/check_v12_projective_torus_falsifier.py
```
