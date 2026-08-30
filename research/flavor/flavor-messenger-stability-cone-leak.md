# Messenger stability-cone leak: WP665

## Question

Does WP664's positive tangent at the repaired benchmark imply an
RG-preserved radial-stability chamber for the disjoint messenger completion?

## Exact boundary test

Restrict to the symmetric submanifold

\[
\lambda_n=\lambda_m=\lambda>0,
\qquad F=F_n+F_m.
\]

The radial stability margin is

\[
D=4\lambda^2-\lambda_x^2.
\]

Combining the complete scalar flow with the disjoint Dirac supertrace and
evaluating on the positive boundary \(\lambda_x=2\lambda\) gives

\[
\left.\frac{dD}{dt}\right|_{D=0,\,\lambda_x=2\lambda}
=-32F\lambda.
\]

For every \(F>0\), the vector field points out of the stable cone. In the
pure-scalar limit it is tangent. The smallest hostile witness is
\(F=\lambda=1\), where the boundary derivative is \(-32\).

## Consequence

WP664's inequality is a local nonerosion test at the WP661 benchmark, not an
all-scale invariant-chamber theorem. Any positive fixed disjoint-messenger
strength makes the full radial cone noninvariant. This does not prove that the
benchmark trajectory crosses the boundary before a physical threshold; it
proves that such survival cannot be inferred from cone geometry alone.

The next admissible test must derive Yukawa running and threshold decoupling,
then study a smaller domain over a declared finite scale interval. No selector
authority follows.

Reproduce with: uv run --with sympy python research/flavor/checkers/wp665_messenger_stability_cone_leak.py

Generated result: results/wp665_messenger_stability_cone_leak.json.
