# Partial-orbit completion test: what the Ramsey generator still lacks

Date: 2026-11-09. Status: exact finite tests and a conditional selection rule; no universal successor theorem and no general formula for R(3,k).

## Question

Can a successor be selected without a prescribed target size by maximizing compatible partial symmetry-orbit completion? A useful test requires distinguishing (i) local Ramsey admissibility, (ii) branch terminality, (iii) symmetry-orbit choice, and (iv) maximum attainable extension size.

For a triangle-free red graph G and parameter k, a new vertex with red neighborhood S is admissible exactly when S is independent and alpha(G-S) <= k-2. The red adjacency matrix is A. Two old support vectors x,y have cross-incidence x^T A y, which is not determined by their intersection x^T y.

## Test A: the smallest counterexample to greedy terminal completion

Take G=C5 on old vertices 0,...,4, with red cycle edges i~i+1 (mod 5). Raise the parameter to k=4. Add a new vertex a=5 whose only old red neighbor is vertex 0. Then add b=6, red adjacent to a and to one old vertex i, i in {1,2,3,4}. Each of the four seven-vertex graphs is triangle-free and has alpha=3.

| Second old contact i | A[0,i] | Independent red neighborhoods for an eighth vertex |
|---:|---:|---:|
| 1 | 1 | 0 |
| 2 | 0 | 2 |
| 3 | 0 | 2 |
| 4 | 1 | 0 |

These are two stabilizer orbits under the dihedral symmetry of C5 fixing vertex 0: nearby contacts {1,4} and distant contacts {2,3}. Both make legal intermediate states. One orbit is terminal at seven vertices; the other can extend to eight. An explicit eighth-vertex red neighborhood in the i=2 branch is {1,3,5}.

Full enumeration from C5 using all admissible single-vertex neighborhoods, modulo graph isomorphism, gives:

| Current order | Nonisomorphic C5 descendants | Terminal | Extendible |
|---:|---:|---:|---:|
| 5 | 1 | 0 | 1 |
| 6 | 3 | 0 | 3 |
| 7 | 8 | 4 | 4 |
| 8 | 3 | 3 | 0 |

Therefore "continue until no admissible extension" does not determine the largest graph. Choosing an inclusion-maximal partial completion is insufficient. Choosing the maximum-length completion instead simply reintroduces the global search objective.

The first informative additional matrix observable in this fixture is x^T A y: the old-support indicators x=e_0 and y=e_i have equal sizes and zero intersection for every i, but x^T A y distinguishes the two future behaviors exactly.

## Test B: an independently observed cross-phase selector at 13 -> 17

Take G=C13(+/-1,+/-5), sigma(v)=5v mod 13. The twelve nonzero old vertices form three sigma-cycles of length four. Choose one seed vertex from each cycle, subject to independence, and let s_t be the indicator of sigma^t(S). Attach four vertices with neighborhoods s_0,...,s_3 and an internal red C4.

The transversals form five orbits of independent seeds modulo sigma. Compute

a = s_0^T A s_1,  b = s_0^T A s_2.

| Seed orbit representative | a (consecutive) | b (opposite) | Alpha of 17-vertex graph |
|---|---:|---:|---:|
| {1,7,11} | 2 | 7 | 5 |
| {1,4,10} | 3 | 5 | 6 |
| {1,4,11} | 3 | 5 | 6 |
| {1,3,7} | 4 | 3 | 6 |
| {1,7,10} | 4 | 3 | 6 |

Every phase support is independent, and the four supports partition the twelve nonzero vertices. The 13-vertex graph has 26 red edges, four incident to vertex 0, leaving 22 among the twelve. Rotation symmetry therefore yields 4a+2b=22. Exactly the unique class minimizing a has independence number five after attachment, producing four successful labelled seeds in one quarter-turn orbit.

This is an **exact conditional selector** using only the old matrix and the sigma-orbit. It still prescribes a four-vertex orbit and one point from each old length-four orbit. Without that restriction, minimum cross-incidence fails: of the 183 independent old subsets, 25 have a=0 and do not yield an admissible four-vertex extension. Thus this experiment does not establish a universal minimization rule.

## What this discriminates

1. Symmetry-orbit counts, neighborhood sizes, and local admissibility do not determine successor capacity. Relative old incidence matters.
2. The bilinear observable x^T A y separates the nearest/distant C5 branches and, within the specified C13 orbit family, selects the unique valid sector.
3. These two finite observations justify investigating phase cross-incidence as a candidate component of a source-defined operation. They do not justify asserting it always selects an extremal extension.
4. Six of the seven known 17-vertex extremal graphs have no order-four automorphism. A universal extension must permit locally defined phase comparisons or other transport beyond global automorphism orbits. Earlier finite tests also showed a minimum-cost compatible blue pair can terminate prematurely, while a higher-cost pair succeeds. Such tests prevent conflating one local optimization rule with a global completeness theorem.

## Next falsifiable conjecture

An incidence-aware phase successor may need a **joint condition**:
(a) compatibility under the old graph's local incidence pairing x^T A y,
(b) conservation/coverage of the inherited phase sectors,
(c) nonextinction of the next admissible-extension frontier.

The first two can be computed from the current matrix and a proposed phase action. The third is a lookahead condition and must be replaced by an actual theorem or a bounded source-owned invariant before the proposed operation deserves to be called a universal generator.

## Reproduction

    python check_ramsey_partial_orbit_selector.py

The script uses Python standard library only and verifies both displayed small comparisons with exact bitset independence-number calculations. The eight-vertex C5 example is constructed explicitly. Complete C5 descendant isomorphism counts were additionally checked against NetworkX graph isomorphism.
