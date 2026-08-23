# Directed box certificate for the hostile theta adjacent block

## Result

For the outer-quadrant parameter

\[
(a,b)=(1,11)
\]

and the source exchange orbit of labels

\[
\mathcal O_{12}=\{(1,2),(2,1)\},
\]

the cusp-free three-chart enclosure gives

\[
B_{\mathcal O_{12}}(1,11)
\in
[-3.777844703347796\!\times\!10^{-5},
 -2.272768028044715\!\times\!10^{-6}].
\]

In particular, its upper endpoint is strictly negative.  This finitely
falsifies the proposed universal claim that every source-labelled canonical
adjacent two-band block is nonnegative.

This is a falsifier for that *mechanism*.  It is not a falsifier for the Pick
inequality, the zero-free conclusion, or RH.

## Exact source-reflection reduction

For fixed \(d\geq0\) and \(x\geq0\), charts A and B have

\[
s=2x+d,
\]

and the exchanged-label density product is identical on the two charts.
Writing that positive orbit density as \(P(x,d)\), their sum is evaluated
before intervalization as

\[
P(x,d)\left[
 \beta s\cos(bd)(e^s-e^{-s})
 +\alpha d\sin(bd)(e^s+e^{-s})
\right].
\]

This identity is forced by the source reflection; it is not an
answer-dependent regrouping.  It removes the dominant interval dependency
that appears if charts A and B are enclosed independently.

Chart C is retained separately with \(x=dq\), \(0\leq q\leq1\), including its
Jacobian factor \(d\).  Both source labels are summed inside every box.  Four
fixed half-bands of width \(\pi/(2b)\) cover the adjacent block
\([0,2\pi/b]\).

The band enclosures after summing the reflection-paired AB chart and chart C
are

\[
\begin{aligned}
I_0&=[9.293563212270072\!\times\!10^{-6},
      1.718765825601841\!\times\!10^{-5}],\\
I_1&=[-1.8371938877527384\!\times\!10^{-5},
      -7.080361034682991\!\times\!10^{-6}],\\
I_2&=[-3.267480091136121\!\times\!10^{-5},
      -2.0369446353083266\!\times\!10^{-5}],\\
I_3&=[3.974729543140588\!\times\!10^{-6},
      7.989381103703126\!\times\!10^{-6}].
\end{aligned}
\]

Their directed sum remains strictly negative.

## Certification status

The checker uses outward `nextafter` rounding for binary64 arithmetic and a
deliberately loose \(10^{-100}\) allowance for the two infinite chart tails
past \(x=3\).  The computation is reproducible and the negative separation is
large relative to zero.

It is nevertheless labelled **not fully formal**.  A proof-grade certificate
still requires:

1. replacing the assumed correct rounding of `exp`, `sin`, and `cos` by a
   certified transcendental implementation;
2. enclosing the exact \(\pi\)-defined partition endpoints rather than relying
   on the host `math.pi` value; and
3. writing and checking the explicit analytic estimate that bounds both
   \(x\geq3\) tails by \(10^{-100}\).

Until those three closures are supplied, the appropriate claim is a strict
directed-binary64 enclosure under stated assumptions, not a formal interval
proof.

## Program consequence

The strongest surviving statement is negative and explanatory:

> Source exchange covariance and canonical adjacent bands do not by
> themselves impose blockwise variation diminution on the theta two-copy
> kernel.

Any successful global positivity argument must therefore use a larger
canonical block, cancellation across different source-label orbits, or a
different source-derived order.  Accumulating more finite disks does not repair
this failed local mechanism.

## Larger-block diagnostic

The first prescribed escape route was tested without changing the label orbit
or choosing new boundaries.  At \((a,b)=(1,11)\), direct converged quadrature
of the cumulative intervals \([0,k\pi/b]\) gives

\[
\begin{array}{c|rrrrrr}
k&1&2&3&4&5&6\\ \hline
10^5 B_k&0.04720&-1.96314&-1.61689&-1.61902&-1.61902&-1.61902.
\end{array}
\]

The values through \(k=10\) remain at approximately
\(-1.61902454011204\times10^{-5}\).  This scan is diagnostic rather than
interval-certified, but it sharply disfavors the explanation that only the
first adjacent boundary was chosen too narrowly.  The natural next conjecture
must allow cancellation **between distinct source-label orbits**; positivity
orbit by orbit is not supported.

Artifacts:

- `checkers/theta_adjacent_block_directed_box_certificate.py`
- `results/theta-adjacent-block-directed-box-certificate.json`
- `checkers/theta_adjacent_block_parameter_scan.py`
- `results/theta-adjacent-block-parameter-scan.json`
