# A Scale-Free Positive Functional Selects the Minimal Completion

## Question

Can WP835's clock fiber be removed while retaining positive sensitivity to
both charged and neutral spectral sectors?

## Scale-free spectral shape

For a nondegenerate finite operator on an \(n\)-dimensional real carrier,
define

\[
R_n(D)=
\frac{\operatorname{Tr}(D^TD)}
{\det(D^TD)^{1/n}}.
\]

If \(s_i^2\) are the positive squared singular values, arithmetic-geometric
mean gives

\[
R_n(D)=
\frac{\sum_i s_i^2}{(\prod_i s_i^2)^{1/n}}
\geq n,
\]

with equality exactly when all singular values are equal. The functional is
invariant under \(D\mapsto mD\), so it imports no absolute mass clock.

## Combined completion selector

Take

\[
\Phi_\lambda(Q,D)
=\operatorname{Tr}Q^2+\lambda R_n(D),
\qquad \lambda>0.
\]

The primitive three-charge packet has Ward index 14. It admits an irreducible
saturating operator

\[
D_a=I-\frac23\mathbf1\mathbf1^T,
\qquad
D_a^TD_a=I,
\]

and therefore score

\[
\Phi_{\rm base}=14+3\lambda.
\]

Complete the packet by \(k\) nonzero charged vectorlike pairs with charges
\((r_j,-r_j)\) and by \(\ell\) neutral states. The dimension is
\(3+2k+\ell\), and

\[
\Phi_{\rm completion}-\Phi_{\rm base}
\geq
2\sum_jr_j^2+\lambda(2k+\ell).
\]

This is strictly positive for every nonempty completion and every positive
\(\lambda\). The ordering does not depend on tuning the numerical weight.

Within this declared finite completion grammar, \(\Phi\) therefore uniquely
selects no charged pairs, no neutral additions, and equal singular values.
This repairs both the WP831 charged threshold fiber and the WP834 neutral
kernel without reintroducing WP835's scale coefficient.

## Remaining fibers

The theorem does not select the absolute singular scale because

\[
R_n(mD)=R_n(D).
\]

It also does not select mixing orientation. For example,

\[
D_b=I-\frac17(1,2,3)^T(1,2,3)
\]

is a second irreducible three-state saturator distinct from \(D_a\). Both have
the same charge packet, singular values, anomaly, and score.

Thus the functional is a genuine finite-completion and singular-shape
selector, but not yet a full finite-operator selector. It supplies neither an
absolute scale nor the interacting coupling magnitude and basin.

## Authority and instrument boundary

No current source action derives minimization of \(\Phi\). Its two summands
are mathematically natural and positive, but that does not by itself establish
a physical operation that minimizes their sum. No admitted apparatus measures
this global comparison over alternative source completions.

Finite threshold survival is only partial: the matter multiplicity is fixed
inside the declared grammar, while the common mass scale, relevant
deformations, finite matching, and detector response remain open.

## Disposition

Progressive conditional selector. A scale-free Ward-spectral functional
uniquely eliminates all direct charged and neutral finite completions for every
positive relative weight. Source authority, mixing orientation, absolute
scale, RG basin, threshold matching, and physical readout remain unresolved.

## Verification

Run:

```text
uv run --with sympy python research/flavor/checkers/wp836_scale_free_ward_spectral_completion_selector.py
```
