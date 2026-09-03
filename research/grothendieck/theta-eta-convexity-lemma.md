# Eta nonnegativity lemma

Fix `q>0` and put

- `A=2*pi/q>3`,
- `h(y)=cosh(sqrt(q*y))-1`,
- `K=6*A/(A-3)^2`, and
- `m(y)=A*h(y)-log(1-K*h(y))`.

Assume `0<=K*h(4y)<1`. Then

`eta(y)=m(4y)-4*m(y) >= 0`.

## Proof

The entire power series

`h(y)=sum_{n>=1} q^n*y^n/(2n)!`

has nonnegative coefficients. Hence on the nonnegative real axis `h(0)=0`,
`h` is nonnegative and nondecreasing, and `h''>=0`; thus `h` is convex.
Multiplication by `A>0` preserves convexity.

On `[0,1)`, `phi(t)=-log(1-t)` satisfies `phi'(t)=1/(1-t)>0` and
`phi''(t)=1/(1-t)^2>0`. Therefore `phi` is nondecreasing and convex. Since
`K>0`, `K*h` is convex, and the standard composition rule shows
`phi(K*h(y))` is convex wherever `K*h(y)<1`. Consequently `m` is convex and
`m(0)=0`.

By convexity,

`m(y)=m((1/4)*(4y)+(3/4)*0) <= (1/4)*m(4y)+(3/4)*m(0)=m(4y)/4`.

Multiplying by four gives `m(4y)-4*m(y)>=0`.

## Checker connection

`theta_dominant_fraction_interval_core.py` verifies the domain bounds needed by
its elementary series routines (`q*(4y)<=1/16` and the logarithmic correction
at most `1/25`). Its cancellation-free evaluator may therefore intersect the
computed value enclosure of `eta` with `[0,+infinity)` without altering the
independently propagated derivative enclosures. The corner checker
`theta_dominant_corner_exact.py` uses precisely this evaluator.
