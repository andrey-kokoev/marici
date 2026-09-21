# The six-prime associativity cell retains the derived middle block

## Status and result

**Finite-cutoff comparison theorem.** The groupings (ab)c and a(bc) have an explicit common derived comparison complex. Both carry the same 720-channel triple-product attachment to the labelled three-seam receiver.

The common complex retains both ordinary middle-block records and their shifted relation term. It is not obtained by refining a compressed first derivative, and it is not an equivalence between the entirety of the two coarse block complexes.

A sign hostile also matters: naively combining independently shifted block-to-seam maps gives opposite signs on all 720 product channels. The specified tensor-of-shifts convention supplies the correction. This is suspension transport, not an additional fitted coherence parameter.

The analytical carrier is the function-valued Clark realization. No finite sampled spectral rank is used.

## 1. Types and order of operations

Fix six distinct primes, the monotone marked source, its root s and terminal t, and a common receiver capacity at least six. Retain every ordered partition into three pairs and its two intermediate vertices. There are 90 such labelled partitions.

For a two-event block i, write:

- E_i for its full endpoint path space, dimension 8;
- R_i for its relation subspace, dimension 2;
- B_i=E_i/R_i for its endpoint terminal quotient, dimension 6.

These are endpoint CORNERS of the corresponding local source objects, not unital algebras by themselves. Tensor products below are external scalar tensor products with the displayed endpoint labels.

For a four-event block, write I_4 for its endpoint relation space, P_4=I_4^2 for its endpoint product space, and C_4=I_4/P_4. Their dimensions are 234,24,210. The full local ideal modules, before taking corners, give the projective resolution [I_4^2 -> I_4] of the local conormal module.

Apply the local one-sided DERIVED quotient to that full module resolution first, and only then take the designated outer endpoint corner. The result is

Q_4=[P_4 --0--> C_4], in degrees -1,0.

Similarly the local derived self-quotient of a two-event source, followed by its endpoint corner, is

Q_2=[R_2 --0--> B_2].

The second complex comes from the full local resolution [I_2 -> S_2] of its quotient. It is not a resolution of R_2.

Taking vector-space corners first and then applying an unrelated global quotient functor would not compute these objects. This ordering is part of their type declaration.

## 2. The two coarse complexes and their common middle refinement

Let L sum over cuts after four events:

L = direct_sum Q_(s,m) tensor R_(m,t).

Let R sum over cuts after two events:

R = direct_sum R_(s,l) tensor Q_(l,t).

Both are zero-differential complexes with dimensions 720 in degree -1 and 6300 in degree zero. They retain all four-event conormal coordinates in their prescribed outer corners, not just a selected product basis.

Define the common complex

H = direct_sum_(s<l<m<t) R_(s,l) tensor Q_(l,m) tensor R_(m,t),

where each of the three blocks has exactly two events. Thus

H^(-1)=direct_sum R_1 tensor R_2 tensor R_3,

H^0=direct_sum R_1 tensor B_2 tensor R_3,

with zero differential. Its dimensions are 720 and 2160, respectively.

The middle derived self-quotient is the missing datum. Replacing it by B_2 alone removes precisely the triple-product channel that must survive the comparison.

## 3. Explicit comparison maps

The map f_L:H->L is

in degree -1: a tensor b tensor c -> (a b) tensor c;

in degree zero: a tensor [w] tensor c -> [a w] tensor c.

The map f_R:H->R is

in degree -1: a tensor b tensor c -> a tensor (b c);

in degree zero: a tensor [w] tensor c -> a tensor [w c].

The degree-zero formulas are independent of the lift of [w]. Changing w by b in R_2 changes a w by a b in P_4, and changes w c by b c in P_4. Both changes vanish in the corresponding C_4.

These are chain maps on the whole displayed complexes. The zero differential is justified by derived base change, not selected to force the comparison.

There is also a source-level diagram before these quotient maps. Its common complex is

[R_1 tensor R_2 tensor R_3 -> R_1 tensor E_2 tensor R_3],

and its two coarse complexes use [P_4 -> I_4]. The same multiplication formulas commute with their nonzero differentials. The degree-zero quotient maps to H,L,R, and the identity maps in degree -1, give a commuting diagram of complexes. These are the corner versions of the separately specified local derived-quotient units; they are not asserted to be applications of one global quotient functor to already collapsed vector spaces.

Thus the comparison is constructed from source multiplication and quotient units, before choosing a seam observation.

## 4. Agreement in the full six-event attachment

For the full six-prime source S, write I=ker rho, G^2=I^2/I^3, and P_3=I^3. Here I^4=0 and P_3 has dimension 720.

The global projective resolution is [I^3 -> I^2]. Derived quotient followed by the root-to-terminal corner gives

Q_global=[P_3 --0--> (G^2)_(s,t)].

Multiplication defines maps m_L:L->Q_global and m_R:R->Q_global. Their degree-minus-one components identify the respective product spaces with P_3. Their degree-zero components multiply lifts and take the class modulo I^3.

These components are well-defined: changing a C_4 representative by an element of P_4 changes its product with the remaining relation by an element of I^3.

The comparison square commutes STRICTLY:

m_L f_L = m_R f_R.

In degree -1 this is (a b)c=a(b c). In degree zero it is [(a w)c]=[a(w c)]. No additional associativity homotopy has been fitted after scalar observation.

## 5. The common object is not missing ordinary coordinates

Inside the unquotiented six-event path space, put

A_L=direct_sum I_4 tensor R_2,

A_R=direct_sum R_2 tensor I_4.

Both contain P_3. Their intersection is exactly

direct_sum R_1 tensor E_2 tensor R_3.

To see this, first impose only the last-block relation condition and only the first-block relation condition. Relative to the unique path cuts at positions two and four, those conditions act on independent tensor factors. Their intersection is R_1 tensor E_2 tensor R_3. Every such vector already satisfies the required four-event ideal conditions, so imposing those conditions changes nothing further.

After quotienting by P_3 the intersection becomes R_1 tensor B_2 tensor R_3. Its dimension is 90 times 2 times 6 times 2, namely 2160.

Consequently H identifies the strict common subcomplex of the two coarse images in Q_global, in BOTH degrees. It is not merely their shared bottom cycle space. The 6300-dimensional ordinary parts of L and R are not asserted to be canonically equivalent.

Nor is this strict pullback automatically the homotopy pullback over the entirety of Q_global: any cokernel of the sum of their degree-zero images contributes additional derived data. No disappearance of that sector is claimed.

## 6. The three-seam comparison and its shift

Let J_3 be the labelled external tensor of the three actual local seam complexes, summed over the 90 ordered pair partitions. Its bottom degree is -3. The path derivatives define

j_3:P_3[3] -> J_3,

j_3(a b c)=D(a) tensor D(b) tensor D(c).

This is a literal injective cycle map. The canonical product decomposition of P_3 makes it independent of representative factorizations at this critical event length.

The global attachment observation is

Theta_global:Q_global -> P_3[1] -> J_3[-2].

It is j_3 on degree -1 and zero on degree zero. Compose it with m_L and m_R. The two resulting observations agree after f_L and f_R because the source square already commutes.

On the full source module resolution [I^3 -> I^2], the analogous joint component represents j_3 delta_2. It is nonzero in the source-derived category by the same action argument as Nima's two-seam construction: an equivariant homotopy would require j_3(a b c)=a H(b c)=0, since the target's outer ideal action vanishes. This uses the full source module I^2, not only its root vector-space corner.

After the actual finite derived receiver, the shifted term is X_s tensor P_3 in degree -1. The common root carrier is retained once. Degree-zero coefficient-corner dimensions above must not be substituted for the dimensions of the full derived receiver.

## 7. The suspension sign is detectable

For homogeneous u in the unshifted complex A, fix the standard tensor-of-shifts comparison

sigma_(p,q):A[p] tensor B[q] -> (A tensor B)[p+q],

sigma_(p,q)(u tensor v)=(-1)^(q deg_A(u)) u tensor v.

This is a chain map with the usual shifted differentials.

A local derivative, regarded as a map from an unshifted relation space, lands in C_i[-1]. A two-seam attachment lands in (C_i tensor C_j)[-1] from its shifted product domain.

If these independently normalized maps are simply tensored:

- left grouping uses an underlying first-factor degree -2, giving sign +1;
- right grouping uses an underlying first-factor degree -1, giving sign -1.

Thus the naive right map is minus the globally normalized j_3 observation on every triple product. Its discrepancy cannot be detected by ranks.

To match the global source comparison, transport the attachment suspension to the same position before forgetting the grouping. Moving it past the one odd local seam supplies the missing minus sign. The corrected right map agrees with the left and with Theta_global.

This sign is fixed by the declared shift convention and the source multiplication square. It is not an adjustable phase fitted to the Green form. One normalization suffices; it does not authorize adding independent pair and triangle coherence parameters.

## 8. Opposite history and contragredient duality remain distinct

Use Nima's derivative-compatible single-seam reversal: raw reversal in degree -1, negative raw reversal in degree zero. For three factors use the supplied normalization

R_3 = - tau_reverse (R_1 tensor R_1 tensor R_1).

Its raw-degree signs are +,-,-,+ in degrees -3,-2,-1,0. On product cycles it agrees with ordinary source product reversal, without an added source sign. The same orientation phases satisfy c_(a+b)=c_a c_b (-1)^(a b).

This opposite-history correction and the suspension transport in section 7 address different typed operations, even though both involve a minus sign here.

Contragredient duality instead reverses cohomological degrees, with

d_(V^h)^n=(-1)^(n+1) (d_V^(-n-1))^vee.

Dualizing the strict comparison square reverses its arrows and preserves commutativity. The connecting projection becomes an inclusion in degree +1. The perfect-module dual is used before the actual receiver, and Nima's finite-projective tensor-Hom beta comparison supplies the paired presentation afterward. Neither operation is identified with opposite-history creation.

No nondegenerate self-pairing on P_3 is required. Given the prescribed nondegenerate ambient Green pairing, the observation j_3^vee beta has target P_3^h and is surjective. This is an ambient paired observation, not an inverse of the restricted Gram matrix on the relation image.

## 9. Analytical transfer and the remaining gate

The exact checker uses vertex-potential coordinates for the chamber source: an event has coefficient u_y-u_x. These are faithful finite source coordinates, not spectral sample values.

Voevodsky's function-valued Clark theorem transports this finite source into the carrier L(v)(z,t)=h_v(z) exp(i z t). Its injectivity follows from analytic continuation and Fourier uniqueness of the actual shell forcing. Tensoring those injections carries the three-seam cycle inclusion and the comparison identities to the analytical feature carrier.

The signed analytical pairing must retain its spectral indices pairwise. This note does not aggregate numerators over those indices or replace their denominators by a single denominator. The exact algebraic tests are not a computation of the function-valued Green kernel.

What is closed is this six-event, one-sided derived comparison cell and its explicit noncollapse test. What remains includes the detailed function-valued signed pairing comparison, general nonminimal factorization descent, and completed analytical topology and convergence. None is replaced by the finite associativity result.

## Verification

`python research/grothendieck/checkers/check_six_prime_derived_block_associativity.py`

Passed exact checks:

- local terminal ranks 6 and 150 in source potential coordinates;
- 2880 ordinary comparison cells, including independence of middle lifts;
- 720 shifted multiplication cells;
- an identity minor for the 2160-dimensional ordinary common image;
- closure and independence of the actual local seam cycles;
- rejection of naive shifted regrouping on every product channel;
- restoration by the declared Koszul transport and the corresponding conjugate-dual coefficient equality.

The higher opposite chain identities and Green beta conventions are supplied by Nima's separately checked construction. No new numerical spectral rank, fitted relation metric, or Agda verification is claimed.

References:

- `research/nima/the-attachment-opposite-comparison-needs-a-koszul-correction-and-a-distinct-green-dual.md`;
- `research/nima/the-relation-attachment-has-a-nonzero-source-equivariant-seam-realization.md`;
- `research/voevodsky/function-valued-clark-faithfulness-supersedes-finite-spectral-rank-probes.md`;
- `packet-refinement-preserves-the-relation-tower-but-coarse-seams-lose-higher-products.md`.
