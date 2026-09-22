# Source-bound merge languages have a verified common refinement

## Frozen domain

Use the current independently replayed P,A,B,AB primitive-evidence states for one frozen middle-threshold input and one analytical source object. A retains theta refinement; B retains signed pairing refinement. Each source derivation maps a continuation letter to its actual bound primitive package, with composition interpreted as coordinatewise intersection.

This test uses the separately rebound branch contract in `results/continuation-quotient/`. It preserves the original historical contract. Analytical soundness of primitive bounds remains supplied by their owning proofs.

## Complete finite closure

The A-only semantic continuation monoid is {identity,A}; the B-only monoid is {identity,B}. Their shared semantic continuation is identity, also implemented by merging the common ancestor P. Their common closure is exactly {identity,A,B,AB}.

Every one of the 16 mixed products is verified against intersection of its independently bound primitive packages. All intersections are nonempty. The checker verifies all 64 associativity instances, A and B idempotence, and AB=BA. Because this set is closed, arbitrary finite continuation words reduce to these four semantic actions; bounded word sampling is not the sole evidence.

Overlap agreement in this example is only agreement on identity. The nontrivial content is mixed composition and common observer descent, not a general nontrivial-overlap theorem.

## Observer comparison

The minimal A-only observer partitions states as {P,A}, {B}, {AB}. The B-only observer partitions them as {P,B}, {A}, {AB}. The common observer distinguishes all four states.

Explicit projections from the common observer to both local observers are exported. All 16 relevant transition squares commute. Moreover, the pair of local observer values distinguishes all four common states: the common equivalence is exactly the intersection of the two local equivalences in this example.

Thus the locally erased distinctions complement one another when observations concern the same retained evidence state. This does not authorize combining local states from different evidence histories without joint admission.

## DPC disposition

Corroborated on this closed finite source-bound family: the two languages have compatible source semantics, a closed joint composition law, and a common continuation observer with verified projections. The source-compatible evidence intersections also establish joint executability as evidence merges for this particular pair.

The construction does not claim that arbitrary same-source branches have a common executable extension, nor that mixing the separately bound midpoint ladder with this frozen input is admitted. It supplies no physical execution guarantee or universal finite-state bound.

## Reproduction

    uv run --with python-flint python research/voevodsky/checkers/check_common_continuation_refinement.py

Artifact: `results/continuation-quotient/common-continuation-refinement.json`.
