# Theta–RH corrected-G4 SCC contract revision

Owner: `marici.Aspect`

## Question

Can SCC represent the corrected G4 architecture, preserve its evidence boundary, and expose the actual post-rigging RH frontier?

## Claim boundary

The version-two pass certifies declared topology, witness presence, shared-interface compatibility, migration rules, executable no-go gates, terminal cut sets, hostile rejection, and execution provenance. It does not prove prime-shell cancellation, global Fourier–Poisson response intertwining, the Evans-to-Green chain map, physical realization, Green confinement, or RH.

## Disposition

Version two refines the frozen version-one certificate without rewriting it. It is registered as model `theta-rh-corrected-g4-v2` and check `theta-rh-g4-v2`.

The exact Evans history domain, three-port block-domain membership, five-port arithmetic summability, and maximal-isotropic Evans domain are constructed with source-digested witness objects from `research/nima/rh-rigging-frontier-after-exact-evans-domain-and-five-port-summability.md`. The former `seam_limiting_absorption_domain` slot was removed because it conflated those constructed facts with two open equations.

The non-rigging frontier is exactly:

- `prime_shell_adjoint_residual_family`;
- `global_fourier_poisson_response_intertwining`.

The first requires every multiplicity jet:

\[
B_\Sigma^\dagger\partial_z^j u(\cdot;z_0)=0,
\qquad 0\le j<m.
\]

The second requires the full Fourier–Poisson response trace to lie in the global maximal-isotropic sewing relation. Both feed `evans_to_conservative_green_chain_map`; `rh_proved` remains false.

## SCC additions

1. First-class registry and model entries for v2.
2. Witness-bearing constructed cells with source and checker digests, assumptions, regime, and proof strength.
3. Explicit v1-to-v2 preservation, retyping, and nontransportability metadata.
4. A shared interface descriptor checked on every dependency edge.
5. Executable negative-knowledge gates for finite moments, scalar seam data, range closure, and local coercivity.
6. Computed completion frontier and singleton minimal terminal blockers.
7. Executable semantic nonpromotion invariants.
8. A persisted receipt containing command, runtime, contract/compiler/checker digests, fixtures, and evidence digest.

## Verification

- `python research/aspect/checkers/check_theta_rh_g4_interaction_net_state.py`: passed.
- Historical v1 compilation: passed.
- Corrected v2 compilation and all hostile mutations: passed.
- `python research/aspect/scc/scc.py run core`: all five checks passed, including `theta-rh-g4-v2`.
- `python research/aspect/scc/scc.py validate all`: all 48 registered models passed manifest validation.
- `python research/aspect/scc/scc.py check theta-rh-corrected-g4-v2`: passed; subsequent status is `current_checks_passed`.
- Constructor synthesis emits only the two source-specific frontier candidates: complete prime-shell adjoint jet cancellation and global Fourier–Poisson response intertwining. Generic keyword candidates are suppressed when these exact signatures match.
- `python research/aspect/scc/scc.py doctor`: healthy; 44 discovered model manifests; no manifest or path errors.
- Result: `research/aspect/results/theta_rh_g4_interaction_net_state.json`.
