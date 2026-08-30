# Symbolic proof of the tower logarithmic normal form

Let

\[
D_{g,a}=z^{-a}\bar z^{-(g+a-1)}
=\bar z^{1-g}u^{-a},
\qquad u=z\bar z.
\]

Define the one-variable transport factors

\[
T_s=\partial_u+\frac{2s}{1+u},
\qquad s=2,\ldots,g+1,
\]

and

\[
L_g=T_{g+1}T_g\cdots T_2.
\]

## Radialization lemma

For every integer `k`, rational function `H(u)`, and weight `s`, the
`z`-covariant factor satisfies

\[
\left(\partial_z+\frac{2s\bar z}{1+u}\right)
\left(\bar z^kH(u)\right)
=\bar z^{k+1}T_sH(u).
\]

Iterating from `k=1-g` gives

\[
f_{g,a}=\bar zL_gu^{-a}.
\]

Reflection gives the other component

\[
\bar f_{g,a}=zL_gu^{-a}.
\]

Consequently the folded one-form is radial:

\[
\boxed{
\omega_{g,a}
=f_{g,a}\,dz+\bar f_{g,a}\,d\bar z
=L_gu^{-a}(\bar z\,dz+z\,d\bar z)
=L_gu^{-a}\,du.
}
\]

Closedness is now formal rather than a cancellation between unrelated
two-variable expressions.

## Residue character

For the formal residue pairing,

\[
\operatorname{Res}_{u=0}(1+u)^{-r}T_sH\,du
=(r+2s)\operatorname{Res}_{u=0}(1+u)^{-r-1}H\,du.
\]

Moving all transport factors across gives

\[
\operatorname{Res}_{u=0}L_gu^{-a}\,du
=\frac{(2g+2)!}{(g+2)!}[u^{a-1}](1+u)^{-g}.
\]

For admitted positive even `a`, this is

\[
r_{g,a}
=-g(g+1)C_{g+1}a^{\overline{g-1}}.
\]

The only finite poles are `u=0` and `u=-1`.  There is no residue at infinity,
so the second residue is `-r_{g,a}`.

## Hermite reduction

A rational one-form on the `u`-line is rational-exact precisely after all its
simple-pole residues are removed.  Therefore there is a rational function
`Phi_{g,a}(u)` such that

\[
L_gu^{-a}\,du
=d\Phi_{g,a}
+r_{g,a}\left(\frac{du}{u}-\frac{du}{1+u}\right).
\]

Equivalently,

\[
\boxed{
\omega_{g,a}
=d\Phi_{g,a}
+r_{g,a}\,d\log\frac{u}{1+u}.
}
\]

This proves the normal form for arbitrary grade and positive admitted even
depth.  At depth zero the residue coefficient vanishes and the displayed
rational primitive is

\[
\Phi_{g,0}
=-\frac{(g+3)!}{6(g-1)(1+u)^{g-1}}.
\]

No finite census supplies either quantifier: radialization is an operator
identity, the residue is a formal adjoint calculation, and Hermite reduction
is exact on the rational `u`-line.
