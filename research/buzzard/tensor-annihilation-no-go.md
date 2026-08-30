# Tensor annihilation no-go packet

## Grothendieck source

This formalizes the reusable no-go core of
`research/grothendieck/theta-gaussian-annihilation-produces-only-an-archimedean-recurrence.md`.

## Formal objects

- `tensorSeparatedReadout archimedean finite` represents the factored global
  Mellin/Euler evaluation.
- `local_annihilation_kills_separated_readout` proves that a zero local factor
  annihilates every finite factor.
- `annihilated_tensor_readout_not_injective` proves loss of faithfulness.
- `no_decoder_recovers_finite_factor` proves that post-processing or replay of
  the common zero cannot recover arbitrary finite source data.
- `mixedSourceReadout_zero_injective` is the repair witness: a genuinely mixed
  channel can remain faithful, but it is an additional nonseparable coupling.

## Assumptions and coefficient type

The equalities use an arbitrary commutative ring. The hostile faithfulness
theorems additionally require a nontrivial ring so that zero and one differ.

## Missing analytic interfaces

Formalizing the Mellin integration-by-parts identity requires the chosen
function space, differentiability and integrability hypotheses, endpoint
decay, the initial convergence chamber, and the exact Mellin normalization.
The Gaussian recurrence then concerns only its archimedean transform.

No mixed lattice-incidence operator joining the real scale to finite
prime-power labels has been supplied. Additive Poisson sewing, an Euler shift,
division by zeta, global zero information, and RH are not consequences of the
local annihilation equation and are not assumed here.

## Verification boundary

Static placeholder checks are permitted. Lean elaboration is withheld under
Nima's active no-build instruction.
