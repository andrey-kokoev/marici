# Polarized Gram data cannot select a canonical quaternionic frame, so the Cayley--Dickson product does not descend

## Candidate frame source

Suppose one positive boundary mode is a quaternionic line

\[
L
\cong
\mathbb H.
\]

A unit frame `u in L` identifies the line with the coefficient algebra:

\[
\phi_u:
\mathbb H
\to
L,
\qquad
q
\longmapsto
u q.
\]

Two framed copies can then be Cayley--Dickson doubled to one octonion coefficient fiber.

The question is whether the polarized semilocal observer or its positive Gram operator canonically determines `u`.

## Residual quaternionic phase

For a nonzero feature vector `xi in L`, the positive rank-one operator is

\[
G_\xi
=|\xi\rangle
\langle\xi|.
\]

For every unit quaternion `r in Sp(1)`,

\[
G_{\xi r}
=G_\xi.
\]

Thus polarized Gram data sees only the quaternionic line/ray

\[
\xiSp(1),
\]

not a preferred unit vector.

This is the quaternionic analogue of the complex phase loss

\[
g
\mapsto
g*g^*.
\]

## No equivariant frame selection

The unit frames of one quaternionic line form a free transitive `Sp(1)`-torsor. A frame-selection rule depending only on the invariant Gram datum would have to choose one point of this torsor while remaining invariant under its free `Sp(1)` action.

If `s(G_xi)` were such a frame, invariance of `G` would imply

\[
s(G_{\xi r})
=s(G_\xi).
\]

Equivariance of a frame under source rotation would instead require

\[
s(G_{\xi r})
=s(G_\xi)r.
\]

Therefore

\[
s(G_\xi)
=s(G_\xi)r
\]

for every `r in Sp(1)`, impossible for a nonzero frame.

Hence

\[
\boxed{
\text{no }Sp(1)\text{-equivariant canonical frame can be recovered from polarized Gram data}.}
\]

## Multiplication depends on the frame

A chosen frame `u` transports quaternion multiplication to `L` by

\[
x\star_u y
=
\phi_u
\left(
\phi_u^{-1}(x)
\phi_u^{-1}(y)
\right).
\]

Change frame to

\[
u'=u r,
\qquad
|r|=1.
\]

If `x=uq` and `y=us`, their new coordinates are `r^(-1)q` and `r^(-1)s`, so

\[
x\star_{ur}y
=
u r
\left(
r^{-1}qr^{-1}s
\right).
\]

This is not generally equal to `u(qs)`.

For example, take

\[
q=s=1,
\qquad
r=i.
\]

Then

\[
1\star_u1
=1,
\]

while the multiplication transported through the frame `ui` gives coefficient

\[
i(-i)(-i)
=-i.
\]

Therefore a quaternionic line has no frame-independent algebra multiplication, even though it is canonically a quaternionic module.

## Consequence for Cayley--Dickson doubling

The Cayley--Dickson formula

\[
(a,b)(c,d)
=
(ac-\overline d b,
da+b\overline c)
\]

requires multiplication and conjugation in a specified quaternion coefficient algebra.

If the two boundary fibers are merely quaternionic lines known through their Gram operators, their independent frame groups are

\[
Sp(1)
\times
Sp(1).
\]

Generic frame changes do not act by automorphisms of the transported octonion product. Hence the product does not descend to the unframed polarized fibers.

## What does descend

The following structures are frame-independent:

- quaternionic norm;
- Hermitian inner product;
- positive rank-one Gram operator;
- right `H`-module structure, if supplied before polarization;
- the projective quaternionic line;
- `Sp(1)`-invariant quadratic forms.

Thus the positive boundary construction can remain quaternionic-Hermitian without becoming an octonion algebra.

## Possible repairs

### Retain unpolarized source phase

Carry the original observer amplitude and its quaternionic phase through every realization functor instead of replacing it by `g*g*`. This gives a frame per observer, but the resulting multiplication is observer-dependent and must be shown natural under source morphisms.

### Add a gauge fixing

Choose a boundary evaluation `ell` and impose

\[
\ell(\xi)

\in\mathbb R_{>0}
\]

real. This selects a local frame only where `ell(xi)` is nonzero and introduces singular transition loci. Global compatibility is an additional theorem.

### Keep the principal `Sp(1)` bundle

Do not choose frames. Treat boundary modes as a principal `Sp(1)` frame bundle and ask whether its doubled bundle admits a reduction of structure group to

\[
G_2
=
\operatorname{Aut}(\mathbb O).
\]

This is the coordinate-free octonionic question. A reduction requires new topological/sewing data and is not supplied by the Gram form.

## Relation to source polarization

The existing construction intentionally uses

\[
h=g*g^*
\]

to obtain positivity. This operation removes exactly the phase needed to select an algebra frame.

Accordingly there is a structural tradeoff:

\[
\boxed{
\text{polarized positivity retains norms but forgets octonionic framing}.}
\]

An octonionic refinement must either retain an unpolarized lift alongside `h`, or work gauge-covariantly with the full frame bundle.

## Updated acceptance test

Before applying the successful coefficient-level Cayley--Dickson checker to the semilocal boundary, one must construct one of:

1. a natural unpolarized quaternionic amplitude lift;
2. a globally compatible frame selection;
3. a `G2` reduction of the doubled `Sp(1)xSp(1)` frame bundle.

Without one of these, the Cayley--Dickson product is coordinate-dependent.

## Disposition

The attempt to derive a canonical quaternionic frame from the positive boundary Gram feature fails:

\[
\boxed{
G_{\xi r}=G_\xi
\quad(r\in Sp(1))
}
\]

leaves a full quaternionic phase torsor. Therefore the modewise octonion multiplication does not descend to the polarized semilocal boundary.

The viable next formulation is gauge-covariant: retain the quaternionic frame bundle and test for a source-derived `G2` reduction rather than choosing a frame by hand.
