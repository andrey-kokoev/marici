# The semilocal prolate transition bound reduces to a geometrically summable family of local orbit estimates

## Target

Let

\[
P=P_{\Lambda,S},
\qquad
Q=F_SP F_S^{-1},
\qquad
B=PQP
\]

on `L2(X_S)`. The positive sewing estimate requires

\[
\boxed{
\operatorname{Tr}_{X_S}(B-B^2)
=O_S(\log\Lambda).
}
\]

Equivalently,

\[
\operatorname{Tr}_{X_S}(B-B^2)
=
\|P Q(I-P)\|_{HS,X_S}^2.
\]

## Quotient trace decomposition

For an `O_S*`-equivariant operator `T` with kernel `K_T` on the additive semilocal cover, Connes's quotient trace rule is

\[
\operatorname{Tr}_{X_S}(T)
=
\sum_{q\in O_S^*}
\int_D
K_T(x,qx)dx,
\]

where `D` is a fundamental domain on the conull idele locus.

Apply this to the positive transition operator

\[
T_{\Lambda,S}
=P Q(I-P)Q P
=B-B^2.
\]

Define its orbit contributions

\[
\boxed{
I_{q,\Lambda,S}
=
\int_D
K_{T_{\Lambda,S}}(x,qx)dx.
}
\]

Then, whenever absolute convergence is justified,

\[
\boxed{
\operatorname{Tr}_{X_S}(B-B^2)
=
\sum_{q\in O_S^*}
I_{q,\Lambda,S}.
}
\]

The total is nonnegative, although individual orbit terms need not be.

## Source geometric decay

Connes's Section VII, Lemma 1 uses the logarithmic embedding

\[
L:O_S^*
\to
\left\{
(y_v)_{v\in S}:
\sum_vy_v=0
\right\},
\qquad
L(q)_v
=
\log|q_v|_v.
\]

Its image is a lattice and its kernel is finite. For a suitable word metric `d`, one obtains exponential control of the form

\[
\sup_{v\in S}|q_v|_v
\ge
\exp(c_Sd(q,1)).
\]

Matrix coefficients of semilocal Schwartz vectors then decay geometrically in `q`. This proves absolute convergence of the orbit sums used to define `L2(X_S)` and the trace formula.

The same lattice mechanism can control the prolate transition kernel once its nonsmooth cutoff boundary is isolated.

## Required per-orbit estimate

It is sufficient to prove constants `C_S>0`, `delta_S>0`, and a finite cutoff-independent seminorm packet such that

\[
\boxed{
|I_{q,\Lambda,S}|
\le
C_S
(1+\log\Lambda)
\exp(-\delta_Sd(q,1))
}
\]

for every `q in O_S*` and `Lambda>=2`.

Indeed, finite generation gives

\[
\sum_{q\in O_S^*}
\exp(-\delta_Sd(q,1))
<\infty
\]

when the decay exponent dominates the growth rate. Therefore

\[
\boxed{
\sum_q
|I_{q,\Lambda,S}|
=O_S(\log\Lambda),
}
\]

which proves the target transition bound.

If the first available exponent is too small relative to group growth, Connes's Schwartz estimates permit increasing the decay order until summability holds.

## Identity orbit

For `q=1`, the orbit term is the direct semilocal analogue of the local boundary-crossing integral. The Fourier kernel of `Q` and the module cutoff produce a transition layer around

\[
|x|_S=\Lambda.
\]

The expected estimate is

\[
\boxed{
I_{1,\Lambda,S}
=O_S(\log\Lambda).
}
\]

At the real place this is the sinc-kernel calculation

\[
\frac{2}{\pi^2}
\log\Lambda+O(1).
\]

Finite places contribute valuation-shell transition terms. Since the global cutoff is by total module, these pieces remain coupled inside the identity-orbit integral.

## Nonidentity orbits

For `q 
e 1`, the point pair `(x,qx)` is separated in at least one local logarithmic coordinate by an amount controlled by `d(q,1)`. The Fourier kernels are Schwartz away from their singular transition diagonal after smooth cutoff approximation.

The required strategy is:

1. replace the sharp cutoff by upper and lower smooth module cutoffs differing only in a fixed boundary strip;
2. apply Connes's Lemma-1 matrix-coefficient estimate to the smooth transition kernels;
3. control the sharp-minus-smooth boundary strip by the identity-orbit transition norm;
4. increase the Schwartz decay order to obtain geometric summability in `q`.

This yields the stated per-orbit estimate if the constants are uniform in `Lambda` after extracting the one logarithmic transition factor.

## Sharp-cutoff difficulty

Connes's Lemma 1 is stated for Schwartz vectors on `A_S`. The projections `P` and `Q` use characteristic functions, so their kernels are not Schwartz uniformly at the moving boundary.

Therefore geometric summability cannot be cited without a smoothing argument. The exact missing estimate is the uniform bound

\[
\boxed{
\sup_{\Lambda\ge2}
\frac{
e^{\delta_Sd(q,1)}
|I_{q,\Lambda,S}|
}{
1+\log\Lambda
}
\le
C_S.
}
\]

Proving this inequality is the remaining analytic core.

## Smooth sandwich

Choose smooth functions `chi_minus, chi_plus` with

\[
0\le\chi_-\le1_{(-\infty,0]}\le\chi_+\le1
\]

and with `chi_plus-chi_minus` supported in a fixed-width interval. Set

\[
P_{\Lambda}^\pm
=
\chi_\pm
(\log|x|_S-\log\Lambda).
\]

Then

\[
P_\Lambda^-
\le
P_\Lambda
\le
P_\Lambda^+,
\]

and the difference is confined to one module boundary strip. The smooth kernels admit repeated integration by parts/Fourier decay, while the strip has logarithmically controlled transition mass.

This is the appropriate bridge between the local sinc computation and Connes's geometric `S`-unit estimates.

## Consequence if the estimate holds

The observer commutator norm is already cutoff-independent:

\[
\|[P_\Lambda,U_S(h)]\|_{HS}^2
=
\int_{C_S}
|h(a)|^2
|\log|a|_S|d^*a.
\]

Hence the sewing term obeys

\[
|\mathcal E_{\Lambda,S}(g)|
\le
O_S(\sqrt{\log\Lambda})
\|[P_\Lambda,U_S(h)]\|_{HS},
\]

and therefore

\[
\mathcal E_{\Lambda,S}(g)
=o_g(\log\Lambda).
\]

This would prove that the positive triple compression has the same leading `2 log Lambda h(1)` density as Connes's trace.

## What is proved here

This packet proves the logical reduction:

\[
\boxed{
\text{uniform geometric per-orbit estimate}
\Longrightarrow
\text{semilocal }O(\log\Lambda)
\text{ transition trace}.
}
\]

It also identifies the exact source mechanism for summing the orbit estimates: the `S`-unit lattice decay in Connes's Lemma 1.

It does not yet prove the uniform sharp-cutoff per-orbit inequality.

## Disposition

The semilocal transition problem is no longer an undifferentiated spectral estimate. It is the single uniform bound

\[
\boxed{
|I_{q,\Lambda,S}|
\le
C_S
(1+\log\Lambda)
e^{-\delta_Sd(q,1)}.
}
\]

The identity orbit is the local prolate transition calculation; all other orbits should be geometrically summable by the same `S`-unit lattice mechanism used in Connes's proof. The next executable analytic step is a smooth-cutoff estimate uniform in `Lambda` and `q`.
