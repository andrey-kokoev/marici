# A compositional port summary for the existing retained path successor

## Structural result

The previous arrival quotient closes under appending a specified future path to a history with fixed starting vertex. The existing `RetainedSuccessorLedger.compose_payloads` asks a stronger question: compose TWO independently supplied, endpoint-typed path families, potentially starting at different vertices.

The final-occurrence summary alone does not descend through that binary constructor. Retaining the starting vertex together with the final occurrence gives an exact composition-compatible summary. This is derived from the existing endpoint rule, not from a guessed interaction or a new path law.

No change was made to `RetainedSuccessorLedger` or its provenance mechanism.

## Why the older summary is insufficient for this new task

Use existing valid paths with unit structural coefficients:

    left = CA,
    right_a = AB BC,
    right_b = DB BC.

Both right operands have the same final occurrence BC. Their starting vertices are A and D. Therefore:

    left * right_a = CA AB BC,
    left * right_b = structurally empty.

Here star denotes chronological left-then-right composition. This difference is visible in the final-occurrence output itself, not just hidden ancestry.

This does not contradict the earlier formal arrival-continuation theorem. That theorem compared histories with the SAME fixed source and target and appended the SAME known continuation. The binary payload constructor accepts a larger interface; erasing a right operand's input port is not allowed merely because its final observation agrees.

## Derived summary and exact square

For a retained family x with coefficients x_p, define

    S(x)[s,e] = sum x_p over paths p starting at s and ending in occurrence e.

The final target of p is already target(e). For nonempty paths, the starting vertex and final occurrence therefore retain the endpoint data needed by the constructor and the desired final-occurrence observation.

Its binary operation is forced by expanding the existing product:

    (S(x) star S(y))[s,f]
      = sum_(e,u with target(e)=u) S(x)[s,e] S(y)[u,f].

Consequently

    S(compose_payloads(x,y)) = S(x) star S(y).

**Derivation:** partition all compatible pairs of original paths by the left starting vertex s, the left final occurrence e, the right starting vertex u, and the right final occurrence f. Compatibility depends only on target(e)=u. The coefficient of each original product is exactly x_p*y_q, so distributivity factors each block into the product of its two sums. No independence assumption, averaging measure, or fitted coefficient is added.

The same expansion proves associativity: a three-factor term has conditions target(e)=u and target(f)=v regardless of bracketing. The exact checker compares both summary bracketings and both existing retained-path bracketings.

This is a homomorphic observation of an already implemented constructor. It does not make the summary a faithful encoding of its operands or assembly histories.

## Do not confuse zero response with absent support

The ledger distinguishes an unavailable composition from a nonempty path family carrying zero coefficients. Signed coefficients may also cancel after aggregation.

The new `PortSummary` keeps both:

- admitted coarse support: which (starting vertex, final occurrence) ports have actual paths;
- the rational coefficient sum at each admitted port, including zero.

Support composes by existence of a compatible intermediate port, independently of numerical cancellation. Coefficients compose by the formula above. Empty dictionaries and zero-valued admitted entries are therefore distinct. Original path multiplicities and construction histories remain in the ledger, not in this coarse support.

## Finite carrier and retained presentations

The unchanged seed has four vertices and six occurrence identities. All24 starting-vertex/final-occurrence ports are reachable; the checker exhibits them within the existing first five stages, whose word counts are6,10,16,26,42.

Twenty-four is the size of this coarse port carrier, NOT a rung number, field census, physical state count, or a universal minimality theorem. Starting-port information is necessary for the exhibited constructor interface; global uniqueness or minimality of this particular encoding is not claimed.

Both existing source-indexed and target-indexed families preserve the summary and the composition square. Coefficients are carried by their actual words during regrouping, not reassigned by flattened group position. This connects the observation to the existing vertical presentation machinery without declaring a new horizontal generator.

The older final-occurrence summary is recovered by summing S(x)[s,e] over s. It is therefore a further observation of this port summary, not an independently invented readout.

## What remains deliberately outside the quotient

One ABC traversal and two ABC traversals have identical source/final summaries but different retained histories. The summary cannot recover them, their lengths, or their assembly trees. Those are separately retained source data and require a finer task interface if observed.

The implementation covers the existing ledger's positive-length homogeneous path families and exact rational coefficients. It handles structurally empty products. It does not add zero-length identity payloads to the ledger or claim a unital algebra on this interface.

Structural support and coefficients also do not by themselves specify which source families a physical experiment may prepare or compose.

## Consequence for the rung programme

We now have two precise existing-operation contracts, rather than one ambiguous use of "descent":

1. Known continuation / arrival-only task: the existing arrival state closes under every typed finite continuation (Agda theorem).
2. Binary composition of independently supplied path families: the source/final-occurrence support-and-coefficient summary closes under the actual retained composition constructor (algebraic identity and exact executable checks).

The second gives an actual operation/readout square and respects existing indexed presentations. It still does not identify this path-family composition with intended T9 or this summary with the original matrix J4. That identification would need to explain which operand families and endpoint policy the rung constructor uses. No reference return or137-row matrix preparation was smuggled into this path-typed interface.

## Verification

    python research/nima/checkers/check_seed_composition_port_summary.py

18 audit checks pass, covering the fresh native path-quotient receipt and source inventory plus:

- the exact old-summary collision;
-1024 singleton basis-pair products from existing stages of lengths1–3;
-81 positive, zero and signed rational family products;
-216 primitive triples and associativity;
- source and target retained regroupings;
- cancellation versus empty-domain support;
- all24 reachable coarse ports;
- a remaining full-history collision.

The36 existing actual-triangle branch-composition checks are freshly rerun. The universal coefficient identity is derived above; finite tests are not presented as a new Agda proof of rational bilinear algebra. The subsequent `seed-composition-port-quotient.md` supplies a freshly checked Agda theorem for all positive paths, binary congruence, and all typed prefix/suffix arrival contexts. Its scope is the path-level operation, not finite coefficient summation.

Artifacts:

- `checkers/seed_composition_port_summary.py`
- `checkers/check_seed_composition_port_summary.py`
- `results/seed-composition-port-summary.json`

No physical dynamics, normalization, schedule, or source-selection claim is made.
