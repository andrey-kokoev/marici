# Finite-Ringed Duality Types the D03 q-Shriek

## Result

The extraordinary inverse image for the actual Entry-356 target projection
is defined on the full derived category of modules. The remaining
Beck--Chevalley, dualizing-trace, and PC-purity gates concern its computation
and comparison, not its type or existence.

Entry 352 constructs the finite ringed target

\[
X=((P_{K_6}^{\rm or})^{\rm op},\mathcal O_X)
\]

and its module \(\mathcal L^{\check C}\). Entry 356 constructs the finite
ringed correspondence

\[
I_{\rm occ}
\xleftarrow{\ p\ }
Z_{03}^{\rm pre}=G_{03}\times I_{\rm occ}
\xrightarrow{\ q\ }
X
\]

with \(\mathcal O_Z=q^{-1}\mathcal O_X\). Both \(p\) and \(q\) are actual
morphisms of ringed finite spaces.

Theorem 4.1 of Fernando Sancho de Salas and Juan Francisco Torres Sancho,
“Derived category of Finite Spaces and Grothendieck Duality”
(arXiv:1904.06935), states that for every morphism
\(f:Y\to X\) between finite ringed spaces,

\[
Rf_*:D(Y)\longrightarrow D(X)
\]

has a right adjoint. Apply this theorem to the Entry-356 projection \(q\).
Define

\[
q^!:D(X,\mathcal O_X)\longrightarrow D(Z_{03}^{\rm pre},\mathcal O_Z)
\]

to be that right adjoint. Therefore

\[
q^!\mathcal L^{\check C}
\]

is an honest, type-correct object attached to the actual correspondence,
not a placeholder for a future scheme or log stack.

The structure-ring restriction maps of Entry 352 are localizations and
hence flat. Thus the target is a finite space in the standard ringed-finite
sense. This is useful for quasi-coherent refinements, but the existence
claim above already holds in the full derived module categories and does
not require a perfectness assumption.

## What is and is not closed

This closes the ringed/log enhancement needed to type the actual \(q^!\)
correspondence:

1. the ringed target exists;
2. the pre-quotient correspondence space exists;
3. the projections \(p,q\) are ringed morphisms; and
4. \(Rq_*\) has a right adjoint \(q^!\).

It does not compute \(q^!\mathcal L^{\check C}\). In particular, the
following stronger assertions remain unproved:

- identification of \(q^!\mathcal L^{\check C}\) with the pulled-back
  cellular module tensored with Entry 176's relative exceptional cap;
- preservation of the selected perfect/constructible subcategory;
- a Beck--Chevalley homotopy relating the generic \(q_J\) restriction to
  the conductor Cartier/Gysin class;
- a relative dualizing orientation and proper trace; and
- the PC-purity comparison.

Entry 176 supplies a normalized local rank-one cap, but delegation run
run-bcdfd3ef5de34beb998f3068ca4a9e00 confirms that it is not yet identified
with the relative dualizing object of this \(q\). The required
Beck--Chevalley comparison remains the concrete equation

\[
dH+Hd=\operatorname{ob}_{03},
\]

where Entry 160 defines

\[
\operatorname{ob}_{03}
=k[1](\kappa_A\otimes\mathrm{id}_Q)
-b[1](\mathrm{id}_B\otimes\kappa_E).
\]

That matrix/nullhomotopy is the next research obligation; it is not needed
to assert that \(q^!\) exists.

## Evidence boundary

The external theorem is used only for existence of the right adjoint on
full derived module categories. No algebraic-scheme, fs-log, étale, or
Kato--Nakayama comparison is inferred from it. The finite-ringed
construction and projection data remain those verified internally in
entries 352 and 356.
