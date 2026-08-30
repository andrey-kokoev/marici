# Fourfold Five-Site Branching Requires a Circumsphere Discriminant

Choose four external points and translate the first to the origin. Let

\[
a,\ b,\ c\in\mathbb A^3,
\qquad
G_{ij}=v_i\cdot v_j,
\qquad
d=(a^2,b^2,c^2)^T.
\]

The four branch equations

\[
\ell^2=(\ell-a)^2=(\ell-b)^2=(\ell-c)^2=0
\]

first force the unique circumcenter equations

\[
2G\alpha=d,
\qquad
\ell=\alpha_1a+\alpha_2b+\alpha_3c.
\]

Away from \(\det G=0\),

\[
\ell^2
=
\frac14d^TG^{-1}d
=
\frac{d^T\operatorname{adj}(G)d}{4\det G}.
\]

Therefore

\[
\boxed{
\text{four Kummer branches meet}
\iff
d^T\operatorname{adj}(G)d=0
}
\]

on the Gram-nondegenerate chart.

This numerator is the zero-circumradius Cayley--Menger/Gram discriminant of
the four external points. It is extra external support, not a generic
codimension-four stratum in the three loop coordinates.

The exact checker evaluates all five quadruples of a frozen generic rational
five-point configuration. Each Gram matrix is nondegenerate, the derived
circumcenter agrees with the direct squared radius, and every numerator is
nonzero, reproducing the empty-quadruple result.

## Interpretation of the degree-four Loewy class

The formal mod-two monomial of deck degree four exists in the integral deck
shadow independently of geometry. It can acquire geometric branch support
only after restriction to the corresponding circumsphere discriminant (or a
Gram-degenerate chart requiring separate analysis).

Thus the higher Loewy degree is best typed as a potential supported
coefficient grade, not as evidence for an always-present physical branch
intersection.

Artifacts:

- research/nima/check_fourfold_null_branch_support.py
- research/nima/results/fourfold-null-branch-support.json
