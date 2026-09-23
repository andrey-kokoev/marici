# Filling restrictions separate existence from witness uniqueness

## Independently frozen square

Use the source-admitted 70-state behavioral runtime packet, freshly independently verified. Let W consist of its behavioral witnesses with discrete identity. Declare four boundary coordinates:

- a: source-only local observer value;
- b: acquisition-only local observer value;
- c: recipient-only local observer value;
- d: retained origin bit.

Construct edge relations as exact pair images: u=(a,b), v=(b,c), x=(a,d), w=(d,c). Each edge here retains existential membership, with a unit witness. This is a newly declared square on actual existing source observations, not a claim that the four vertices are interchangeable frames.

For fixed a,c, compare the filling pencil (all b,d and their source witness) with the independent edge factorizations through b and through d. Globally the restriction maps send each row to (a,b,c) and (a,d,c).

## Complete fiber classification

The uv factorization has 61 boundary triples. Its restriction fibers consist of 52 singletons and nine doubletons. Every pair of edge witnesses lifts, but nine do not determine a unique behavioral witness. Those alternatives are distinguished by the existing origin audits, so no behavioral equivalence between them is silently imposed.

The xw factorization has 1,820 boundary triples. Exactly 70 have a singleton source fiber; the other 1,750 have empty fibers. Sharing the origin bit alone lets unrelated source and recipient observer values be combined.

Thus neither factorization individually gives the claimed equivalence with the filling pencil. One fails uniqueness, the other existence. In this discrete test singleton fibers are contractible and larger fibers are not; no nontrivial higher identity structure is supplied.

## Positive four-edge result

Impose all four edge relations on the same boundary tuple (a,b,c,d). Exactly 70 tuples remain, each with one source witness. Hence this particular complete boundary relation is exactly the source image and reconstructs the behavioral filling.

The complementary factorizations therefore recover the source together even though neither separately presents its filling pencils. This is an exact checked gluing property of these boundaries. Pairwise reconstruction is not valid for arbitrary source constraints, as the parity obstruction already showed.

## Structural consequence

A quarter-turn can exchange two different losses: a nonempty ambiguous fiber and an empty candidate fiber. Rotating a diagram alone cannot identify them. The comparison with the actual filling space reveals the difference.

The positive object in this instance is the jointly constrained four-boundary relation, with its unique behavioral filling witness. It is a 70-state representation, not a reconstruction of 638 concrete execution histories or an authorized inverse execution.

## Reproduction

    python research/voevodsky/checkers/check_filling_restriction_fibers.py

Artifacts:

- `results/filling-restriction-fibers-contract.json`
- `results/filling-restriction-fibers.json`
