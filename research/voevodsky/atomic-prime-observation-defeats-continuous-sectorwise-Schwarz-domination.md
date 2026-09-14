# Atomic prime observation defeats continuous sectorwise Schwarz domination

## Candidate route

A sufficient source proof of universal rung-four Schwarz positivity would dominate the signed prime square functional by a positive continuous archimedean reference:

\[
|P(p^*p)|\leq\theta A(p^*p),
\qquad \theta<1,
\]

uniformly over the complete polynomial primitive tower.

## Atomic obstruction

Point evaluation is not bounded in the \(L^2\) norm of a non-atomic measure on a polynomial-dense closure.

For the interior atom \(z=1/2\), take

\[
p_n(z)=(4z(1-z))^n.
\]

Then

\[
p_n(1/2)=1,
\]

while

\[
\int_0^1|p_n(z)|^2\,dz
=
16^n\frac{((2n)!)^2}{(4n+1)!}
\longrightarrow0.
\]

Hence the ratio of atomic square observation to continuous square norm diverges. No degree-uniform relative constant exists.

The same obstruction applies whenever the transformed prime functional retains a nonzero atom at a point where the proposed archimedean reference has no matching atom.

## Consequence for the rung-four programme

Universal Schwarz positivity cannot be proved by separating sectors and absolutely dominating discrete prime observations with a purely continuous gamma measure.

A surviving source proof must use one of:

- a stronger common topology controlling point evaluations;
- matching atomic reference mass;
- cancellation retained in the fully coupled endpoint–gamma–prime Schwarz determinant.

The third option matches the earlier conclusion that sectorwise positivity is impossible. The correct target remains the coupled residual

\[
L(1)L(p^*p)-|L(p)|^2,
\]

not independent positivity or absolute domination of its source sectors.

## Verification

```text
python research/voevodsky/checkers/check_atomic_prime_vs_continuous_square_domination_no_go.py
```

Artifacts:

- `research/voevodsky/checkers/check_atomic_prime_vs_continuous_square_domination_no_go.py`
- `research/voevodsky/results/atomic_prime_continuous_square_domination_no_go.json`
