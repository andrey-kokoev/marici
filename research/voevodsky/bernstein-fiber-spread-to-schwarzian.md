# Bernstein fiber spread implies Schwarzian positivity

## Question

Why does the conditional spread bound on convolution fibers imply rank-two Loewner positivity?

## Claim boundary

This proves the reduction. It does not construct the Bernstein measure or prove the spread bound for the theta source.

## Tilted curvature

Let \(f=H'\) be represented by a positive Bernstein measure and let \(P_x\) be its exponential tilt. Write

\[
m=\mathbb E_x[T],
\qquad
\sigma^2=\operatorname{Var}_x(T).
\]

The Laplace identities give

\[
\frac{f'}f=-m,
\qquad
\frac{f''}f=\sigma^2+m^2.
\]

For \(p=f^{-1/2}\), direct differentiation yields

\[
\frac{p''}{p}=\frac{m^2-2\sigma^2}{4}.
\]

Thus concavity of \(p\), equivalently rank-two Loewner positivity and nonnegative Schwarzian of \(H\), is exactly

\[
\sigma^2\geq\frac{m^2}{2}.
\]

## Convolution-fiber reduction

Let \(T,U\) be independent with law \(P_x\), and set \(V=T+U\). Symmetry gives

\[
\mathbb E[T\mid V]=\frac V2.
\]

Assume

\[
\operatorname{Var}(T\mid V=v)\geq\frac{v^2}{20}.
\]

The total-variance identity then gives

\[
\sigma^2
\geq
\frac{
2\sigma^2+4m^2
}{20}
+
\frac{2\sigma^2}{4}.
\]

Rearrangement yields \(\sigma^2\geq m^2/2\), exactly the Schwarzian condition.

A collapsed point-mass fiber has \(\sigma^2=0<m^2/2\) and produces positive \(p''/p\); the checker retains this deliberate failure.

## Disposition

The constant \(1/20\) is sufficient because conditional spread plus the variance of the faithful sum coordinate supplies the exact missing curvature. The remaining source obligations are to derive the Bernstein measure from completed arithmetic data and prove this fiber inequality for almost every sum fiber under every required tilt. Rank two alone does not establish all-rank Herglotz positivity or RH.

## Verification

- `research/voevodsky/bernstein-fiber-spread-to-schwarzian-v1.json`
- `research/voevodsky/checkers/check_bernstein_fiber_spread_to_schwarzian.py`
- `research/voevodsky/results/bernstein_fiber_spread_to_schwarzian.json`
