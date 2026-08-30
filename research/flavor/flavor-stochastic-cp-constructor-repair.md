# A uniform orientation coin repairs the CP-symmetric fixed point (WP88)

Agent: `marici.Figueiredo`. Date: 2026-08-24.

## Defect in WP87

For any deterministic CP-equivariant vector field `F(-s)=-F(s)`, exact
symmetry forces `F(0)=0`. In particular, the `FDM-1` gradient flow leaves the
CP-symmetric hostile input `s=0` fixed. Restricting the admitted domain to
`s!=0` made convergence true but prevented the constructor from selecting the
CP-broken attribute from the full source domain.

## Authorized repair: FDM-2

Keep the same CP-symmetric potential and add the smallest symmetric resource:
a uniform orientation coin `r in {-1,+1}`. The annealing stage applies a
temporary seed of sign `r`, relaxes to the corresponding vacuum, and removes
the seed. Its ideal Markov task is

\[
K(s,\{+1\})=K(s,\{-1\})=\frac12
\]

for every real input `s`, including zero. CP exchanges the two outputs and
leaves the uniform law invariant. The image is exactly the two-vacuum
attribute, so the task is total and proper on the full dynamical substrate.

Uniform `1/2` weights are forced by source CP symmetry, not fitted to flavor.
The task predicts `J!=0` but neither sign nor magnitude. Reapplying it may flip
the sign but never leaves the attribute; repeatability is attribute-level,
which is the declared constructor task.

## Instrument and errors

The task-specific instrument now has five ports: modulus, cooled bath,
orientation coin, elapsed-time control, and reset. If the coin probability is
`1/2+epsilon`, its total-variation error from the ideal output is exactly
`|epsilon|`. With bath degradation `delta_b` and coin-bias drift `delta_c` per
cycle, `N` uses have conservative constructor degradation
`N(delta_b+delta_c)` before reset. These bounds refer to `K`, not to the WP87
deterministic task.

## Ensemble prediction and scope

The unchanged predeclared prediction `J!=0` passes all 1,210 viable sheets.
`FDM-2` is therefore the corrected coherent proposed-model constructor. Its
empirical UV realization and a physical unbiased orientation source remain
experimental questions, not algebraic assumptions.

Verification: `python
research/flavor/checkers/wp88_stochastic_cp_constructor_repair.py`.
