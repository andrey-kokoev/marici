# Endpoint domination of the gamma intersection core

## Question

Does separate coherent-state density in the endpoint and gamma sectors leave a genuine intersection-density obstruction?

## Claim boundary

The obstruction collapses if both sectors use one transported coordinate in which endpoint control has exponential weight and gamma has logarithmic graph growth. That common-coordinate identification and the completed prime-row bound remain open.

## Weight comparison

Let

\[
H_\beta=L^2(\mathbb R,e^{\beta|x|}dx),
\qquad \beta>0,
\]

and let the gamma graph weight be bounded by

\[
w_\Gamma(x)=1+\log^2(2+|x|).
\]

For \(y\geq0\),

\[
\log(2+y)
\leq
\log2+\frac y2.
\]

Using

\[
y^2e^{-\beta y}
\leq
\frac{4}{e^2\beta^2},
\]

we obtain

\[
1+\log^2(2+y)
\leq
C_\beta e^{\beta y},
\]

where

\[
C_\beta=
1+2\log^2 2+rac{2}{e^2\beta^2}.
\]

Therefore

\[
\|f\|_{\Gamma}^2
\leq
C_\beta\|f\|_{H_\beta}^2.
\]

## Collapse of the pullback domain

If endpoint and gamma terms inhabit the same transported \(L^2\) coordinate, then

\[
H_\beta\hookrightarrow D(M_\Gamma)

\]

continuously. Consequently,

\[
H_\beta\cap D(M_\Gamma)=H_\beta
\]

as sets, with equivalent intersection and endpoint norms.

Thus separate density does not need to be combined abstractly. Endpoint exponential control already dominates gamma logarithmic control. Coherent-state density in \(H_\beta\) implies density in the endpoint--gamma intersection graph norm.

Categorically, the pullback

\[
H_\beta\times_{L^2}D(M_\Gamma)
\]

is equivalent to its stronger endpoint leg \(H_\beta\). The apparent extra intersection object introduces no new completion constraint.

## Exact conditionality

This reduction applies only if:

1. both transported sectors use the same variable and measure;
2. the actual gamma multiplier obeys the logarithmic bound in that coordinate;
3. endpoint control is genuinely represented by the exponential weight;
4. domain identifications preserve the completed explicit formula.

Separate unitary descriptions do not establish these compatibility cells.

## Prime-row consequence

After endpoint domination absorbs the gamma graph norm, the remaining topology question is whether the completed labelled-prime row is bounded on \(H_\beta\), or at least relatively bounded with respect to its norm.

If its row norm is controlled by a convergent sum of fixed-width weights, then adjoining it preserves the endpoint core. If not, its graph contribution defines a stronger intersection and the density theorem must be repeated there.

## Updated proof bracket

The topology lane is now:

\[
\text{common Segal--Bargmann coordinate}
\Longrightarrow
H_\beta\hookrightarrow D(M_\Gamma)
\Longrightarrow
\text{endpoint--gamma common core}
\Longrightarrow
\text{add prime row if bounded}.
\]

The first and last arrows remain source-verification gates. The middle arrow follows from the explicit weight domination.

## Disposition

The previously reported simultaneous-density obstruction is not intrinsic. It disappears under a common transport because exponential endpoint control dominates logarithmic gamma growth. The first missing typed object is now the common transported coordinate/measure identification; the next is a completed prime-row norm bound in \(H_\beta\). Positivity remains separate.

## Verification

- `research/voevodsky/endpoint-dominates-gamma-intersection-core-v1.json`
- `research/voevodsky/checkers/check_endpoint_dominates_gamma_intersection_core.py`
- `research/voevodsky/results/endpoint_dominates_gamma_intersection_core.json`
