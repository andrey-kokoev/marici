# Regulator comparison reduces to two Hilbert--Schmidt leg limits and one angular dominated-convergence bound

## Finite regulated sewing

Fix an angular character `chi` and finite regulators

\[
\alpha
=(\Lambda,R,N).
\]

After recentering the physical boundary and extracting the universal exponential cutoff translation, write the two observer-localized Gram legs as

\[
B_{\alpha,\chi}(g),
\qquad
C_{\alpha,\chi}(g)
\]

in a common Hilbert--Schmidt space. Their sewing entry is

\[
\boxed{
\mathcal E_{\alpha,\chi}(g)
=
\langle
B_{\alpha,\chi}(g),
C_{\alpha,\chi}(g)
\rangle_{HS}.
}
\]

The angular cutoff `N` is assumed large enough to retain `chi`; it is kept in the notation because the full operator is initially a finite angular sum.

## Target relative Hardy legs

Let

\[
B_{\chi}^{rel}(g),

C_{\chi}^{rel}(g)
\]

be the observer-localized Hardy/Tate legs defining the relative projection-pair trace. Thus

\[
\boxed{
\mathcal E_{\chi}^{rel}(g)
=
\langle
B_{\chi}^{rel}(g),
C_{\chi}^{rel}(g)
\rangle_{HS}
}
\]

or, when only their product is trace class, the corresponding relative trace pairing.

The relative trace formula identifies this target with

\[
\mathcal E_\chi^{rel}(g)
=
\frac1{2\pi i}
\int
|m_{g,\chi}(s)|^2
\partial_s
\log\gamma_\chi(s)ds
+
e_{end,\chi}(g).
\]

## Hilbert--Schmidt comparison lemma

For any four Hilbert--Schmidt operators `B,C,B0,C0`,

\[
\begin{aligned}
|\langle B,C\rangle
-
\langle B_0,C_0\rangle|
&\le
\|B-B_0\|_2\|C\|_2\\
&\quad+
\|B_0\|_2\|C-C_0\|_2.
\end{aligned}
\]

Equivalently, using `C=C-C0+C0`,

\[
\boxed{
\begin{aligned}
|\langle B,C\rangle
-
\langle B_0,C_0\rangle|
&\le
\|B-B_0\|_2
(\|C-C_0\|_2+
\|C_0\|_2)\\
&\quad+
\|B_0\|_2
\|C-C_0\|_2.
\end{aligned}
}
\]

Therefore convergence of both legs in Hilbert--Schmidt norm implies convergence of the sewing pairing.

## Corrected positive estimates

The raw annular leg has norm growing like the square root of annular volume, so it cannot converge in Hilbert--Schmidt norm. The following estimates apply only after cutoff-dependent orthogonal bulk removal and endpoint recentering. Writing these corrected legs as `tilde B_(alpha,chi)` and `tilde C_(alpha,chi)`, it suffices to prove

\[
\boxed{
\|\widetilde B_{\alpha,\chi}(g)
-
B_{\chi}^{rel}(g)
\|_{HS}
\longrightarrow0,
}
\]

\[
\boxed{
\|\widetilde C_{\alpha,\chi}(g)
-
C_{\chi}^{rel}(g)
\|_{HS}
\longrightarrow0,
}
\]

and an angular majorant

\[
\boxed{
\|B_{\alpha,\chi}(g)
\|_{HS}
+
\|C_{\alpha,\chi}(g)
\|_{HS}
\le
M_g(\chi),

\sum_\chi
M_g(\chi)^2
<\infty.
}
\]

The convergence is along the ordered or correlated regulator limit chosen for the construction.

## Angular dominated convergence

The Cauchy bound gives

\[
|\mathcal E_{\alpha,\chi}(g)|
\le
M_g(\chi)^2.
\]

If the three estimates hold, dominated convergence yields

\[
\boxed{
\lim_\alpha
\sum_\chi
\mathcal E_{\alpha,\chi}(g)
=
\sum_\chi
\mathcal E_\chi^{rel}(g).
}
\]

Hence the finite regulated semilocal sewing converges to the sum of relative Tate--Hardy traces.

## Uniform bounded-packet version

For functoriality, let `G` be a bounded packet of smooth observers. Require a common summable majorant

\[
M_G(\chi)
=
\sup_{g\in G}
M_g(\chi),
\qquad
\sum_\chi
M_G(\chi)^2
<\infty,
\]

and leg convergence uniform over `g in G`. Then the regulator comparison is a continuous modification on the observer test category rather than merely a pointwise scalar limit.

## Decomposition of each leg error

Each difference can be split into typed analytic errors:

\[
B_{\alpha,\chi}-B_\chi^{rel}
=
E_{outer}
+E_{angular}
+E_{hardy}
+E_{phase}
+E_{observer}.
\]

### Outer-cutoff error

`E_outer` is the tail beyond the finite annulus `R`. Compact radial propagation gives exact stabilization in the elementary translation model; semilocally it should be rapidly small by the same Schwartz tail mechanism as Connes's Lemma 2.

### Angular-cutoff error

`E_angular` is `(I-K_N)` applied to smooth angular observer blocks. Peter--Weyl decay makes it rapidly small in `N`.

### Hardy recentering error

`E_hardy` compares the finite physical cutoff, after boundary translation, with the limiting Hardy projection. In the logarithmic coordinate this is exact for an ideal half-line and is a boundary-chart error for the quotient carrier.

### Tate-phase error

`E_phase` compares the transported additive Fourier operator with

\[
M_{\gamma_\chi}R.
\]

The Tate local functional equation should make this exact once all Radon--Nikodym and basic-character normalizations are fixed.

### Observer-order error

`E_observer` consists of the explicit Hardy commutators

\[
[\Pi,M_{m_{g,\chi}}].
\]

These are Hilbert--Schmidt and rapidly decreasing in `chi`.

## What is already available

The current construction supplies:

- exact characterwise ordering of `P`, `Q`, and `M_m`;
- polynomial Tate-phase derivative control;
- logarithmic localized Hardy-commutator estimates;
- rapid angular decay for smooth observers;
- exact finite-regulator Gram typing.

These give plausible summable majorants after the linear bulk contribution is separated.

## What is not supplied by Connes's scalar remainder

Connes's `O(Lambda^(-N))` scalar remainder controls the **combined trace** after orbit summation. It does not imply Hilbert--Schmidt convergence of each Gram leg.

Thus it cannot replace the two leg estimates above. Cancellation in a scalar trace can occur even when neither feature converges.

## Weaker trace-class variant

If separate Hilbert--Schmidt limits are unavailable, it suffices to factor

\[
B_{\alpha,\chi}^*C_{\alpha,\chi}
-
(B_\chi^{rel})^*C_\chi^{rel}
\]

in trace norm and prove

\[
\boxed{
\left\|
B_{\alpha,\chi}^*C_{\alpha,\chi}
-
(B_\chi^{rel})^*C_\chi^{rel}
\right\|_1
\longrightarrow0.
}
\]

This is weaker and may preserve cancellations essential to the product cutoff. It still requires a summable angular trace-norm majorant.

Given the known failure of the unregulated outside Hilbert--Schmidt leg, this trace-class product route may be the correct final topology when `R -> infinity`.

## Regulator order

A safe iterated limit is

\[
\boxed{
N\to\infty,
\qquad
R\to\infty,
\qquad
\Lambda\to\infty,
}
\]

after forming each finite `(Lambda,R,N)` product. A correlated limit is admitted only if the same majorant is uniform in all regulator ratios.

The outer-cutoff limit should be taken at the product level if the individual outside leg loses Hilbert--Schmidt class.

## Acceptance criterion for `C_34`

The regulator comparison is complete if either:

### Strong feature criterion

Both orthogonally bulk-removed, recentered Gram legs converge in Hilbert--Schmidt norm with a summable angular majorant.

### Minimal product criterion

Their product converges in trace norm with a summable angular majorant.

In either case,

\[
\boxed{
\lim
\mathcal E_{\Lambda,R,N,S}(g)
=
\sum_\chi
\left[
\frac1{2\pi i}
\int
|m_{g,\chi}|^2d\log\gamma_\chi
+
e_{end,\chi}(g)
\right].
}
\]

## Positivity distinction

The minimal product criterion identifies the signed sewing trace but may not produce a positive boundary feature. Positive rung four requires the strong feature criterion or another positive correspondence retaining the complete Gram matrix.

Thus:

- trace-norm product convergence completes signed `C_34`;
- Hilbert--Schmidt leg convergence is the stronger positive-feature gate.

## Disposition

The remaining regulator theorem has been reduced to explicit norm convergence:

\[
\boxed{
\widetilde B_{\alpha,\chi}\to B_\chi^{rel},
\qquad
\widetilde C_{\alpha,\chi}\to C_\chi^{rel}
\quad\text{in }\mathcal L^2,
}
\]

with one square-summable angular majorant, or alternatively convergence of their product in `L1`.

No further categorical ambiguity remains. The unresolved content is analytic trace-ideal convergence of the outer-cutoff and boundary-recentering errors.
