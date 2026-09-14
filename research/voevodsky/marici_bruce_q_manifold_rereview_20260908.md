# Re-review of Bruce after the strict D35/D04 construction

Date: 2026-09-08

Reference: Andrew James Bruce, *Derived Associative Algebras and Cyclic Cohomology of Q-manifolds*, arXiv:2609.04805v1, especially Sections 2 and 3. Local source copies are `research/chatgpt/arxiv_2609.04805v1_section2.txt` and `...section3.txt`.

## Decision

Bruce's construction applies **after** a genuine Q-manifold has been supplied. It does not construct a Q-manifold from an arbitrary strict complex, homotopy pullback, or singular coefficient module. Therefore the newly completed strict `D35/D04` target does not by itself satisfy the geometric hypothesis needed to invoke Bruce's cyclic theory.

This is now a sharply located gap rather than the earlier chain-level gap: the first missing datum is a function algebra (or structure sheaf) that is locally the smooth supercommutative algebra of a supermanifold and an odd derivation `Q` on it whose linear/tangent sector is the constructed strict pullback.

## What Bruce supplies

For a Q-manifold `(M,Q)`, Bruce defines the odd derived associative product on functions from the ordinary multiplication and the homological vector field. In conventional notation it is the lopsided product

\[
f\star g=(-1)^{|f|+1}Q(f)g
\]

(up to the paper's displayed grading convention). Associativity follows from `Q^2=0` and the derivation law. A Q-morphism induces a homomorphism of these derived associative algebras.

For a compact, superoriented, unimodular Q-manifold with a Q-invariant Berezin volume, integration is a shifted graded trace and hence a derived cyclic zero-cocycle. Higher derived cyclic cohomology is then the cyclic cohomology of this derived product, with completed nuclear Frechet tensor products.

These are functorial consequences of a Q-manifold. They are not a representability theorem for complexes.

## Comparison with the completed Marici data

The strict target now has

\[
D_k=\operatorname{holim}\bigl(\omega[2]\xrightarrow q C\Pi^\vee[3]
\xleftarrow{\pi_k}E_{\beta,k}\Pi^\vee[3]\bigr)
\]

and a verified square-zero **module differential**. This is enough to form a linear dg module and, formally, a free graded-commutative dg algebra `Sym(D_k^vee)` with the differential extended as a derivation. That formal algebra is a candidate linear derived affine Q-space.

It is not yet Bruce's smooth Q-manifold for three reasons.

1. The native node `B=A/(I_E I_O)` is singular at the conductor. At the conductor all first derivatives of the nine mixed quadratic relations vanish, while the local embedding dimension is six and each branch has relative dimension three.
2. `D_k` contains conductor-supported `C` terms and the nonsplit dualizing complex. It has not been shown to be a locally free finite-rank super vector bundle over a smooth reduced base.
3. No compact supermanifold, Berezinian, or proof of `div_rho Q=0` has been supplied. Consequently Bruce's trace theorem cannot yet be applied.

Passing to `Sym(D_k^vee)` would solve only the formal derivation law: `d_D^2=0` extends to `Q^2=0`. It would not prove smooth representability, identify the physical outer vector fields as geometric vector fields, establish compactness/unimodularity, or show that its derived cyclic class is the requested P24 class.

## Exact next gate

Construct one of the following and state explicitly which category is intended:

- a genuine smooth supermanifold `M_k` with homological vector field `Q_k`, together with an identification of the required linear/tangent sector with `D_k`; or
- a derived/formal affine enhancement `Spec Sym(D_k^vee)` and a proved extension of Bruce's definitions from smooth Q-manifolds and nuclear Frechet function algebras to this singular derived setting.

In either route one must then provide:

1. geometric lifts of the outer operation vector fields and their commutators with `Q_k`;
2. the reflection comparison `M_35 <-> M_04`;
3. a Berezinian/density and a calculation of the modular class;
4. compactness or an explicit compact-support/LF replacement;
5. the cyclic cocycle and a direct comparison with the P24 deformation class.

## Conclusion

Re-reading Bruce is useful now because it separates the completed algebraic target from the remaining geometry. It validates the derived-product and cyclic-cohomology steps **conditionally**, but it does not close Part III. The first unresolved object is the Q-manifold (or a justified derived analogue), not `q`, the pullback differential, or the eight spatial maps.
