# Chart-1 dominant residual derivative DPC

## Problem

Certify, by exact outward enclosures on
`q in [3/10,7/16]`, `y in [1/1000,1/28]`, the signs required for the dominant
residual. This packet currently addresses only the `Nq=y^2 Dq` gate. It makes
no claim about the separate `Ny=y^3 Dy` gate.

## Bold conjecture

`Nq` is coordinatewise nondecreasing on Chart 1:

- `partial_q Nq >= 0`, and
- `partial_y Nq >= 0`.

Together with an exact positive lower-corner enclosure for
`Nq(3/10,1/1000)`, this would prove `Nq>0` throughout Chart 1 without a deep
two-dimensional residual cover.

## Named rivals

1. **Direct fixedpoint cover:** exact outward subdivision of the final
   residual or its two partial derivatives.
2. **Local-dependency propagation:** affine or Hessian transport through the
   cancellation-free variables `m` and `eta`.
3. **Analytic series:** a Taylor polynomial in `y` plus a uniform Cauchy
   remainder bound.
4. **Source-derived finite grid:** admissible only if its geometry and
   between-point control are recovered from an authoritative source.

A coefficientwise-positive Taylor series is a falsification target inside
rival 3, not a separate theorem.

## Risky consequences

The bold conjecture requires continuum—not sampled—lower bounds for both
partials. For the analytic-series rival this requires all of the following:

1. exact parameter-uniform coefficient enclosures, including the exact value
   `2*pi`, rather than evaluations only at rational bracket endpoints;
2. treatment of both `partial_q Nq` and `partial_y Nq`;
3. a uniform bound on the omitted Taylor tail for every Chart-1 `q`; and
4. a positive exact lower-corner enclosure for `Nq`.

Failure of any item prevents certification. Positivity of finitely many
truncations, small observed coefficient ratios, or positivity at finitely many
parameter points is not a substitute.

## Strongest falsification attempt and residual

The strongest completed attack on the direct-cover rival is an exact outward
adaptive run capped at 5,000 box evaluations. It accepted 2,495 boxes and left
11 DFS boxes pending at depth 18. Because its disjoint residual geometry was
not persisted, it is diagnostic only and is not accepted as cover evidence.
The earlier breadth-first run likewise left normalized unresolved area
`198287/262144` at depth 18. These runs reject natural subdivision as a
practical backend, not the derivative signs.

The strongest completed attack on the analytic rival is the dependency-free
exact rational formal-series checker
`research/grothendieck/checkers/theta_nq_fraction_series.py`, with durable
output `research/grothendieck/results/theta-nq-fraction-series.json`. At four rational
`(p,q)` endpoint cases, where `p` brackets `2*pi`, coefficients of the
degree-18 `partial_y Nq` polynomial have mixed signs. Therefore the proposed
**endpoint-uniform coefficientwise-positive certificate** is rejected. This
does not determine coefficient signs at exact `2*pi`, throughout the
`q` interval, or beyond degree 18. The weakest tested degree-18 truncation at
`y=1/28` is positive (approximately `0.387123037496`), but this is only a
finite endpoint test.

A durable analytic lemma survives. The checker
`research/grothendieck/checkers/theta_nq_complex_disk.py`, with durable output
`research/grothendieck/results/theta-nq-complex-disk.json`, proves exactly that,
uniformly for Chart-1 real `q` and the rigorous rational bracket for `2*pi`,
both logarithms used by `m(y)` and `m(4y)` are analytic for complex
`|y|<=1/4`. Its perturbation bound is

`962112750161874179137500000000000000 /`
`6348509442023664851915189583023594773 < 1`.

A second exact checker,
`research/grothendieck/checkers/theta_nq_cauchy_magnitude.py`, with durable
output `research/grothendieck/results/theta-nq-cauchy-magnitude.json`, propagates
this disk bound through `Nq`. It gives `|Nq|<=167061174` on `|y|=1/4` and an
order-20-and-higher contribution to `partial_y Nq` below
`1.38e-6` at `y<=1/28`. The checker records the exact rational tail in
hexadecimal numerator/denominator form as well as its decimal rendering. This
is a uniform tail certificate. It does not make the endpoint-only degree-18
polynomial parameter-uniform and does not address
`partial_q Nq`.

## Disposition

**Certified by the direct scaled-residual rival.** With `z=qy`, write
`D=q^2R/z^2`, `H=zR_z-2R`, and `J=qR_q+zR_z`; positive prefactors reduce the
required signs to `H<0` and `J>0`.

The exact degree-13 cover has 484 accepted base `q` cells and 56 accepted
bisected cells, with no unresolved geometry. Its finite scaled bounds are
`H/z^3<=-2307.19` and `J/z^2>=0.719384` on base cells; refined cells have
`J/z^2>=8.22851`. Exact Cauchy tails on `|z|<=1/8` are at most `13.5124` and
`0.696635`. The finite margins strictly dominate both tails, proving
`D_y<0` and `D_q>0` throughout Chart 1.

The scoped evidence map is `theta-chart1-sign-certificate.md`. Earlier failed
natural covers, factorwise signs, and `Nq` monotonicity experiments remain
falsification history and are not premises of this theorem. This packet does
not re-prove the separately certified Chart-2 signs or exact corner theorem.
