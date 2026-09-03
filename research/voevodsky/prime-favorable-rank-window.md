# Prime-favorable rank window

## Question

How far in rank does the Laguerre sign theorem make every prime atom favorable along the near-null observer at small heat?

## Claim boundary

For fixed scaled mesh \(h=\kappa t\), the termwise prime contribution is nonnegative for polynomial degree up to an explicit order \(t^{-1/2}\). This concerns only the near-null family \((1-y)^m\), not arbitrary polynomials or full Hankel positivity.

## Sufficient Laguerre condition

Let

\[
q=2m+1
\]

be the high-difference order. Every point in the difference cube has

\[
U\leq t+qh.
\]

The smallest prime has

\[
a_2=\frac{(\log2)^2}{4}.
\]

A classical upper bound for the largest root of \(L_q^{-1/2}\) is

\[
x_{q,\max}<4q+2.
\]

Therefore every prime atom remains above the Laguerre turning region if

\[
\frac{(\log2)^2}{4(t+qh)}>4q+2.
\]

For odd \(q\), this makes the Laguerre polynomial negative throughout every prime difference cube. The completed prime prefactor is also negative, so every prime contributes nonnegatively.

## Scaled mesh

Put

\[
h=\kappa t.
\]

The sufficient condition becomes

\[
(
\log2)^2
>
4(4q+2)t(1+q\kappa).
\]

Equivalently,

\[
16t\kappa q^2
+t(16+8\kappa)q
+8t-(\log2)^2
<0.
\]

Let \(q_*(t,\kappa)\) be the positive root of the corresponding quadratic. Then every odd integer

\[
q<q_*(t,\kappa)
\]

lies in the favorable window.

As \(t\to0^+\) with fixed \(\kappa>0\),

\[
\sqrt t\,q_*(t,\kappa)
\longrightarrow
\frac{\log2}{4\sqrt\kappa}.
\]

Since \(q=2m+1\), the polynomial-degree window is

\[
m
<
\frac{\log2}{8\sqrt{\kappa t}}
+O(1).
\]

## Coherence interpretation

The near-null polynomial observer, high-difference observer, and prime-translation observer agree on this region with zero algebraic residue. Their quantitative coherencer has positive sign up to rank of order \(t^{-1/2}\).

The uncontrolled region begins beyond that scale, where some prime atoms enter Laguerre turning intervals. Thus the earlier candidate obstruction near \(m\asymp1/t\) is separated from the first proven rank window by a substantial intermediate regime.

## Limitation

This theorem does not control:

- arbitrary polynomial directions;
- gamma corrections uniformly at growing rank;
- the Laguerre turning region;
- ranks between order \(t^{-1/2}\) and order \(t^{-1}\);
- the full prime sum once individual atoms have mixed signs.

## Disposition

The prime sector is not an obstruction along the explicit near-null family through degree order \(t^{-1/2}\); it helps positivity there. The next unresolved range begins when

\[
q\sqrt t
\]

is no longer small. The correct next calculation is a Plancherel--Rotach turning-point estimate for the weighted prime sum, not a coefficientwise norm bound.

## Verification

- `research/voevodsky/checkers/check_prime_favorable_rank_window.py`
- `research/voevodsky/results/prime_favorable_rank_window.json`
