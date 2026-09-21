# Prime-cube faithful observers: paths, relations, and nested reconstruction

## Outcome

The three-prime theta-history-plus-cycle packet reconstructs the linearized free source-path category when each response retains its source, target, and identity coefficient. The seven interval and five cycle coordinates are a minimal linear observation of the full twelve-dimensional edge-chain space.

A four-prime stress test identifies the next missing information: the twenty-four full routes have an eighteen-dimensional edge-chain image. Six independent second-order route-correlation probes complete reconstruction. We construct them, prove the composition law, and verify an exact inverse.

The distinction between free paths and the endpoint quotient is essential throughout. Declaring square-route equalities produces a separate quotient category with a different algebra and different extension theory.

## 1. The actual finite source

Use the three-prime Boolean directed cube with primes (2,3,5), root label 2, and vertices indexed by subsets S of {0,1,2}:

\[
n_S=2\prod_{j\in S}p_j.
\]

An edge adds one unused prime. There are eight vertices and twelve edges. Their ordered numerical labels are 2,4,6,10,12,20,30,60.

Let Q₃ be the directed edge graph. Its free path category has:

- eight objects;
- paths specified by a starting subset and an ordered word of distinct unused prime indices;
- composition by concatenation;
- one empty identity path at each vertex.

There are

\[
\sum_{k=0}^3\binom3k2^{3-k}k!=38
\]

paths, including identities. Its complex-linear path algebra A_free therefore has dimension 38.

The Boolean poset category identifies every pair of parallel paths. Its incidence algebra A_end has dimension 3³=27, one basis element for every comparable endpoint pair. We will exhibit the eleven-dimensional kernel of A_free→A_end.

This source is the retained arithmetic edge cube of the existing forest checker. No independent analytical path relation is assumed.

## 2. The existing forest observer

Let c(p)∈C¹² be the oriented edge-count vector of a path p. Ordering the numerical vertices defines seven consecutive interval atoms. The interval coverage matrix J:C¹²→C⁷ satisfies

\[
\partial=D J,
\]

where ∂ is vertex incidence and D is the injective incidence matrix of the consecutive-vertex path. Thus rank J=7 and ker J=ker ∂ has dimension 5.

A prime priority order chooses a spanning tree by the existing Kruskal rule. Let Z_F select the five remaining edges, and set

\[
C_F=\begin{pmatrix}J\\Z_F\end{pmatrix}.
\]

Fixing chord coefficients reduces recovery to a boundary problem on a tree. Reduced tree incidence and reduced consecutive-path incidence are unimodular. Hence C_F is unimodular, and

\[
c=C_F^{-1}(Jc,Z_Fc).
\tag{1}
\]

Every priority order therefore gives an exact integral coordinate system on the edge space.

### Minimality

Any linear observer containing J and injective on C¹² requires at least five additional scalar coordinates, by rank-nullity. Z_F restricts to an isomorphism on ker J. The five chord probes attain the lower bound. Deleting any one lowers the combined rank to eleven.

This is minimality relative to retaining J on the entire edge space. A fixed endpoint path space has smaller dimension and admits its own reduced observer.

## 3. From edge recovery to path recovery

An invertible edge observer recovers the edge chain of each path. Recovering formal linear combinations of paths additionally requires injectivity on each linearized Hom space.

For endpoints S⊂T, put k=|T\S|. Its path space has dimension k!. For k≤3 the edge-chain columns of all paths are linearly independent:

- k=1: the sole edge is unique;
- k=2: the two orders have different first edges;
- k=3: each of the six paths has a distinct middle edge, between relative levels one and two.

For k=3 the middle edge determines its starting singleton, its added prime, and its ending pair; the first and last steps are then forced. Restriction to these six middle-edge coordinates gives a permutation matrix. This proves independence without numerical rank estimation.

For S=T the sole path is the identity. Its edge chain is zero, so we retain its scalar coefficient separately.

Define the observer category B_F as follows:

- objects: the eight source vertices;
- Hom(S,T), S⊂T: the image under C_F c of the formal source paths;
- Hom(S,S)=C, carrying the identity coefficient;
- all other Hom spaces zero.

The resulting linear maps on Hom spaces are isomorphisms onto their images. Explicitly, if O_ST is the real integer matrix of observed path columns, then

\[
R_{ST}=(O_{ST}^{\mathsf T}O_{ST})^{-1}O_{ST}^{\mathsf T}
\tag{2}
\]

is an exact rational left inverse. Its transpose is ordinary real transpose; linear independence makes the Gram matrix positive definite.

The checker constructs (2) for all twenty-seven comparable endpoint pairs. Every left inverse is exact. The sum of the recovered Hom dimensions is 38.

## 4. Composition on observed packets

For x=Σ_p a_p p in a fixed Hom block, write

\[
\lambda(x)=\sum_p a_p,\qquad c(x)=\sum_p a_pc(p).
\]

For a nonidentity endpoint pair S⊂T,

\[
\partial c(x)=\lambda(x)(e_T-e_S).
\]

Thus λ is recovered from c, or from its interval boundary. On the identity block λ is the separately retained unit coefficient.

If x:S→T and y:T→U, bilinear path concatenation gives

\[
\lambda(y\circ x)=\lambda(y)\lambda(x),
\]

\[
c(y\circ x)=\lambda(y)c(x)+\lambda(x)c(y).
\tag{3}
\]

For individual paths this is addition of edge chains. Formula (3) handles arbitrary signed or complex linear combinations. It supplies the observer composition law after applying C_F. Unmatched endpoints give zero in the category algebra.

Associativity follows by expanding either triple composite:

\[
c(z\circ y\circ x)
=\lambda(z)\lambda(y)c(x)
+\lambda(z)\lambda(x)c(y)
+\lambda(y)\lambda(x)c(z).
\]

The units have (λ,c)=(1,0). Consequently the observation is a linear-category isomorphism

\[
\boxed{\mathbb C[\operatorname{Path}(Q_3)]\cong B_F.}
\tag{4}
\]

The endpoints are structural indices. A single unlabelled twelve-vector is not the direct sum of these thirty-eight-dimensional Hom spaces.

## 5. Forest changes, braid, and nesting

For two forests F,G, let T_GF=C_G C_F⁻¹. It preserves λ because it preserves all interval coordinates, and therefore respects (3). Thus forest transport extends to an isomorphism of the entire observed path categories, acting as identity on objects and unit scalars.

Cancellation gives

\[
T_{HG}T_{GF}=T_{HF}.
\]

Both adjacent-swap words 121 and 212 carry the same source-labelled path response to the same final forest response. This is an equality of presentation-change functors. Physical prime routes remain distinct source morphisms.

An algebra isomorphism induces an exact equivalence of perfect module categories. Applying any finite sequence of S-constructions preserves that equivalence. Hence

\[
S_{n_1}\cdots S_{n_r}\operatorname{Perf}(A_{free})
\simeq
S_{n_1}\cdots S_{n_r}\operatorname{Perf}(B_F).
\tag{5}
\]

All forest changes commute with interval restrictions, cuts, and reconstruction. This follows from functoriality of exact diagrams, rather than separate matrix fitting at each nesting depth.

Acyclic path algebras are hereditary. Accordingly the free-source module category has Ext^k=0 for k≥2. Higher extension groups arising after imposing relations belong to the corresponding quotient algebra. Nesting depth and extension degree retain their separate meanings.

## 6. The six square relations

Each cube face has two directed length-two routes. Their difference is a nonzero free path combination. Under the edge observer it becomes the signed boundary of that square.

The six face boundaries span the five-dimensional cycle space. In the face order used by the checker, their unique relation has coefficients

\[
(-1,1,-1,1,-1,1).
\]

This is the oriented boundary-of-boundary relation for the cube. It concerns edge chains; its six terms have different endpoint types as path relations. It cannot be read as an equality between those differently typed morphisms.

Inside A_free let I be the two-sided ideal generated by the six square-route differences. Adjacent transpositions connect any two orders of a fixed set of added primes. Each such transposition is one square relation, placed between a source prefix and suffix. Thus all parallel paths become equal modulo I.

It follows that

\[
A_{free}/I\cong A_{end},\qquad \dim I=38-27=11.
\tag{6}
\]

Explicitly, six independent degree-two route differences and five independent full-route differences span the kernel. The checker generates the ideal using every admitted prefix and suffix and obtains rank eleven.

The cycle probes distinguish the free routes. Passing to (6) intentionally identifies them. A source model must specify which of these two categories it intends.

## 7. Four primes: the first route-correlation failure

For four primes, a full bottom-to-top route is a permutation of four indices. There are 24 such routes, 32 cube edges, and 16 vertices.

The linear map from route coefficients to edge chains has rank 18. Here is the general rank argument for a directed cube with d coordinates. All full-path chains satisfy ∂c=λ(e_top−e_bottom), so they lie in a space of dimension

\[
|E|-|V|+2=d2^{d-1}-2^d+2.
\]

Conversely the average of all full paths is strictly positive on every edge. Small perturbations in the fixed-unit-flow affine space remain nonnegative. Every nonnegative unit flow in a finite acyclic graph decomposes into source-to-sink paths, by successively subtracting a positive bottleneck path. Hence the full-path convex hull contains a relatively open subset of that affine space. Its affine dimension is |E|−|V|+1, and its linear span has the asserted dimension.

For d=4 this is 18, giving a six-dimensional kernel. For d=3 it is 6, explaining why the earlier six routes were linearly independent.

An explicit four-prime relation is

\[
c(0123)+c(1032)=c(0132)+c(1023).
\tag{7}
\]

Both sides are positive sums of two different full routes. They have the same endpoints, total coefficient, edge counts, interval history, and every linear cycle observation. An invertible change of forest coordinates preserves this collision.

Equation (7) compares pairing the first two-step order with the last two-step order in two different ways. The missing information is route correlation.

## 8. Minimal second-order completion

For a path p=(e₁,…,e_k), define

\[
S_0(p)=1,\qquad
S_1(p)=\sum_i e_i,\qquad
S_2(p)=\sum_{i<j}e_i\otimes e_j.
\tag{8}
\]

Extend linearly to path combinations. S₂ records the joint occurrence of ordered edges. For a mixture it is a separate linear observable; it cannot generally be recovered from the aggregate S₁.

For a four-step cube path, its two central edges identify the whole path. The first central edge starts at a singleton, determining the first step, and the second ends at a triple, determining the last step. Thus the twenty-four central-edge-pair coordinates of S₂ give a permutation matrix on the twenty-four full routes.

Starting from the eighteen-dimensional edge image, choose independent central-pair rows until the rank reaches 24. Exactly six are required, and six suffice. The deterministic lexicographic rank selection in the checker returns, in mask notation (source mask, target mask, added prime index):

| Probe | First edge | Second edge |
|---|---|---|
| 1 | (1,3,1) | (3,7,2) |
| 2 | (1,5,2) | (5,7,1) |
| 3 | (1,9,3) | (9,11,1) |
| 4 | (2,6,2) | (6,7,0) |
| 5 | (2,10,3) | (10,11,0) |
| 6 | (4,12,3) | (12,13,0) |

For the resulting augmented observation matrix O, the checker verifies

\[
\operatorname{rank}O=24,
\qquad (O^{\mathsf T}O)^{-1}O^{\mathsf T}O=I_{24}.
\]

Minimality follows from the six-dimensional kernel. All other endpoint intervals in the four-cube have at most three added primes, so their linearized path observations were already injective. Retaining endpoints and units, these six added probes therefore complete reconstruction of the entire four-prime free path category.

### Composition law

For individual routes p followed by q, the signature satisfies

\[
S_2(q\circ p)=S_2(p)+S_1(p)\otimes S_1(q)+S_2(q).
\tag{9}
\]

For arbitrary combinations x,y, the correct bilinear formula is

\[
S_2(y\circ x)
=\lambda(y)S_2(x)+S_1(x)\otimes S_1(y)+\lambda(x)S_2(y).
\tag{10}
\]

Every ordered pair either lies inside the prefix, crosses the cut, or lies inside the suffix. This proves (9) and (10). The checker tests (9) on every composable basis-path pair in the four-cube. Bilinearity proves (10) for all coefficients.

For the six selected coordinates, apply the corresponding coordinate functionals to (10). Their cross terms are computable from the retained full edge vectors. Thus the minimal completed observer has its own explicit composition law. Applying the same source-to-image and S-construction arguments as in (4)–(5) yields nested reconstruction for this completed four-prime observer.

## 9. General finite acyclic source theorem

Let Q be any finite acyclic graph with maximum path length L. Form the ordered tensor signature

\[
S(p)=\prod_{j=1}^k(1+e_j)
\in T^{\le L}(\mathbb C^{E(Q)}),
\tag{11}
\]

where multiplication follows chronological order. Retain source and target as Hom indices and extend linearly. The target composition is defined in that same chronological order, so

\[
S(q\circ p)=S(p)S(q).
\]

This identity follows by splitting the product at the composition interface. At degree m it reads

\[
S_m(q\circ p)=\sum_{i+j=m}S_i(p)\otimes S_j(q),
\tag{12}
\]

and extends bilinearly to formal path combinations. The factor S₀ is the coefficient sum.

The signature is injective on each linearized Hom space. To prove this, take a nonzero linear combination of paths and choose its maximum occurring length k. In degree k each such path contributes its unique full ordered edge word. These distinct tensor basis vectors cannot cancel unless all their coefficients vanish. Descend through the lengths. Identity coefficients are recovered in degree zero.

Hence endpoint-labelled signatures give a faithful compositional realization of every finite acyclic free path category, and therefore exact reconstruction at every finite nested closure depth. Lower signature degrees can be selected when they already have full rank, as the three- and four-cube calculations demonstrate.

The construction is the finite discrete tensor-signature/Chen identity. Its role here is explicit: it supplies the missing correlation probes while preserving the source composition law.

## 10. Analytical realization boundary

The earlier theta theorem gives an injective realization H of the finite interval-atom space, with recovery L=(H*H)⁻¹H*. Thus replacing Jc by HJc preserves the three-prime finite reconstruction when the cycle and endpoint data are retained. This uses the recorded theta injectivity premise; the present checker evaluates no theta integrals.

Four-prime reconstruction additionally requires the six source-defined correlation probes. They are defined and certified on formal routes. Realizing them as independent analytical measurements of a theta signal is a further interface: the aggregate theta interval response already identifies the two sides of (7), so these probes require retained source data or an enriched analytical channel.

## Verification

`uv run --with sympy python research/nima/checkers/check_prime_cube_path_observer_reconstruction.py`

All checks use exact rational arithmetic. Results are in `research/nima/results/prime-cube-path-observer-reconstruction.json`. The original six-forest braid checker remains unchanged. The categorical and general tensor-signature statements are proved above; finite rank checks certify the declared source-specific instances.
