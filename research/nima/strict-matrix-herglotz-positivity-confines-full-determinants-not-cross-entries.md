# Strict matrix Herglotz positivity confines full determinants, not cross entries

## Cross-port no-go

A rigged two-port Weyl matrix can be strictly Herglotz while an off-diagonal
entry vanishes inside the domain. Therefore passivity of the full boundary
system does not orient or confine the divisor of one cross response.

This closes the claim that the bordered readout

\[
\delta_0A_s^{-1}f
\]

inherits zero-freeness merely because it is an entry of a positive matrix Weyl
function.

## Full-determinant theorem

Let \(M(z)\) be a matrix Herglotz function on the upper half-plane and assume
strict positivity:

\[
\operatorname{Im}M(z)>0.
\]

Then \(M(z)\) is invertible.

Indeed, if \(M(z)v=0\) for some nonzero \(v\), then

\[
v^*\operatorname{Im}M(z)v
=
\operatorname{Im}(v^*M(z)v)
=0,
\]

contradicting strict positivity.

Consequently,

\[
\det M(z)\ne0
\]

throughout the open Herglotz domain.

Thus strict passivity can confine the divisor of a full boundary determinant
to the domain boundary. It cannot do the same for an individual matrix entry.

## Exact hostile cross response

Consider

\[
M(z)=
\begin{pmatrix}
0&-i\\
i&0
\end{pmatrix}
+
z
\begin{pmatrix}
2&1\\
1&2
\end{pmatrix}.
\]

The coefficient of \(z\) is positive definite, so \(M\) is strictly
Herglotz. At \(z=i\), the upper-right entry vanishes, but the determinant is
nonzero.

This is the smallest finite falsifier for cross-entry confinement and the
smallest positive witness for full-determinant nonvanishing.

## Theta/Tate gate

The remaining passive route requires all of the following:

1. construct a rigged boundary matrix \(M(z)\) from tail, seam, source, and
   endpoint ports;
2. prove strict matrix Herglotz positivity from a source conservation law;
3. prove the completed scalar section satisfies

\[
\Xi(s)=u(s)\det M(z(s)),
\]

with a source-derived nowhere-zero unit \(u\);
4. show the open half-planes map to the strict Herglotz domains and the critical
   seam maps to their common boundary;
5. preserve minimality and determinant typing under completion.

If \(\Xi\) remains only a cross entry or an arbitrary bordered overlap, the
strict Herglotz theorem does not apply.

## Noncircularity

Neither determinant equality nor strict positivity may be inferred from the
zero set. The matrix, its boundary form, and its positive imaginary part must
be derived before scalar projection from the theta/Tate source.

