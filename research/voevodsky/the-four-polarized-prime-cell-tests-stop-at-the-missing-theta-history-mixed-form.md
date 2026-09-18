# The four polarized prime-cell tests stop at the missing theta-history mixed form

## Question

Can the available source data materialize the complete theta-history form on

\[
q_1=Q_p^{\rm lin}e_1=\binom{1/2}{1/2},
\qquad
q_2=Q_p^{\rm lin}e_2=\binom{1/4}{-1/4},
\]
form its radical quotient, and test all four ordered identities

\[
G_p^{\rm St}(e_j,e_k)=G_p^\theta(q_j,q_k),
\qquad j,k\in\{1,2\}?
\]

## Materialized coefficient table

The source fixes the endpoint columns and their endpoint-metric contribution. With the declared endpoint metric \(2I\),

\[
E=\begin{pmatrix}1&0\\0&1/4\end{pmatrix}.
\]

Let the complete relative theta-history form be decomposed before summation into endpoint, wall--tail, derivative-tail, fourth-grade, and forcing contributions:

\[
G_p^\theta|_{\langle q_1,q_2\rangle}
=E+W_p+T_p+F_p+C_p.
\]

Write the unresolved sum as the Hermitian ordered table

\[
W_p+T_p+F_p+C_p
=
\begin{pmatrix}
\alpha_p&\beta_p+i\gamma_p\\
\beta_p-i\gamma_p&\delta_p
\end{pmatrix},
\qquad
\alpha_p,\beta_p,\gamma_p,\delta_p\in\mathbb R.
\]

Therefore the complete target table is

\[
G_p^\theta(q_j,q_k)=
\begin{pmatrix}
1+\alpha_p&\beta_p+i\gamma_p\\
\beta_p-i\gamma_p&1/4+\delta_p
\end{pmatrix}_{jk}.
\]

This is the maximal source-typed materialization currently licensed by the repository. The known Volterra identity fixes the antisymmetric compression on the unnormalized source frame,

\[
V_{\rm src}^*iTV_{\rm src}
=
\begin{pmatrix}
0&i\|\Phi\|_2^2\\
-i\|\Phi\|_2^2&0
\end{pmatrix},
\]

but the repository does not provide the comparison identifying that compression with the complete ordered coefficient \(\gamma_p\) after wall, tail, fourth-grade, forcing, and radical descent. Substitution would therefore be an unsupported identification.

## Radical quotient

Set

\[
A_p=1+\alpha_p,
\quad
D_p=1/4+\delta_p,
\quad
Z_p=\beta_p+i\gamma_p.
\]

The radical is determined by

\[
\det G_p^\theta=A_pD_p-|Z_p|^2.
\]

- If \(A_pD_p>|Z_p|^2\), the radical is zero.
- If \(A_pD_p=|Z_p|^2\) and the matrix is nonzero, the quotient has rank one.
- If all entries vanish, the quotient is zero.

No source-derived radical quotient can be selected before \(\alpha_p,\beta_p,\gamma_p,\delta_p\) are fixed. Declaring the unspecified cross terms zero would silently choose both the radical and the ordered orientation.

## Four tests

For

\[
G_p^{\rm St}=
\begin{pmatrix}
s_{11}&s_{12}\\s_{21}&s_{22}
\end{pmatrix},
\]

the four defects are exactly

\[
R_{11}=s_{11}-(1+\alpha_p),
\]

\[
R_{12}=s_{12}-(\beta_p+i\gamma_p),
\]

\[
R_{21}=s_{21}-(\beta_p-i\gamma_p),
\]

\[
R_{22}=s_{22}-(1/4+\delta_p).
\]

None is presently evaluable because the repository explicitly leaves undeclared:

1. wall--tail cross pairings;
2. pairings involving the fourth Gaussian grade;
3. the common closed form domain;
4. radical restriction and descent;
5. the complete theta-history mixed coefficients on \(q_1,q_2\).

The first missing typed object is the source-derived sesquilinear table

\[
\bigl[(W_p+T_p+F_p+C_p)(q_j,q_k)\bigr]_{j,k=1}^2
\]

on a declared common closed domain. Its acceptance test is that each contribution has a source formula, the sum is Hermitian with ordered off-diagonal entries retained, and its radical annihilates both argument slots before quotienting.

## Claim boundary

This packet materializes the complete four-entry test and its radical alternatives from currently declared data. It does not assign values to undeclared mixed coefficients, infer Green orthogonality from auxiliary Hilbert orthogonality, identify moment order with Euler grade, prove prime-uniform completion, or establish an RH criterion.

## Disposition

The requested four tests are blocked at one absent authoritative object: the complete source-derived theta-history mixed form on \(q_1,q_2\). Existing endpoint columns determine only \(E=\operatorname{diag}(1,1/4)\). Numerical fitting, parity defaults, positive face sums, determinant equality, and Fourier sewing cannot supply the four missing ordered coefficients. Reopen this branch only when a source formula for the displayed sesquilinear table and its common closed domain is supplied.
