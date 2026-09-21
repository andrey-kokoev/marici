# Joint-cut carriers as pointed multi-input derived images

## Result

The prescribed finite joint-cut record carriers are images of explicit projective objects under an external, multi-input derived receiver. Their actual observation columns are evaluations of external path morphisms at the prepared segment vacua. This identifies the joint record, including its intermediate labels, without assuming that the one-input receiver is monoidal.

Rejoining agrees exactly with source composition on these emitted records. Its signed mate is the prescribed sum over tensor splittings and cut-label preimages. All coarsening and contravariant mate composition laws follow.

There is a precise boundary: rejoining is not generally an intertwiner for independent right-creation actions on arbitrary input memories. Thus this construction gives the pointed multi-input comparison, not an automatic natural transformation between ordinary one-input derived functors on all states.

## 1. Fixed finite receiver and its capacities

Let S be the marked source path algebra over C. Use the finite prepared-source receiver from the preceding extension theorem. Let W=W0+J W0 be its finite J-invariant sheet-reduced feature space and define

F_c=direct_sum_(r=0)^c W^(tensor r).

For each source vertex a and capacity c, set

X_a^(c)=C phi_a tensor F_c,

where phi_a=R_a^(-1)Phi/||Phi|| is the unit prepared vector. This normalization is only a basis choice in the source line; the emitted feature g_e remains computed from the original prescribed forcing Phi.

Reassembly sends phi_a to phi_b. Hence the source-line identification

theta_a:X_a^(c)->F_c, theta_a(phi_a tensor u)=u

is unitary and takes the marked generator maps to

A_e^0 -> I,

A_e^1 -> c_R^(c)(g_e).

These assignments give a right S-module X^(c)=direct_sum_a X_a^(c), and therefore the exact receiver

E_c(P)=X^(c) tensor_S^L P.

The capacity-c creation operators are truncated at degree c. This still defines a representation of the free marked path algebra. When a source segment has c events, its vacuum record has degree at most c, so the truncation removes none of that segment's forward record.

## 2. External multi-input extension

For k segments of capacities c_1,...,c_k, put

S_k=S tensor_C ... tensor_C S,

X_vec_c=X^(c_1) tensor_C ... tensor_C X^(c_k).

The latter is a right S_k-module, with independent source actions on its factors. Define

E_vec_c:Perf(S_k)->Perf(C),

E_vec_c(P)=X_vec_c tensor_(S_k)^L P.

This functor is exact. On external products of perfect modules it has the natural comparison

E_vec_c(P_1 external_tensor ... external_tensor P_k)
  equivalent to E_(c_1)(P_1) tensor_C^L ... tensor_C^L E_(c_k)(P_k).

Proof: take bounded projective representatives and apply the associativity and balancing identities of tensor product. Over the field C the external tensor products compute the derived external products. These identifications commute with differentials and extend to retracts. The resulting functor is exact in each input, with the usual totalization signs.

This is an external multi-input extension. It does not equip Perf(S) with an unspecified internal tensor product or assert a monoidal structure on E_c.

## 3. Explicit source objects for a joint cut

Fix an n-event source packet, initial vertex x_0, terminal vertex x_k, and a cut set with k segments. Let their event lengths be c_1,...,c_k. Denote an admitted tuple of internal cut vertices by y=(x_1,...,x_(k-1)).

For P_a=S e_a, define in Perf(S_k)

U_y=P_(x_0) external_tensor P_(x_1) external_tensor ... external_tensor P_(x_(k-1)),

V_y=P_(x_1) external_tensor ... external_tensor P_(x_k).

Take U_cut and V_cut to be the direct sums of these objects over the admitted tuples y. The summand index is part of the source object; it is not summed away by evaluation.

A route split into typed segments p_1,...,p_k determines the external morphism

p_1 external_tensor ... external_tensor p_k : U_y -> V_y.

Indeed each path is a map P_(x_(j-1))->P_(x_j), and the projective external-Hom identification is exactly the tensor product of these path Hom spaces. Segmentation is the source path-cut decomposition already established, now realized as actual projective morphisms in the multi-input source category.

The receiver image is

E_vec_c(V_cut) equivalent to direct_sum_y F_(c_1) tensor ... tensor F_(c_k),

after the prescribed theta identifications of the prepared source lines. This is precisely the finite typed joint-record carrier, with its correct capacity profile and cut labels.

For the three-prime full cut the capacities are (1,1,1). For its two single-cut observations they are (1,2) and (2,1), and for terminal recording the capacity is (3). These are different external source objects, not interchangeable presentations of one terminal memory space.

## 4. Recovering the actual record columns

At each input projective use the specified prepared vacuum

eta_a: C -> E_c(P_a), 1 -> phi_a tensor Omega.

At the y summand of U_cut use eta_(x_0) tensor ... tensor eta_(x_(k-1)). Applying E_vec_c to the external path morphism and then evaluating at this vector gives

record(p_1) tensor ... tensor record(p_k),

where each segment record is the ordered product of its emitted retained features. Forgotten generators contribute the coefficient unit while still acting on the source line through their actual reassembly transport.

Summing over the marked lifts of the events gives the existing factors product_e(1+g_e), with event order retained. Extending linearly in source paths gives exactly the prescribed cut observation O_cut.

The vacua are extra pointed receiver data already provided by the pilot. The theorem does not manufacture them from the bare exact functor. It uses independently prepared fixed vectors in multiple inputs; it does not define a linear cloning map on an unknown source state.

## 5. Rejoining on emitted records

Define

mu_(a,b):F_a tensor F_b -> F_(a+b)

by concatenation of tensor words, extended linearly. No input term exceeds the target capacity a+b. Deleting a cut applies this map and forgets only that cut's vertex label; colliding labels are summed.

For two composable source segments p and q of lengths a and b,

mu_(a,b)(record(p) tensor record(q))=record(p followed by q).

Proof: the source-line transports compose, and on record factors the generator actions are right multiplication by either 1 or g_e. Induction on q proves the displayed identity. This uses the specified creation receiver, not merely existence of arbitrary bounded generator maps.

Hence for cut sets T subset S,

J_(T<-S) O_S=O_T.

Concatenation is associative and forgetting vertex labels is transitive, so

J_(U<-T) J_(T<-S)=J_(U<-S).

These statements hold on the full finite record spaces for the rejoining maps themselves, and on all source columns for the observation square. No uniqueness of reconstruction from coarser records is inferred.

## 6. Why this is not a monoidal shortcut

The multiplication map of a noncommutative algebra is not in general an algebra homomorphism S tensor S->S. The two independent elements e tensor 1 and 1 tensor f commute in the external algebra, whereas their proposed images e and f need not commute. Thus the change from k inputs to k-1 inputs cannot simply be called scalar restriction along algebra multiplication.

The analogous receiver failure is explicit. Let a,b be independent feature letters. On arbitrary memories,

mu(c_R(a) Omega tensor b)=a tensor b,

c_R(a) mu(Omega tensor b)=b tensor a.

Therefore mu does not intertwine the first independent right-creation action with the ordinary right-creation action on joined memory. This is not an obstruction to the proved vacuum-record identity; it is an obstruction to promoting it to an unqualified naturality assertion on all input states.

A fuller functorial coarsening framework would use an appropriate composition correspondence, bimodule action, or enriched arrow category. None is silently supplied by the one-input exact functor. At source coefficient level composition is the typed pairing

S tensor_B S -> S,

with B the vertex-idempotent algebra, rather than an algebra map from an unconstrained external product. Establishing its full derived receiver semantics is a separate statement from the explicit projective-object comparison above.

## 7. Pairing and unique rejoin mate

On F_c retain the prescribed degree weights tau^(2r) and signed operator J^(tensor r). Since W is finite-dimensional and J is an involution, this pairing is nondegenerate. Use product pairings for segment factors and orthogonal direct sums over cut labels.

The unique mate of mu_(a,b) sends a degree-r tensor word to the sum of its splittings at degrees p,q satisfying

p+q=r, 0<=p<=a, 0<=q<=b.

The formula follows from tensor contraction: the total degree weight is tau^(2r) on both sides, and J^(tensor r) factors as J^(tensor p) tensor J^(tensor q). No inverse of a degenerate four-port matrix is involved after the prescribed sheet reduction.

If a rejoining map forgets a cut label, its mate also copies the dual observation to each admitted label preimage. Thus the complete J^sharp is the prescribed split-and-copy map. Nondegeneracy makes it unique, and

(J_2 J_1)^sharp=J_1^sharp J_2^sharp.

Tensoring the component beta maps identifies this mate with the contragredient on the joint carrier. Opposite reflection reverses the factors and vertex labels as in the preceding opposite-history theorem. This remains distinct from identifying right creation with its opposite-polarity creation map.

The full cut carrier pairing is nondegenerate; the pullback to a particular arithmetic source subspace need not be. No positive or nondegenerate terminal pullback is inferred.

## 8. Derived duality and the two gradings

The external functor has the same perfect-module duality square as the one-input extension, with the conjugate opposite external algebra. Reversing the order of factors identifies it with the multi-input mate receiver in reflected order. This follows either from the perfect-module theorem applied to S_k or by tensoring its evaluation maps.

Record degree and cohomological degree must be distinguished. The finite feature records here are objects in cohomological degree zero even when their words have positive record degree. Reversing feature slots introduces no Koszul sign from record degree.

When source objects are actual complexes, external totalization and duality use their cohomological degrees, including the usual tensor differential sign and the cofiber-to-fiber shift. This does not alter the degree-zero record formulas above.

## 9. Faithfulness and remaining boundary

For the finest event cut, the source morphisms and the local pointed evaluations satisfy the earlier joint-observation criterion whenever each event feature is nonzero. The full typed observation is therefore injective at each finite packet, even though the one-input terminal receiver can lose path information.

The two-prime rank-eight and three-prime rank-48 joint observations are instances of this multi-input construction. The separate three-prime cut marginals still have joint rank 46. Nothing in exactness, external tensoring, or the pairing comparison removes their two-dimensional kernel after the joint attachment data is discarded.

Constructed here:

- actual projective source objects and morphisms for each typed cut chart;
- exact external derived receivers whose images are the prescribed finite record carriers;
- the vacuum evaluation giving the actual observation columns;
- exact rejoining on those columns, with associative coarsening and unique signed mates.

Not established:

- an internal monoidal one-input receiver;
- a natural coarsening transformation for arbitrary independent memory actions;
- equality of a tensor cut-record chart with an independently prescribed cofiber quotient in Perf(S);
- infinite-dimensional or physical realization.

The remaining structural task, if all-state derived coarsening is required, is the typed composition-correspondence semantics identified in section 6. It is now localized to a specific action/variance issue rather than an unspecified comparison map.

## Verification

`uv run --with sympy python research/grothendieck/checkers/check_joint_cut_multi_input_extension.py`

Exact checks pass for pointed records, all three-event cut coarsenings, weighted signed rejoin mates, contravariant mate composition, the explicit arbitrary-memory noncommutativity hostile, and a cochain tensor-differential sign fixture.

The fixture uses a two-dimensional signed feature space, so its raw chart dimensions are 15,21,21,27; these are ambient carrier dimensions, not the arithmetic ranks 26,36,36,48. The external perfect-module comparison is proved above, not inferred from those finite matrix checks.
