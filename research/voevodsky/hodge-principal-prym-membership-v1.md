# Global iteration 16 (new series 6/10): the fixed principal eightfold is not a smooth etale Prym

## Result and exact scope

The constructed principally polarized Gaussian eightfold (Y,theta_Y) is **not** the canonical principally polarized Prym of any smooth connected etale double cover. In particular there is no smooth etale cyclic-quartic genus-17/9/5 tower whose primitive Prym is this specified principally polarized Y.

The same proof covers all **four** Gaussian-equivariant degree-nine principal quotients of the fixed A with q*theta=E_A and the native Gaussian action. It does not exclude other polarizations, different principal isogeny models, ramified or singular/admissible cover constructions, or arbitrary Pryms isogenous to A. It neither invalidates the preceding actual quotient construction nor changes X, alpha or the algebraicity question.

The new obstruction is geometric, not another determinant mismatch: the fixed polarization leaves a principal elliptic factor untouched, while the remaining sevenfold contains an elliptic curve of polarization degree three. Mumford's theorem then forces an impossible hyperelliptic curve.

## 1. Actual product structure left by the gluing

Write B=E_+ x E_- using the two actual CM elliptic factors of the previous construction. Its polarization is theta_+ + 3 theta_-. The subgroup H is supported entirely in X x E_-:

    H=Z[i]*(e6+(1+i)e8)/3 modulo the old lattice.

The untouched coordinate e7 is the actual J_A-stable E_+ factor, not just a diagonal entry of an abstract Hermitian matrix. Thus the lattice, complex structure and polarization all split:

    (Y,theta_Y) = (E_+,theta_+) x (Z,theta_Z),
    Z=(X x E_-)/H, dim Z=7,

and theta_Z is principal. This is an isomorphism of principally polarized abelian varieties, not merely an isogeny decomposition. No lattice marking matrix is asserted to be an endomorphism of X x B.

For every one of the four mixed F9 isotropic lines, both coordinate projections are injective. In particular H intersects E_- trivially. The quotient therefore embeds E_- into Z, and restriction of the principal polarization has degree

    deg(theta_Z restricted to E_-)=3.

This degree is a line-bundle degree on the elliptic curve, not the degree-nine isogeny, nor the degree of the polarization homomorphism (which would be nine for a degree-three elliptic polarization). The untouched factor E_+ has degree one.

The four-line enumeration is exhaustive only for the specified pullback polarization and Gaussian action: ker lambda_A is F9^2, an invariant subgroup of order nine is an F9 line, and isotropy requires slopes of norm two. Other polarizations can have different kernels and are not excluded.

## 2. The principal sevenfold is indecomposable

The previous fixed-point results give X simple with End^0(X)=Q(i), NS(X)_Q of rank one and raw Hermitian discriminant norm class -3 invariant under repolarization and isogeny. Since X has dimension six and E_- dimension one, they are not isogenous; hence

    End^0(Z)=Q(i) x Q(i).

If the principally polarized Z decomposed nontrivially, its factors would have dimensions six and one, isogenous to X and E_- respectively. The actual Gaussian automorphism of Z commutes with their rational idempotents (the displayed endomorphism algebra is commutative), so it preserves both actual factors and their principal polarizations. The sixfold factor would carry an integral Gaussian lattice, balanced signature (3,3) and a principal polarization. Its integral unimodular Hermitian determinant would then be -1.

This contradicts the retained -3 norm class: the ratio 3 has odd 3-adic valuation, whereas a rational Gaussian norm has even valuation at the inert prime three. Consequently (Z,theta_Z) is indecomposable. This argument uses the original simple-factor rigidity, not a claim that the sevenfold itself is simple.

Thus the indecomposable principal factors of Y have dimensions exactly one and seven. We import the standard uniqueness of decomposition into indecomposable principally polarized factors. Smooth curve Jacobians are indecomposable, since their canonical theta divisors are irreducible.

## 3. Fresh primary theorem, with inequalities checked in the PDF

David Mumford, *Prym Varieties I*, Contributions to Analysis (1974), pp. 325-350, section 7, Theorem (a) and (d), printed p. 344; hyperelliptic construction on printed p. 346. The complete author-hosted PDF was retrieved through its directory listing:

https://www.dam.brown.edu/people/mumford/alg_geom/papers/1974a--PrymVar-I-NC.pdf

The retained rendered PDF pages 20 and 22 show the inequalities and polarized decomposition. Existing OCR corrupts some mathematical signs, so the inequalities are read from those images, not guessed from plain text. PDF page 4 (printed 328) records Jacobian norm/pullback duality. Full PDF, full extracted OCR, all three images and directory/search provenance are hashed in `inputs/hodge-principal-prym-membership-v1/sources.json`.

Mumford's theorem concerns a smooth connected unramified double cover with base curve C of genus g and its **canonical principal** Prym polarization Xi:

- if C is not hyperelliptic and g>=5, dim Sing Xi <= g-5;
- if C is hyperelliptic, its Prym is a hyperelliptic Jacobian or a product of two hyperelliptic Jacobians, as principally polarized varieties.

On p. 346 the branch points split into sets of sizes 2h+2 and 2k+2 with h+k+1=g; the principal Prym is J(C_h) x J(C_k). Factors of genus zero disappear.

The local `pnpm pdf:search Prym` returned no matches in its bounded index. This did not establish literature absence; direct author-directory retrieval supplied the primary theorem. The source is not a dimension-eight cycle-algebraicity theorem, and its use here produces no cycle witness.

## 4. A hypothetical smooth etale Prym forces a hyperelliptic sevenfold Jacobian

Suppose (Y,theta_Y) were the canonical principally polarized Prym of a smooth connected etale double cover. Its base genus would be nine because its Prym has dimension eight.

The product theta divisor on E_+ x Z is, up to translation,

    ({point} x Z) + (E_+ x Theta_Z).

These two components meet along {point} x Theta_Z, of dimension six, and the product equation is singular there. Therefore dim Sing theta_Y >=6. A nonhyperelliptic genus-nine base would have dim Sing Xi <=9-5=4 by Mumford (d), a contradiction. This is a theta-divisor singularity calculation on the actual target, not a moduli-dimension avoidance argument.

The base must therefore be hyperelliptic. By Mumford (a), Y is a product of at most two hyperelliptic Jacobians with total dimension eight. Uniqueness of indecomposable principal factors and the preceding sevenfold indecomposability force dimensions (1,7); hence (Z,theta_Z) would be the canonical Jacobian of a smooth hyperelliptic genus-seven curve D.

## 5. The degree-three elliptic map contradicts genus seven

Let j:E_- -> Z be the actual embedded elliptic curve of section 1, with j*theta_Z of degree three. If Z=J(D) as principally polarized varieties, let f:J(D)->E_- be the polarization adjoint of j and let phi:D->E_- be its composition with an Abel--Jacobi map. Standard Jacobian functoriality identifies phi_*=f and phi*=j. The elliptic polarization restriction gives

    f j=[3].

For a nonconstant map of curves, norm-pullback composition is multiplication by its degree. Therefore phi has degree three. This uses principal polarizations on both Jacobians; no unpolarized isogeny is substituted for an isomorphism.

Hyperellipticity also supplies a degree-two map D->P1. The combined map

    D -> P1 x E_-

is birational onto its image: the function-field degree onto the normalization of that image divides both two and three, so is one. The image has projection degrees (2,3). Its self-intersection is 12 and its canonical intersection is -4. Surface adjunction gives arithmetic genus

    1+(12-4)/2=5.

The normalization has genus at most five, contradicting genus(D)=7. Equivalently this is the coprime-degree case of the Castelnuovo--Severi bound g<=2*0+3*1+(2-1)(3-1)=5. The argument does not claim that equality controls actually construct a curve, nor apply a coprime-degree shortcut when the degrees are not coprime.

This contradiction completes the fixed-principal-target exclusion. No Torelli classification of arbitrary Gaussian Jacobians is required; only the hyperelliptic Jacobians forced by the primary Prym theorem are used.

## 6. What changes in the live frontier

The preceding degree-nine quotient and all cycle-preserving transfer maps remain valid. What fails is the proposed **exact canonical principally polarized smooth etale Prym realization** of those four quotients. Searching for that exact genus-17/9/5 tower on the fixed theta_Y is now a closed bounded attempt, not a ready action.

A genuinely different polarization or principal isogeny model avoiding the forced principal elliptic factor is not excluded. Neither are ramified Pryms, singular/admissible covers, other Gaussian embeddings or unrelated cycle constructions on X. Any new model must provide its actual compatible correspondence and typed cycle theorem, and any supplied eightfold cycle must still be tested by all four channels. Being isogenous to a Prym or merely having nonzero Chow is not by itself the required exceptional class.

All-cycle annihilation and nonzero algebraic-witness search remain open, as does independent review. This argument does not imply alpha nonalgebraic or algebraic, and is not a Hodge conjecture verdict.

## Reproduce and audit

Contract: `research/conjecture_net/contracts/hodge-principal-prym-membership.v1.json`.
Checker: `research/voevodsky/checkers/check_hodge_principal_prym_membership.py`.
Receipt: `research/voevodsky/results/hodge-principal-prym-membership-v1.json`.

    python research/voevodsky/checkers/check_hodge_principal_prym_membership.py

Exact finite controls enumerate all four kernel lines and their trivial axis intersections, test discriminant pairings, the inherited simple-factor norm barrier, theta dimension comparison and the coprime surface-adjunction bound. They do not formally prove Mumford's theorem, uniqueness of principal factors, Jacobian adjoint functoriality or algebraic geometry foundations. Those are explicit mathematical imports in the written proof. Primary-source freshness and headless graph closure are wiring checks, not independent mathematical review. Pins v1-v16 and the predecessor snapshot are retained unchanged.
