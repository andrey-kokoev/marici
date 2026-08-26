# The flagged section is driven by second-fundamental-form leakage

## Status

Exact coupling identity. For a moving rank-one boundary line and a fixed
ordered source vector, the covariant derivative of the scalar readout is the
second fundamental form applied to the source component outside the retained
line.

This identifies the missing constructor precisely. Zero exclusion requires the
leakage forcing to close homogeneously on the flagged section. An independent
forcing term permits a transverse zero even when the ambient transport,
compressed connection, and curvature are all regular.

## Moving line and ordered source

Let \(u\) be a normalized local frame,

\[
u^*u=1,
\qquad
P=uu^*.
\]

Let \(b\) be the fixed ordered source vector. Define the flagged scalar section

\[
\sigma=u^*b.
\]

Decompose the source into retained and complementary components:

\[
b=u\sigma+b_\perp,
\qquad
u^*b_\perp=0.
\]

The line connection in the frame \(u\) is

\[
\mathcal A=u^*du.
\]

## Exact leakage identity

Differentiate the scalar section:

\[
d\sigma=du^*b.
\]

Using

\[
du^*u=-u^*du=-\mathcal A
\]

and the decomposition of \(b\), obtain

\[
d\sigma
=
-\mathcal A\sigma
+du^*b_\perp.
\]

Therefore the covariant derivative satisfies

\[
D\sigma
:=
d\sigma+\mathcal A\sigma
=
du^*b_\perp.
\]

The right-hand side is the adjoint second fundamental form evaluated on the
discarded source component. It is the exact forcing term for the ordered
readout.

## Operator form

The retained source section is

\[
s=Pb=u\sigma.
\]

For fixed \(b\), its compressed derivative is

\[
P\,ds=P\,dP\,(I-P)b.
\]

The off-diagonal block

\[
P\,dP\,(I-P)
\]

is the leakage channel from the invisible complement into the observable
boundary state.

Curvature involves a quadratic composition of off-diagonal blocks. The scalar
section equation sees one directed block together with the actual ordered
source. This is why curvature alone loses the required incidence information.

## Homogeneous-closure criterion

Suppose the source laws imply, without dividing by \(\sigma\), that

\[
du^*b_\perp=\kappa\sigma
\]

for a regular one-form \(\kappa\). Then

\[
D\sigma=\kappa\sigma.
\]

Along any path this is a homogeneous first-order equation. A nonzero anchored
value remains nonzero under its transport.

This would be a genuine zero-exclusion mechanism because it acts before scalar
projection and uses the ordered source incidence.

But defining

\[
\kappa=\frac{du^*b_\perp}{\sigma}
\]

afterward is forbidden. It divides by the section whose nonvanishing is at
issue. The factorization must be derived from source constructors and remain
regular at candidate zeros.

## Transverse-zero hostile

Take the real moving frame

\[
u(a)=
\begin{pmatrix}
\cos a\\
\sin a
\end{pmatrix}
\]

and fix

\[
a_0=\frac\pi4,
\qquad
b=
\begin{pmatrix}
-\sin a_0\\
\cos a_0
\end{pmatrix}.
\]

Then

\[
\sigma(a)=b^*u(a)=\sin(a-a_0).
\]

At \(a=a_0\),

\[
\sigma(a_0)=0,
\qquad
\sigma'(a_0)=1.
\]

The connection is regular and the line remains normalized. The nonzero second
fundamental forcing drives the section directly through zero.

This is the minimal finite falsifier for any proposed coupling law that does
not control the directed leakage block.

## Relation to the theta tail system

The source-derived tail equation already has the form of an inhomogeneous
boundary flow. The doubled Clark--Green calculation isolated an explicit
forcing current rather than a homogeneous scalar transport.

In the present geometry, that forcing should be typed as the second fundamental
leakage from the retained tail--seam state into the ordered endpoint/source
section.

The primitive, prime-square, seam, and archimedean currents may jointly repair
this leakage in one of two ways:

1. they factor it homogeneously through \(\sigma\);
2. they contribute a definite state-level charge that makes a zero-state
   forcing identity impossible off the seam.

If a residual additive forcing survives, transverse zeros remain compatible
with the connection architecture.

## Exact next calculation

At every finite Euler cutoff, construct:

\[
P_X,
\qquad
b_X,
\qquad
P_XdP_X(I-P_X)b_X.
\]

Then test whether the typed sum of primitive, square, seam, and archimedean
currents yields a source-authorized factorization

\[
P_XdP_X(I-P_X)b_X=K_XP_Xb_X
\]

with \(K_X\) regular and compatible across cutoffs.

Immediate falsifiers are:

- failure of the incidence maps defining \(P_X\);
- a nonzero leakage vector when \(P_Xb_X=0\);
- a factorization constant diverging with the cutoff;
- factorization requiring division by the scalar readout;
- mismatch between reciprocal sheets;
- disappearance of primitive or square boundary types after completion.

## Decisive conclusion

The rotation programme has reached the directed coupling hidden beneath
curvature. A flagged zero is created by complement-to-boundary leakage. The
source-level theorem needed for RH is not positivity of the ambient bundle or
its curvature; it is homogeneous closure, or an independently definite
balance law, for that leakage channel.

This is now a finite operator-valued question at every cutoff. It cannot be
answered until the valuation/Fock-to-boundary incidence maps are explicitly
constructed.
