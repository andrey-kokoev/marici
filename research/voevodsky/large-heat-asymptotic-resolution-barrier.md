# Large-heat asymptotic resolution barrier

## Question

Can ordinary PNT or algebraically decaying error estimates certify the rank-two cone uniformly when its positive margin collapses at the least-zero spectral scale?

## Claim boundary

A general asymptotic no-go is proved. The asserted leading endpoint--least-zero expansion remains conditional on the exact source decomposition.

## Conditional margin scale

The Cauchy--Binet ordering predicts that the leading large-heat pair consists of the endpoint feature and the least zero rate. Thus

\[
D_2(t,h)
\sim
C(h)e^{-\alpha t},
\qquad
\alpha=\gamma_1^2-\frac14,
\qquad C(h)>0.
\]

Zero--zero pairs decay at faster combined rates.

## Algebraic-error no-go

For every \(m>0\),

\[
\frac{t^{-m}}{e^{-\alpha t}}
=
\frac{e^{\alpha t}}{t^m}
\longrightarrow\infty.
\]

Therefore an error estimate of order \(t^{-m}\), however high the fixed order, eventually exceeds the target margin.

A fixed absolute error has the same defect.

## Slower exponential no-go

If an error satisfies only

\[
E(t)\leq C_0e^{-\beta t}
\]

with \(\beta<\alpha\), then

\[
\frac{E(t)}{e^{-\alpha t}}
\lesssim
C_0e^{(\alpha-\beta)t},
\]

and the available bound again becomes larger than the margin.

To certify by direct comparison, the error exponent must satisfy

\[
\beta\geq\alpha.
\]

At equality, coefficient control is essential.

## Surviving asymptotic routes

A global large-heat proof requires one of:

1. exact symbolic cancellation that exposes the leading positive endpoint--least-zero pair;
2. a remainder bound decaying strictly faster than \(e^{-\alpha t}\);
3. renormalization
   \[
   e^{\alpha t}D_2(t,h)
   \]
   with a certified positive limit and a vanishing remainder at the same scale;
4. an exact positive identity avoiding subtraction of separately large source sectors.

Ordinary PNT control does not reach the necessary spectral exponent merely by increasing algebraic order.

## Relation to finite certification

Validated quadrature can certify bounded \(t\)-boxes. It cannot be extrapolated to all large \(t\) with a fixed absolute tolerance because the target margin tends to zero exponentially.

Thus local interval certification and global asymptotic proof are different objects:

- finite boxes require absolute enclosures;
- the tail region requires relative or renormalized spectral-scale control.

Neither substitutes for the other.

## Source risk

The leading asymptotic currently uses the conditional ordering of endpoint and zero-side rates. A source proof must derive:

- the exact coefficient \(C(h)\);
- its sign;
- the least relevant rate;
- absence of cancellation at that rate;
- a strictly faster remainder.

Invoking the positive zero measure to obtain these would be circular.

## Disposition

Global rank-two positivity cannot be proved by ordinary algebraic source errors layered over finite-box numerics. The large-heat branch must be renormalized at the least-zero spectral scale or closed by an exact completed identity. This is a stopping condition for PNT-only extrapolation.

## Verification

- `research/voevodsky/large-heat-asymptotic-resolution-barrier-v1.json`
- `research/voevodsky/checkers/check_large_heat_asymptotic_resolution_barrier.py`
- `research/voevodsky/results/large_heat_asymptotic_resolution_barrier.json`
