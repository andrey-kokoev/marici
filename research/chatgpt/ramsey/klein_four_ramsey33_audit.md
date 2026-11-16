# Klein-four node sharing: first exhaustive R(3,3) test

## Question and status

Can growth in nodes required by compatible local Klein-four structures explain the five-to-six threshold R(3,3)=6?

**Result:** a natural local commuting-square rule has a striking match at five vertices, and the five-cycle cannot extend to six while retaining unique square completion. However, the rule admits other six-vertex colorings with monochromatic triangles. It therefore does **not** explain the Ramsey threshold universally. This tests one explicitly selected candidate, not every possible formulation of the user's conjecture or a native Marici construction.

## The tested node-sharing rule

For a red/blue coloring of a complete graph, require both colors at every vertex (excluding vacuous monochromatic examples). For every mixed wedge

- x —red— a,
- x —blue— b,

require a fourth, distinct vertex y with

- a —blue— y,
- b —red— y.

On these four vertices define

r = (x a)(b y), b = (x b)(a y).

Then r²=b²=1 and rb=br; the action is free and transitive on the four-state square. The checker verifies these identities directly for the named five- and six-vertex examples.

Two candidate rules are tested:

1. **Existence:** every mixed wedge has at least one completion.
2. **Uniqueness:** every mixed wedge has exactly one completion.

Nodes may be shared across squares. The uniqueness version removes arbitrary choices in completing a wedge. Neither rule assumes that an involution acts globally on the entire graph or preserves the square's diagonal colors. In fact, they only specify two-color moves along its perimeter. They do not yet enforce all higher overlap or cut compatibility conditions.

## Exhaustive enumeration

All 33,856 labeled colorings of K4, K5 and K6 were checked, without symmetry reduction.

| n | All colorings | No monochromatic triangle | Existence passes | Unique completion passes |
|---|---:|---:|---:|---:|
| 4 | 64 | 18 | 6 | 6 |
| 5 | 1,024 | 12 | 32 | 12 |
| 6 | 32,768 | 0 | 650 | 30 |

At n=4 the rule misses 12 triangle-free colorings. At n=5 **unique completion selects exactly the 12 labeled five-cycle colorings**, with no false positives or negatives. At n=6 it accepts 30 false positives.

### The positive five-cycle result

Take red edges (0,1),(1,2),(2,3),(3,4),(4,0), with blue edges the complementary five-cycle. All 20 mixed wedges have a unique completion; there are five alternating four-state squares.

All 32 possible ways of adding a sixth vertex destroy unique completion and create a monochromatic triangle. Ten extensions still satisfy the weaker existence rule. Thus unique-square closure detects the obstruction to extending this particular critical witness.

Deleting any one vertex from the five-cycle destroys even existence closure. Each resulting four-vertex coloring can be repaired with one additional vertex, and all 16 possible attachment patterns are checked. Zero added vertices fail, so the minimum is exactly one. This gives a genuine **four-to-five closure cost**, but the local rule is not cut-invariant on induced pieces.

### The decisive six-vertex counterexample

Color (0,1),(2,3),(4,5) red and every other edge blue. The red graph is a perfect matching; the blue graph is K_{2,2,2} and has eight triangles (choose one endpoint from each red pair).

Every mixed wedge still completes uniquely. If x's red partner is a, and b is any blue neighbor, then y must be b's red partner. The remaining required edge a—y is blue automatically. The six local alternating squares obey the Klein-four laws and share the six existing nodes without requiring a seventh.

The exhaustive audit also checks that **all 30 six-vertex unique-completion examples are precisely the 15 perfect matchings and their color complements**.

So local four-state closure, even with uniqueness, can survive beyond the Ramsey threshold while forbidden triangles already exist. Failure of extending C5 is not equivalent to failure of every six-node realization.

## What remains open

The broad conjecture could still involve an additional, independently motivated compatibility law on overlapping squares. That law must:

- accept the critical C5 coloring;
- reject the perfect-matching/K_{2,2,2} example;
- explain how restrictions/cuts inherit or repair their structures;
- connect to monochromatic-clique avoidance rather than simply restating it.

Demanding two nontrivial global, everywhere color-realized commuting involutions is too strong for this formulation: their orbits would all have four distinct vertices, so a five-node carrier could not satisfy it. An auxiliary carrier or genuinely local structure would be necessary.

**Next useful target:** identify a source-derived overlap law that fails on the six-vertex matching example but holds on C5. No such law has been proved here.

## Reproduction

```sh
python research/chatgpt/ramsey/check_klein_four_ramsey33.py
```

The standard-library checker writes `klein_four_ramsey33_results.json`, including the complete aggregate census, explicit counterexamples, all five vertex cuts and their one-node repairs, and all 32 extensions of the five-cycle. This is finite computational evidence for the stated rules, not a proof of a general Klein-four/Ramsey correspondence.
