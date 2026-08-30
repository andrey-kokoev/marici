# Prime shifts act unipotently on the five-cell

## Question

How do the primitive and prime-square logarithmic translations act on the
corrected five-component Fourier tail extension?

## The translation cocycle

Let

\[
(\tau_Lf)(q)=f(q+L)
\]

and retain the centered Gaussian tail

\[
K(q)=H(q)-\frac12.
\]

Then

\[
\tau_LK=K+g_L,
\qquad
g_L(q)=H(q+L)-H(q)
=-\int_q^{q+L}e^{-\pi v^2}\,dv.
\]

The difference \(g_L\) decays with Gaussian bounds at both ends. Its Fourier
transform is

\[
\widehat g_L(\xi)
=
(e^{2\pi iL\xi}-1)
\frac{i}{2\pi}
\operatorname{pv}\left(\frac{e^{-\pi\xi^2}}{\xi}\right).
\]

The zero of the phase difference cancels the principal-value singularity.
Therefore \(g_L\) lies in the Gaussian bulk rigging for every finite \(L\).

The cocycle identity is exact:

\[
g_{L+M}=g_L+\tau_Lg_M.
\]

Thus logarithmic translation acts triangularly on the extension: it fixes the
boundary class of \(K\) and adds a source-derived bulk vector.

## Boundary quotient

Let \(\mathcal E\) denote the five-component tail extension and let
\(\mathcal G\) be its Gaussian bulk subobject. In the quotient,

\[
[\tau_LK]=[K]
\quad\text{in}\quad
\mathcal E/\mathcal G.
\]

Every finite prime shift therefore acts as the identity on the asymptotic
tail class. Prime labels remain visible in the cocycle \(g_{\log p}\), but
not in the quotient coordinate alone.

This is a unipotent rather than diagonal action. In schematic block form,

\[
\tau_L=
\begin{pmatrix}
\tau_L^{\mathcal G}&g_L\\
0&1
\end{pmatrix}.
\]

## Primitive and square packets

For a finite prime cutoff \(X\) and coefficients \(a_p\),

\[
\sum_{p\in X}a_p\tau_{\log p}K
=
\left(\sum_{p\in X}a_p\right)K
+
\sum_{p\in X}a_pg_{\log p}.
\]

The first term is the boundary-quotient current. The second is its bulk
repair cocycle. They are source-coupled and may not be continued separately
after the Euler chamber.

For the primitive and prime-square choices, the boundary coefficients are
respectively proportional to

\[
p^{-s}
\quad\text{and}\quad
p^{-2s}.
\]

At the critical seam their absolute coefficient sums are governed by
\(\sum_pp^{-1/2}\) and \(\sum_pp^{-1}\), so neither becomes a continuous
scalar boundary functional merely because the archimedean five-cell has been
constructed. The primitive pro-Gram and square Hilbert grades remain
independent arithmetic types.

## Meaning

The five-cell solves the archimedean closure problem, not the arithmetic
completion problem. Its exact contribution is to reveal how arithmetic
translations meet the seam: every label produces a Gaussian bulk cocycle
over one invariant boundary class.

Consequently the combined topology must retain two axes:

1. the five-component archimedean extension;
2. the Fourier-saturated arithmetic pro-Gram family.

Collapsing either axis loses information. A scalar sum loses the prime-labelled
bulk cocycles; a bulk-only quotient loses the invariant seam class.

## Falsifier and next gate

The unipotent description fails if some authorized local prime transport
changes the asymptotic class rather than adding a Gaussian bulk cocycle. For
ordinary logarithmic translation the formula above proves it does not.

The remaining gate is modular sewing of the finite-cutoff packet:

\[
\left(
\sum_{p\in X}a_p,
\sum_{p\in X}a_pg_{\log p}
\right).
\]

One must determine whether reciprocal primitive and square packets cancel or
renormalize the quotient coefficient while their labelled bulk cocycles glue
in the Gaussian rigging. A cancellation visible only after scalar summation
is insufficient.

## Result

Prime shifts act unipotently on the five-component tail extension. They are
identity on the boundary quotient and carry all label dependence in a
Gaussian bulk cocycle. The five-cell introduces no new arithmetic
regularization; primitive and square completion grades must remain explicit
in a two-axis tensor construction.
