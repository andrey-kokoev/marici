# Modular jet sewing is the high-frequency theta mechanism

## Exact one-copy factorization

For each source label define

\[
Z_n(z)=\int_{\mathbb R}e^{zu}\phi_n(|u|)\,du
      =2\int_0^\infty\phi_n(r)\cosh(zr)\,dr.
\]

Let a prime denote differentiation in \(z\). The ordered labelled two-copy
contribution is exactly

\[
Q_{nm}=
\beta\Re\left(Z_n'\overline{Z_m}+Z_n\overline{Z_m'}\right)
+\alpha\Im\left(Z_n'\overline{Z_m}-Z_n\overline{Z_m'}\right).
\]

Thus the entire labelled two-copy problem factors through one-copy transforms.
For \(Z=\sum_n Z_n\), the full expression becomes

\[
Q=2\beta\Re(Z'\overline Z)+2\alpha\Im(Z'\overline Z).
\]

This identity preserves every label and phase while removing the artificial
two-dimensional oscillatory quadrature.

## What the high-frequency cancellation is

Each individual folded summand \(\phi_n(|u|)\) has nonzero odd one-sided jets
at \(u=0\). Those jets generate algebraic boundary terms under repeated
Fourier integration by parts. Treating labels separately therefore creates
large terms that are not features of the full theta source.

The modularly completed source is smoothly even. Its sewing conditions are

\[
\boxed{\sum_{n\geq1}\phi_n^{(2k+1)}(0)=0\qquad(k\geq0).}
\]

The sum over labels must therefore occur before folding, integration by parts,
absolute values, or high-frequency asymptotics. This cancels every spurious
boundary jet and exposes the genuinely small completed transform.

## High-precision audit

Writing \(c=\pi n^2\), a labelled source term is

\[
\phi_n(r)=4c^2e^{(9/2)r-ce^{2r}}-6ce^{(5/2)r-ce^{2r}}.
\]

For \(e^{pr-x}P(x)\), differentiation in \(r\) acts on the polynomial by

\[
P\longmapsto(p-2x)P+2xP'.
\]

This gives arbitrary-order labelled jets without numerical differencing. A
70-decimal audit through label 20 finds relative cancellation of approximately
\(10^{-68}\) for odd orders \(1,3,5,7,9\). For order nine, the first two
labelled jets are individually about \(4.18\times10^7\) and
\(-4.12\times10^7\), while the completed sum is zero to about 60 decimal
places.

This is direct numerical evidence for the modular sewing identity, not its
proof; the proof belongs to the theta functional equation.

The same recurrence gives \(V''(0)\approx18.7269049295\) for
\(V=-\log\Phi\). Together with the certified theorem \(V'''(u)>0\) on the
positive half-line, this excludes saddle degeneracy on the real source axis.
The thimble topology can first change only through genuinely complex source
geometry.

## Stable high-frequency factorization

One-dimensional factorized quadrature at \(a=1\) gives:

\[
\begin{array}{c|rrr}
b&Q[\phi_1]&Q[\phi_1+\phi_2]&Q[\phi_1+\phi_2+\phi_3]\\ \hline
24&1.53218\times10^{-8}&7.47258\times10^{-10}&7.47249\times10^{-10}\\
32&4.47576\times10^{-10}&1.08473\times10^{-14}&1.08432\times10^{-14}\\
40&1.24812\times10^{-10}&3.88483\times10^{-19}&2.01903\times10^{-19}.
\end{array}
\]

Two Simpson resolutions, 10,000 and 20,000, agree at the displayed scales.
At \(b=40\), orbit terms of size \(10^{-10}\) sew into a completed value of
size \(10^{-19}\). The earlier two-dimensional binary64 sign at \(b=32\) was
therefore quadrature cancellation error and is retracted.

## Consequence for the conjecture

The previously proposed frequency-adaptive finite cutoff \(N(b)\) is not the
canonical high-frequency explanation. Finite partial sums are useful audits,
but the source-derived operation is the **full modular label resummation**.

The next theorem should:

1. resum the complete theta source and prove its even analytic sewing;
2. derive a phase-preserving representation of \(Z'\overline Z\) with all
   boundary jets cancelled;
3. perform saddle or contour analysis on that completed representation; and
4. prove the angular cone inequality, with a local falsifier stated for the
   completed saddle kernel.

Artifacts:

- checkers/theta_one_copy_orbit_factorization.py
- results/theta-one-copy-orbit-factorization.json
- checkers/theta_labelled_boundary_jet_cancellation.py
- results/theta-labelled-boundary-jet-cancellation.json
