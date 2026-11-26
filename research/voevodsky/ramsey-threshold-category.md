# Ramsey threshold categories, extension constraints, and extremal growth

Status: mathematical specification with finite executable checks. Not a Lean or Rzk proof. Red denotes the first forbidden clique; blue denotes the second. Graphs are finite, complete, undirected, and loopless. The empty graph is allowed. Write M(l,k)=R(l,k)-1 for the maximum admissible order. A maximum witness has maximum order; a maximal witness need only lack a proper extension. Use thresholds at least two unless stated otherwise.

## 1. Threshold change is not graph growth

Let R(l,k) have the admissible colorings as objects and color-preserving injections as arrows. Such injections are induced embeddings because every pair has a color. Identities and composites are those of injections. The threshold grid is a poset category under coordinatewise order. It maps to Cat: relaxing either bound gives a full inclusion, unchanged on vertices and edges. The two inclusions around a grid square commute strictly. Color exchange gives an isomorphism R(l,k) ≅ R(k,l), not in general an automorphism of an individual witness. An antidiagonal step tightens one threshold: neither inclusion generally applies.

In the total category an arrow (p,G) → (q,H) consists of p≤q and an embedding G→H. Composition composes embeddings. For fixed G at p the comma category (I_pq G ↓ R(q)) records actual extensions: maps must commute with the specified copy of G. For a two-step endpoint embedding i:G→H, a factorization through an intermediate threshold r is a choice of induced vertex set U with i(G)⊆U⊆H and H[U] legal at r, up to relabeling of the intermediate object. U=i(G) always works for a relaxation. A *maximum* intermediate is an additional constraint. Maximum objects do not in general map to maximum objects under inclusion.

## 2. Root decomposition, including both colors

In a rooted (l,k+1) graph, write C for the blue neighbors of the root, J for its red neighbors. Then C lies in R(l,k) and J avoids a red (l−1)-clique and a blue (k+1)-clique. A root-preserving embedding restricts to embeddings on each part. In particular H↦C is a functor. To reconstruct H from two legal parts one must still color all cross-edges. For each red clique U in C and red clique V in J with |U|+|V|=l and both nonempty, forbid the assignment making every U×V edge red. Apply the dual rule to blue cliques of total size k+1. These clauses are necessary and sufficient: a forbidden clique either contains the root, stays in one part, or meets both parts. The same crossing-clique rule applies when two sides share a marked seed: include any common seed vertices in the candidate clique, discard candidates with incompatible fixed colors, constrain only the missing cross-edges.

### Exact fiber theorem for l=3

Fix a labeled core C in R(3,k), an indexed set J of size d, and one new root. Each j in J has a red support S_j⊆C. The following conditions characterize the rooted (3,k+1) endpoints with these fixed parts:

1. The root is blue to C and red to J. All edges inside J are blue.
2. Each S_j contains no red edge. Make j red to S_j and blue to its complement in C.
3. For **every blue clique Q in C, including the empty clique**, require

       |Q| + #{j : S_j ∩ Q = ∅} ≤ k.

   Equivalently, at least max(0,d+|Q|−k) supports meet Q. Q empty gives d≤k. No distinctness condition applies to supports.

Proof: A red triangle through j would require a red edge in its support, or a red edge inside J. A blue clique containing the root uses only core vertices besides the root; C excludes a blue k-clique. A blue clique not using the root consists of a blue Q and a subset of the vertices of J that miss Q. Taking all such vertices gives the largest clique with that Q. Conversely, every rooted endpoint yields exactly these data by restriction. Thus labeled support tuples and labeled endpoints are in bijection. With the core fixed pointwise but J unlabeled, quotient by permutations of J (retaining stabilizers if counting a groupoid). To forget the labeling of C as well, also quotient by Aut(C). Do not equate raw counts, orbit counts, and weighted groupoid counts.

Restriction to a smaller induced core intersects every support with that core. Removing members of J deletes the corresponding supports. Both preserve legality. More generally the data map along an embedding when the new supports restrict to the old ones on the image. Arbitrary enlargement of C is not a free operation. For existence at fixed C,d one may enlarge each support to a maximal red-independent set: this cannot reduce a hit. This reduction does not preserve counts or every marked embedding.

## 3. Capacity is an integer feasibility problem

For each maximal support S use a nonnegative integer x_S. Require sum x_S=d and, for every blue Q, sum over S meeting Q of x_S ≥ max(0,d+|Q|−k). This is an exact test of nonemptiness, not just a score. Real nonnegative x_S give a necessary relaxation. Weighted sums of the constraints give necessary counting bounds. If every support hits demands of total weight at most B but the required weighted hits exceed dB, no endpoint exists. Fractional feasibility does not imply integer feasibility. Removing one neighbor preserves legality, so feasible degrees for a fixed core form an initial interval starting at zero. Define cap_k(C) as the last feasible degree.

The exact optimization target is

    M(3,k+1) = 1 + max over C in R(3,k) of ( |C| + cap_k(C) ).

Every feasible tuple constructs a graph. Conversely any nonempty maximum graph has a root and appears in this maximization. Isomorphism representatives suffice; restricting to maximum cores does not. With sigma=M(3,k)−|C| the exact gain is 1+max_C(cap_k(C)−sigma). For a known endpoint of order n, d−sigma=n−1−M(3,k) is an identity, not a predictor. A finite search over only selected cores gives a lower bound unless its exclusions cover every better case.

[Core-first tests](results/ramsey_core_capacity_36.json): for (3,6), one 12-vertex core has a fractional solution of mass 4 but no four whole supports. Other 12-vertex cores admit degree 4. [Minimum certificate](results/ramsey_capacity_minimum.json): 14 blue-clique demands suffice for the failed core and 13 never suffice. These are findings for specified cores.

## 4. Squares: arithmetic versus witnesses

Write A,B,C,E for witnesses at (l,k),(l+1,k),(l,k+1),(l+1,k+1). A commuting witness square requires that both routes send every vertex of A to the same vertex of E. Identify the images in E. Then B∩C is legal at (l,k). If A is maximum and contained in the intersection, B∩C=A. Consequently |E|−|B|−|C|+|A| counts E outside the union. It is the mixed difference of the *maximum orders* only when the four sizes have those values. Shared vertices give an intersection square (a pullback of the two inclusions in the ambient category of colored graphs). A compatible union need not be a categorical pushout: edges between the additions need colors that the two sides do not specify. An optimal common endpoint need not exist for fixed marked sides.

[Positive square](results/ramsey_maximum_square_33.json): 272 pairs in one maximum (4,4) endpoint share a maximum (3,3) seed. [Negative square](results/ramsey_asymmetric_square_all.json): neither symmetry class of matches for the tested (3,5) and (4,4) sides admits a legal (4,5) union over a maximum shared seed. No conclusion about all side types follows without their classification.

## 5. Returning one threshold: a separate optimization

For an endpoint H in R(3,k+1), a deletion returns H to R(3,k) exactly when it meets every blue k-clique. The minimum deletion size is the minimum hitting-set size tau. The best intermediate inside H has order |H|−tau. This intermediate can be larger than the core of a given root. If H is maximum, its order gain from the previous maximum equals tau minus the shortfall of this best intermediate from M(3,k).

A saturated alternating square gives one such demand in R(3,k+1): a red xa and blue xb have at most k−1 common completions y with ay blue and by red. All completions form a blue clique with a. At saturation this gives a blue k-clique. Distinct squares may give the same demand. [Deletion tests](results/ramsey_saturated_square_cuts.json) found the full minimum hit cost using just these demands for the tested representatives. This is not a universal sufficiency theorem. The observed 3+3+1 symmetries do not supply a functor selecting maximum endpoints, a polarity, or an esd_7 realization.

## 6. Test distillation: specify what must survive

On the fixed corpus of 16 order-11 cores at degree five, [all 16 size-class ablations and marked repairs](results/ramsey_test_distillation.json) distinguish three questions. For verdicts, {3,4} is the unique inclusion-minimal sufficient set. For the actual feasible multisets of **maximal** supports, {1,3,4} is the unique inclusion-minimal sufficient set. Equality of counts suffices for this comparison only because removing requirements gives nested witness sets on each core. Neither statement is a universal reduction. For carrying forward a chosen witness, even verdict equivalence is insufficient: repair cost counts changed red/blue edges on the fixed labeled core and five neighbor slots. Mark survival tests protect one complete row or one complete column at a time; they do not assert joint survival or naturality under restriction. The [replay](checkers/ramsey_distill_tests.py) records each exact pass mask, the actual old and new supports, and feasible individual marks. Use held-out cores and timing comparisons before admitting a pruning or speed claim.

## 7. Verification boundary and next use

[Small exhaustive checker](checkers/ramsey_root_fiber_laws.py) compares the support theorem with a direct clique test on all labeled graphs through six vertices, with root 0, and checks restriction of the root split under deletions. [Capacity checker](checkers/ramsey_core_capacity.py) constructs actual endpoint witnesses. The next predictive test must select cores and constraints **without using the target endpoint as input**. One-step and two-step numerical recurrences, including discount and parity corrections, are hypotheses, not consequences of this category.
