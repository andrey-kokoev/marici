# Frozen-rule transfer test: R(3,4)

## Scope

Red triangles and blue K4s are forbidden. The previous balanced-square rule is kept unchanged and evaluated, not retuned. The enumeration and derivations below distinguish necessary consequences of Ramsey avoidance from extra carrier axioms.

## 1. An asymmetric square constraint that can actually be derived

For the mixed wedge x–red–a and x–blue–b, let

C(x;a,b) = { y distinct from x,a,b : ay is blue and by is red }.

Every pair of vertices in C must be blue: otherwise that pair together with b is a red triangle. Also every vertex of C is blue to a. Therefore {a} ∪ C is a blue clique.

For a coloring with no red triangle and no blue K_t, this proves

**|C(x;a,b)| ≤ t−2.**

Thus the independently derived necessary capacity changes from **at most one completion** for (3,3) to **at most two completions** for (3,4). No desired value of the Ramsey number is inserted into this rule.

This is an upper bound, not a demand that completions exist. Existence fails in some valid small colorings. Nor is this bound sufficient: red perfect matchings on arbitrarily many even vertices have exactly one completion per mixed wedge but arbitrarily large blue cliques. The checker includes a ten-node matching with an explicit blue K4.

## 2. Exhaustive extension enumeration

A graph is encoded by red adjacency bitmasks. Starting with the empty graph, try every possible red neighborhood of each new vertex. An extension is valid exactly when:

- its red neighborhood is independent in red, preventing every new red triangle;
- its blue neighborhood contains no blue triangle, preventing every new blue K4.

Deleting the last labeled vertex of any valid coloring gives a unique valid parent. Consequently this process enumerates **all labeled admissible colorings**, not a sample or a selected symmetry family. Invalid branches are pruned immediately. Every accepted eight-node coloring is also independently checked by enumerating its triples and quadruples.

| Nodes | Admissible labeled colorings |
|---|---:|
| 1 | 1 |
| 2 | 2 |
| 3 | 7 |
| 4 | 40 |
| 5 | 322 |
| 6 | 2,812 |
| 7 | 13,842 |
| 8 | **17,640** |
| 9 | **0** |

All 17,640 eight-node colorings have red degrees 2 or 3:

| Red-degree multiset | Colorings |
|---|---:|
| 2,2,2,2,3,3,3,3 | 5,040 |
| 2,2,3,3,3,3,3,3 | 10,080 |
| 3,3,3,3,3,3,3,3 | 2,520 |

These are degree-profile counts; the checker does not claim an independent isomorphism classification.

## 3. The frozen Klein-four rule fails transfer

Among the 17,640 critical eight-node colorings:

- **17,640** satisfy local square existence;
- **0** satisfy unique completion;
- **0** satisfy diagonal balance;
- **0** satisfy the frozen balanced-square rule.

Every mixed wedge has either one or two completions, exactly respecting the derived upper bound. The multiplicities per degree-profile representative are:

| Red edges | Wedges with one completion | Wedges with two completions |
|---|---:|---:|
| 10 | 40 | 48 |
| 11 | 32 | 60 |
| 12 | 16 | 80 |

### No pointwise diagonal-color replacement can rescue this

Take the explicit eight-node Wagner graph: the red edges are the eight-cycle plus its four antipodal chords. Blue is its complement. This is a valid (3,4) coloring.

Its alternating squares have:

- 32 opposite-color (RB) diagonal pairs;
- 8 red/red (RR) diagonal pairs;
- 4 blue/blue (BB) diagonal pairs.

Every diagonal-color type therefore occurs in a **single** critical witness. Any universally necessary rule based only on which of these three diagonal patterns is allowed must allow all three. An asymmetric rule would have to use more context—shared neighborhoods, completion multiplicities, or overlap incidence—not merely a different permitted diagonal color.

## 4. Where the previous pentagon survives

For every vertex x, the blue neighborhood B(x) avoids both red and blue triangles: red triangles are globally forbidden, while a blue triangle in B(x) would form a blue K4 with x.

In an eight-node critical coloring:

- if d_R(x)=2, then |B(x)|=5, and B(x) is a red/blue C5. The earlier balanced-square structure appears **inside this link**;
- if d_R(x)=3, then |B(x)|=4. The enumerated red link is P4 or 2K2, not a closed five-cycle.

Across the entire labeled census there are 40,320 five-node C5 links, 60,480 four-node P4 links, and 40,320 four-node 2K2 links. These counts are vertex occurrences, not distinct unlabelled structures.

The cubic Wagner witness has no five-node blue neighborhood. Thus the C5-link observation cannot be promoted into a universal assertion that every critical eight-node graph contains this particular closed carrier as a vertex link.

## 5. The nine-node obstruction, derived without a tuned carrier rule

The standard asymmetric neighborhood argument gives a short proof:

1. The red neighbors of any vertex form a blue clique. Therefore d_R≤3.
2. Its blue neighborhood is (3,3)-admissible. Since R(3,3)=6, d_B≤5.
3. On nine vertices d_R+d_B=8, forcing d_R=3 at every vertex.
4. Nine vertices of red degree three have total red degree 27, impossible by the handshake lemma.

So no nine-node (3,4) coloring exists.

For the lower bound, the Wagner graph is triangle-free: the cycle has no triangles, its antipodal chords are disjoint, and no chord closes a two-edge cycle path. Any independent four-set in its underlying C8 would have to be one of the two alternating vertex classes; the antipodal chords destroy both possibilities. Its red independence number is therefore three. This supplies an eight-node witness and proves R(3,4)=9.

This is the standard Ramsey neighborhood/parity mechanism. The computation checks it; no new Klein-four proof of the bound is claimed.

## Verdict

The transfer test rejects **fixed diagonal balance** as a general Ramsey mechanism. A more defensible surviving lead is **completion multiplicity plus overlap**: the allowable local square-completion capacity changes from one to two under the asymmetric forbidden-clique condition, and the critical eight-node objects saturate existence while using both multiplicities.

But local completion capacity is still insufficient, as the unbounded matching family proves. The necessary next object would couple these local completion sets to the shared blue-neighborhood constraints. Without an independent compatibility law for that coupling, calling the Ramsey threshold “Klein-four node growth” remains a conjectural interpretation, not an explanation.

## Reproduction

```sh
python research/chatgpt/ramsey/check_klein_four_ramsey34.py
```

Machine-readable evidence: `klein_four_ramsey34_results.json`. The earlier (3,3) checkers and evidence are unchanged.
