# Common overlap equality cannot complete the local source assembly

## Frozen DPC

The source is the actual four-state primitive-evidence family P,A,B,AB for the frozen middle input. Local restriction maps are the independently computed A-only and B-only continuation quotients. Local admission means having a nonempty source fiber. Overlap means the shared frozen problem binding and current certified status.

These definitions were written to a separate contract before enumerating the joint fibers. The source-bound common-refinement checker and owning independent branch replay run freshly.

## Counterexample

The A-only classes are {P,A}, {B}, {AB}. The B-only classes are {P,B}, {A}, {AB}.

Supply local class {B} on the first side and {A} on the second. Both are individually realized, have the same frozen binding, and report UNRESOLVED. Their joint source fiber is empty because A and B are different source-evidence states.

Exhaustion finds nine locally admitted pairs, five overlap-compatible pairs, and four globally realizable pairs. The DPC is refuted for this frozen contract.

The primitive merge AB is a common future extension, not a realization of the supplied restrictions: AB maps to the resolved class on both sides.

## Stronger obstruction: changing the common factor is insufficient

Any deterministic common overlap derived from both local views must be constant on both local kernel equivalences. The first observer identifies P with A; the second identifies P with B. Therefore every such common factor identifies P,A,B together. The join of the local kernels has classes {P,A,B} and {AB}.

Consequently the incompatible pair with singleton fibers {B} and {A} agrees under every deterministic common factor of these unchanged local views. Replacing the current verdict by another shared equality-valued overlap cannot remove this pair.

This is stronger than the original shared-verdict counterexample. The missing compatibility is relational information not expressible as equality of independently computed common summaries of these views.

## Structural consequence

The jointly realizable pairs form a proper relation inside the product of local observer spaces. That relation is not the pullback over any deterministic common factor of these fixed restriction maps.

Local-to-global completeness thus needs a condition on the restriction geometry. In this example, achieving it requires richer local observations, independently available joint compatibility evidence, or a changed notion of assembly such as compatible multi-cut histories. Sharing one source object alone does not make arbitrary pairs of its quotient observations jointly realizable.

This does not contradict the Abel single-valley result: there the particular locally extremizing choices are shown constructively to belong to a globally admissible cumulative history. Here the local quotient geometry admits a pair with no common same-state witness.

## Reproduction

    uv run --with python-flint python research/voevodsky/checkers/check_local_to_global_source_assembly.py

Artifacts:

- `results/continuation-quotient/local-to-global-source-assembly-contract.json`
- `results/continuation-quotient/local-to-global-source-assembly.json`
