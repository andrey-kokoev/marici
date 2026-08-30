# Positive expectations need a bath, compiler, and randomness (WP78, move 7/12)

Agent: `marici.Figueiredo`. Date: 2026-08-24.

For a three-level Gram operator the exact cyclic phase twirl

\[
E(H)=\frac13\sum_{k=0}^{2}D^kH D^{-k},\quad
D=\operatorname{diag}(1,\omega,\omega^2)
\]

is spectral pinching: it preserves the diagonal, kills off-diagonal entries,
is trace preserving and idempotent, and has a proper image. It is therefore
stabilization-shaped mathematics.

The formula does not supply a constructor. Its resource ledger requires a
spectral-frame coupling, three executable branches, uniform randomness
(`log2(3)` ideal bits per independent draw), timing, discard/reset dynamics,
and uniform substrate/apparatus error. None is declared. Its commuting fixed
locus also fails the fitted ensemble. Positive Gram pairings and commutator
scores have instruments but merely append records.

The smallest channel falsifier is one off-diagonal matrix unit, which the
twirl kills; the physical falsifier is one observed nonzero mixing entry.
Algebraic branch span is not executable control.

Verification: `uv run --with sympy python
research/flavor/checkers/wp78_positive_randomized_constructor_resources.py`.
