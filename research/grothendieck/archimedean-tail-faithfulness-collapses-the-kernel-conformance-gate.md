# Archimedean tail faithfulness collapses the kernel-conformance gate

## Positive archimedean feature

The completed gamma weight on the real spectral line has logarithmically positive tails. Hence there is a nonempty open tail region on which

\[
w_\Gamma^+(u)>0.
\]

The fixed-width Gaussian translate span consists of functions of the form

\[
f(u)=e^{-\sigma u^2}
\sum_{j=1}^nc_je^{-ia_ju},
\]

which extend analytically in `u`.

If the positive gamma feature vanishes,

\[
\sqrt{w_\Gamma^+}\,f=0,
\]

then `f` vanishes almost everywhere on an open tail interval. Analytic uniqueness forces

\[
f=0.
\]

Therefore the assembled positive row `A_N`, which contains this gamma feature, is injective on every finite Gaussian translate span:

\[
\ker A_N=0.
\]

## Consequence for the Douglas map

The rule

\[
C_N(A_Nf)=B_Nf
\]

is automatically well-defined. No separate infinite identity theorem is needed to prove `ker A_N subset ker B_N` on this probe domain. The entire positivity content is the norm inequality

\[
\|B_Nf\|\le\|A_Nf\|.
\]

Thus conformance remains essential for identifying the common endpoint--gamma--prime form, but it does not supply a hidden part of the Douglas positivity crossing once the positive archimedean tail is retained.

## Correction to cutoff compatibility

The labelled feature ambient spaces are nested by appending coordinates, but the source ranges are not nested by the zero-coordinate embedding:

\[
A_{N+1}f=(A_Nf,a_{N+1}f),
\]

not `(A_Nf,0)`. Consequently it is incorrect to demand literal restriction of `C_(N+1)` to `ran A_N`.

Let `P_N^+` and `P_N^-` be coordinate projections from cutoff `N+1` to cutoff `N`. The correct conformance cells are

\[
P_N^+A_{N+1}=A_N,
\qquad
P_N^-B_{N+1}=B_N,
\]

and

\[
P_N^-C_{N+1}A_{N+1}
=
C_NP_N^+A_{N+1}
=
B_N.
\]

These equations compare the contractions only on source-generated graph vectors. They do not assert that arbitrary old feature vectors embed as invariant subspaces of the new contraction.

## Disposition

Collapse the kernel-inclusion gate on the analytic Gaussian probe span: archimedean positive-tail faithfulness makes it automatic. Correct cutoff naturality from restriction to a projected commuting square. The remaining RH-strength condition is uniform contractivity on source-generated vectors, followed by closure in the completed graph norm.
