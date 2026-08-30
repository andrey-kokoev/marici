# Exponent-adapter quarter-divisor convention packet

## Frozen object

The packet uses the source-generated affine pencil

\[
M(\gamma)=M_0+\gamma M_1
\]

at the frozen kinematic point \((X_1,X_2,X_3)=(2,3,4)\).  The matrix has 720 source-relation rows and 535 active labelled coordinates.  Appending the 36 low-readout rows gives

\[
N(\gamma)=\begin{bmatrix}M(\gamma)\\L\end{bmatrix},
\]

with 756 rows.  The two full sparse packets preserve row order, coordinate order, and all coefficients modulo their declared primes.

## Rank convention

At a parameter value \(\gamma\), the reported relative readout rank is

\[
\operatorname{rank}N(\gamma)-\operatorname{rank}M(\gamma).
\]

The generic value is 26.  The checker evaluates both matrices directly by sparse finite-field elimination; it does not infer ranks from determinants.

## Adapted-minor convention

At every tested exceptional parameter, row and column operations first reduce the constant matrix to a rank-normal form.  A full-rank core is then selected from the first-normal bottom block.  The resulting 505-dimensional maximal minor has the minimum valuation licensed by that local rank defect.  Taking the gcd across the frozen adapted-minor family removes chart-specific factors.

At prime 32003 the adapted gcd has degree 266.  Previously certified rational torsion factors account for degree 254.  The residual is

\[
(4\gamma+5)^5(4\gamma+7)^7
\]

up to a nonzero field unit.

## Evidential scope

The following are exact for each of the two finite fields 32003 and 32009:

- \(\operatorname{rank}M=479\) and \(\operatorname{rank}N=505\) at the generic checkpoint \(\gamma=17\);
- \(\operatorname{rank}N=500\) at \(\gamma=-5/4\);
- \(\operatorname{rank}N=498\) at \(\gamma=-7/4\);
- \(\operatorname{rank}M=479\) at both quarter points.

The multiplicities five and seven are exactly reconstructed from the adapted gcd at prime 32003.  Their characteristic-zero lift is a source-rational candidate, not yet a characteristic-zero theorem.  A proof over \(\mathbb Q\) still requires rational rank witnesses and an exact polynomial-minor certificate.

## Prohibited inference

Do not identify five with the five marked denominators, or seven with those marks plus two base directions, merely because the dimensions match.  The next mechanism test must compute the labelled kernel and cokernel representations at both quarter points before assigning provenance.
