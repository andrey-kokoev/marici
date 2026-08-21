# The Rank-Two Branch Cover Is an Intrinsic Kummer Line

The conditional two-sheeted cover on the rank-two Gram locus has a
coordinate-free equation.

Choose two independent planar vectors \(a,b\), with

\[
H=\begin{pmatrix}a^2&a\cdot b\\a\cdot b&b^2\end{pmatrix},
\qquad
d=(a^2,b^2)^T,
\qquad
\Delta=\det H\ne0.
\]

Let \(h\) be their planar circumcenter and \(n=a\times b\). Then

\[
h^2=\frac{R}{4\Delta},
\qquad
R=d^T\operatorname{adj}(H)d,
\qquad
n^2=\Delta.
\]

After the cocircular consistency equation for the third planar vector is
imposed, every affine circumcenter is

\[
\ell=h+\tau n.
\]

Define \(w=2\Delta\tau\). The null equation becomes

\[
\boxed{w^2+R=0.}
\]

Thus the two sheets are not an accidental pair of roots in a chosen frame.
They form an algebraic anti-invariant Kummer line associated with the square
root of the planar zero-radius numerator \(-R\). The sheets collide at
\(R=0\).

For a transverse fifth point \(p\), define

\[
N=p\cdot n,
\qquad
C_p=\Delta p^2-g_p^T\operatorname{adj}(H)d,
\qquad
g_p=(p\cdot a,p\cdot b)^T.
\]

Its bisector equation is exactly

\[
Nw=C_p.
\]

Eliminating the Kummer coordinate gives

\[
\boxed{C_p^2+N^2R=0.}
\]

This separates the roles cleanly:

- cocircularity selects the rank-two carrier stratum;
- \(w^2=-R\) supplies its anti-invariant coefficient line;
- \(Nw=C_p\) is the fifth-point algebraic incidence/selection map.

Benincasa's earlier Entries 1216--1217 already identify the physical object as
the marked degree-32 \(C_2^5\) cover with support on the external-Gram and five
edge-soft divisors. Accordingly, the line above is typed as an algebraic
incidence subcover inside that marked geometry. It is not independently
established as a physical current or physical readout. A chain/current map is
still required for such an activation claim.

The narrower positive result is that the local geometry produces a specific
Kummer coefficient object and an incidence selector together; it does not by
itself prove physical selection.

Artifacts:

- `research/nima/check_rank_two_kummer_cover.py`
- `research/nima/results/rank-two-kummer-cover.json`
