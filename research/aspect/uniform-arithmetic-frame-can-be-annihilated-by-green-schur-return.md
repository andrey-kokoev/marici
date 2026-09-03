# A uniform arithmetic frame can be annihilated by Green Schur return

## Question

Does the source-native prime-uniform bilateral valuation frame suffice to produce strong scalar-null confinement after embedding into the enlarged Green cell?

## Source result retained

The normalized central Euler current and first jet already form a prime-uniform two-port frame on the bilateral valuation direct sum. This is the desired noncompact arithmetic observer before theta sampling. Its lower margin is not conjectural at that level.

The unresolved step is transport through the enlarged wall–history–tail/PV–reciprocal Green cell.

## Exact cancellation hostile

On one scalar cyclic mode, take cyclic form, auxiliary form, and cross-coupling

\[
A=1,
\qquad
D=1,
\qquad
C=1.
\]

The full Green block is

\[
G=\begin{pmatrix}1&1\\1&1\end{pmatrix}\ge0.
\]

Before extension, the arithmetic observer \(B=I\) has lower bound one. It is noncompact on an infinite direct sum and cannot factor boundedly through a compact diagonal theta map with singular values tending to zero.

After eliminating the auxiliary coordinate, however,

\[
A_{\rm eff}
=A-CD^{-1}C^*
=1-1
=0.
\]

The vector \((v,-v)\) lies in the full radical for every arithmetic \(v\). Thus the enlarged Green coupling can annihilate the complete arithmetic margin even though the upstream observer is uniformly faithful and independent of theta incidence.

## What is falsified

The implication

\[
\text{uniform noncompact arithmetic observer}
\Longrightarrow
\text{strong completed Green confinement}
\]

is false.

The local core of the bold conjecture survives: the bilateral valuation two-port is a genuine source-native essential observer. What fails is the claim that its existence identifies the missing global confinement mechanism.

## Required global condition

Let

\[
K_p^{\rm return}
=A_p^{-1/2}C_pD_p^\dagger C_p^*A_p^{-1/2}.
\]

The arithmetic lower margin survives only if

\[
\|K_p^{\rm return}\|
\le1-\delta_{\rm ext}
\]

for one \(\delta_{\rm ext}>0\) uniform in prime and grade, together with radical annihilation and domain intertwining. The hostile saturates the forbidden boundary \(\|K^{\rm return}\|=1\).

Exact decoupling \(C_pD_p^\dagger C_p^*=0\) is sufficient but not expected when the tail/PV sector generates a genuine odd return.

## Relation to theta incidence

Theta compactness is no longer the decisive obstruction once the valuation frame is retained. The decisive obstruction moves to terminal cancellation in the Green extension. Theta may remain a compact realization/calibration port, but it cannot control the return norm by itself.

## Verification

`research/aspect/checkers/check_arithmetic_frame_schur_cancellation.py` verifies upstream unit coercivity, positivity of the full block, exact Schur annihilation, a radical vector with nonzero arithmetic component, and unbounded inverse norms for compact theta cutoffs using exact rational arithmetic.

## Disposition

Reject the bold conjecture in its global form. Retain the proved local statement that the bilateral valuation frame supplies essential arithmetic coercivity. The next programme-changing test is the source-derived return operator \(K_p^{\rm return}\): construct it on the enlarged Green cell and determine whether its norm is uniformly below one or reaches the cancellation boundary.
