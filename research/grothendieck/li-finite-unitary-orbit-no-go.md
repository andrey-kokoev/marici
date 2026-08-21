# Finite unitary-orbit norms cannot carry Li growth

## Proposition

Let `U` be unitary on a Hilbert space and let `e` be a vector of finite norm.
Set

`v_n=(I-U^n)e`.

Then, for every integer `n`,

`0 <= ||v_n||^2 <= 4||e||^2`.

Equivalently, if a finite positive measure `mu` on the unit circle realizes

`a_n = integral |1-z^n|^2 d mu(z)`,

then `0 <= a_n <= 4 mu(T)` for every `n`.

## Proof

Unitarity gives `||U^n e||=||e||`. The triangle inequality gives

`||(I-U^n)e|| <= ||e||+||U^n e|| = 2||e||`.

Squaring proves the assertion. The measure formulation is the same estimate
integrated pointwise, since `|1-z^n| <= 2` on the unit circle.

## Consequence for Gate C

The exact Cauchy-jet identity makes the Li features look like the coboundary
`1-u^n`. This does **not** permit a finite unitary-orbit Gram model for a
Li sequence with unbounded long-range growth. Such a model would be bounded
independently of `n`.

Therefore a successful source construction must expose at least one of the
following pieces of noncompact structure rather than hide it:

1. an infinite spectral measure with a specified renormalization;
2. an unbounded or distributional cyclic source object;
3. an `n`-dependent domain whose dependence is itself arithmetically forced;
4. a positive form not reducible to one finite-norm unitary coboundary.

This is an architectural falsifier, not an RH proof and not a proof of Li
positivity. It prevents a superficially attractive but scale-incompatible
completion of the Cauchy-jet construction.

## Small exact checker

`checkers/li_finite_unitary_orbit_no_go.py` verifies the sharp scalar bound
and finite-dimensional unitary examples symbolically. Its purpose is
regression and witness generation; the proof above is the theorem.
