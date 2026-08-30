# Theta forcing is an exact impedance port and wave-flux difference

## Status

Exact control-theoretic reformulation of the source-tail forcing. It replaces
the impossible attempt to treat the constant source channel as a finite-energy
autonomous state by a typed input/output port. The remaining theorem is global
losslessness of the source-derived arithmetic scattering relation.

## Forced tail as an impedance system

Consider the source-derived tail equation

\[
G'=-zG-f(q)c.
\]

Type the constant channel as an input

\[
u=c
\]

and define the conjugate output

\[
y=-\overline{f(q)}G.
\]

Then

\[
2\operatorname{Re}(\overline u,y)
=
-2\operatorname{Re}(fc\overline G).
\]

The tail energy identity becomes

\[
\partial_q|G|^2
=
-2\operatorname{Re}z\,|G|^2
+
2\operatorname{Re}(\overline u,y).
\]

This is an exact impedance-passivity balance. The indefinite forcing is not a
defective bulk norm. It is boundary work through a conjugate input/output
pair.

## Cayley rotation to wave variables

Define incoming and outgoing wave amplitudes

\[
a_{\mathrm{in}}
=
\frac{u+y}{\sqrt2},
\qquad
a_{\mathrm{out}}
=
\frac{u-y}{\sqrt2}.
\]

Their positive flux difference is

\[
|a_{\mathrm{in}}|^2-|a_{\mathrm{out}}|^2
=
2\operatorname{Re}(\overline u,y).
\]

Therefore

\[
\partial_q|G|^2
+
2\operatorname{Re}z\,|G|^2
=
|a_{\mathrm{in}}|^2-|a_{\mathrm{out}}|^2.
\]

The forcing polarization has become the difference of two independently
nonnegative wave fluxes. Neither flux may be deleted or declared positive in
isolation as an RH argument; their relation must come from the complete source
scattering law.

## Why a frozen source is not an autonomous reservoir state

The homogeneous augmentation uses

\[
\Psi=inom{G}{c},
\qquad
\Psi'
=
\begin{pmatrix}
-z&-f\\
0&0
\end{pmatrix}
\Psi.
\]

On the seam, take \(\operatorname{Re}z=0\). No fixed positive-definite metric
can make this triangular generator conservative when \(f\ne0\). At \(z=0\),
the off-diagonal block of the Lyapunov equation already requires

\[
af=0,
\]

where \(a>0\) is the state weight on \(G\). This is impossible.

A finite conservative coupling would need a reciprocal equation for \(c\), so
the source amplitude would no longer remain constant. Thus \(c=1\) is
correctly typed as an external incoming field or an idealized coherent drive,
not as an ordinary closed-system state.

## Two-sector scattering law

For the doubled Fourier–Tate system, introduce ports

\[
(u_+,y_+),
\qquad
(u_-,y_-),
\]

with

\[
y_+=-\overline{f_+}G_+,
\qquad
y_-=-\overline{f_-}G_-.
\]

The previously isolated forcing difference is a signed impedance supply. A
sector-aware Cayley transform converts it into a signed sum of incoming and
outgoing positive fluxes.

The desired Fourier–Tate constructor is therefore a scattering relation

\[
\mathsf S_z:
\mathcal A_{\mathrm{in}}
\longrightarrow
\mathcal A_{\mathrm{out}}
\]

on the complete labelled boundary field. On the critical seam it should be
lossless:

\[
\mathsf S_z^*\mathsf S_z=I.
\]

Off the seam its flux defect must be exactly the positive tail energy weighted
by \(2\operatorname{Re}z\).

## Integrated confinement identity

For a two-ended zero-state,

\[
G(0)=G(\infty)=0.
\]

Integrating the wave balance gives

\[
2\operatorname{Re}z
\int_0^\infty|G(q)|^2\,dq
=
\int_0^\infty
\left(
|a_{\mathrm{in}}(q)|^2
-
|a_{\mathrm{out}}(q)|^2
\right)dq.
\]

If source-derived reciprocal sewing proves equality of total incoming and
outgoing flux for an admissible zero-state, the right side vanishes. A nonzero
tail state then forces \(\operatorname{Re}z=0\).

This is the exact physical theorem sought by the programme. Its missing part
is not positivity; both wave fluxes are already positive. The missing part is
the global arithmetic losslessness relation.

## Where the arithmetic channels belong

The endpoint, primitive, prime-square, connected-tail, seam, and archimedean
channels should be components of the complete boundary wave field. Their
coupled current must determine the scattering relation before scalar
projection.

The local Tate gamma factors may supply local phase transitions, but local
unitarity does not establish restricted-product losslessness. The first two
non-trace-class currents must remain as boundary ports rather than being
discarded during determinant regularization.

## Relation to the full seam history

An instantaneous scalar port is insufficient at growing cutoffs. The earlier
finite-jet obstruction requires the incoming and outgoing objects to retain
the complete moving-boundary history or another source-derived
cutoff-growing realization. The Cayley transformation is pointwise in the
port variables; it does not justify compressing their history to finitely many
coordinates.

## Hostile-source test

Every forced scalar equation admits the impedance identity above. Therefore
that identity alone carries no RH-specific information. The arithmetic content
begins only with a source-derived scattering relation that hostile signed prime
perturbations fail.

The decisive hostile test keeps:

- the same two-sector analytic architecture;
- the same reciprocal scalar functional equation;
- the same local Cayley port conversion;

while changing the labelled prime boundary incidence. If the proposed global
losslessness law survives unchanged, it adds no information beyond symmetry.

## Finite falsifier

At cutoff \(X\), assemble the boundary maps

\[
A_{\mathrm{in},X},
\qquad
A_{\mathrm{out},X}.
\]

The losslessness residual is

\[
R_X
=
A_{\mathrm{in},X}^*A_{\mathrm{in},X}
-
A_{\mathrm{out},X}^*A_{\mathrm{out},X}
-
2\operatorname{Re}z\,H_X.
\]

Any nonzero typed entry or minor of \(R_X\) falsifies the proposed scattering
completion. Scalar cancellation of nonzero typed residual blocks is not
admissible.

## Verdict

The constant channel does not need to be forced into the state Hilbert space.
It is naturally an input port. The indefinite forcing current is exactly its
impedance supply, and a Cayley rotation turns that supply into incoming minus
outgoing positive wave energy. RH-strength content is now concentrated in one
source theorem: global Fourier–Tate scattering must be lossless on completed
zero-states, with every arithmetic and archimedean boundary channel retained.
