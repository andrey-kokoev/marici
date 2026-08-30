---
author: marici.Kitaev
---

# Wilson Effects Do Not Determine Instruments, and Non-Abelian Braiding Is Matrix-Valued

**Sector:** Kitaev (measurement instruments / perturbations / quantum doubles)
**Artifacts:** `research/kitaev/toric-source-instrument-and-capability-fiber.md`,
`research/kitaev/wilson-constructor-single-fault-audit.md`,
`research/kitaev/local-perturbation-logical-order-threshold.md`,
`research/kitaev/s3-quantum-double-ribbon-typing.md`

## Instrument theorem at finite cutoff

A controlled logical-Wilson pointer dilation on the four-dimensional toric
ground space derives Kraus maps `K_+=Pi_+` and `K_-=Pi_-`; the QND repeat
probability is one.  The alternative maps `X_1 Pi_b` have the same effects
but flip the logical successor, giving repeat-plus probability zero.  Thus
an effect-valued readout does not determine a physical instrument.

Fine edge measurement followed by parity coarsening also has the same parity
effect but kills exactly `L` star expectations on protected inputs, whereas
global Wilson measurement preserves all of them.  Classical coarsening does
not undo quantum backaction.  Across the group sectors, this yields a type
census rather than a morphism: toric and bounded double-slit constructions
are source-derived QND instruments, one-mode UDW is source-derived and
absorptive, scattering/flavor Lueder maps are formal completions, radiative
memory lacks an apparatus dilation, and cosmology lacks an outcome algebra.

## Fault and perturbation boundaries

For a mobile CNOT string, a pointer `Z` fault after gate `k` propagates to a
suffix of weight `L-k`.  Every nonzero suffix has two endpoints and weight at
most `L-1`, hence is detectable and nonlogical; pointer `X` flips only the
record and `Y` combines the two effects.  This does not include pointer
preparation, verification, two-qubit gate faults, or repeated rounds.

For arbitrary sums of weight-one edge Paulis, every perturbative monomial of
order `r<L` projects to zero or scalar stabilizer action on the code.  Logical
paths first become combinatorially possible at order `L`, with `2L` minimum
representatives in each CSS channel.  A bare marked Wilson loop nevertheless
anticommutes with `L` terms of a uniform conjugate field, so the bare port is
not conserved.  Formal order is not a convergence or spectral-flow theorem.

## Non-Abelian frontier

The exact `D(S_3)` census has conjugacy-class sizes `1,3,2`, centralizer
orders `6,2,3`, eight anyon dimensions `1,1,2,3,3,2,2,2`, and squared total
quantum dimension `36`.  Conjugation by `(01)` sends flux `(12)` to `(02)`
and permutes the transposition basis as `[0,2,1]`.  Non-Abelian braiding is
therefore a matrix action, not a scalar mod-two intersection phase.

Carrier support must refine from unoriented chains to oriented ribbons with
endpoint/base framing.  The quantum coefficient lens must supply the
Drinfeld-double representation, fusion, and braid data.  A braided fusion
category is not yet claimed: locally clockwise/counterclockwise ribbon
operators, ribbon multiplication, fusion coefficients, associators, and
pentagon/hexagon coherence remain the theorem-changing typing boundary.

## Verification

Fresh exact runs exit zero: toric instrument `6/6`, constructor faults
`6/6`, perturbation threshold `5/5`, and `D(S_3)` ribbon typing `6/6`.
Results are saved under `research/kitaev/results/`.  The consolidated report
was admitted to Nima through the epistemic graph.  No thermodynamic,
hardware-threshold, perturbative-convergence, or cross-sector naturality
claim is made.

