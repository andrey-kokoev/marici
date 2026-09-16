# The principal-angle obstruction has a canonical positive edge feature

## Projection-pair data

Fix one regulated projection pair \((P_\alpha,Q_\alpha)\). On the inside generic carrier, define

\[
B_\alpha
=P_\alpha Q_\alpha P_\alpha
\big|_{\operatorname{ran}P_\alpha}.
\]

Its spectrum lies in \([0,1]\). The exact atoms at \(0\) and \(1\) are split off, leaving the generic-angle sector.

## Obstruction multiplier

Define

\[
\eta(t)
=
\frac{
\sqrt t+
\sqrt{1-t}-1
}{2}.
\]

The function is continuous and nonnegative on \([0,1]\). It vanishes at the endpoints.

Functional calculus therefore defines the positive operator

\[
\eta(B_\alpha)\succeq0.
\]

## Canonical edge feature

Define

\[
E_\alpha^{Witt}
=
\eta(B_\alpha)^{1/2}.
\]

Its Gram is

\[
(E_\alpha^{Witt})^*E_\alpha^{Witt}
=
\eta(B_\alpha).
\]

This feature measures exactly the negative magnitude of the forced common remainder on every principal-angle block.

No eigenbasis choice is involved. The construction is canonical under unitary intertwiners of projection pairs.

## Outside realization

Let \(V_\alpha\) be the Halmos polar unitary intertwining the inside and outside generic contractions. Then

\[
B_\alpha^{out}
=V_\alpha B_\alpha V_\alpha^*.
\]

Functional calculus gives

\[
\eta(B_\alpha^{out})^{1/2}
=V_\alpha
\eta(B_\alpha)^{1/2}
V_\alpha^*.
\]

Thus the inside and outside obstruction features are canonically isometric. The obstruction belongs to the generic edge itself, not to a choice of side.

## Compatibility with dyadic refinement

Every dyadic defect row is obtained by functional calculus in \(B_\alpha\). Hence it commutes with the spectral projections of \(\eta(B_\alpha)\).

The obstruction feature can be carried through every dyadic refinement without changing its Gram. Refinement resolves its spectral distribution but neither creates nor removes its mass.

## Cutoff asymptotic

In the scalar prolate model,

\[
\operatorname{Tr}
(E_c^{Witt})^*E_c^{Witt}
=
2C_W(\log2)\log c+O(1).
\]

Define the normalized edge feature

\[
\widetilde E_c^{Witt}
=
(\log c)^{-1/2}E_c^{Witt}.
\]

Its scalar Gram has the finite limit coefficient

\[
2C_W\log2.
\]

This identifies the exact normalization required for a positive edge comparison.

## Tate and reference copies

Apply the construction separately to the Tate and reference regulated projection pairs:

\[
E_{\alpha,T}^{Witt}
=
\eta(B_{\alpha,T})^{1/2},
\]

\[
E_{\alpha,0}^{Witt}
=
\eta(B_{\alpha,0})^{1/2}.
\]

The scalar Widom law predicts the same leading coefficient when the two pairs have the same physical cutoff geometry. Equality of scalar coefficients is not yet an isometric feature comparison.

## Exact comparison condition

A positive removal of the universal edge requires source-labelled partial isometries whose Grams agree asymptotically. A convenient form of the required estimate is

\[
\left\|
\frac1{\log c_\alpha}
(E_{\alpha,T}^{Witt})^*E_{\alpha,T}^{Witt}
-
\frac1{\log c_\alpha}
(E_{\alpha,0}^{Witt})^*E_{\alpha,0}^{Witt}
\right\|_{graph}
\longrightarrow0.
\]

A weaker pairwise form limit may identify the scalar boundary observation but does not construct an isometry between the positive edge features.

## Source-labelled edge carrier

If the normalized Grams converge to one positive form \(G_{edge}\) on the observer core, define its minimal feature carrier by completion of

\[
E/\ker G_{edge}
\]

in the norm induced by \(G_{edge}\).

Both normalized obstruction features then admit asymptotic comparison maps into this common carrier, provided the required liminf and recovery estimates hold.

## Relation to the absolute fold

The feature \(E_\alpha^{Witt}\) is not itself a common positive subfeature whose subtraction produces the Jordan legs. The noncommuting two-dimensional hostile excludes that interpretation.

Instead, it measures the universal generic-angle capacity that must be matched between the Tate and reference folds before taking the finite absolute boundary.

## Disposition

The logarithmic edge layer now has an explicit canonical feature:

\[
E_\alpha^{Witt}
=
\eta(B_\alpha)^{1/2}.
\]

The open edge theorem is comparison of the normalized Tate and reference Grams of this feature in the observer graph topology. This is sharper than asking for an unspecified observer-weighted Widom law.
