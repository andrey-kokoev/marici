# A coherence observer must distinguish fixed points from symmetry-orbit equivalence

## Finite test

On the stationary residual double, let

\[
T(z)=\begin{pmatrix}z&0\\0&z^{-1}\end{pmatrix},
\qquad
R=\begin{pmatrix}0&1\\1&0\end{pmatrix}.
\]

Reciprocity gives

\[
RT(z)R=T(z)^{-1}
\]

for every nonzero \(z\). Therefore the direct and reciprocal presentations are conjugate for every parameter value.

By contrast, literal fixed-point equality is

\[
T(z)=T(z)^{-1}
\quad\Longleftrightarrow\quad
z^2=1.
\]

On the positive component this leaves \(z=1\).

## Falsification

The proposed implication

```text
same complete unframed behavior
=> symmetry-fixed parameter
```

is false. An observer that quotients by all admitted isomorphisms identifies reciprocal orbit mates for every \(z\), because reversal itself supplies the conjugacy.

Thus ordinary Yoneda equivalence in the unframed action groupoid detects symmetry orbits, not fixed points.

## Required refinement

To detect a fixed locus, the meta-observer must retain a frame and distinguish:

```text
orbit equivalence:     A is isomorphic to R(A)
literal fixed point:   A equals R(A) in the retained frame
framed fixed point:    A -> R(A) preserves the declared orientation/interface
```

The relevant comparison is therefore not merely

\[
Y^2(A_z)\simeq Y^2(RA_z).
\]

It must ask whether the reciprocal comparison lies over the identity of the retained frame, or whether its defect vanishes in a relative equalizer:

\[
\operatorname{Eq}(\mathrm{id},R).
\]

## Meta-Pyramid consequence

The next coherence level must observe the comparison morphism, not only its source and target:

```text
P1  direct and reciprocal objects
P2  comparison morphism R
P3  compatibility of R with ports and orientation
P4  equalizer defect: does R reduce to identity in the retained frame?
```

This prevents a symmetry from proving its own fixed-point condition merely by exhibiting an orbit equivalence.

## Verification

The exact-rational checker verifies reciprocal conjugacy for 64 positive rational values and literal equality exactly at \(z^2=1\):

```text
python research/coherence/check_reciprocal_fixed_locus_vs_orbit_equivalence.py
```

Artifacts:

- `check_reciprocal_fixed_locus_vs_orbit_equivalence.py`
- `reciprocal-fixed-locus-vs-orbit.v1.json`
