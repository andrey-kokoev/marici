# The two-cone Toeplitz current is relative flux, not unsigned density

## One-prime bilateral carrier

Let `H` have basis `e_r` for integer valuations `r`, and let

\[
Be_r=e_{r+1}.
\]

The two closed valuation cones are

\[
H_+=\operatorname{span}\{e_r:r\ge0\},
\qquad
H_-=\operatorname{span}\{e_r:r\le0\}.
\]

They meet in the vacuum line `C e_0`. Reflection

\[
Re_r=e_{-r}
\]

exchanges the cones and satisfies

\[
RBR=B^{-1}.
\]

The outward unilateral shifts are `V_+=B` on `H_+` and `V_-=B^{-1}` on
`H_-`. Their depth-`k` defects are

\[
P_k^+=I-V_+^kV_+^{*k},
\qquad
P_k^-=I-V_-^kV_-^{*k},
\]

with

\[
\operatorname{rank}P_k^+
=\operatorname{rank}P_k^-=k,
\qquad
RP_k^+R=P_k^-.
\]

## Three combinations that must not be conflated

There are three distinct constructions.

First, the direct-sum unsigned density counts both cone copies and has total
rank `2k`.

Second, the union inside the bilateral carrier identifies the common vacuum
and has rank `2k-1`.

Third, the oriented relative current is

\[
J_k=P_k^+-R^{-1}P_k^-R.
\]

As an abstract transported class it vanishes, expressing flat bilateral
sewing. Before transporting both terms into the same cone, it is the
anti-diagonal pair

\[
(P_k^+,-P_k^-),
\]

which records nonzero boundary flux with zero total index.

Thus cancellation of the scalar index does not mean disappearance of the
boundary data. It means that the data live in a relative, anti-invariant
channel.

## Why the Euler current selects the relative channel

The determinant section is a scalar degree-zero object. Its logarithmic
derivative is a current: under reversal of the scale coordinate, derivatives
change orientation. For an even completed section `D(q)=D(-q)`,

\[
\frac{d}{dq}\log D(-q)
=-rac{d}{dq}\log D(q).
\]

Therefore the Toeplitz realization of the Euler logarithmic derivative must
transform in the sign representation of cone exchange. The unsigned sums are
not candidates for this current. The source-selected object is the relative
flux pair `(P_k^+,-P_k^-)`.

This is the missing typing behind the earlier statement that Fourier reverses
the local index. It reverses orientation, not the positivity of each defect
projection.

## Common-vacuum cancellation

At every depth, both defects contain the vacuum projection. In the oriented
difference it cancels. The remaining reduced defects are

\[
\widetilde P_k^+
=P_k^+-P_1^+,
\qquad
\widetilde P_k^-
=P_k^--P_1^-,
\]

each of rank `k-1`. Hence the primitive vacuum is seam incidence, while the
new cells from depths two and higher live on the two relative arms. This gives
a geometric reason to separate the primitive and square completion grades
without treating them as independent source operators.

## What remains source-dependent

The local reflection determines the sign representation, but not the global
pairing of this relative flux with the archimedean theta boundary. A scalar
functional can annihilate the anti-diagonal pair even though the relative
class is nonzero. Conversely, summing absolute defect energies would replace
the current by an unsigned density and lose the Fourier orientation.

The next global map must therefore land in a relative boundary line or
two-term complex that retains the anti-diagonal class until archimedean
sewing. It cannot first sum the two cone defects.

## Falsifiers

1. Counting `2k`, `2k-1`, and zero as though they were the same boundary
   invariant.
2. Declaring the positive projections themselves to change sign under
   Fourier.
3. Summing the two cone energies before applying the oriented current map.
4. Concluding that zero total index means zero relative boundary class.
5. Inferring archimedean cancellation from the one-prime reflection alone.

## Result

The two-cone Toeplitz object has positive defect density on each cone but an
anti-invariant relative flux under Fourier. Its scalar total index cancels,
while its anti-diagonal boundary class survives. The common vacuum is the seam
incidence; higher prime-power cells occupy the two reduced arms. The live RH
gate is the archimedean pairing of this relative flux, not another local
positivity statement.
