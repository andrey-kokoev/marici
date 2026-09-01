# Alternating-cubic production-kernel no-go: WP1100

## Question

Do the \(SU(3)\) alternating cubic carriers from WP1080 supply the missing
production/decay kernel?

## Tensor gate

The invariant \(\epsilon_3\) has six nonzero components, indexed by the six
permutations of \((1,2,3)\): three are \(+1\) and three are \(-1\).

These components are internal tensor entries. They are not six soft-branch
production rows and not six physical16 output rows. The admitted map counts
are

\[
\epsilon\to{\rm soft}:0,
\qquad
\epsilon\to{\rm physical16}:0.
\]

## Degeneracy gate

The six localized soft branches retain

\[
q=\frac1{23}(6,8,1,4,2,2),
\]

not the six event weights \((1/4)^6\). The alternating carriers preserve the
\(SU(3)\) indices and do not distinguish the \(A\)-triplet directions or
select a branch.

## Classification

Negative gate. Six epsilon components, their signs, and \(SU(3)\) invariance
cannot be promoted to six event branches, reweighting, production couplings,
or gain.

Checker: `research/flavor/checkers/wp1100_alternating_cubic_production_kernel_no_go.py`

Result: `results/wp1100_alternating_cubic_production_kernel_no_go.json`
