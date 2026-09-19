# Reciprocity constructs a formal CG interval, but the self-dual facet needs its comparison with the independent Green cofiber

In a stable cone-package category equipped with reciprocal duality, the edge
orbit

\[
X_{SA}\leftrightarrow X_{CG}
\]

produces a formal candidate

\[
X_{CG}^{\rm rec}:=\mathbb D(X_{SA}).
\]

Likewise

\[
X_{AG}^{\rm rec}:=\mathbb D(X_{SC}),
\]

while the fixed intervals require forms

\[
X_{SG}\simeq\mathbb D(X_{SG}),
\qquad
X_{AC}\simeq\mathbb D(X_{AC}).
\]

If these data and the first two cofiber triangles are given coherently, stable
category axioms generate a formal reflected octahedral boundary.  This explains
why reciprocal chart gluing can make the combinatorial middle facet appear
complete.

That construction does not establish the required independence.  The Green
side supplies a different candidate: let

\[
X_{CG}^{\rm Gr}:=\operatorname{cofib}
  (X_{SC}\longrightarrow X_{SG})
\]

using the independently sourced Green transpose/forcing map.  Equivalently,
the fourth face asks for the same object as

\[
\operatorname{cofib}(X_{AC}\longrightarrow X_{AG}).
\]

The actual missing mate is therefore a comparison

\[
\kappa_{CG}:X_{CG}^{\rm rec}\longrightarrow X_{CG}^{\rm Gr}
\]

compatible with both cofiber presentations, graph domains, determinant
orientation, and reciprocal biduality.  Its obstruction package is

\[
\operatorname{Ob}_{CG}:=\operatorname{Cone}(\kappa_{CG}).
\]

The middle facet exists with the intended independent Green meaning exactly
when `kappa_CG` is an equivalence, equivalently when `Ob_CG` is acyclic in the
admitted completed category.

This separates two notions that were previously conflated:

1. **formal reflected facet:** define `CG` as the dual of `SA`; available once
   the cone-package duality is constructed;
2. **analytic self-dual facet:** prove that formal reciprocal `CG` agrees with
   the independently constructed Green cofiber; still open.

Defining `X_CG^Gr` to be `D(X_SA)` would set the obstruction to zero by
notation and repeat the earlier independence failure.  The executable target
is instead to construct both packages separately and calculate
`Cone(kappa_CG)`.
