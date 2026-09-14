# Cutoff-direction comparison is a source-labelled correspondence and becomes an operator exactly under Douglas Gram domination

## Two cutoff features

Let `E_S` be the common observer-amplitude source. For each cutoff/depth index

\[
\alpha
=(\Lambda,n),
\]

let

\[
\Phi_\alpha:
E_S
\longrightarrow
\mathcal K_\alpha
\]

be the observer-generated positive feature map. It may include:

- the positive prolate bulk slot;
- finitely many dyadic defect slots;
- angular and outer regulators;
- bulk removal and endpoint recentering when those are defined.

For two indices `alpha,beta`, the desired cutoff transition would satisfy

\[
T_{\beta\alpha}
\Phi_\alpha(g)
=
\Phi_\beta(g).
\]

## Well-definedness criterion

The rule

\[
\Phi_\alpha(g)
\longmapsto
\Phi_\beta(g)
\]

is well-defined on `ran Phi_alpha` exactly when

\[
\boxed{
\ker\Phi_\alpha
\subseteq
\ker\Phi_\beta.
}
\]

If two observers become indistinguishable at cutoff `alpha` but distinct at cutoff `beta`, no operator on the earlier feature space can recover the later feature.

This kernel test must precede every norm estimate.

## Gram forms

Define the positive observer Gram forms

\[
G_\alpha(g,h)
=
\langle
\Phi_\alpha(g),
\Phi_\alpha(h)
\rangle,
\]

\[
G_\beta(g,h)
=
\langle
\Phi_\beta(g),
\Phi_\beta(h)
\rangle.
\]

The feature maps satisfy

\[
G_\alpha
=
\Phi_\alpha^*
\Phi_\alpha,
\qquad
G_\beta
=
\Phi_\beta^*
\Phi_\beta
\]

as quadratic forms on the common source.

## Douglas factorization criterion

There exists a bounded operator

\[
T_{\beta\alpha}:
\overline{\operatorname{ran}\Phi_\alpha}
\to
\overline{\operatorname{ran}\Phi_\beta}
\]

satisfying

\[
T_{\beta\alpha}\Phi_\alpha
=
\Phi_\beta
\]

if and only if there is a finite constant `c_(beta,alpha)` such that

\[
\boxed{
G_\beta
\preceq
c_{\beta\alpha}G_\alpha
}
\]

on the source form domain.

Equivalently,

\[
\boxed{
\|\Phi_\beta(g)\|^2
\le
c_{\beta\alpha}
\|\Phi_\alpha(g)\|^2
\qquad
\text{for all }g.
}
\]

The domination inequality automatically implies the kernel inclusion.

The least constant is

\[
\|T_{\beta\alpha}\|^2.
\]

## Contraction and isometry cases

A contraction exists exactly when

\[
\boxed{
G_\beta
\preceq
G_\alpha.
}
\]

An isometry implementing the observer labels exists when

\[
\boxed{
G_\beta
=G_\alpha
}
\]

on the source quotient by the common kernel.

Raw cutoff features generally have increasing volume and do not satisfy either relation without normalization and bulk removal.

## Why nested physical cutoffs are insufficient

For `Lambda<=Lambda'`, one has

\[
P_\Lambda
\preceq
P_{\Lambda'},
\qquad
Q_\Lambda
\preceq
Q_{\Lambda'}.
\]

But

\[
B_\Lambda
=P_\Lambda Q_\Lambda P_\Lambda
\]

and

\[
B_{\Lambda'}
=P_{\Lambda'}Q_{\Lambda'}P_{\Lambda'}
\]

need not commute. Separate order of `P` and `Q` does not imply

\[
B_\Lambda
\preceq
B_{\Lambda'}.
\]

Hence cutoff nesting does not supply a canonical contraction between prolate feature towers.

## Canonical source-labelled correspondence

Even when Douglas domination fails, the common observer source defines a canonical closed linear relation

\[
\boxed{
\mathcal R_{\beta\alpha}
=
\overline{
\left\{
(\Phi_\alpha(g),
\Phi_\beta(g)):
 g\in E_S
\right\}
}
\subset
\mathcal K_\alpha
\oplus
\mathcal K_\beta.
}
\]

This relation preserves source provenance. It does not identify arbitrary vectors from unlike cutoff feature spaces.

It is:

- the graph of an operator exactly when the kernel condition holds;
- the graph of a bounded operator exactly when Douglas domination holds;
- a multivalued relation when later features distinguish an earlier kernel;
- potentially nonclosed before taking the displayed closure.

## Composition of correspondences

For three cutoffs, relational composition gives

\[
\mathcal R_{\gamma\beta}
\circ
\mathcal R_{\beta\alpha}.
\]

Every source observer supplies an element of the composite relation:

\[
(\Phi_\alpha(g),
\Phi_\gamma(g)).
\]

Thus

\[
\mathcal R_{\gamma\alpha}
\subseteq
\mathcal R_{\gamma\beta}
\circ
\mathcal R_{\beta\alpha}
\]

at the algebraic observer-generated level. Equality after closure requires a gluing condition: an intermediate feature match must arise from one common observer modulo the relevant kernels.

The potential excess composite consists exactly of pairs represented by different observers whose `beta` features coincide.

## Exact coherence obstruction

Suppose

\[
\Phi_\beta(g)=
\Phi_\beta(h)
\]

but

\[
\Phi_\alpha(g)

e
\Phi_\alpha(h),
\qquad
\Phi_\gamma(g)

e
\Phi_\gamma(h).
\]

Then relational composition can glue the `alpha` feature of `g` to the `gamma` feature of `h`, creating a pair not in `R_(gamma,alpha)`.

Therefore strict composition is equivalent to the source-descent condition

\[
\boxed{
\ker\Phi_\beta
\subseteq
\ker\Phi_\alpha
+
\ker\Phi_\gamma
}
\]

with the precise quotient formulation depending on the observer category.

Retaining the observer label as part of the correspondence eliminates this ambiguity and gives strict composition by definition.

## Labelled span category

Define a cutoff feature not merely as `K_alpha`, but as the span

\[
\boxed{
E_S
\xrightarrow{\Phi_\alpha}
\mathcal K_\alpha.
}
\]

A comparison from `alpha` to `beta` is the common-source span

\[
\mathcal K_\alpha
\xleftarrow{\Phi_\alpha}
E_S
\xrightarrow{\Phi_\beta}
\mathcal K_\beta.
\]

Compositions are fiber products retaining the source label. On the diagonal observer-generated component, composition is strict and does not create spurious kernel gluings.

This is the correct category before Douglas domination is proved.

## Interaction with dyadic depth

At fixed `Lambda`, the dyadic maps `J_n` are actual isometries and satisfy

\[
J_n\Phi_{\Lambda,n}
=
\Phi_{\Lambda,n+1}.
\]

Thus depth comparisons are graphs of operators.

Between different cutoffs, use source-labelled spans until Gram domination is established. Squares mixing cutoff and depth commute as labelled spans because both routes retain the same observer `g` and functional calculus is applied only after selecting the cutoff-specific `B_Lambda`.

They need not commute as unlabelled Hilbert-space operators.

## Normalized residual target

The most plausible place for Douglas domination is not the raw feature, whose norm contains growing volume, but the bulk-removed recentered boundary feature

\[
\widetilde\Phi_{\Lambda,n}(g).
\]

A cutoff contraction would require

\[
\boxed{
\widetilde G_{\Lambda',n'}
\preceq
\widetilde G_{\Lambda,n}
}
\]

along the chosen cofinal path. Equality in the limit would produce asymptotic isometries.

No such inequality is currently proved; asserting it would be equivalent to a substantial positivity/coercivity theorem.

## Consequence for the positive refinement

The complete positive diagram currently lives naturally in a bicategory of:

- observer sources;
- Hilbert feature realizations;
- source-labelled spans/correspondences;
- actual isometries in the dyadic-depth direction.

It does not yet live in an ordinary category whose every cutoff arrow is a bounded Hilbert-space operator.

This is still well-typed and preserves the realization-functor principle: nodes are presentations of one source observer form, not barycentric mixtures.

## Acceptance test for cutoff operators

For each proposed cutoff arrow, compute or bound

\[
\boxed{
c_{\beta\alpha}
=
\sup_{
G_\alpha(g,g)>0
}
\frac{
G_\beta(g,g)
}{
G_\alpha(g,g)
}.
}
\]

Then:

- `c<infinity` gives a bounded operator;
- `c<=1` gives a contraction;
- `c=1` plus equality of forms gives an isometry;
- `c=infinity` proves that only a relation/span is available.

The kernel case `G_alpha(g,g)=0<G_beta(g,g)` immediately forces `c=infinity`.

## Disposition

The cutoff-direction comparison is canonically available as

\[
\boxed{
\mathcal K_{\Lambda,n}
\xleftarrow{\Phi_{\Lambda,n}}
E_S
\xrightarrow{\Phi_{\Lambda',n'}}
\mathcal K_{\Lambda',n'}.
}
\]

It promotes to a bounded operator exactly when the later observer Gram form is dominated by the earlier one. The dyadic direction already consists of strict isometries; the unresolved positive theorem is Douglas domination for bulk-removed boundary Gram forms along a source-derived cofinal cutoff path.
