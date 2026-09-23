# Compact audit query access does not imply audit-preserving transport

## Frozen extension

Extend the owning normalized tail family's mathematical query language by rational threshold audits of h=t_0. This is a separate prototype; it does not modify Nima's runtime admission contract. Fix an observable boundary (U,V) and ask which h values are feasible, which threshold predicates are possible, and which are forced. Assume m>=3.

Fixing h reduces the source problem exactly to

    (U-h,V-h) = sum_(j>=1) t_j (1,128^-j),
    0<=t_j<=100+2j, 0<=h<=100.

Thus one audit retains a residual generator rather than requiring a stored original polygon.

## Exact query mechanism

For each residual generator slope q_j, the normals +( -q_j,1) and -( -q_j,1) give the two corresponding support inequalities. Their exact bounds are sums of positive generator contributions. These are the edge normals of the two-dimensional residual zonotope: as a support direction rotates, its maximizing source corner changes only when it becomes perpendicular to a generator. Their intersection therefore describes the whole residual polygon.

Substitute (U-h,V-h) into each inequality and intersect the resulting scalar bounds with [0,100]. This yields exactly an interval [lo,hi], or emptiness. The implementation streams the inequalities and records the active bounds rather than storing a polygon. It currently materializes O(m) coefficient and witness arrays and computes each support sum directly, taking O(m^2) rational operations overall; this is not a constant-memory or fast-query implementation claim.

For nonempty fibers:

- h<=r is possible iff lo<=r;
- h<=r is forced iff hi<=r;
- additional accepted scalar bounds restrict the interval by intersection;
- minimizing/maximizing h returns lo/hi with their source support bounds.

Endpoint source witnesses come from greedy residual profiles and convex interpolation. The active inequalities bound all possible h; matching feasible endpoint witnesses certify sharpness. Empty fibers must be reported as empty rather than silently treating universal predicates as informative answers.

## Exact separation from transport

At m=3, take the strictly interior source points

    x=(20,30,40), y=(70,30,40).

Their corresponding observable fibers have exact h intervals

    [315/16, 870/43],
    [1115/16, 3020/43].

The intervals are disjoint. The rational threshold 61865/1376 lies between them: every witness in the first fiber satisfies it, and every witness in the second violates it. No audit-preserving map from the first nonempty fiber into the second exists, despite exact generator-based query access to both. This is a comparison between two fibers on the owning source, not a claim that these particular boundaries form a commuting saturation diamond.

The two original source points certify that this is not merely a zero-mass or full-cap tip degeneracy. The checker also verifies simpler extreme-slice controls with singleton audit fibers {0} and {50}.

## Scope and verification

The exact checker constructs 75 feasible lifts at lower, middle and upper audit values for m=3,4,8,16,64, retaining active support bounds. The continuum interval characterization rests on residual zonotope geometry and the source decomposition, not sampling. There is not yet a separate independent packet verifier or a fresh replay of upstream all-m analytical admission in this prototype.

This implements audit-conditioned feasibility and audit optimization at a fixed observable boundary. It does not yet implement global observable optimization subject to arbitrary persistent audit/observable histories, nor actual-source inference. Returning one h witness does not determine the unknown actual h.

## Structural consequence

A query language can become richer while a generative presentation still answers it exactly. That does not create witness interchange: query access describes each fiber's admitted audits, and may certify that their audit profiles are incompatible.

Presentation size, query work, retained evidence, and comparison structure are independent obligations. Here avoiding a stored facet table shifts work into streamed support calculations; the active query certificate is small in number of rows, but its rational bit size is not bounded.

## Reproduction

    python research/voevodsky/checkers/check_audited_tail_fibers.py

Artifact: `results/audited-tail-fibers.json`.
