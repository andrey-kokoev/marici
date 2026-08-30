# Fourier-orbit completion makes the response density an exact sewing intertwiner

## Why the base response is not Fourier natural

In the base analytic presentation, the source response density is

\[
r_0'=M_f u_0,
\]

where \(M_f\) denotes multiplication by the theta forcing \(f\).

Fourier does not preserve multiplication:

\[
\mathcal F M_f\mathcal F^{-1}
\]

is convolution by \(\widehat f\), not multiplication by \(f\). Therefore the
naive identity

\[
\mathcal F(fu)=(\mathcal Ff)(\mathcal Fu)
\]

is false. A scalar or multiplication-only response trace cannot satisfy the
full sewing square.

## Four response presentations

Define

\[
M_j
=
\mathcal F^jM_f\mathcal F^{-j},
\qquad
u_j=\mathcal F^ju_0,
\qquad
j\in\mathbb Z/4.
\]

The response density in presentation \(j\) is

\[
r_j'=M_ju_j.
\]

Then

\[
\mathcal F r_j'
=
\mathcal F M_j u_j
=
M_{j+1}u_{j+1}
=
r_{j+1}'.
\]

Thus Fourier sewing cyclically permutes the complete response packet exactly.

The four presentations are:

1. multiplication by \(f\);
2. convolution by \(\widehat f\);
3. multiplication by the reflected forcing;
4. convolution by the reflected Fourier forcing.

No product formula for Fourier transform is assumed.

## Integrated response histories

Let

\[
r_j(q)=r_j(q_0)+\int_{q_0}^{q}M_ju_j(\xi)\,d\xi
\]

on the declared relative-history core. If the integration basepoint and
endpoint trace are transported with the moving-seam fiber, then

\[
\mathcal F r_j=r_{j+1}
\]

up to the initial response coordinate, which is itself part of the external
boundary port.

Therefore the complete response endpoint trace obeys the cyclic Fourier
intertwining law before scalar aggregation.

## Orbit-completed kernel state

Let the base scalar Schur kernel state satisfy

\[
\mathcal D_0(s)\Psi_0=0.
\]

Define conjugate systems and states by

\[
\mathcal D_j(s)
=
\mathcal F^j\mathcal D_0(s)\mathcal F^{-j},
\qquad
\Psi_j=\mathcal F^j\Psi_0.
\]

Then

\[
\mathcal D_j(s)\Psi_j=0.
\]

The direct orbit packet

\[
\Psi_{\mathrm{orb}}
=
(\Psi_0,\Psi_1,\Psi_2,\Psi_3)
\]

is therefore a kernel state of the orbit-completed block system, and global
Fourier acts by the cyclic shift. Its response trace lies in the graph of that
shift with contragredient transport on the dual response coordinates.

This is a genuine lift of one kernel state, not an assertion that the
multiplication presentation is itself Fourier invariant.

## Green metric

The Fourier-saturated Gram is

\[
Q_{\mathrm{sat}}
=
\sum_{j=0}^{3}(\mathcal F^j)^*Q\mathcal F^j.
\]

Every conjugate response system has the same graph bound. Hence the cyclic
shift is unitary in the saturated metric, and its graph is maximal isotropic
in the doubled hyperbolic boundary form.

The analytic response packet therefore terminates its Fourier sewing flux
exactly.

## Arithmetic labels

Prime and grade coefficients remain external to the analytic presentation.
The Fourier orbit acts inside each feature fiber, while

\[
w_{p,k}=\frac1k p^{-k/2}
\]

is unchanged. Thus response orbit completion preserves prime labels, Adams
grade, cutoff restriction, and the Euler cocycle.

The primitive, square, and connected modalities are not collapsed by the
four-cycle. Each receives four conjugate analytic presentations with the same
coefficient topology.

## What this closes

On the source-generated analytic orbit, the response-density and response-trace
intertwining theorem is exact:

\[
\mathcal F\,\operatorname{Tr}_{\mathrm{resp},j}
=
\operatorname{Tr}_{\mathrm{resp},j+1}\mathcal F.
\]

Consequently a scalar Schur kernel admits a canonical orbit-completed kernel
lift whose analytic response trace lies in the maximal isotropic Fourier graph.

## Remaining global qualification

The orbit-completed kernel is a direct sum of four conjugate systems. To use it
as the completed zeta kernel state, one must prove that the global adelic
boundary totalization identifies this orbit block with one source object
rather than four diagnostic copies.

Equivalently, the determinant line of the orbit block is the fourth power of
the scalar determinant unless a source-authorized descent or fixed-point
construction removes the redundant copies.

Therefore response intertwining is closed, but determinant-faithful descent is
not.

The required next cell is

\[
\operatorname{Desc}_{\mathcal F}
\left(
\bigoplus_{j=0}^{3}\mathcal D_j(s)
\right)
\longrightarrow
\mathcal D_{\mathrm{adelic}}(s)
\]

with:

- one copy of the completed \(\Xi\) divisor;
- the full Fourier response packet retained;
- no fourth-power multiplicity;
- and the maximal isotropic boundary graph preserved.

## Hostiles

1. Apply Fourier directly to the pointwise product \(fu\).
2. Keep only multiplication presentations.
3. Multiply the Euler coefficient by a presentation-dependent phase.
4. Claim the four-block determinant is the original scalar determinant.
5. Quotient the orbit copies without retaining the response boundary graph.
6. Verify intertwining only after scalar integration.

## Verdict

Fourier-orbit completion repairs the response-trace sewing defect exactly:
multiplication and convolution responses form one cyclic packet, and every
scalar kernel state has a canonical orbit-completed lift.

The remaining obstruction is determinant-faithful Fourier descent. The four
conjugate presentations must be recognized as one adelic source object without
multiplying the \(\Xi\) divisor by four.
