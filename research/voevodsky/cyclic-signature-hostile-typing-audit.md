# Hostile typing audit of the cyclic signature

## Question

Do the simultaneously declared cyclic interfaces correspond to actual maps in the current RH model, or did the symmetric signature silently promote candidates into admitted transitions?

## Claim boundary

This audit checks semantic availability against `rh-three-pyramid-factorization.md`, `entire-kernel-observer-nerve.md`, and the fork packets. It does not realize a missing map.

## Findings

### Vertex A to B

The comparison \(\Phi_A:O_A\to O_B\) is available at classical normalization strength as \(\rho_{\rm an}\simeq\rho_{\rm ar}\). Its exact source normalization remains tracked separately, but this is the only full cross-pyramid transition currently materialized.

### Vertex B to C

Two codomains had been conflated. The arithmetic apex maps to raw probe data by evaluation,

\[
\rho_{\rm ar}\longmapsto K_\sigma(d).
\]

That map does not land in the positive cone without the missing positivity lift. Therefore \(\Phi_B\) is admissible only if \(O_C\) means unrestricted probe-data objects. If \(O_C\) means positive cone objects, \(\Phi_B\) is absent.

### Vertex C to A

The spectral-shift and gauge transports are fork deformations. They do not define a transition from the main model's positivity-probe object to its fixed analytic apex. Thus \(\Phi_C\) is a declared candidate, not an admitted main-model arrow.

## Defect and repair

The original signature called all three maps `admitted_transitions`. That was an overstatement. The signature now calls them `transition_candidates` and records each status. Symmetric declaration is preserved without fabricating semantic equality among edges.

## Disposition

The cyclic signature is syntactically complete but semantically asymmetric:

- \(\Phi_A\): materialized;
- \(\Phi_B\): partial after splitting raw probes from positive-cone objects;
- \(\Phi_C\): speculative fork deformation.

The repair refines \(O_C\) into raw probe data \(O_C^{\rm raw}\) and positive cone \(O_C^+\), with a separate candidate lift \(L_C\) between them. Consequently \(\Phi_B:O_B\to O_C^{\rm raw}\) is materialized as evaluation without assuming positivity, while \(L_C\) remains missing. The counterclockwise cycle is represented in the deformation envelope and remains distinct from the main RH-model transitions. Realization of \(G_B\) may now proceed without this coercion.

## Verification

- `research/voevodsky/checkers/check_cyclic_signature_typing_audit.py`
- `research/voevodsky/results/cyclic_signature_typing_audit.json`
