# Defect-augmented restatement of the Suzuki-to-semilocal comparison

## Status correction

Prior research already proves that Suzuki's unconditional positive carrier cannot reproduce the off-axis arithmetic hyperbolic block and that universal equality is equivalent to the zero-location theorem. The construction below packages that known result as a Hermitian-form comparison cone; it does not add a new analytic comparison edge to the canonical semilocal pyramid.

## Comparison problem

Let

\[
\mathcal Q_{semi}
\]

denote the established semilocal Hermitian-form presentation of the completed observer pairing, and let

\[
\mathcal Q_{Suz}^{+}
\]

denote Suzuki's unconditional positive \(L^2\) presentation.

Both are defined from completed arithmetic source data, but they do not represent the same Hermitian form unconditionally.

## Two source pullbacks

For a source coefficient packet \(c_Z\), Suzuki's pullback is

\[
q_{Suz,Z}(c,d)
=
\frac12
d^*G_{F,Z}c.
\]

The completed arithmetic pullback is

\[
q_{arith,Z}(c,d)
=
\frac12
d^*J_{\Xi,Z}c.
\]

Their exact difference is

\[
\delta_Z(c,d)
=
\frac12
d^*
(
J_{\Xi,Z}-G_{F,Z}
)c.
\]

Thus

\[
q_{arith,Z}
=
q_{Suz,Z}
+
\delta_Z.
\]

## Defect-augmented Suzuki presentation

Define

\[
\mathcal Q_{Suz}^{aug}
=
(
\mathcal Q_{Suz}^{+},
\delta
).
\]

This object retains:

1. the unconditional positive Suzuki feature;
2. the signed comparison defect;
3. their summed arithmetic readout.

By construction, its source pullback equals the semilocal arithmetic form:

\[
\mathcal Q_{Suz}^{aug}

ightsquigarrow
q_{arith}
=
\mathcal Q_{semi}.
\]

Therefore there is a source-authorized signed comparison

\[
\eta_{semi,Suz}^{signed}:
\mathcal Q_{semi}
	o
\mathcal Q_{Suz}^{aug}
\]

in the category of Hermitian-form presentations.

This comparison is equality of represented forms with different retained factorization data.

## Why the positive comparison is absent

Forgetting the defect would replace

\[
q_{arith}
\]

by

\[
q_{Suz}.
\]

A form-preserving edge

\[
\mathcal Q_{semi}
	o
\mathcal Q_{Suz}^{+}
\]

would therefore require

\[
\delta=0
\]

on the admitted source.

On finite packets this is

\[
J_{\Xi,Z}=G_{F,Z}
\]

on the reached coefficient subspace. On the completed source, Suzuki's theorem identifies universal equality with the zero-location condition.

Hence the missing positive edge is not an unconstructed change of coordinates. It is the arithmetic theorem.

## Relation-valued comparison

Before equality, the two positive carriers still have a canonical source-labelled relation

\[
\mathcal R_{semi,Suz}
=
\left\{
(
A_{semi}p,
A_{Suz}p
):
p\in\mathscr G
\right\}.
\]

This relation becomes the graph of a bounded operator exactly when the corresponding source Gram domination holds. It becomes an isometry exactly when the two pullback Grams agree.

Thus the joint graph is the maximal unconditional comparison object.

## Placement relative to the canonical pyramid

The established semilocal pyramid already has its four realization vertices and signed subdivision. Suzuki's presentation should not replace canonical vertex \(V_2\).

Instead, attach

\[
\mathcal Q_{Suz}^{aug}
\]

as an external comparison vertex over the completed arithmetic form. The signed edge to the pyramid is available because the defect is retained.

The pure positive Suzuki vertex lies over the same source only after applying the forgetful operation

\[
(
q_{Suz},
\delta
)
\longmapsto
q_{Suz},
\]

which changes the represented form unless \(\delta=0\).

Therefore the correct geometry is a comparison cone attached to the canonical tetrahedron, not an unproved identification of one of its vertices.

## Homotopy-fiber formulation

Let

\[
F:
\mathsf{PosPres}
	o
\mathsf{HermPres}
\]

forget the positive factorization while retaining the represented form.

The signed comparison determines a point in \(\mathsf{HermPres}\). A positive Suzuki comparison is a point in the corresponding homotopy fiber.

That fiber is nonempty exactly when the defect can be absorbed by a source-authorized contraction. Vanishing defect is the isometric special case.

Higher coherence organizes choices inside the fiber but does not create a point when the Gram condition fails.

## Consequence for lattice work

No new edgewise subdivision should be built from the Suzuki coefficient diagram until one of the following is supplied:

1. a natural positive comparison edge to an established canonical vertex;
2. a defect-absorbing contraction compatible with the canonical source;
3. a proof that the defect vanishes on the admitted source.

Without one of these, subdivision merely repeats the signed defect identity at every cell.

## Disposition

The prior-research-compatible comparison is now exact:

\[
\mathcal Q_{semi}
=
\mathcal Q_{Suz}^{+}
+
\delta_{Suz}
\]

as source pullback forms.

This constructs a signed defect-augmented comparison cone. It does not construct a positive lattice edge. The missing positive edge is equivalent to absorption or vanishing of the Suzuki comparison defect.
