# A symmetry-preserving circle torsor and a recursive BU(1) construction

Date: 2026-10-19

## Result and assumptions

A four-cycle determines an origin-free cyclic heap on its vertices. Under the standard equal-edge affine geometric realization, this heap extends to a continuous circle torsor. The torsor has an intrinsic topological group of translations, isomorphic to U(1). Repeated joins of the torsor, retaining this diagonal translation action, produce the usual projective-space tower and its universal circle bundle.

This is an explicit construction relative to declared topology-producing operations. It is not a derivation of those operations from the frozen Marici native grammar. It does not derive a physical U(1) interaction, SU(2), SU(3), or the original tetrahedral action on one Hopf base.

The fresh checker is `check_wg_circle_torsor.py`. Its `wg_circle_torsor_results.json` reports 53,205 exact finite/rational checks. Agda is not installed in the active runtime; no Agda or Lean compilation was performed. No repository files were changed.

## 1. Source status

Marici's native grammar [M1] has eight header forms and twelve rule schemas. It includes dependent sums/products, paths, maps, equivalences, retained inputs and comparison packages. Its rules can retain supplied functions and higher witnesses. The inspected register contains no graph-realization, topological-join, action-quotient or sequential-homotopy-colimit constructor. This absence from the register is not a general impossibility theorem about definitions in the surrounding type theory.

The input four-cycle is the equator obtained from the previously discussed octahedral promotion, after choosing a pole pair. All pole-pair choices can instead be retained as a family. Here the calculation is over one cycle, with its complete graph automorphism group retained.

## 2. Intrinsic finite relative composition

Let P be the vertices of a four-cycle. Its graph automorphisms form the order-eight dihedral group. Its orientation-preserving subgroup R_P is defined without choosing an orientation: it is the kernel of the action on the rank-one integral homology H_1 of the graph. It has order four and acts freely and transitively on P.

For x,y in P there is exactly one r_xy in R_P with r_xy(y)=x. Define

    h(x,y,z) = r_xy(z).

A cyclic coordinate P ≅ Z/4 writes this as h(x,y,z)=x-y+z mod 4. It satisfies

    h(x,y,y)=x,
    h(y,y,x)=x,
    h(h(x,y,z),u,v)=h(x,y,h(z,u,v)),
    h(x,y,z)=h(z,y,x).

These are the abelian heap laws. No point has been designated the unit.

Every graph automorphism has coordinate form g(x)=epsilon*x+a, epsilon in {+1,-1}. Therefore

    h(gx,gy,gz) = epsilon*(x-y+z)+a = g(h(x,y,z)).

Equivalently, g r_xy g^(-1)=r_(gx,gy). The operation is independent of the cyclic coordinate used to calculate it.

A binary group multiplication preserved by every graph automorphism would have an invariant identity. The quarter-turn has no fixed point, so this cannot exist. This excludes an invariant *choice of origin*, not an origin-free group of displacements.

### A nontrivial alternative excluded by circle continuity

Symmetry and the heap equations alone are not enough. There is also the XOR heap on the four-set, h_V(x,y,z)=x xor y xor z, which is invariant even under S4.

Every heap on four elements becomes a group after selecting one element. The only groups of order four are C4 and V4. Transporting both heap operations by all 24 bijections therefore enumerates every such heap: three cyclic tables and one XOR table. Exactly two preserve the specified four-cycle's D4 action.

The XOR translation z ↦ 1 xor z is (01)(23), which reverses the cyclic order 0,1,2,3. It cannot extend to a translation in a continuous heap on the connected circle. Indeed, after temporarily choosing y as origin, all translations belong to a continuous family starting at the identity, and hence preserve orientation. Equivalently, an orientation-preserving circle homeomorphism cannot induce this reversed permutation of its four cyclically ordered marked points.

The cyclic heap is the only D4-equivariant heap in this exhaustive four-element comparison whose translations extend to a continuous circle heap.

This does not assert uniqueness of all possible continuous extensions under arbitrary reparameterizations. The standard affine realization selects the concrete extension used below.

## 3. Continuous realization and displacement group

Give each edge its standard affine interval, with equal lengths. The resulting metric cycle T is a circle of circumference four. An affine coordinate identifies T with R/4Z, and define

    h(s,t,u) = s-t+u mod 4.

Changing coordinates by s ↦ epsilon*s+a leaves this operation invariant in the required covariant sense. A uniform change of the edge length has no effect on the resulting torsor up to the corresponding isomorphism. Unequal lengths or arbitrary nonlinear edge coordinates are not silently included in this construction.

The translations tau_(s,t)(u)=h(s,t,u) form a topological group G, whose unit is the identity map, not a chosen point of T. This group acts freely and transitively on T and is isomorphic to R/4Z and U(1). Reflection of T conjugates a translation to its inverse.

The topology matters. The four vertex rotations alone form the discrete group C4. The connected translation group G acts on the *realized* circle and includes translations that do not preserve the four marked vertices. Passing to the realization is an explicit enlargement, not an identification of Aut(C4) with U(1).

The standard edge subdivision is compatible: the injection Z/N → Z/2N, x ↦ 2x, obeys

    2 h_N(x,y,z) = h_(2N)(2x,2y,2z).

The checker verifies several finite instances; the displayed formula proves the claim for every N.

## 4. Origin-free Hopf construction

Form E_1=T*T with the diagonal G action. Its realization is S3. A point of the join has two circle coordinates x,y and a weight t in [0,1], with irrelevant coordinates forgotten at the endpoints.

Because T is a torsor, there is a unique displacement delta(x,y) in G taking y to x. Since G is abelian, delta(gx,gy)=delta(x,y). The map

    [x,y,t] ↦ [delta(x,y),t] in Sigma G

is therefore invariant under the diagonal action. At t=0 and t=1 the suspension coordinate collapses, so the formula is well-defined. It identifies the orbit space with Sigma G ≃ S2.

The action is free: at least one join weight is positive, and fixing its T-coordinate forces g=1. Thus

    G → T*T → (T*T)/G ≃ S2

is the Hopf circle bundle. In a temporary coordinate T ≅ U(1), the join is the unit sphere in C2 and the quotient is CP1. The coordinate can be used to prove the identification without becoming a preferred origin of the construction.

The Hopf invariant is ±1, depending on domain/target orientation conventions. This uses the standard Hopf-bundle theorem [T3]; no fifth canonical filler is being reinterpreted as a nonzero class.

## 5. The entire tower uses one recursive operation

For n≥0 define

    E_n = T^{*(n+1)},
    B_n = E_n/G,
    E_(n+1) = E_n*T,

always with the diagonal G action and the retained projection p_n:E_n→B_n.

The unit-sphere identification is explicit. After choosing a coordinate on T only for the proof,

    [(lambda_j,x_j)] ↦ (sqrt(lambda_0) exp(2pi i x_0/4), ...,
                         sqrt(lambda_n) exp(2pi i x_n/4)).

Weights are nonnegative with sum one. Zero-weight circle coordinates are forgotten, as required by the join definition. This gives a homeomorphism E_n ≅ S^(2n+1). Translation by a acts by common scalar multiplication, so B_n ≅ CP^n.

The first stages are

    n=0: S1 → point,
    n=1: S3 → CP1 ≃ S2,
    n=2: S5 → CP2,
    n=3: S7 → CP3.

The inclusion E_n→E_(n+1) gives the last join coordinate weight zero. It is equivariant and descends to the standard projective inclusion. In particular CP2 is CP1 with a four-cell attached along the preceding Hopf projection. Independent arbitrary attaching maps are not required at each stage.

At the finite simplicial level C4=S0*S0, so m copies of C4 have 2m antipodal vertex pairs. Their join is the boundary complex of the 2m-dimensional crosspolytope. Every simplex chooses at most one vertex from each opposite pair. Its f-vector satisfies

    f_d = 2^(d+1) binomial(2m,d+1),  0≤d≤2m-1.

This proves the sphere realization in every dimension. The checker independently enumerates the first four joins. The continuous circle action need not be simplicial for these finite triangulations.

The rank-one Hermitian projector z z* supplies an origin-independent concrete description of each projective quotient. Common phase cancels; changing the origin of T gives just such a common phase. Reversing its orientation complex-conjugates the projective point. Exact rational projector tests check trace, idempotence, phase invariance and inclusion compatibility.

Taking the sequential colimit with the standard CW topology gives the contractible total space E_infinity and

    B_infinity ≃ CP^infinity ≃ BU(1) ≃ K(Z,2).

This all-dimensional conclusion is Milnor's universal-bundle construction [T1], not an extrapolation from the finite checks. Join-based constructions and their homotopy-colimit interpretation are available in HoTT [T2,T4].

The circle bundle's Gysin sequence gives H*(B_n;Z)=Z[u]/(u^(n+1)), |u|=2: multiplication by its primitive first Chern class identifies successive even groups below the top dimension, since E_n has no intermediate cohomology. The limit has H*(B_infinity;Z)=Z[u]. Orientation reversal sends u to -u, not to zero.

## 6. What must be retained between WG steps

The generator state must retain E_n, the G action, p_n, and the construction record. Keeping only the orbit space and discarding the action is insufficient:

    (T*T)/G ≃ S2,
    (T/G)*(T/G) ≃ point*point ≃ point.

Quotienting separate pieces before joining loses relative phase. This is a concrete obstruction to an endpoint-only WG encoding.

Join associators are represented by flattening barycentric weights. The resulting maps commute with diagonal G action, so they descend to the quotient. The usual coherence identities hold because each composition yields the same flattened coordinates. Retained source trees can remain distinct; equality of evaluated spaces is not erasure of their construction history.

## 7. Relation to A4 and the earlier spin-lift obstruction

Graph isomorphisms induce isomorphisms of heaps, circles, displacement groups, and the complete tower. Therefore this construction can be performed on all three equatorial choices and transported under their A4 action.

That statement is weaker than recovering the original tetrahedral rotational action on a *single* S2 base. On one equator, an orientation-preserving graph translation acts diagonally on every join factor and hence acts trivially after quotienting by G. An equatorial reflection induces complex conjugation. The resulting action on one B_n therefore factors through the orientation sign.

In particular this tower does not remove the earlier obstruction to a strict A4 lift of the degree-one Hopf bundle over the original tetrahedral sphere. The binary-tetrahedral cover question and the comparison to that original base action remain separate.

## 8. What has changed in the WG question

Relative to standard affine graph realization, join, group quotient and sequential homotopy colimit, the circle-to-BU(1) tower is now a uniform construction; neither a preferred identity nor an independently chosen degree-one cocycle is necessary.

The remaining native-source obligation is to derive or explicitly admit those topology-producing constructors and their interpretation into the frozen Marici grammar. The result does not show that the four-state set or its discrete symmetry group alone generates U(1). It shows exactly which realization and recursive operations make the stronger result true.

## References

[M1] Marici, implemented native generating grammar, default-branch file read through GitHub on 2026-10-19:
https://github.com/andrey-kokoev/marici/blob/main/research/nima/generating-grammar/NATIVE-CORE.md
The read registers eight headers, twelve rule schemas, and the distinction between supplied packages and their native derivations.

[T1] J. Milnor, Construction of Universal Bundles, II, Annals of Mathematics 63 (1956), 430–436.
https://www.home.uni-osnabrueck.de/mfrankland/Math527/Milnor_Universal2.pdf

[T2] U. Buchholtz and E. Rijke, The real projective spaces in homotopy type theory (2017). Its concluding discussion explicitly covers the complex-projective and Milnor-construction extension of join methods.
https://arxiv.org/abs/1704.05770

[T3] G. Brunerie, On the homotopy groups of spheres in homotopy type theory (2016), Section 2.5, Hopf construction and the circle case.
https://arxiv.org/abs/1606.05916

[T4] E. Rijke, The join construction (2017).
https://arxiv.org/abs/1701.07538

[T5] S. Mimram and E. Oleon, Delooping cyclic groups with lens spaces in homotopy type theory (2024). Relevant negative comparison: discrete cyclic quotient versus continuous circle quotient.
https://arxiv.org/abs/2405.10149

## Reproduction

    python check_wg_circle_torsor.py --output wg_circle_torsor_results.json

The executable uses only the Python standard library. Its finite identities and exact rational tests are separate from the cited infinite-dimensional topological theorems. It is not proof-assistant verification.
