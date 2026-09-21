# Coherent spectral realization: matrix blocks and extension gluing

## Result

The translation Fourier theorem extends in two concrete directions.

1. For a finite nonabelian group, irreducible matrix realizations give a Fourier isomorphism. The corresponding Morita equivalence decomposes every finite iterated Waldhausen closure diagram.
2. For the incidence algebra of a directed two-stage system, scalar realizations recover its diagonal quotient. Full reconstruction is the arrow category of its two component complexes, including their attachment map. The attachment is an Ext¹ class in the elementary case.

These are standard representation-theoretic constructions applied explicitly to the nested closure language. We prove the identifications and their compatibility with nesting. The two-stage example provides a complete extension-bearing model.

Work over C. Perf(A) denotes the stable infinity-category of perfect left A-module complexes; mapping objects below are derived mapping complexes. All nesting depths and diagrams are finite.

## 1. Nonabelian Fourier theorem

Let G be a finite group. Choose one unitary irreducible representation π:G→U(V_π) in each equivalence class, and put d_π=dim V_π. On C[G] use convolution

\[
(f*h)(x)=\sum_{ab=x}f(a)h(b).
\]

Use the positive-representation Fourier convention

\[
\mathcal F_\pi(f)=\sum_{g\in G}f(g)\pi(g).
\tag{1}
\]

For abelian G this is the earlier convention with conjugate characters relabelled. This convention preserves product order for noncommuting matrices:

\[
\mathcal F_\pi(f*h)=\mathcal F_\pi(f)\mathcal F_\pi(h).
\tag{2}
\]

Indeed, expand the left side over a,b and use π(ab)=π(a)π(b).

### Orthogonality and completeness

Maschke's averaging argument gives complete reducibility: average any projection onto an invariant subspace over G to produce an equivariant projection. Schur's lemma then gives matrix-coefficient orthogonality

\[
\frac1{|G|}\sum_g\pi(g)_{ij}\overline{\rho(g)_{kl}}
=\begin{cases}
\delta_{ik}\delta_{jl}/d_\pi,&\pi=\rho,\\
0,&\pi\ne\rho.
\end{cases}
\tag{3}
\]

For completeness, average π(g)Aρ(g)⁻¹. It is an intertwiner. It vanishes between distinct irreducibles; on one irreducible it equals Tr(A)I/d_π. Taking matrix units proves (3).

The regular representation contains V_π with multiplicity d_π. This follows by applying (3) to its character: the regular character is |G| at the identity and zero elsewhere, so its inner product with the character of π is d_π. Complete reducibility therefore gives

\[
\sum_\pi d_\pi^2=|G|.
\]

Consequently the orthogonal matrix coefficients form a basis of functions on G. Thus (1) is an algebra isomorphism

\[
\boxed{\mathbb C[G]\simeq\bigoplus_\pi\operatorname{End}(V_\pi).}
\tag{4}
\]

Explicitly,

\[
f(g)=\frac1{|G|}\sum_\pi d_\pi
\operatorname{Tr}\bigl(\pi(g^{-1})\mathcal F_\pi(f)\bigr).
\tag{5}
\]

To verify (5), substitute (1). The coefficient of f(h) is |G|⁻¹ times the regular character at g⁻¹h, hence δ_(g,h).

With f*(g)=overline(f(g⁻¹)), equation (1) gives F_π(f*)=F_π(f)†. Orthogonality yields

\[
\sum_g f(g)\overline{h(g)}
=\frac1{|G|}\sum_\pi d_\pi
\operatorname{Tr}\bigl(\mathcal F_\pi(f)\mathcal F_\pi(h)^\dagger\bigr).
\tag{6}
\]

The weight d_π/|G| is the finite nonabelian Plancherel measure. The multiplication channels are matrix-valued and retain order.

### Coherence and nesting

The nerve N(BG) supplies the composition correspondences exactly as in the abelian case. Its scalar realizations are replaced by all finite-dimensional irreducible unitary realizations.

Morita equivalence sends an A-module M to its multiplicity complexes

\[
W_\pi=\operatorname{Hom}_G(V_\pi,M),
\qquad M\simeq\bigoplus_\pi V_\pi\otimes W_\pi.
\]

This is an exact equivalence

\[
\operatorname{Perf}(\mathbb C[G])
\simeq\prod_\pi\operatorname{Perf}(\mathbb C).
\tag{7}
\]

The fixed representation spaces V_π remain part of the reconstruction functor. On the regular module, each V_π occurs d_π times, accounting for the block size in (4).

Exact equivalences preserve zero objects and bicartesian squares; finite products compute both componentwise. Therefore, for every r and n₁,…,nᵣ,

\[
S_{n_1}\cdots S_{n_r}\operatorname{Perf}(\mathbb C[G])
\simeq\prod_\pi S_{n_1}\cdots S_{n_r}\operatorname{Perf}(\mathbb C).
\tag{8}
\]

This equivalence commutes with interval restrictions, face and degeneracy maps, and all cut-change comparisons. The comparisons are induced from the same exact diagrams. Their higher compatibilities are transported by the exact equivalence as well.

## 2. A two-stage incidence system

Take the ordered set 0<1. Its interval algebra has basis e₀,e₁,u and faithful matrix realization

\[
e_0=\begin{pmatrix}1&0\\0&0\end{pmatrix},
\quad e_1=\begin{pmatrix}0&0\\0&1\end{pmatrix},
\quad u=\begin{pmatrix}0&0\\1&0\end{pmatrix}.
\]

Here u is the directed interval 0→1. An element is

\[
(a,b,c)\equiv\begin{pmatrix}a&0\\c&b\end{pmatrix}.
\]

Cutting the interval at either endpoint gives convolution

\[
(a,b,c)(a',b',c')=(aa',bb',ca'+bc').
\tag{9}
\]

This is the incidence convolution of the poset nerve, with row=target and column=source. The same Segal/2-Segal gluing mechanism now produces a nonsemisimple algebra A.

### Scalar observers and the radical

Every unital scalar algebra homomorphism A→C annihilates u, because u²=0. Orthogonal idempotents e₀,e₁ sum to 1, so their scalar images are (1,0) or (0,1). The two scalar observers are therefore

\[
\lambda_0(a,b,c)=a,\qquad\lambda_1(a,b,c)=b.
\]

Their combined kernel is Cu, the Jacobson radical. Thus scalar observation gives the quotient A→C×C. The faithful two-dimensional triangular realization retains c and reconstructs every element.

The center of A is C·I. In fact commuting with e₀ forces c=0, and commuting with u forces a=b. The vertex idempotents are noncentral; they decompose vector spaces while leaving a directed attachment between their components.

## 3. Exact reconstruction of objects and maps

A finite-dimensional left A-module is exactly a pair of vector spaces and a map

\[
M=(V_0\xrightarrow{T}V_1).
\tag{10}
\]

Proof: take V_i=e_iM; the action of u maps V₀ to V₁ and vanishes on V₁. Conversely define

\[
(a,b,c)(v_0,v_1)=(av_0,\;cT v_0+bv_1).
\]

Equation (9) verifies the module law. A module map is a pair (f₀,f₁) satisfying

\[
T_W f_0=f_1T_V.
\tag{11}
\]

This establishes an equivalence of the module category with the arrow category of vector spaces.

For bounded complexes the derived equivalence is

\[
\boxed{\operatorname{Perf}(A)
\simeq\operatorname{Fun}([1],\operatorname{Perf}(\mathbb C)).}
\tag{12}
\]

Here A is the path algebra of the acyclic quiver 0→1; its global dimension is one, so every bounded finite-dimensional module complex is perfect. Derived arrows can be represented by chain maps after replacing complexes, and their homotopies are encoded by the mapping complex below. This describes the derived enhancement in (12).

For arrows T_V and T_W,

\[
\operatorname{RHom}_A(V,W)
\simeq
\operatorname{fib}\left[
\operatorname{RHom}(V_0,W_0)\oplus\operatorname{RHom}(V_1,W_1)
\xrightarrow{D}\operatorname{RHom}(V_0,W_1)
\right],
\tag{13}
\]

where D(f₀,f₁)=T_W f₀−f₁T_V and fib(D)=Cone(D)[−1]. It is the homotopy-commutative-square mapping object in the arrow category. For vector spaces concentrated in degree zero it has

\[
\operatorname{Hom}_A(V,W)=\ker D,
\qquad\operatorname{Ext}^1_A(V,W)=\operatorname{coker}D.
\tag{14}
\]

One can also derive (13) from the length-one projective resolution of quiver representations, so its higher comparison data are explicit.

### Faithful coherent observers

Let P₀=(C→C,id), P₁=(0→C). Then

\[
\operatorname{RHom}_A(P_i,M)\simeq V_i.
\]

The canonical inclusion P₁→P₀ induces, by precomposition, the map V₀→V₁. Thus the complete observer packet consists of the two component complexes together with the map induced by this relation between probes. It is faithful by the explicit reconstruction above. P₀⊕P₁ is the projective generator A.

This is a concrete enriched-Yoneda realization: observers include their maps and composition law.

## 4. The first extension class

Let S₀=(C→0), S₁=(0→C). There is a projective resolution

\[
0\longrightarrow P_1\longrightarrow P_0\longrightarrow S_0\longrightarrow0.
\]

Since Hom(P₀,S₁)=0 and Hom(P₁,S₁)=C,

\[
\operatorname{Ext}^1_A(S_0,S_1)\cong C.
\]

Its representatives are

\[
0\longrightarrow S_1\longrightarrow E_t\longrightarrow S_0\longrightarrow0,
\qquad E_t=(C\xrightarrow{t}C).
\tag{15}
\]

With the end identifications fixed, t is the extension coordinate. The sequence splits exactly at t=0: a section of the quotient must have identity at vertex 0 and zero at vertex 1, and (11) then requires t=0.

In the derived category this is the triangle

\[
S_1\longrightarrow E_t\longrightarrow S_0
\xrightarrow{\delta_t}S_1[1],
\]

where δ_t represents t in Ext¹. All E_t have the same component dimensions and the same scalar trace on every algebra element:

\[
\operatorname{Tr}_{E_t}(a,b,c)=a+b.
\]

Yet dim End(E₀)=2 and dim End(E₁)=1. Indeed D:C²→C is (α,β)↦t(α−β). The objects E₀ and E₁ are distinguished by their coherent attachment.

Nonzero t give isomorphic middle objects if endpoint framings are allowed to vary. Keeping those framings distinguishes the individual extension classes.

## 5. Nested closure with attachment retained

Functor categories into a stable category are stable, with limits and colimits computed pointwise. Consequently

\[
S_n\operatorname{Fun}([1],\mathcal C)
\simeq\operatorname{Fun}([1],S_n\mathcal C).
\]

To prove this, uncurry an interval diagram of arrows into a diagram on Ar[n]×[1]. Its zero and bicartesian conditions are checked at each endpoint of [1]. Currying back gives an arrow between complete interval diagrams. This is an equivalence of the full diagram categories with the specified exactness conditions, including all mapping spaces.

Iterating yields

\[
\boxed{
S_{n_1}\cdots S_{n_r}\operatorname{Perf}(A)
\simeq
\operatorname{Fun}\left([1],
S_{n_1}\cdots S_{n_r}\operatorname{Perf}(\mathbb C)\right).
}
\tag{16}
\]

Every nested closure is therefore two nested component closures joined by a natural attachment map. Each interval has its own arrow, and the interval restriction maps form coherent squares with these arrows. Cofibers, cuts, and reconstruction are computed pointwise and retain their induced attachment.

Taking maximal infinity-groupoids gives the corresponding statement about spaces of nested closure objects. The arrow category is formed before taking the core; it retains noninvertible attachments.

Equations (8) and (16) are two exact forms of the same reconstruction question:

- semisimple group algebra: a product of independent component closure systems, with irreducible representation spaces specifying matrix readout;
- directed interval algebra: a diagram of component closure systems joined by extension data.

## 6. General finite-poset reconstruction and a higher extension

Let P be any finite poset, and let A_P be its category algebra, with basis u_(q,p) for p≤q and product

\[
u_{r,q}u_{q,p}=u_{r,p},
\]

with unmatched endpoints giving zero. A left module is precisely a diagram of vector spaces on P. Since P is finite and its nonidentity arrows strictly increase the order, the normalized bar resolution has finite length. Its degree-k terms are sums of projectives indexed by strict chains p₀<⋯<p_k, tensored with the vector space at p₀. The augmentation is evaluation of the diagram; the usual bar contraction proves exactness. Thus A_P has finite global dimension and bounded finite-dimensional module complexes are perfect.

Derived diagram rectification identifies their derived category with homotopy-coherent P-diagrams of perfect complex vector spaces. Hence

\[
\operatorname{Perf}(A_P)
\simeq\operatorname{Fun}(N(P),\operatorname{Perf}(\mathbb C)).
\tag{17}
\]

Here the functor category is infinity-categorical. Composable routes carry the specified coherent comparisons. The diagram-model proof uses objectwise quasi-isomorphisms and projective replacements; its homotopy-coherent nerve is the displayed functor category.

Pointwise exactness gives the full nested reconstruction theorem

\[
\boxed{
S_{n_1}\cdots S_{n_r}\operatorname{Perf}(A_P)
\simeq
\operatorname{Fun}\left(N(P),
S_{n_1}\cdots S_{n_r}\operatorname{Perf}(\mathbb C)\right).
}
\tag{18}
\]

The source poset therefore prescribes the complete pattern of component observers and their attachment comparisons. This covers every finite interval poset with its full incidence relations.

### Diamond: the first Ext² attachment

Take the diamond 0<1<3 and 0<2<3. The two composites 0→3 agree in its category algebra. Let P_i=A_P e_i and S_i be the vertex simple. There is a projective resolution

\[
0\longrightarrow P_3
\xrightarrow{(1,-1)}P_1\oplus P_2
\xrightarrow{(1,1)}P_0
\longrightarrow S_0\longrightarrow0.
\tag{19}
\]

The displayed constants denote the canonical path maps where their supports overlap. At vertex 3 this is the exact sequence C→C²→C with difference and sum maps. At vertices 1 and 2 the corresponding map to P₀ is the identity; at vertex 0 the augmentation to S₀ is the identity. This verifies exactness vertexwise and proves (19).

Since Hom(P_i,S₃)=S₃(i), applying Hom(-,S₃) leaves a single C in degree two. Thus

\[
\operatorname{Ext}^1(S_0,S_3)=0,
\qquad
\operatorname{Ext}^2(S_0,S_3)=\mathbb C.
\tag{20}
\]

The two-stage example carries a degree-one attachment. The diamond carries a genuine degree-two extension between its bottom and top simples. Its source is the relation between the two routes. Formula (18) retains this derived information at every nesting depth.

## 7. Positive metric diagnostic

In the triangular model u is nonzero and nilpotent. A normal nilpotent operator on a finite-dimensional positive Hilbert space is zero, by the spectral theorem. Thus u cannot be normal for any positive definite inner product.

The faithful matrices form a non-self-adjoint algebra. Adjoining the usual adjoints adds the reverse matrix unit u† and generates all M₂(C). Its representation theory is a different, semisimple operator algebra.

More generally every finite-dimensional complex C*-algebra is a sum of matrix algebras. Persistent extensions in a finite model locate the failure of a proposed independent orthogonal-block interpretation: the retained algebra carries directed coupling, a different involution, or a category beyond finite-dimensional C*-modules.

This supplies an operational test for a richer coherence system: identify its composition algebra, its radical, its involution, and the maps between its projective probes before selecting spectral blocks.

## 8. Verification and scope

The checker `check_coherent_matrix_and_extension_realization.py` performs exact rational checks on:

- all six elements of S₃, with its trivial, sign, and standard representations;
- representation laws, noncommuting block order, full-basis inversion, and Plancherel;
- the invariant positive Gram matrix of the rational standard representation;
- triangular convolution, the scalar observer kernel, and its square-zero radical;
- the center and the Hom/Ext dimensions of the split and nonsplit arrows;
- exactness of the diamond projective resolution at every vertex, and its degree-two extension.

The nested equivalences are proved by exact functor-category arguments above. Finite tests exercise the algebraic examples; they do not replace the categorical proofs.

The next source-specific application is an explicit algebra or enriched category of the chosen closure system, followed by its probe-and-attachment reconstruction. The two models here provide complete worked templates with opposite extension behavior.
