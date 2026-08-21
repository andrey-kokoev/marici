# Fivefold Five-Site Branching Requires Two External Discriminants

Use four external points to define the relative vectors \(a,b,c\), Gram
matrix \(G\), and squared-length column

\[
d=(a^2,b^2,c^2)^T.
\]

Away from \(\det G=0\), their common circumcenter is

\[
\ell
=
\frac{1}{2\det G}
\begin{pmatrix}a&b&c\end{pmatrix}
\operatorname{adj}(G)d.
\]

The first four null-branch equations require

\[
R_0=d^T\operatorname{adj}(G)d=0.
\]

For a fifth relative point \(p\), the remaining branch equation becomes,
after clearing \(\det G\),

\[
C_5
=
\det(G)p^2
-
p^T
\begin{pmatrix}a&b&c\end{pmatrix}
\operatorname{adj}(G)d
=0.
\]

Therefore

\[
\boxed{
\text{five Kummer branches meet}
\iff
R_0=C_5=0
}
\]

on the Gram-nondegenerate chart.

The first equation says the four-point circumsphere has zero radius. The
second says the fifth point lies on that same sphere. Thus the formal
degree-five deck monomial can acquire geometric support only on a deeper
intersection of two external discriminants (or on a separately resolved
Gram-degenerate chart).

The exact rational checker verifies both cleared formulas directly against
the derived circumcenter and shows that the frozen generic five-point control
lies on neither condition.

This completes the generic geometric typing of the formal Loewy tower:

- degrees one through three can occur on the generic complex loop base;
- degree four requires the zero-circumradius discriminant;
- degree five additionally requires fifth-point cosphericity.

Artifacts:

- research/nima/check_fivefold_null_branch_support.py
- research/nima/results/fivefold-null-branch-support.json
