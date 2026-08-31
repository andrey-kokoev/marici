# The polarized pullback test is three matrix identities, not one odd-line norm

## Question

Does the one-dimensional pullback metric for the odd Stokes--Wronskian line
already prove the required quadratic comparison?

## Claim boundary

No. It proves only the odd diagonal entry after the source comparison exists.
The completed Hermitian cell also contains an even diagonal and a
reciprocal-odd mixed entry. Quadratic functoriality is an exact two-by-two
matrix identity, equivalent to three independent scalar identities under the
frozen real structure.

## Source cell

On the retained two-output source frame, write the Hermitian form as

\[
 G_S=
 \begin{pmatrix}
 a_S&r_S+i\ell_S\\
 r_S-i\ell_S&d_S
 \end{pmatrix},
\]

where

- \(a_S,d_S\) are positive diagonal energies;
- \(r_S\) is the reciprocal-even mixed entry;
- \(\ell_S\) is the ordered reciprocal-odd linking entry.

These four real quantities have different source origins. In particular,
\(\ell_S\) is not a positive norm.

## Target cell and comparison

Write the target Wronskian/history form as

\[
 G_W=
 \begin{pmatrix}
 a_W&r_W+i\ell_W\\
 r_W-i\ell_W&d_W
 \end{pmatrix}.
\]

Let the typed comparison preserve the even and odd lines with real positive
source coefficients

\[
 T_p=\operatorname{diag}(\alpha_p,\lambda_p).
\]

The odd scalar \(\lambda_p=-\kappa_p/(2s_p)\) is forced only after the
arithmetic mate square is constructed. The even coefficient \(\alpha_p\) is
independently fixed by its wall/history comparison.

Direct multiplication gives

\[
 T_p^*G_WT_p
 =
 \begin{pmatrix}
 \alpha_p^2a_W&
 \alpha_p\lambda_p(r_W+i\ell_W)\\
 \alpha_p\lambda_p(r_W-i\ell_W)&
 \lambda_p^2d_W
 \end{pmatrix}.
\]

## Exact polarized identities

The equality

\[
 G_S=T_p^*G_WT_p
\]

is equivalent to

\[
 a_S=\alpha_p^2a_W,
\]

\[
 d_S=\lambda_p^2d_W,
\]

\[
 r_S+i\ell_S
 =\alpha_p\lambda_p(r_W+i\ell_W).
\]

The last complex equality contains two real tests. Symmetry or purity may force
one of \(r_S,r_W\) to vanish, but that reduction must be source-proved.

Thus a general two-output cell has four real identities. In the common
reciprocal-pure setting where the even mixed entries are already matched or
zero by type, three nontrivial tests remain: two diagonals and the oriented odd
entry.

## What the odd pullback proves

The one-dimensional construction

\[
 G_{\rm odd,pb}=\lambda_p^2G_{W,\rm odd}
\]

proves only the target value that the source odd diagonal would need to equal.
It does not prove:

- the even comparison coefficient \(\alpha_p\);
- the real mixed-tail identity;
- the ordered linking identity;
- compatibility of positive and skew-originated forms on one carrier.

Therefore a positive pullback norm cannot substitute for the oriented linking
polarization.

## Determinant consistency

If the matrix identity holds, determinants obey

\[
 \det G_S
 =|\alpha_p\lambda_p|^2\det G_W.
\]

This determinant equality is necessary but not sufficient for the matrix
identity. Two Hermitian matrices can have equal determinant and unequal mixed
orientation.

For a resolved positive block plus linking entry, positivity remains

\[
 \ell_p^2<\Delta_p^{\rm res}.
\]

That inequality checks a margin after assembly; it does not prove the assembly
map.

## Finite hostile basis

A complete source check must reject:

1. correct odd norm with reversed \(\ell_W\);
2. correct diagonals with the mixed block set to zero;
3. correct determinant with exchanged even and odd lines;
4. correct scalar \(\lambda_p\) but wrong \(\alpha_p\);
5. a primewise identity that loses continuity at completion.

## Disposition

The canonical odd pullback is one entry of the required comparison, not the
whole theorem. The next exact calculation is the full retained two-output
matrix identity, with the odd scalar, even coefficient, real mixed tail, and
reciprocal orientation separately sourced. No RH conclusion is authorized.
