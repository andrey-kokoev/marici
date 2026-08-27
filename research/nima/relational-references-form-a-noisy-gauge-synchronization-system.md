# Relational references form a noisy gauge-synchronization system

## Question

What additional structure is required after a dual-character reference makes a
signed local observable descend?

## Claim boundary

A relational reference solves only local gauge descent. A physical reference
system also has finite reliability, may admit several gauge-equivalent choices,
must transform naturally between presentations, and must synchronize with other
local references around context cycles.

This packet gives exact finite models for those gates. It does not construct the
remaining collider calibration or optical reference lineage.

## Character pairing

For a cyclic gauge action, let the signal transform through a character and the
reference through its inverse. Their product is gauge invariant. In exponent
coordinates for (Z_4),

\[
z\longmapsto z+g,
\qquad
\lambda\longmapsto\lambda-g,
\]

so the relative exponent

\[
q=z+\lambda
\]

is invariant. A target reversal acting on the signal while holding the admitted
reference fixed changes (q), so the relative observable retains target
sensitivity.

This identifies the observable as a pairing between associated character lines,
not as an absolute signed scalar supplied by either factor alone.

## Noisy tag attenuation

For a binary reference tag with error probability (omega), the signed response
is attenuated by

\[
\eta=1-2\omega.
\]

Generic local phase rank survives only when the ideal response and (eta) are
both nonzero. At (omega=1/2), the tag is random and the signed direction
vanishes exactly.

This is an identifiability gate, not yet a stability theorem. Uniform recovery
requires a declared lower bound on (|\eta|) over the admitted calibration and
context domain.

## Reference torsor and naturality

Valid reference choices may form a torsor. A unique reference is automatically
canonical relative to the declared structure. A positive-dimensional choice
space requires a source-authorized selector.

The selector must also be natural under every authorized presentation action.
A vector chosen in one chart and moved to a different vector by an admitted
chart swap is not a global reference. Numerical invariance is insufficient
without authority for the naturality cell.

## Reference-network synchronization

Let local binary frames be (r_i\in\{+1,-1\}). Observable transition data are

\[
h_{ij}=r_ir_j.
\]

The product around every cycle must be (+1). On a connected graph, consistent
edge data determine the vertex frames up to one global sign. One source anchor
selects a unique representative without changing the relative observables.

A single corrupted edge on a triangle produces cycle product (-1), so the
fault is detected. The syndrome alone does not identify which of the three edges
failed. Correction requires additional redundancy or an independently trusted
edge or vertex reference.

## Source lineage

A formal dual-character matrix is not a physical reference. The reference must
be generated, transported, calibrated, and consumed by source-authorized
constructors. Its lineage must declare:

- source preparation;
- transformation character;
- correlation with the target event;
- sign or phase assignment;
- dilution and noise model;
- allowed reuse and backaction;
- context transitions;
- fault and completion behavior.

## DPC

A relational reference network passes only if:

1. local character pairing descends;
2. target sensitivity survives;
3. attenuation is calibrated and uniformly nonzero;
4. reference selection is canonical or source-selected;
5. the selector is natural under presentation changes;
6. all cycle products close;
7. the graph has sufficient distance for the declared fault task;
8. source lineage, execution, and completion are established.

## Disposition

The finite gauge-synchronization DPC is closed. The new common object is a noisy
network of relative references, not one absolute orientation vector. Flavor now
has a source-level candidate tagged process but lacks its calibrated physical
instrument. Optics has exact (Z_4) descent but still requires a physical phase
lineage and selector when its reference torsor is nontrivial.

Verification is provided by
`research/nima/checkers/check_noisy_reference_synchronization.py` and
`research/nima/results/noisy-reference-synchronization.json`.
