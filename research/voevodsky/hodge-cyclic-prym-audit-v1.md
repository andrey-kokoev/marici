# Global iteration 14 (new series 4/10): cyclic-quartic Prym construction audited

## Result

We investigated an actual positive cycle construction instead of adding another detector. Koike's *Algebraicity of some Weil Hodge Classes*, Canadian Mathematical Bulletin 47 (2004), 566--572, DOI https://doi.org/10.4153/CMB-2004-055-x, proves dominance of an etale cyclic-quartic Prym map and a sixfold algebraicity corollary in its specified family.

The fixed X cannot be obtained, even after repolarization and isogeny, as the balanced primitive sixfold Prym of an order-four curve automorphism. More strongly the same arithmetic obstruction applies when the cyclic-quartic cover is ramified. This is a new rejection of this geometric presentation, not a repetition of the sixfold secant-sheaf theorem's hypothesis table.

The key point is independent of source sign conventions: the restricted principal Jacobian polarization has kernel killed by two, while the deck action supplies an integral Gaussian lattice. Its raw Hermitian discriminant has norm class **-1**. The fixed isogeny class of X has norm class **-3**. The ratio has odd 3-adic valuation and is not a Gaussian norm.

No nonzero algebraic Weil class, all-cycle annihilation or Hodge verdict follows. Other Prym presentations, constructions without the specified deck action, and a dimension-eight route for A remain unexcluded.

## 1. Fresh primary-source inspection

The publisher PDF was obtained from

https://www.cambridge.org/core/services/aop-cambridge-core/content/view/S0008439500021986

and retained with SHA-256, full extracted text, and images of PDF pages 2 and 3. DOI metadata is also retained, but is not a replacement for the PDF. All seven PDF pages were read. Relevant scope:

| PDF page / journal page | Role |
|---|---|
| 1 / 566 | Abstract: dominance for fourth cyclic etale covers of genus-four curves, and algebraicity for that family. |
| 2 / 567 | Tower C13 -> C7 -> C4; P=Prym(C13/C7) is a principally polarized sixfold, with order-four Galois action and Gaussian Weil structure; target Shimura variety has dimension nine. |
| 3 / 568 | Theorem 2.1 proves an isomorphic codifferential at a cover and hence dominance. Corollary 2.1 states the sixfold algebraicity result with the source's printed delta=1. |
| 4--7 / 569--572 | Complete-intersection curve construction and the explicit multiplication-map proof. |

The PDF really prints delta=1; this is not a missing-minus OCR repair. We do **not** identify that symbol with a raw positive determinant in our convention. The source's determinant/discriminant notation is not machine-translated into our norm quotient. Instead Sections 2--3 below compute our raw norm class directly from the Prym geometry. This avoids using a convention ambiguity as either a positive transplant or an alleged counterexample to the paper.

Searches used `pnpm pdf:search`. The default repository index did not include these retained Hodge papers. The older dedicated Hodge index located the Koike citation; a new one-PDF index was built for the publisher PDF and searched for theorem/discriminant scope. Its repository-wide added/removed warnings do not establish missing literature. Negative `Prym` searches in other bounded indexes were not used as evidence of nonexistence. Search outputs and the successful source bytes are pinned; no exhaustive current-literature conclusion is asserted.

## 2. Orthogonal involution factors force a two-primary polarization

Let C be a smooth projective curve with an automorphism rho of order four. On J=Jac(C), set iota=rho^2 and

    P=im(1-iota)=ker(1+iota)^0,
    Q=im(1+iota).

These are connected abelian subvarieties. The primitive Gaussian factor is P; on it iota=-Id, so rho^2=-Id. The construction includes etale and ramified quotient maps C -> C/<rho>. We consider the case dim P=6 with Gaussian signature (3,3), as necessary for the fixed target.

The canonical principal polarization lambda_J is invariant under every curve automorphism. Hence P and Q are orthogonal: for p in the anti-invariant tangent space and q in the invariant one, E(p,q)=E(-p,q)=-E(p,q), so their pairing vanishes. Dimension and connectedness identify Q with P-perpendicular. By standard duality of abelian subvarieties in a principally polarized variety, the restriction lambda_P has

    ker(lambda_P)=P intersection Q.

If x lies in the intersection, iota(x)=-x since x lies in P, but iota(x)=x since x lies in Q. Thus 2x=0. The finite polarization kernel is killed by two.

Consequently every elementary divisor of lambda_P is 1 or 2:

    type(lambda_P)=(1^(6-a),2^a), 0<=a<=6,
    chi(lambda_P)=2^a, deg(lambda_P)=2^(2a).

This is an upper list of possible types; we do not claim every type occurs for a curve Prym. No ramification classification is needed for the kernel proof. In the etale double-cover case of Koike's tower, the restricted polarization is twice the usual principal Prym polarization, which is consistent with this argument.

## 3. Integral deck action is essential to the raw discriminant computation

On the actual lattice Lambda=H1(P,Z), rho defines an integral Z[i] action. The lattice is torsion-free as a Z[i] module; Z[i] is a PID, so it has a Gaussian basis of rank six. In this basis the restricted polarization E defines

    h(v,w)=E(v,rho w)+i E(v,w).

This is a Hermitian form with Gaussian integral entries. Its imaginary part is E and, in the corresponding underlying integral basis,

    det(E)=(det h)^2,
    abs(det h)=chi(lambda_P)=2^a.

Balanced signature (3,3) makes det h negative in our convention. Thus

    det h=-2^a,
    det h/(-1)=Norm((1+i)^a).

The raw discriminant norm class is therefore -1. Rescaling from the restricted etale polarization to its principal Prym half does not change that norm class: in K-dimension six the determinant scales by q^6=Norm(q^3).

It is not legitimate to drop the integral deck-action hypothesis. A rational Q(i) embedding on an arbitrary isogeny model need not preserve its lattice. The argument turning polarization Euler characteristic into a Gaussian-basis determinant specifically uses the integral rho action. We do not infer the same result for every principally polarized variety with only rational Gaussian multiplication.

As a finite lattice check, let rho cyclically permute each of three E^4 blocks in the product principally polarized E^12. The primitive anti-involution factor is E^6. Its Gaussian Hermitian blocks are

    [ 0   2i ]
    [-2i   0 ],

with total determinant (-4)^3=-64. This is a PPAV lattice control, **not** a claimed smooth-curve Jacobian or a presentation of the fixed X. The checker also verifies Norm((1+i)^a)=2^a for every candidate elementary-divisor shape.

## 4. Why no repolarized or isogenous model of the fixed X repairs it

The prior fixed-point argument proves End^0(X)=Q(i) and NS(X)_Q=QE. Every polarization scales the Hermitian form by a positive rational q, so its determinant scales by q^6, a Gaussian norm. A K-basis change contributes Norm(det S). Any imaginary quadratic embedding on any isogeny model transports to one of i or -i in End^0(X). Neither changes the raw determinant norm class. Thus every such model retains **-3**.

A cyclic-quartic primitive Prym presentation would instead supply the integral Gaussian structure above with norm class -1. The ratio is

    3/2^a,
    v3(3/2^a)=1.

For a Gaussian rational z, v3(Norm(z)) is even: after removing a common power of three from its two integer numerators, their squares cannot sum to zero modulo three unless both are zero. Denominators contribute even valuation as well. Therefore the ratio is not a norm. The previously proved fixed-isogeny rigidity is reused with this independently derived geometric input.

The checker evaluates all seven upper polarization-type bounds and 140 rational rescaling/basis determinant controls. These regressions are not the universal argument: the lattice/polarization proof and inert-prime parity establish it for all allowed presentations, including ramified covers and arbitrary isogenies of the fixed target.

The same obstruction persists in a marked Weil deformation with transported rational K action and polarization: its Hermitian local system has constant determinant norm class. No claim about all unmarked moduli paths, unrelated correspondences, or arbitrary changes of structures at special fibers is made.

## 5. What remains open

- This rejects the primitive sixfold presentation coming from an order-four curve automorphism, not every double-cover Prym, generalized Prym, or subvariety/correspondence construction.
- It does not reject all ramified covering constructions. Only the stated cyclic-quartic primitive presentation is covered.
- A moduli dimension bound by itself would not exclude this explicitly specified X. Algebraic independence in its rational period chart proves the earlier rational Hodge-tensor statements, not automatic avoidance of every proper algebraic locus in a Shimura variety. No such dimensional shortcut is used.
- The auxiliary A is eight-dimensional and split. It is not excluded by the sixfold isogeny-class argument. But the Koike sixfold theorem cannot be applied to it; an actual dimension-eight cover/cycle construction and transfer hypotheses would still have to be supplied.
- No algebraic representative of alpha, nonalgebraicity proof, all-cycle vanishing, or completed witness search has resulted.

Next seek a genuinely different source on X, a covering construction without this deck-action presentation, or an actual dimension-eight Prym realization of A with correctly licensed cycles. The smooth-threefold and reflexive singularity-cycle criteria from the preceding turn remain available for testing a supplied object.

## Artifacts and trust

Contract: `research/conjecture_net/contracts/hodge-cyclic-prym-audit.v1.json`.
Checker: `research/voevodsky/checkers/check_hodge_cyclic_prym_audit.py`.
Receipt: `research/voevodsky/results/hodge-cyclic-prym-audit-v1.json`.
Sources: `research/voevodsky/inputs/hodge-cyclic-prym-v1/sources.json`.

    python research/voevodsky/checkers/check_hodge_cyclic_prym_audit.py

Primary-source scope is pinned, not every theorem in the paper formally verified. Classical polarization duality, integral-lattice theory and the prior endomorphism/Picard rigidity are standard written/imported mathematics. Finite norm and matrix checks are exact rational controls, not proof-assistant certification or a Hodge verdict. Immutable predecessor pins are retained.
