# The polynomial identity map from moment L2 to Hardy H2 is unbounded

## Question

Can zero-side Hardy boundedness be transferred to the positive archimedean moment completion by the identity map on polynomials?

## Claim boundary

No. For every finite positive measure on `[0,1]`, the identity polynomial map from its `L2` completion to coefficient Hardy `H2` is unbounded. Any useful comparison must be a nontrivial source-derived transform, not the shared polynomial coordinates themselves.

## Hostile polynomial

Let `mu` be a finite positive measure on `[0,1]` and set

\[
p_m(z)=(1-z)^m.
\]

Because `|1-z|<=1` on `[0,1]`,

\[
\|p_m\|_{L^2(\mu)}^2
=\int_0^1(1-z)^{2m}\,d\mu(z)
\le \mu([0,1]).
\]

In coefficient Hardy space,

\[
p_m(z)=\sum_{j=0}^m(-1)^j\binom mj z^j,
\]

so

\[
\|p_m\|_{H^2(\mathbb D)}^2
=\sum_{j=0}^m\binom mj^2
=\binom{2m}{m}
\sim\frac{4^m}{\sqrt{\pi m}}.
\]

Thus no constant `C` can satisfy

\[
\|p\|_{H^2}\le C\|p\|_{L^2(\mu)}
\]

for all polynomials.

## Application to the common-measure programme

The positive leading archimedean GNS space is an `L2` moment space over a finite measure in the Bernstein coordinate. The zero-side paired form is bounded on Hardy space because evaluation inside the disk is continuous there. The identity on polynomial coefficients cannot connect these two completions.

This obstruction is independent of the detailed archimedean density and already uses the same near-null family that exposed Hankel conditioning.

## What remains possible

A comparison map may still exist if it changes coordinates or smooths coefficients. It must specify:

1. a source-derived transform `J` from the archimedean form core into Hardy space;
2. its action on the prime–theta generators;
3. continuity in the archimedean norm;
4. an intertwining identity recovering the required quadratic form.

A diagonal coefficient damping would make Hardy inclusion possible, but choosing damping from zero locations or from the target Gram matrix would be circular.

## Strongest falsification attempt

Unboundedness of the identity map does not rule out every nontrivial transform. It rules out the simplest topology comparison and shows why polynomial-level equality of finite matrices does not extend automatically to the completions.

## Disposition

Reject identity inclusion from the moment GNS space to `H2(D)`. Reopen the Hardy route only with an independently defined smoothing or intertwining map from arithmetic source data.