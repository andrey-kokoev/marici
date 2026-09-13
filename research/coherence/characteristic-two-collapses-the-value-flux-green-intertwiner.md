# Characteristic two collapses the value/flux Green intertwiner

## Integral transfer matrix

The seam-to-asymptotic transfer uses a factor \(1/2\). Before dividing, its matrix at reciprocal position weights \((y^{-1},y)\) is

\[
2C_y=
\begin{pmatrix}
-y^{-1}&-y^{-1}\\
y&-y
\end{pmatrix}.
\]

Its determinant is

\[
\det(2C_y)=2.
\]

Thus the full value/flux to incoming/outgoing comparison requires that two be invertible.

## Characteristic-two failure

In characteristic two,

\[
-1=1.
\]

The matrix becomes

\[
2C_y=
\begin{pmatrix}
y^{-1}&y^{-1}\\
y&y
\end{pmatrix},
\]

which has rank one. Simultaneously, the reflection action

\[
(J^0,J^1)\mapsto(-J^0,J^1)
\]

becomes trivial on both coordinates. The value-odd and flux-even parity labels can no longer be distinguished by reflection.

Therefore the seam double and asymptotic hyperbolic double are not related by the characteristic-zero Green intertwiner after reduction modulo two.

## Scope table

### Valid over a general commutative ring

- unnormalized reciprocal/direct moment map;
- additive assembly of labelled fluxes;
- formal reflection swap of direct and reciprocal weights;
- polynomial Pfaffian and cofactor identities.

### Requires selected units

- localized adjacent hyperbolic minimalization;
- split endpoint quotient from a chosen two-seam frame.

### Requires two invertible

- normalized Green kernel \(\frac12e^{-|x-y|}\) as the inverse of \(1-\partial^2\);
- isomorphism between value/flux and incoming/outgoing doubles;
- separation of reflection-odd and reflection-even seam eigenspaces by projectors.

## Consequence

The coefficient regime is part of the constructor alphabet. “The seam type has rank two” is insufficient: in characteristic two its intended parity splitting and Green transfer degenerate.

A portable theorem must declare one of:

```text
base is a Z[1/2]-algebra
base has an explicit inverse of two
characteristic-two fiber is a separate singular stratum
```

## Verification

```text
python research/coherence/check_characteristic_two_seam_transfer_obstruction.py
```

The checker verifies rank one in characteristic two and rank two in characteristics three, five, seven, and eleven.

Artifacts:

- `check_characteristic_two_seam_transfer_obstruction.py`
- `characteristic-two-seam-transfer-obstruction.v1.json`
