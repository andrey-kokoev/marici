# v168: physical soft-D1 realization gate

A fresh audit of the physical principal-Cech support packet identifies the exact
kind of missing geometric map.

The literal maps to D2, D3, Z12, Z13, and Z23 vanish by support, and both D1
corner maps vanish. The D1 map is explicitly marked as requiring soft nearby-
cycle specialization and as not being an ordinary fibre boundary. The primary
source supplies no analytic continuation.

Therefore the inhabited synthetic relation-cell model cannot be promoted to
physical road cells by a literal boundary inclusion. The required new datum is
a soft nearby-cycle specialization/analytic-continuation morphism, followed by
a check that its boundary equals the Cech image of Bx.

Evidence is `results/physical-soft-D1-realization-gate.json` from
`checkers/check_physical_soft_D1_realization_gate.py`.
`rzk/196-physical-soft-d1-realization-gate.rzk.md` passes all eight declarations
without assumptions.
