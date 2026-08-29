# Rotate the critical seam into the Nevanlinna half-plane

Once the RH defect is written as an intersection of boundary Lagrangians, the seam geometry has a natural analytic coordinate. Set
\[
z=-i\left(s-\frac12\right).
\]
Then
\[
\operatorname{Im}z
=
-\left(\operatorname{Re}s-\frac12\right).
\]
The two off-seam sectors become the upper and lower \(z\)-half-planes, while the critical line becomes the real axis.

For an ordinary boundary triple of a symmetric operator, the Weyl function is operator-valued Nevanlinna:
\[
M(\bar z)=M(z)^{*},
\]
and
\[
\frac{\operatorname{Im}M(z)}{\operatorname{Im}z}\ge0.
\]
More precisely,
\[
\frac{M(z)-M(w)^{*}}{z-\bar w}
=
\gamma(w)^{*}\gamma(z),
\]
so at \(w=z\),
\[
\operatorname{Im}M(z)
=
(\operatorname{Im}z)\,\gamma(z)^{*}\gamma(z).
\]

This gives a direct off-seam exclusion mechanism if the arithmetic boundary relation has the opposite dissipative sign. Suppose the source-derived \(\Theta(z)\) satisfies
\[
\operatorname{Im}z>0
\quad\Longrightarrow\quad
\operatorname{Im}\Theta(z)\le0.
\]
If
\[
(\Theta(z)-M(z))b=0,
\]
then taking imaginary parts yields
\[
\langle b,\operatorname{Im}\Theta(z)b\rangle
=
(\operatorname{Im}z)\|\gamma(z)b\|^{2}.
\]
The left side is nonpositive and the right side nonnegative. Under strictness on either side, both can agree only for \(b=0\). Hence no collision occurs in the upper half-plane. Reflection and adjoint symmetry then exclude the lower half-plane.

The quantitative form is
\[
-\operatorname{Im}\Theta(z)
+
\operatorname{Im}M(z)
\ge
\varepsilon_C I
\]
on compact off-seam sets. This is a boundary-space version of the five-margin coercivity theorem, but now its sign is dictated by the general Weyl identity rather than an invented positive bulk operator.

There are three possible source outcomes:

1. \(\Theta\) is anti-Nevanlinna after seam rotation. Then RH reduces to strict boundary dissipation plus spectral identification.
2. \(\Theta\) is self-adjoint and independent of \(z\). Then \(\operatorname{Im}\Theta=0\), and injectivity of \(\gamma(z)\) already excludes nonreal \(z\), as in the standard theorem that self-adjoint extensions have real spectrum.
3. \(\Theta\) has an indefinite imaginary part. Then the ordinary self-adjoint-extension route cannot by itself confine collisions to the seam; one needs a generalized Nevanlinna, Krein-space, or sectorial relation.

This identifies the strongest desirable theorem:

> After the rotation \(z=-i(s-\tfrac12)\), the arithmetic boundary relation is self-adjoint or anti-Nevanlinna in the same boundary metric for which the history Weyl function is Nevanlinna.

The phrase “same boundary metric” is essential. Separate metric unitarizations of \(M\) and \(\Theta\) do not permit the imaginary-part comparison.

The next finite audit is therefore to compute the \(2\times2\) arithmetic relation in the wall/tail Darboux frame and test
\[
\frac{\Theta(z)-\Theta(z)^{*}}{2i}.
\]
The determinant identity with \(\xi(s)\) comes afterward. If the sign theorem fails, no amount of determinant matching explains seam confinement.

The minimal hostile has
\[
\det(\Theta(z)-M(z))=\xi\!\left(\frac12+iz\right)
\]
as a scalar identity, but \(\operatorname{Im}\Theta(z)\) has the same sign as \(\operatorname{Im}M(z)\). Zeros may then arise by cancellation off the real \(z\)-axis, so the determinant representation merely restates RH.

This is the first route in the programme where seam confinement could follow from a standard extension-theoretic sign law rather than from a global norm contraction.
