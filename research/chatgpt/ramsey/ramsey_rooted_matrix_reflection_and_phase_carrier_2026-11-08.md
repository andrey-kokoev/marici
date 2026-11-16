# Rooted reflection and source-generated phase carriers for the original Ramsey rows

8 November 2026. Exact matrix/row audit of the initial symbolic construction for `k=3,...,10`; algebraic proofs for all row lengths. Companion executable: `ramsey_original_matrix_sector_audit.py`.

## Initial records and the embedding question

The original symbolic row is

`x_k = (R,G,R,G,..., two final zero slots)`.

Here `R`, `G`, and `0` are *symbolic*. When discussing linear algebra below we explicitly encode `R=+1`, `G=-1`, `0=0`. No part of the original process establishes that this row is automatically a red-edge adjacency row of a graph with k vertices. We test that **candidate embedding** separately, and never infer a Ramsey threshold from a row count.

## The source-selected reflection

Positions are indexed `0,...,k-1`. The final two zero slots have indices `k-2,k-1`. Their midpoint gives a canonical index reflection

`H_k(j)=k-3-j (mod k)`.

It interchanges the two zero positions. On the colored prefix `0,...,k-3`, it reverses the alternating word. Therefore

- odd `k`: `H_k x_k=x_k`;
- even `k`: `H_k x_k=τ x_k`, where `τ` exchanges `R` and `G` and leaves `0` fixed.

In the real contrast encoding this is the single identity

`H_k x_k = (-1)^(k+1) x_k`.

This holds for **every** `k>=3`. The color interchange is a symmetry of the *symbolic primitive*, not automatically a red/blue symmetry of the asymmetric Ramsey problem `(3,k)`.

## Pivot/axis formation law

If the colored position `p` is treated as the diagonal/root of a proposed circulant adjacency matrix, reflection about `p` requires that the specified colors at offsets `+d` and `-d` agree whenever neither is `0`. Exactly:

- for even `k`, every colored root `p=0,...,k-3` is compatible;
- for odd `k>=5`, only `p=(k-5)/2,(k-3)/2,(k-1)/2` work;
- for `k=3`, only `p=0` is available.

**Proof:** `i,j` paired about `p` satisfy `i+j ≡ 2p (mod k)`. Their colors differ precisely when `i,j` have opposite parity. If `k` is even, every admissible sum `i+j=2p` modulo `k` has even parity; no conflict. For odd `k`, a parity mismatch occurs exactly on an odd-wrap sum `i+j=2p±k`. With `0<=i,j<=k-3`, the absence of either type is equivalent to `2p<k` and `2p+n>2(k-3)`, where `n=k`, hence `(k-5)/2<=p<k/2`. The claimed three integers follow. A pair with the relevant odd sum always exists when either inequality fails, so these are necessary as well as sufficient.

The three compatible roots for odd `k` are **three reflection-center choices**, not three independent spatial rotation axes.

## Full-space square-root obstruction

For the selected reflection `H_k`, the dimension of its `-1` eigenspace is `t=floor(k/2)`. A **real matrix on all k coordinates** satisfying `P²=H_k` exists exactly when `t` is even: each `-1` plane requires a real complex structure, and these planes pair into two-dimensional 90° blocks. Thus a full-space real root exists iff `k ≡ 0,1 (mod 4)`.

| k | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |
|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| negative dimension t | 1 | 2 | 2 | 3 | 3 | 4 | 4 | 5 |
| whole-space real root? | no | yes | yes | no | no | yes | yes | no |

When `t` is odd, `det H_k=-1`, while `det(P²)>=0` for real `P`. The minimum *whole-space* augmentation making a real root possible is one extra `-1` direction. The complex Fourier transform supplies a complex square root without augmentation. **This obstruction concerns the full k-dimensional carrier. It is not required for the restricted source carrier below.**

## Four phases without requiring a root on every coordinate

Define three explicit real vectors (using standard coordinate vectors `e_j`):

- `x`: the signed colored row, with alternating ±1 followed by two 0s;
- `a=e_(k-2)-e_(k-1)`: **oriented empty-pair contrast**;
- `b=e_0-e_(k-3)`: colored-prefix endpoint contrast (`k>=4`).

The intrinsic reflection sends `a -> -a`, `b -> -b`. It sends `x -> -x` for even `k` and `x -> x` for odd `k`.

**Even `k>=4`:** `x` and `a` are nonzero orthogonal `-1` eigenvectors of `H_k`, with squared norms `k-2` and `2`. On their two-dimensional span let `u=x/sqrt(k-2)`, `v=a/sqrt(2)` and define a real quarter-turn `P(u)=v`, `P(v)=-u`. Then `P²=H_k` **on this span**, and the row has four distinct coefficient phases:

`x -> sqrt((k-2)/2) a -> -x -> -sqrt((k-2)/2) a -> x`.

**Odd `k>=5`:** the three vectors `x,a,b` are pairwise orthogonal. The row `x` is fixed by `H_k`, while `a,b` span a `-1` plane. Define `P(x)=x`, `P(a)=b`, `P(b)=-a`. Then `P²=H_k` **on the three-dimensional span** and the retained state has four phases:

`x+a -> x+b -> x-a -> x-b -> x+a`.

This second case explains why the unmarked odd-k row collapsed to two phases under a whole-space permutation square root: its `x` component was fixed and the orientation of the two empty slots was not retained. The phase is restored by retaining `a`. The coefficient phases `x±a` and `x±b` are not automatically valid R/G/0 edge-coloring rows.

The `k=3` case is degenerate because `b=e_0-e_0=0`; this particular source-generated two-plane is not available.

These are exact universal phase-carrier identities for the symbolic primitive. They do **not** prove a Ramsey threshold formula.

## Optional circulant graph test (explicit hypothesis)

Treat one colored slot as a diagonal marker; other `R/G` values as specified edges to that vertex; `0` as an unassigned edge; complete all rows by cyclic translation. Evaluate both choices of which symbol denotes red, because `R/G` were not assigned Ramsey meanings by the algebraic primitive.

| k | compatible root positions | roots allowing valid graph if R=red | roots allowing valid graph if G=red |
|--:|---|---|---|
| 3 | 0 | none | none |
| 4 | 0,1 | 0,1 | 0,1 |
| 5 | 0,1,2 | 0,1,2 | 0,1,2 |
| 6 | 0,1,2,3 | 1,3 | 0,2 |
| 7 | 1,2,3 | 2 | 1,2,3 |
| 8 | 0,1,2,3,4,5 | 1,2,3,5 | 0,2,3,4 |
| 9 | 2,3,4 | none | 3 |
| 10 | 0,...,7 | 1,3,5,7 | 0,2,4,6 |

Validity here means triangle-free red graph with independent-set size `alpha<k` on **k vertices**. These are not extremal Ramsey witnesses. For example, at `k=9`, shifting the root to `p=3` repairs symmetric incidence, but only the `G=red` interpretation of the completed circulant graph passes the triangle test. The original row was not required to define a circulant matrix, so no impossibility conclusion transfers to unrestricted Ramsey colorings.

## Full-graph matrix check: one real Ramsey success

The known source-derived orbit constructor begins with the 13-vertex red graph `C13(±1,±5)` and its true order-four automorphism `σ(j)=5j (mod 13)`. Its seed `S={1,7,11}` generates four disjoint independent red neighborhoods

`{1,7,11}`, `{3,5,9}`, `{2,6,12}`, `{4,8,10}`.

Writing `X=[1_S,1_σS,1_σ²S,1_σ³S]` and taking the new internal graph to be a red `C4`, the complete 17-vertex adjacency matrix is

`A17 = [[A13,X],[X^T,C4]]`.

The exact checker confirms triangle-freeness, 42 red edges and `alpha(A17)=5`, providing the valid lower-bound witness `R(3,6)>=18`. This construction lives on a **13-vertex graph** and is distinct from the symbolic length-6 row test.

For arbitrary `A,X,C`, the triangle expression is

`tr([[A,X],[X^T,C]]^3) = tr(A³) + 3tr(X^T A X) + 3tr(C X^T X) + tr(C³)`.

Its vanishing is equivalent to triangle-freeness for a nonnegative 0/1 adjacency matrix; the complementary blue clique condition must be checked separately.

## Status and discriminating next target

We have recovered exact parity-sensitive reflection, compatible moving roots, an intrinsic two-/three-dimensional real quarter-turn carrier, and one genuinely Ramsey-admissible block extension. These identities are not fitted to Ramsey thresholds.

**Next discriminator:** define an incidence-preserving map from the source phase carrier `(x,a,b)` to the full red adjacency graph, and test whether phase orientation `a` changes the available neighborhood blocks `X` or only their presentation. If it acts only on presentations, it cannot explain new Ramsey vertices. If it determines a compatible new block without fitted sector size, it is a candidate part of the missing Ramsey successor operation.
