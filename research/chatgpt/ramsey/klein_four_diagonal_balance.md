# Adding diagonal balance to local Klein-four closure

## Added condition

Retain the first audit's mixed-wedge square:

- xa and by are red;
- xb and ay are blue;
- x,a,b,y are distinct.

Add **diagonal balance**:

> The remaining comparisons xy and ab must have opposite colors, for every such square.

The involutions r=(x a)(b y) and b=(x b)(a y) each exchange these two diagonals; their product preserves each diagonal. Thus the diagonal colors carry the nontrivial character χ(r)=χ(b)=−1, χ(rb)=+1. This is an extra coloring/phase axiom. The Klein-four group relations alone do not imply it, and it has not been derived from native Marici operations.

For the five-cycle, the diagonals of each alternating square have opposite colors. For the six-node red-perfect-matching counterexample, both diagonals are blue, so it is rejected.

Equivalent graph formulation: the red graph contains neither an induced C4 nor an induced 2K2. Equal red diagonals produce a red C4; equal blue diagonals produce red 2K2. Conversely either forbidden induced graph supplies an alternating square with equal diagonal colors.

## Exhaustive rerun

All labeled two-colorings of K3, K4, K5, K6 were checked: 33,864 colorings. The original checker and evidence were preserved.

| n | Triangle-free colorings | Previous unique-square rule | Unique squares + diagonal balance |
|---|---:|---:|---:|
| 3 | 6 | 0 | 0 |
| 4 | 18 | 6 | 0 |
| 5 | 12 | 12 | 12 |
| 6 | 0 | 30 | 0 |

The extra condition eliminates all 30 six-node false positives and retains all 12 critical five-cycle colorings. Requiring square **existence** rather than uniqueness gives exactly the same augmented result; uniqueness becomes redundant.

Every one of the 32 ways to attach a sixth vertex to a fixed C5 was also checked. Only the all-red and all-blue attachments preserve diagonal balance, and both violate mixed-wedge square existence.

**Important limitation:** this is not an exact test for triangle avoidance on arbitrary sizes. It rejects all 18 valid four-node colorings. It selects a closed critical carrier rather than every admissible partial coloring.

## General theorem: this rule rigidly selects C5

Let a nonempty finite complete graph be colored red/blue. Assume:

1. Both colors occur at every vertex.
2. Every mixed wedge closes into an alternating square on four distinct vertices.
3. Every alternating square has opposite-colored diagonals.

Then the red graph is exactly C5 and the blue graph its complementary C5. Conversely, this coloring satisfies all three assumptions, with unique completions.

### 1. Closure and balance force an induced C5

Start with any alternating square x,a,y,b. By swapping the role names if necessary, its red edges are xa, xy, yb, while ay, xb, ab are blue: the induced red path is a–x–y–b.

Apply square closure to the mixed wedge a–red–x and a–blue–b. Its completion z satisfies xz blue and bz red. It cannot be y, since xy is red, so z is a new fifth vertex.

Diagonal balance in the square a,x,z,b forces az red because xb is blue. Finally yz must be blue: otherwise a–x–y–z–a is an induced red C4, forbidden by diagonal balance.

The induced red graph on a,x,y,b,z is therefore exactly the cycle a–x–y–b–z–a.

### 2. Any vertex outside that C5 must be monochromatically attached

Write S for its red-neighbor set in the cycle. Diagonal balance is invariant under swapping red and blue, and the complement of C5 is another C5, so it suffices to consider |S|≤2.

- |S|=1: label its neighbor 0 around the cycle. Together with the cycle edge 2–3, the edge u–0 gives an induced red 2K2.
- |S|=2 with adjacent neighbors, labeled 0,1: again {u,0,2,3} induces red 2K2.
- |S|=2 with nonadjacent neighbors, labeled 0,2: {u,0,1,2} induces red C4.

Thus only |S|=0 or 5 is possible. The checker independently enumerates all 32 attachments and confirms this lemma.

### 3. No outside vertices can survive square closure

Partition outside vertices into K (red to all five cycle vertices) and I (blue to all five).

Every pair in K must be red: a blue pair in K together with a blue pair in the cycle would induce a red C4. Every pair in I must be blue: a red pair in I together with a red cycle edge would induce red 2K2.

If k∈K, choose cycle vertices x,b with xb blue. The mixed wedge x–red–k and x–blue–b needs y such that ky is blue and by red. No y exists:

- y in the cycle or K has ky red;
- y in I has by blue.

If i∈I, choose cycle vertices x,a with xa red. The mixed wedge x–red–a and x–blue–i needs y such that ay is blue and iy red. Again no y exists:

- y in the cycle or I has iy blue;
- y in K has ay red.

Hence K=I=∅. The whole graph is the five-cycle already constructed. This proof does not depend on uniqueness or on the finite enumeration.

## Interpretation for the conjecture

The added axiom produces a genuine rigidity result: local Klein-four squares plus this diagonal color character force a five-node closed carrier, with no six-node extension.

It does **not** establish that Ramsey numbers generally arise from growing Klein-four node requirements. The rule admits only C5, at any size. To claim an independent proof of the Ramsey threshold from this carrier mechanism, one would need a separately justified bridge from arbitrary triangle-avoiding colorings to an appropriate closed carrier. Triangle avoidance alone does not imply these axioms on the original vertex set, as K4 demonstrates.

Cut invariance is also not recovered: deleting a vertex of the carrier destroys square closure. A completed-carrier notion, rather than literal preservation under vertex deletion, would have to be defined and justified.

## Reproduction

```sh
python research/chatgpt/ramsey/check_klein_four_diagonal_balance.py
```

Evidence: `klein_four_diagonal_balance_results.json`. It contains confusion counts, explicit rejected matching squares, all C5 attachment tests, and a triangle-free four-node counterexample to interpreting this rule as general Ramsey avoidance. The computation checks finite cases; the argument above proves the all-size rigidity statement.
