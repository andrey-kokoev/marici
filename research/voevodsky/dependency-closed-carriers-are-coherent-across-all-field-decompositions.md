# Dependency-closed carriers are coherent across all field decompositions

## Frozen DPC and construction

Freeze the existing five-field expression semantics for end, origin, pending, received and issued, including outputs, initial states, source/task/run context, eighteen labels and same-snapshot atomicity. Enumerate every set partition of those five fields: 52 ownership decompositions.

For each partition independently, recompute dependency closure from output/guard reads and retained updates. Derive operation ownership from the field it updates; assign origin audit to the origin owner. Recompute guard/payload ports and remote-read requirements. Explore the reachable product of that partition's local field carriers directly from the initial states.

The owning causal-interface verifier is freshly run. The constructed carriers share the declared expression semantics but do not obtain their state lists from a reference quotient.

## Exact result

Every decomposition reaches 70 states. A posteriori, source-coordinate decoding gives an explicit bijection between each ordered pair of carriers. The exported maps preserve initializations, outputs, accepted/rejected transitions and their successor states.

Checks:

- 52 independently explored decompositions;
- 2,704 ordered comparison maps;
- 3,407,040 transition comparison checks;
- 140,608 strict comparison triangles.

For every triple,

    F_jk F_ij = F_ik.

Double comparison is identity. Thus reassociation coherence is strict; no nontrivial higher homotopy is required for these maps. Every further coherence equation made from these comparisons follows by substitution of the checked triangle identities.

Foreign context bindings are rejected in every carrier. The product is restricted to reachable states rather than all combinations of independently valid coordinates.

## Structural meaning and boundary

Under this contract, ownership boundaries change which dependencies cross ports. They preserve the source-compatible interaction carrier. The 70-state retained causal state has coherent presentations across every field partition tested; its current 62-state view can be transported through these identifications.

The positive result concerns changes of decomposition with the same operational semantics. Because fields are jointly retained and atomic expressions remain fixed, source-coordinate identity is the natural comparison. This is an exact regrouping theorem and implementation check, not evidence that arbitrary component replacements, delayed communication, action splitting or different atomicity assumptions preserve behavior.

The checker uses the owning expression interpreter for each decomposition and checks comparison laws internally. It does not provide an independent implementation of that interpreter. The exported compressed packet contains all carriers, tables, ports and comparison maps for independent inspection.

## Reproduction

    python research/voevodsky/checkers/check_decomposition_coherence.py

Artifacts:

- `results/decomposition-coherence-contract.json`
- `results/decomposition-coherence-carriers.json.gz`
- `results/decomposition-coherence.json`
