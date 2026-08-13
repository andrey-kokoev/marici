# Primitive-Symmetric Sewing Requirements

## Record

Date: 2026-08-12

Status: tree-level state projector understood; naturality for the full surface algebra remains unproved.

## Correction to the earlier ledger

Entry 01 records closure of projected pure-graviton generalized-cut data. That statement must not be read as proving that the primitive-symmetric projector is a natural transformation of the entire surface theory.

Projected cut closure and preservation of cut-free primitive interactions are separate conditions because cuts annihilate contact data.

## Local physical state object

After the scalar first-jet operation and gauge reduction, let

\[
E
=
H_{\mathrm{gauge}}(J_\perp^1\mathrm{Scalar})
\simeq
q^\perp/\langle q\rangle
\]

with nondegenerate metric

\[
g:E\otimes E\to\mathbf1.
\]

Set \(V=E\otimes E\). Assuming the categorical dimension \(d=\dim E\) is invertible, define

\[
P_{\mathrm{grav}}
=
\frac12(1+\tau)
-
\frac1d
\operatorname{coev}_g\operatorname{ev}_g.
\]

Its image is

\[
W
=
\operatorname{im}P_{\mathrm{grav}}
=
\operatorname{Sym}^2_0E.
\]

On physical cohomology this separates the symmetric traceless graviton from the antisymmetric and trace sectors.

## Required state category

The surface state category must be:

1. symmetric monoidal;
2. rigid, with evaluation and coevaluation;
3. cyclic with respect to sewing;
4. idempotent-complete;
5. compatible with gauge cohomology and mapping-class actions.

The projector must obey

\[
P^2=P,
\qquad
P^\dagger=P,
\qquad
[P,Q_{\mathrm{gauge}}]=0.
\]

Self-adjointness makes \(W\) an orthogonal retract rather than an external state subtraction.

## Coevaluation and local sewing

Let \(\eta_V\) be the coevaluation of \(V\). The internal pure-graviton state sum must be

\[
\eta_W
=
(P\otimes P^\vee)\eta_V.
\]

The restricted evaluation and this coevaluation must satisfy the snake identities on \(W\). Equivalently, the restriction of the metric to \(W\) must remain perfect.

This local sewing construction depends on the jet-state metric \(g\). It does not require an all-loop KLT intersection matrix.

## Naturality for surface operations

For every primitive surface operation

\[
\mu_\Sigma:
\bigotimes_{\mathrm{in}}V
\longrightarrow
\bigotimes_{\mathrm{out}}V,
\]

the retract must be preserved:

\[
P_{\mathrm{out}}\mu_\Sigma
=
P_{\mathrm{out}}\mu_\Sigma P_{\mathrm{in}}.
\]

A stronger intertwining relation,

\[
P_{\mathrm{out}}\mu_\Sigma
=
\mu_\Sigma P_{\mathrm{in}},
\]

holds only if the projected sector is an actual modular subalgebra rather than merely a projected theory.

For cuts, define the defect

\[
\mathfrak o_C^P
=
(1-P_{\mathrm{cut\ flags}})
\Delta_CP_\Sigma.
\]

Vanishing of \(\mathfrak o_C^P\) is necessary. It is not sufficient because the global defect

\[
\mathfrak o_\Sigma
=
(1-P_{\mathrm{out}})
\mu_\Sigma P_{\mathrm{in}}
\]

can lie in the cut kernel and represent a nonzero primitive contact interaction.

This contact-sector centrality is the first categorical gravity obstruction.

## Nonseparating sewing

A nonseparating cut tests the wheeled or trace structure. For an endomorphism preserving \(W\), the category must identify

\[
\operatorname{Tr}_V(i f p)
=
\operatorname{Tr}_W(f),
\]

where \(i:W\to V\) and \(p:V\to W\) split the idempotent.

This follows formally for a dualizable retract once the surface operations preserve \(W\). It fails to answer whether the unprojected primitive operations contain off-diagonal maps between \(W\) and its physical complement.

## Local metric versus global KLT pairing

The local metric \(g\) controls one-particle trace removal and internal state sums.

The global scalar intersection pairing

\[
I_\Sigma:
\mathcal H_\Sigma\otimes\mathcal H_{\bar\Sigma}
\to\mathbf1
\]

controls the KLT pairing between ordering sectors. At tree level its inverse supplies the KLT kernel.

The full proposed gravity operation is therefore

\[
\mathrm{GR}_{\mathrm{tree}}
=
\left\langle
\operatorname{PrimSym}_g^2(\mathrm{YM}),
\operatorname{PrimSym}_g^2(\mathrm{YM})
\right\rangle_{I_{\mathrm{scalar}}^{-1}}.
\]

An arbitrary-surface version additionally requires a perfect loop-level scalar intersection matrix and its coevaluation. Current loop inverse-KLT work constructs diagonal surface integrands; off-diagonal entries, their intersection interpretation, closed-curve completion, matrix inversion, and loop double-copy use remain open.

## Exact structural question

The gravity problem should be stated as:

\[
\boxed{
\text{Is }\operatorname{Sym}^2_0E
\text{ an orthogonal modular retract preserved by every primitive surface operation?}
}
\]

This is stronger than closure of generalized cuts and logically independent of searching for a preferred loop integrand representative.

## Next falsification tests

1. List the elementary cut-free generators of the doubled jet surface algebra.
2. Evaluate \((1-P)\mu P^{\otimes n}\) on each generator.
3. Prove or disprove that the resulting defect is a hereditary contact ideal.
4. Verify the snake and trace identities for the projected coevaluation.
5. Separate failures of the local state retract from failures of the global KLT pairing.

## Prohibited overclaims

Do not claim that:

- generalized-cut closure proves naturality on contact operations;
- the dilaton and antisymmetric sectors are gauge exact;
- projecting external states proves closure of internal primitive vertices;
- projecting an inverse pairing always equals inverting its restriction;
- the diagonal loop inverse-KLT integrand is already a loop intersection matrix;
- the existence of a cohomological projector selects a canonical cyclic/BV chain representative.

## Sources

- [Combinatorics and Topology of Kawai-Lewellen-Tye Relations](https://arxiv.org/abs/1706.08527)
- [A Surface Integrand for the Inverse KLT Kernel](https://arxiv.org/pdf/2602.15102)
