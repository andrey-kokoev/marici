# Autonomous milestone: instruments, faults, perturbations, and ribbons

Owner: `marici.Kitaev`

## Disposition

Four consecutive bounded successors are complete.  The first three close
finite toric-code gaps; the fourth reaches a theorem-changing blocker for a
full non-Abelian categorical promotion.

## Exact verification

Each checker was generated and rerun with exit code zero, and each saved JSON
matched fresh stdout after newline normalization:

| checker | gates | finite cases |
|---|---:|---:|
| `check_toric_instrument_surface.py` | 6/6 | `L=2..6` |
| `check_wilson_constructor_faults.py` | 6/6 | `L=2..8` |
| `check_local_perturbation_order_threshold.py` | 5/5 | `L=2..4` |
| `check_s3_quantum_double_ribbon.py` | 6/6 | complete finite `S3` census |

## Source-derived toric instrument and cross-sector group

The controlled-string pointer dilation derives `K_+=Pi_+` and `K_-=Pi_-`
on the four-dimensional toric ground space.  A logical-flip instrument
`X1 Pi_b` has identical effects but opposite repeat behavior: QND repeat
probability one versus flip repeat probability zero.

Fine edge measurement followed by parity coarsening differs on protected
inputs, not only ambient witnesses: it kills exactly `L` star expectations,
whereas global Wilson measurement preserves all of them.

This places the toric protocol in the source-derived instrument group beside
the bounded double-slit QND and one-mode UDW instruments.  Scattering/flavor
Lüders maps remain formal completions; radiative memory lacks apparatus
dynamics and cosmology lacks an outcome algebra.  This is a heterogeneous
type census, not a cross-sector morphism.

## Single-fault constructor audit

For the mobile CNOT string, a pointer `Z` fault after gate `k` propagates to
the remaining `L-k` data suffix.  Every nonzero suffix has two endpoints and
weight at most `L-1`, so it is detectable and sublogical.  Pointer `X` flips
the record without data fanout; `Y` combines both.  Parallel refined
post-coupling faults do not fan into data, but that protocol is already
non-QND in the ideal limit.  Fault fanout cannot be ranked independently of
ideal instrument backaction.

## Generic local-perturbation threshold

For arbitrary sums of weight-one edge Paulis, every order-`r<L` monomial
projects to zero or scalar stabilizer action on the code.  Logical paths first
occur at order `L`, with `2L` minimum representatives in each CSS channel.
The bare marked Wilson loop nevertheless anticommutes with `L` terms of a
uniform conjugate field, so it is not a QND port.  Code distance controls the
formal order threshold; no convergence or dressed instrument is inferred.

## Non-Abelian `D(S3)` frontier

The exact group census gives conjugacy-class sizes `1,3,2`, centralizer orders
`6,2,3`, eight anyon dimensions `1,1,2,3,3,2,2,2`, and squared total quantum
dimension `36`.  Braiding by `(01)` sends flux `(12)` to `(02)` and permutes
the transposition basis as `[0,2,1]`.  Braiding is therefore a matrix action,
not a scalar intersection phase.

The theorem-changing blocker is precise: before claiming a braided fusion
category, the source must freeze locally clockwise/counterclockwise ribbon
operators, endpoint/base conventions, fusion coefficients, associators, and
pentagon/hexagon coherence.  Current Carrier geometry can be refined to an
oriented ribbon with framed endpoints; the `D(S3)` coefficient category is
not supplied by incidence alone.

## Assumptions, falsifiers, unresolved typing

Assumptions and local falsifiers are frozen in the four bounded packets.
Major unresolved items are verified-cat/two-qubit-gate faults, generic
spectral-flow dressing, perturbation convergence, and the full ribbon fusion
category.  No thermodynamic, hardware-threshold, or cross-sector-natural
instrument theorem is asserted.

## Post-objective observation

Excitement: non-Abelian frontier `10/10`, source instrument `9/10`,
perturbative threshold `8/10`, circuit fault audit `7/10`.  Confidence is
`9/10` for the finite results and `4/10` for completing the full ribbon
category without a larger operator derivation.  Realized information gain is
`10/10`.  These are process observations, not evidence.

