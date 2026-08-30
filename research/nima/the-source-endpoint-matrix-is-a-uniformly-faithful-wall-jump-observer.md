# The source endpoint matrix is a uniformly faithful wall--jump observer at every prime

## Primewise endpoint observer

The completed doubled signal-to-history incidence has endpoint matrix

\[
V_p
=
\frac12
\begin{pmatrix}
1&p^{-1}\\
p^{-1}&1
\end{pmatrix}
\]

in the two reciprocal ray coordinates.

This matrix is source-derived from the two half-density endpoint traces; it is
not fitted to pass a rank test.

## Wall--jump diagonalization

Introduce the normalized reciprocal basis

\[
e_{\mathrm{wall}}
=
\frac1{\sqrt2}
\begin{pmatrix}
1\\
1
\end{pmatrix},
\qquad
e_{\mathrm{jump}}
=
\frac1{\sqrt2}
\begin{pmatrix}
1\\
-1
\end{pmatrix}.
\]

Then

\[
V_pe_{\mathrm{wall}}
=
\lambda_{\mathrm{wall},p}e_{\mathrm{wall}},
\]

\[
V_pe_{\mathrm{jump}}
=
\lambda_{\mathrm{jump},p}e_{\mathrm{jump}},
\]

with

\[
\lambda_{\mathrm{wall},p}
=
\frac12(1+p^{-1}),
\]

and

\[
\lambda_{\mathrm{jump},p}
=
\frac12(1-p^{-1}).
\]

Thus the wall and ordered-jump coordinates are independently observed.

## Uniform lower bound

For every prime \(p\ge2\),

\[
\lambda_{\mathrm{jump},p}
\ge
\frac14,
\]

and

\[
\lambda_{\mathrm{wall},p}
\ge
\frac12.
\]

Therefore

\[
\sigma_{\min}(V_p)
=
\frac12(1-p^{-1})
\ge
\frac14.
\]

The determinant satisfies

\[
\det V_p
=
\frac14(1-p^{-2})
\ge
\frac3{16}.
\]

The operator norm is at most \(3/4\), so

\[
\kappa(V_p)
\le3.
\]

All bounds are uniform in \(p\).

## Completed direct sum

On the prime-labelled two-port carrier, define

\[
\mathbf V
=
\bigoplus_pV_p.
\]

Then

\[
\|\mathbf Vy\|
\ge
\frac14\|y\|,
\]

and

\[
\|\mathbf V^{-1}\|
\le4
\]

on its range. Thus the labelled completed observer is uniformly faithful.

This is compatible with the earlier no-go: \(\mathbf V\) retains every prime
label, whereas scalar Euler augmentation does not.

## Reciprocal orientation

The wall eigenvalue is reciprocal even and the jump eigenvalue is reciprocal
odd. Since both are positive in the frozen sign frame, the observer preserves
the orientation rather than identifying \(B\) with \(B^{*}\).

Reflection acts diagonally as

\[
\operatorname{diag}(1,-1)
\]

in the wall--jump basis and commutes with \(V_p\).

## Interaction with Green completion

The Euler--Maclaurin wall routing feeds the wall coordinate, while the
causal/anti-causal ordered port feeds the jump coordinate. The quarter-gap
Green inverse acts in the analytic factor and therefore does not change the
two eigenvalues above.

Hence the full renormalized theta--Green normal form inherits the same
prime-uniform lower frame bound at endpoint readout.

## What this closes

The feasible pushforward theorem is now complete:

\[
\text{primewise two-port faithfulness}
+
\text{uniform direct-sum assembly}
+
\text{downstream scalar augmentation}.
\]

The first Adams edge no longer has an unresolved local reciprocal rank
problem.

## Remaining constructor identity

The live gate is now the exact equality between:

- the source-complete base-plus-curvature Green solution;
- the source endpoint incidence \(V_p\);
- the Stieltjes four-front boundary and ordered primitive.

All components exist and are uniformly controlled. What remains is their
commuting comparison square, not another margin estimate.

## Hostile

Retain only the wall eigenvector. The resulting scalar endpoint port has a
uniform positive coefficient but annihilates the jump coordinate exactly.
Scalar positivity therefore cannot substitute for the two-port matrix.
