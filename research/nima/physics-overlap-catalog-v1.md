# Ordered single-excitation cavity/detector overlap

## Disposition and scope

Accept `overlap-contracts` as a **scoped specification**, not as physical sector transport. The catalog declares one common domain and two concrete routes for the selected target pair. The common source is `passive-port-fock-memory.v1`; imported passive optical and CP instrument laws remain explicit. Dynamics-source selection, physical bindings and sector-transport assembly remain open.

Contract: `contracts/physics-overlap-catalog.v1.json`.
Checker: `checkers/check_physics_overlap_catalog.py`.

## Common domain and inclusion

Let V be the vacuum-plus-single-particle space `C|vac> direct_sum C^10` with ten mode labels from the reviewed geometry. The joint domain is V tensor C^2, with classical ready/dead memory. Optical states may have arbitrary complex coherence, including vacuum/one-particle coherence. Total photon number is at most one, so every local detector port automatically has support n_port<=1.

The inclusion J sends vacuum to Fock vacuum and each mode vector e_j to its single-occupation Fock vector. Tensor J with the identity on memory. Occupation-basis metric weights are all one on this domain, making J isometric.

All initial modes are prepared before this closed three-round example. Future input slots are spectators until their declared round. This overlap does not introduce fresh replacement photons between detector events, nor a memory reset. Those would require an explicitly different preparation operation and resource ledger.

## Two routes

**Route A:** apply the Fock lift Gamma(W_k), then the local spectator-extended source detector instrument at transmitted slot `2+3k`. Keep separate Kraus/environment labels and the complete C/N word.

**Route B:** evolve the retained vacuum/port density matrix using `1 direct_sum W_k`, with W_k computed independently from the ordered mirror/propagation/loss equations. Apply the original local four-state detector matrices tensor identity on spectator modes, restricting to the shared domain. Keep the same complete word and occurrence attachments.

Every round keeps reflected, transmitted, environment, returning and future-input modes. The physical bin duration is not inferred from k: alignment with round-trip duration T remains a separate physical clock binding.

## Operation and instrument squares

The passive inclusion law is

`Gamma(W_k) J = J (1 direct_sum W_k)`.

It follows directly on vacuum and the ten one-particle basis vectors, and extends complex-linearly. No coherent-state preparation is substituted for a one-photon vector.

At a named port p, identify local basis states as |0R>,|1R>,|0D>,|1D>. Each separately labelled source Kraus operator has one nonzero local transition. On a global basis vector, determine local occupation by whether its photon is at p. If it is at p, destruction leaves global vacuum. If it is elsewhere, local occupation is zero and the spectator photon and its coherent amplitudes remain unchanged. Apply the source memory transition without merging environmental labels.

This basis description gives, for **each Kraus label a**,

`K_a^Fock J = J K_a^port`.

Consequently, for every complex density operator rho in the shared domain,

`sum_a K_a^Fock J rho J* K_a^Fock* = J (sum_a K_a^port rho K_a^port*) J*`.

The proof uses complex-linear Kraus intertwining, not an inference of complex channel equality solely from real polarization fixtures. The source's separated environment labels are imported data; classical observations do not independently establish their unique quantum completion.

Compose the passive and outcome squares in their declared order. Induction on prefixes gives agreement of the complete **unnormalized posterior**, not just the endpoint probability, for every allowed word. Taking trace gives the word probability. Normalize only when trace is positive. The empty word is identity. Composed histories retain source ID, round, routed port, outcome, occurrence ID and predecessor ID; numerical endpoint equality does not erase histories.

## Readouts and resources

Occupation projections for returning/reflected/transmitted/environment ports descend through J, as does total photon number. Passive rounds preserve occupation. A detector step can only destroy the routed photon. Define its absorbed occupation as input occupation minus the sum of output occupations over C and N, including no-click loss. This is nonnegative. Summing these balances over the outcome tree telescopes to initial occupation = final occupation + cumulative absorbed occupation. Readiness is a separate dimensionless memory ledger, not an energy term.

Physical energy units remain conditional on the equal-frequency optical convention and a supplied scale. A fixed-one-photon state's field mean is zero; its mode coefficients nevertheless transform by W. Sharing W does not identify it with a coherent field-mean preparation.

## Verification and exclusions

Fresh exact checks compare the independently implemented field/density route against Fock branches on 66 real polarization vectors for each classical memory state, across all three-bin outcome prefixes:

- 1848 unnormalized-posterior and complete-outcome squares;
- 1452 Kraus completeness matrix-unit checks, including spectator off-diagonals;
- 924 occupation-balance nodes;
- spectator coherence preservation and a hidden-reset distinction;
- total multiphoton domain guard;
- rejected dropped no-click, duplicate occurrence, hidden reset, physical-clock substitution and foreign-source records.

Complex coefficients are covered by the written per-Kraus basis argument above; the executable polarization fixtures are explicitly real. No measured records are used.

A nonzero coherent detected amplitude has unbounded photon support and is **not** in this exact finite-detector overlap. Bool/exchange/marked137 are not identified with the optical source; their existing fixed-fibre, spectral and cycle obstructions remain scoped controls. Coherent-memory CP completion is not uniquely selected by classical records.

This catalog supplies the previously missing overlap specification and corroborating conditional comparison squares. `same-witness-sector-transport` and `cross-sector-compatibility` remain open until their physical-sector prerequisites and reviewed coverage are supplied.

```
python research/nima/checkers/check_physics_overlap_catalog.py
python research/aspect/scc/scc.py check physics-programme-v18
```
