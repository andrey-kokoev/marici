# FCC tetrahedral–octahedral Gaussian boundary recursion

Date: 2026-10-19.

## Result and scope

There is an exact recursive construction of Gaussian boundary functions using two shape families, T and O, and their existing factor-two subdivisions. The recipe is fixed across levels; its boundary coordinate spaces are not fixed-dimensional. This implementation tests actual finite polyhedral regions, not four-site periodic quotients.

The recursion reproduces the same microscopic Gaussian theory when that theory is assembled in different orders. It does not establish equality of theories at different microscopic cutoffs, a renormalization fixed point, a Chamon renormalization circuit, or a HoTT formalization.

## Model and additive boundary convention

Let L = {(x,y,z) in Z^3 : x+y+z is even}. The twelve nearest-neighbor offsets are the permutations of (+/-1,+/-1,0). In the full lattice the operator is K = I + Delta_FCC = 13 I - A_FCC.

The canonical cells with edge length sqrt(2) s are

T_s = conv{(0,0,0),(s,s,0),(s,0,s),(0,s,s)},

O_s = (s,0,0) + {r in R^3 : |r_x|+|r_y|+|r_z| <= s},

with s = 2^n. The microscopic spacing remains fixed: increasing s grows the grain. The results are not a continuum limit obtained by shrinking lattice spacing while scaling couplings.

For a microscopic cell c, assign

K_c = I/14 + Delta_c/4,

where Delta_c is the unweighted graph Laplacian of the tetrahedral or octahedral edge graph. The mass term is shared among 14 cells incident on a bulk vertex (8 tetrahedra and 6 octahedra); an edge term is shared among its four incident cells (2 tetrahedra and 2 octahedra). Consequently the sum over the full honeycomb is exactly I+Delta_FCC.

For a finite grain, only its own microscopic cells contribute. This is an additive cell-owned boundary convention, not the principal submatrix of the infinite-lattice operator with the exterior clamped to zero. Shared boundary contributions add correctly when neighboring grains are glued. Each primitive K_c is positive definite. No Gaussian zero-mode regularization is needed.

The code uses integer microscopic input M = 28 K. A cell contributes 2 to each vertex diagonal and 7 times its graph Laplacian. This allows independent rational and finite-field checks.

## Boundary object and recursive construction

Write the boundary response as

Z_R(phi_b) = exp(ell_R) exp(-phi_b^T S_R phi_b / 2).

Here S_R = K_bb - K_bi K_ii^(-1) K_ib and

ell_R = |i| log(2 pi)/2 - log det K_ii/2,

using unnormalized Lebesgue integration over interior variables.

The geometric rules are T_(2s) = 4 T_s + O_s and O_(2s) = 8 T_s + 6 O_s, with their actual coordinate placements and shared faces, not merely these cell counts. A tetrahedron is split at edge midpoints. An octahedron is split using its edge midpoints and center; this adds no preferred diagonal.

To form a parent, obtain each child's response, transport it to the child's actual coordinates, identify shared boundary coordinates, and sum embedded child kernels:

J = sum_j E_j^T S_j E_j.

Let B be the parent's external boundary and I the child-interface coordinates internal to the parent. Set

S_parent = J_BB - J_BI J_II^(-1) J_IB,

ell_parent = sum_j ell_j + |I| log(2 pi)/2 - log det J_II/2.

Only two canonical response templates are evaluated at each level; differently placed copies use coordinate maps. Their matrices grow with level.

### Why the recursion is exact

At the microscopic level the action is a sum of cell contributions. The interiors of distinct children are disjoint; their shared variables lie on child boundaries. Eliminating each child's interior and then the parent interfaces integrates exactly the same variables as eliminating all parent interior variables at once. Positive definiteness makes all these finite-dimensional Gaussian integrals convergent. Schur-complement associativity and the associated determinant identity give equality of the kernels and normalizations. Induction proves the recursive formula at every finite subdivision level.

This is a concrete specialization of established discrete Gaussian gluing, not a claim to a new general gluing theorem.

## Computational validation

Two independent assembly paths are implemented. One recursively combines previously computed child boundary responses; the other enumerates all primitive cells in the parent and eliminates the whole interior directly.

| s | T total vertices | T boundary | O total vertices | O boundary |
|---:|---:|---:|---:|---:|
|1|4|4|6|6|
|2|10|10|19|18|
|4|35|34|85|66|
|8|165|130|489|258|
|16|969|514|3281|1026|

The boundary counts are exactly B_T(s)=2s^2+2 and B_O(s)=4s^2+2. They follow by counting the triangular-face lattices and subtracting duplicate edge/vertex sites. In particular these are area-scaling numbers of scalar boundary coordinates, not area-scaling numbers of dense matrix entries.

The largest kernel disagreement between recursive and direct assembly was 8.881784197001252e-16. The largest absolute log-normalization difference was 5.684341886080801e-13.

Rational checks at s=2 and s=4 prove exact equality of the recursive and direct kernels, determinant products, and numbers of integrated coordinates for both T and O. For O_4 the determinant of the eliminated 19-variable kernel is exactly 935358160188257866125.

### Adjacent-grain gluing

A tetrahedron was attached to the positive (1,1,1)-normal face of O_s. The tetrahedron vertices are (2s,0,0),(s,s,0),(s,0,s),(2s,s,s). The direct primitive-cell calculation was compared with gluing the two separately reduced boundary functions.

| s | Union vertices | Union boundary | Shared-face interior variables | Kernel error | Log-normalization error |
|---:|---:|---:|---:|---:|---:|
|4|105|82|3|8.882e-16|0|
|8|609|322|21|8.882e-16|1.421e-14|
|16|4097|1282|105|8.882e-16|1.023e-12|

Shared-face edge and corner variables remain on the external boundary; they are not eliminated. The union boundary has exactly 5s^2+2 variables.

## Exact versus approximate interface rank

For O_s, consider two opposite triangular faces, using only their strict face-interior vertices. Relative to the octahedron center, these have all coordinates positive and sum s, or all coordinates negative and sum -s. Each face has (s-1)(s-2)/2 such variables. Let C_s be the block of the exact boundary kernel coupling these two faces; all other external boundary variables remain present.

| s | C_s dimensions | Certified rational rank | Rank for relative Frobenius error <=1% | Rank for error <=0.01% |
|---:|---:|---:|---:|---:|
|4|3 x 3|3|3|3|
|8|21 x 21|21|6|15|
|16|105 x 105|105|6|17|

The exact ranks were certified by computing the Schur-complement block modulo the prime 1000003 from integer input M=28K. The eliminated interior block is invertible modulo this prime. Full rank of the reduced block modulo this prime certifies full rank over the rationals. No floating-point threshold is used for these exact-rank conclusions.

For s=16 the largest and smallest computed singular values are approximately 1.2902761632881606e-4 and 2.4811860802495613e-18. Floating-point effective rank is therefore very different from exact rank. The modular test certifies rank 105 despite small singular values.

The approximate ranks concern this specific distant-face coupling block only. They are not error bounds for the full kernel, its inverse, its determinant, or the partition function. Two successive sizes with rank six at 1% do not prove a size-independent approximation theorem.

If every coupling between these faces is required to pass through r scalar Gaussian mediator coordinates, with no direct bypass, the cross block factors as X D^(-1) Y and has rank at most r. Such a direct mediator representation therefore needs r >=105 at s=16. This restricted statement does not exclude networks containing many small factors, alternative representations, or approximate compression.

## Symmetry and its growing representations

The recursion is equivariant under actual spatial point symmetries: T has 12 proper rotations and 24 symmetries including reflections; O has 24 proper rotations and 48 including reflections. All were explicitly checked. Maximum kernel equivariance discrepancy was 8.881784197001252e-16. The normalization is invariant under the same coordinate permutations.

Equivariance follows algebraically as well: symmetric primitive kernels and the symmetric subdivision are carried into themselves by the point group, and Gaussian elimination commutes with relabeling. Thus A4 is preserved as the tetrahedral rotation group, but this scalar model does not single A4 out from the larger symmetries it also preserves.

The complexified boundary-coordinate representation of T_s carries A4. Its characters on the identity, a double transposition, and a three-cycle are (2s^2+2,2,1) for s=2^n with n>=1. Each 180-degree rotation fixes two edge midpoints. A three-cycle fixes one lattice vertex; the opposite face center is not a lattice point because s is not divisible by three. Therefore

V_T(s) = [(s^2+8)/6] 1 + [(s^2+2)/6] (1' + 1'') + [s^2/2] 3.

At s=1, V_T(1)=1+3 instead.

| s | multiplicity 1 | multiplicity 1' | multiplicity 1'' | multiplicity 3 |
|---:|---:|---:|---:|---:|
|1|1|0|0|1|
|2|2|1|1|2|
|4|4|3|3|8|
|8|12|11|11|32|
|16|44|43|43|128|

For real scalar coordinates, the conjugate 1' and 1'' combine into real two-dimensional representations. At s=16 the complex notation gives 514 =44+43+43+3*128. The symmetry labels come from the same finite list while their multiplicities grow. An equivariant kernel can mix repeated copies of an irrep; symmetry alone does not reduce every boundary response to one singlet eigenvalue and one triplet eigenvalue.

## Complexity interpretation

There are two local cell types and two fixed assembly patterns, with exact composition. Each evaluated parent needs only its outer boundary and a normalization scalar to interact through that boundary with its exterior. The number of boundary coordinates is O(s^2), compared with O(s^3) microscopic sites.

An explicitly stored dense boundary matrix nevertheless uses O(s^4) entries. The evaluated response is not yet stored in O(s^2) numbers. A finite recursive generator is not a constant-sized evaluated state or a fixed-bond-dimension exact tensor network. This distinction is essential when interpreting a grain as a higher-level point.

Hierarchical low-rank approximations of elliptic Schur complements are established methods, but applying their quantitative error bounds to this exact lattice, boundary convention, and symmetry-preserving truncation requires further analysis.

## Correction concerning the earlier BA4 shorthand

For the periodic 32-to-4 construction, (L/4Z^3) semidirect C3 acts on eight blocking origins with stabilizer (2L/4Z^3) semidirect C3, of order 12 and isomorphic to A4. Its transitive action groupoid has homotopy type BA4.

On the larger periodic 256-to-32 construction, the analogous stabilizer is (2L/8Z^3) semidirect C3, of order 96, not A4. Reusing BA4 for that entire action groupoid without further quotienting was incorrect. Rescaling the finite window and retaining only the earlier four-anchor presentation is a different construction.

This note uses the actual spatial A4 rotations of tetrahedral grains, independently of that periodic-groupoid shorthand. No identification of full structured grain-data fibers across scales is asserted. Their coordinate representations have different dimensions and multiplicities.

## Reproduction

Dependencies used: NumPy 2.3.5, SciPy 1.17.0, SymPy 1.14.0. No downloaded data are required.

Run in this directory:

```sh
OPENBLAS_NUM_THREADS=2 OMP_NUM_THREADS=2 python fcc_boundary.py --max-level 4 --modular-max-level 4 --output results
OPENBLAS_NUM_THREADS=2 python additional_checks.py
OPENBLAS_NUM_THREADS=2 python exact_recursion_check.py
```

The size-16 finite-field calculation took approximately 30 seconds in this environment; timings depend on hardware. The main validation uses dense matrices, so max-level is deliberately limited to four. All generated kernels, their boundary point coordinates, and log-normalizations are in results/*.npz. JSON files contain measured errors, singular values, representation multiplicities, and exact certificates.

## Primary references

Scott Schaefer, Jan Hakenberg, Joe Warren, *Smooth Subdivision of Tetrahedral Meshes* (2004), section 2.1 and figure 3. Only the linear tetrahedral–octahedral subdivision is used here, not their smoothing/deformation operation.
https://www.cs.rice.edu/~jwarren/papers/tetrahedral.pdf

Nicolai Reshetikhin, Boris Vertman, *Combinatorial Quantum Field Theory and Gluing Formula for Determinants*, Letters in Mathematical Physics 105 (2015), 309–340; especially section 6. This supplies the established Gaussian boundary/gluing framework, not the present FCC numerical values.
https://arxiv.org/abs/1403.6170

Markus Faustmann, Jens Markus Melenk, Dirk Praetorius, *H-matrix approximability of the inverses of FEM matrices*, Numerische Mathematik 131 (2015), 615–642; section 6 on Schur complements. This concerns approximation results in its stated elliptic finite-element setting, not an automatic exact low-rank theorem for this FCC model.
https://arxiv.org/abs/1308.0499
