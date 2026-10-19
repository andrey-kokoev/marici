# Source-law premises: quadratic sufficiency and a clock-branch obstruction

## Current disposition

`dynamics-source-selection` remains **open**. This audit adds a precise sufficient generator principle and an additional exact obstruction: even quadratic, positive, local Hamiltonians are not selected uniquely by the supplied discrete optical component maps.

No new native source principle, physical authority or measurement plan is supplied. The audit narrows the missing source inputs instead of repeating the conditional creation-covariance theorem as if it justified itself.

Contract: `contracts/physics-source-law-premise-audit.v1.json`.
Checker: `checkers/check_physics_source_law_premise_audit.py`.

## What a quadratic source principle would prove

For a finite-dimensional Hermitian one-particle matrix h, define

`K = dGamma(h) = sum_ij h_ij a_i† a_j`.

On the finite-particle core, the CCR gives

`[a_i† a_k, a_j†] = delta_kj a_i†`,

hence

`[K, a_j†] = sum_i h_ij a_i†`.

K preserves each total-number sector. Each sector is finite-dimensional and Hermitian. Their Hilbert direct sum defines the self-adjoint second-quantized generator, with the finite-particle core as an essential self-adjointness core. Vacuum has eigenvalue zero.

Let `U(t)=exp(-itK)`. On adjacent finite number sectors, differentiating `U(t) a_j† U(t)*` gives the linear finite-dimensional ODE with coefficient -ih. Its unique solution is

`U(t) a_j† U(t)* = sum_i (exp(-ith))_ij a_i†`.

Thus U fixes vacuum and satisfies linear creation covariance with `W(t)=exp(-ith)`. The existing dense-core uniqueness argument then identifies it with Gamma(W(t)). These statements extend to the complete Fock space by the direct-sum construction, not by finite test extrapolation.

This provides a **sufficient source principle**: number-conserving quadratic Hamiltonian, no higher-degree terms, no displacement, and a fixed vacuum energy. It is not independently sourced in the reviewed packets. Number conservation and locality alone allow the earlier active-port Kerr terms. Declaring that only bilinear terms occur would still be an additional premise, not a derivation from the source register or the desired coherent recovery.

## A further ambiguity even after quadraticity

The supplied first mirror, in labelled (u,x) coordinates, is

```
S = [[-3/5, 4/5],
     [ 4/5, 3/5]].
```

S is a Hermitian involution. On its two active modes let `Q=(I-S)/2`; Q is an orthogonal projector. Let P_active project onto those modes, with both matrices zero on the eight spectators. Choose any component duration tau>0 and two one-particle generators

`h0=(pi/tau) Q`,
`h1=(pi/tau) (Q+2 P_active)`.

Both are Hermitian, nonnegative and spectator-local. Their second quantizations fix vacuum, conserve number and satisfy creation covariance at every time with their respective one-particle W(t).

Because Q and P_active commute,

`U1(t)=exp(-2*pi*i*(t/tau)*N_active) U0(t)`.

At every integer component duration `t=k*tau`, the first factor is identity on **every Fock number sector**, since N_active has integer spectrum. In particular both generators realize exactly the same mirror endpoint S, identity on spectators, and therefore the same complete coarse cavity/detector histories when that mirror endpoint is inserted into each ordered round.

At `t=tau/2` the factor is `(-1)^N_active`. The base one-particle half-step map is `I-Q-iQ`; the alternative has its negative on the active modes. For normalized `(vac+|1_u>)/sqrt(2)`, the mean a_u is

- h0: `1/10 - 2i/5`;
- h1: `-1/10 + 2i/5`.

These are distinct state/coherence evolutions with identical supplied integer-duration operations. On a fixed active-number sector the halfway sign can be a global phase, so merely asserting a different one-photon matrix is not by itself a density-state discriminator. Vacuum/one-photon coherence in the stated witness removes that alias.

This countermodel does not replace the actual mirror source or claim that its intermediate states have been physically authorized. It proves that the **discrete primitive map** does not determine its logarithm branch or continuous generator, even after adding positive local quadraticity. The reviewed plant provides an ordered delayed scattering map and a physical T slot, not a specified component Hamiltonian or its duration tau.

## Remaining source inputs

1. A native principle excluding higher-degree interactions and implying quadraticity/creation covariance.
2. Source Hamiltonians or a continuous primitive operation family selecting the generator branch and component durations.
3. Provenance for W's coefficients, phase frame, clock and energy normalization.
4. A scoped classical-memory detector claim, or an independent premise selecting the larger environmental/CP completion.

The existing register and optical source packets explicitly label these ingredients as imported, supplied or missing. A new quadratic declaration can support a conditional model assembly, but cannot close independent native-source selection. Measurement work stays parked.

## Fresh exact verification

The checker validates 1320 quadratic creation commutators on number sectors through N=2 (including creation into N=3), spectator commutators, vacuum fixing and number preservation. It checks 286 mirror endpoint columns through N=3, their factorial metric and the integer active-number phase alias. The half-step witness is computed with exact rational real/imaginary components and normalized exactly.

The unrestricted results use the CCR/direct-sum/projector arguments above. Three hostile controls reject presenting quadraticity as native-derived, supplying a branch-selection witness without evidence, and physical promotion. Source hashes are checked before and after execution.

```
python research/nima/checkers/check_physics_source_law_premise_audit.py
python research/aspect/scc/scc.py check physics-programme-v18
```
