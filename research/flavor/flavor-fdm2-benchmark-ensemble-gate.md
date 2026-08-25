# Fixed-benchmark ensemble gate for FDM-2 (WP111)

Agent: `marici.Figueiredo`. Date: 2026-08-25.

Evaluate WP110 on the historically fixed WP90 algebraic benchmark

\[
r_{min}=r_{max}=1,\qquad Z_{max}=1,\qquad
\Sigma_{min}=36/25.
\]

These values come from the declared unit-modulus singlet vacua, unit mediator
mass normalization, and zero-portal zero-temperature slice. They were not
chosen to match the fitted `J` values. The resulting conservative normalized
bound is

\[
J_{bench}=
{1920(36/25)^{3/2}\over729(4+\sqrt{84})^6}
\approx8.7410236088\times10^{-7}.
\]

Every one of the 1,210 stored fitted sheets satisfies
`|J|>J_bench`; the smallest observed margin is about 35.94 times larger. This
is an exact audit of a parameter-fixed algebraic consequence against the full
stored ensemble. Because the numerical inequality was derived after the data
were available, it is not described as a preregistered quantitative
prediction; the preregistered coarse prediction remains only `J != 0`.

## Canonical instrument boundary

WP93 shows that the finite-mass Schur map is not the exact canonically
normalized light readout. If the normalized canonical/matching uncertainty is
`epsilon_J`, the benchmark can distinguish the broken attribute from zero only
if

\[
J_{bench}>2\epsilon_J.
\]

Thus the required benchmark error is
`epsilon_J<J_bench/2`, approximately `4.3705e-7`. No current calculation
certifies that error. The ensemble pass therefore validates compatibility of
the algebraic consequence, not the physical instrument.

Classification: parameter-fixed algebraic branchwise selector compatible with
the complete ensemble; physical selector instrument still conditional. It is
not a rigidifier. Smallest exact falsifier of the instrument claim is
`epsilon_J=J_bench/2`, where the certified symmetric and broken intervals
touch.

Verification: `uv run --with sympy python
research/flavor/checkers/wp111_fdm2_benchmark_ensemble_gate.py`.
