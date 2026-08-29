# Positive angle does not control the determinant frame of Green reduction

## Operator equivalence versus determinant equivalence

Let

\[
C_X:
R_X/(R_X\cap N_X)
\longrightarrow
(R_X+N_X)/N_X
\]

be the canonical comparison between reachable restriction and Green quotient.

A uniform Friedrichs-angle bound gives

\[
\lVert C_X\rVert\le1,
\qquad
\lVert C_X^{-1}\rVert\le\alpha^{-1}
\]

for some \(\alpha>0\). Hence the two reduced carriers are uniformly equivalent
as normed spaces.

This does not control the induced map on determinant lines when the dimension
grows.

## Constant-angle hostile

Let

\[
C_n=\alpha I_n
\]

on an \(n\)-dimensional reduced carrier, with fixed

\[
0<\alpha<1.
\]

Every singular value equals \(\alpha\). Therefore

\[
\lVert C_n^{-1}\rVert=\alpha^{-1}
\]

uniformly, and the transversality angle is uniformly positive.

But

\[
\det C_n=\alpha^n\longrightarrow0.
\]

Thus operator-level equivalence can coexist with collapse of the determinant
frame.

A completed scalar section transported through \(C_n\) may acquire a vanishing
multiplier even though the reduced operators remain uniformly similar or
congruent.

## Polar comparison

Take the polar decomposition

\[
C_X=Q_XP_X,
\qquad
P_X=(C_X^*C_X)^{1/2}>0.
\]

The unitary \(Q_X\) carries orientation and phase. The positive factor \(P_X\)
carries metric distortion.

The Friedrichs-angle bound controls

\[
\alpha I\le P_X\le I.
\]

It does not control the sum of logarithmic distortions

\[
\operatorname{Tr}|\log P_X|.
\]

The determinant magnitude is

\[
|\det C_X|
=
\det P_X
=
\exp\!\left(\operatorname{Tr}\log P_X\right).
\]

Uniform noncollapse requires control of this extensive trace, not only of the
smallest singular value.

## Determinant-class gate

A natural sufficient condition is that, after a source-fixed unitary
normalization \(Q_X\),

\[
P_X-I
\]

belongs to the trace class and satisfies

\[
\sup_X\lVert P_X-I\rVert_1<\infty
\]

on every compact spectral set, together with the positive angle bound.

Because \(P_X\ge\alpha I\), the logarithm is Lipschitz on
\([\alpha,1]\). Hence

\[
\sup_X\lVert\log P_X\rVert_1<\infty.
\]

The relative determinant

\[
\delta_X=\det P_X
\]

is then bounded away from zero and infinity after compatible normalization.

A sharper primary condition is direct convergence of

\[
\log\delta_X
=
\operatorname{Tr}\log P_X.
\]

Trace-norm control is one sufficient route, not the only possible source law.

## Congruence multiplier

Suppose the reachable and quotient pencils are related by

\[
F_X^R=C_X^*\overline F_XC_X,
\qquad
B_X^R=C_X^*\overline B_XC_X.
\]

Then the residuals satisfy

\[
R_X^R=C_X^*\overline R_XC_X.
\]

At finite rank,

\[
\det R_X^R
=
\overline{\det C_X}\,
\det C_X\,
\det\overline R_X
=
|\det C_X|^2
\det\overline R_X.
\]

Therefore the determinant-line comparison multiplier is the square norm of the
top-exterior comparison.

Uniform angle controls the congruence but does not ensure that

\[
|\det C_X|^2
\]

converges to an invertible unit. The constant-angle hostile makes this
multiplier decay as \(\alpha^{2n}\).

## Orientation cell

The positive determinant \(\det P_X\) controls magnitude only. A determinant
line also needs a coherent phase or orientation from \(Q_X\).

A source-fixed unitary comparison must satisfy:

- compatibility with cutoff inclusions;
- reciprocal transport between sectors;
- seam orientation;
- primitive and square anomaly-line frames;
- Gaussian Mellin normalization.

Choosing \(Q_X\) independently at each cutoff can preserve singular values
while rotate the determinant phase without limit.

Thus metric determinant control and orientation control are separate cells.

## Cutoff naturality square

Let

\[
j_{XY}^R
\]

and

\[
j_{XY}^Q
\]

be cutoff maps on reachable and quotient reductions. The comparisons must obey

\[
C_Yj_{XY}^R
=
j_{XY}^QC_X.
\]

This square makes \(C_X\) a natural transformation of reduced-carrier systems.

Without it, convergent determinants at each cutoff may still compare unrelated
finite state objects.

## Reciprocal commuting cube

Let \(J_X^R\) and \(J_X^Q\) be reciprocal maps on the two reduced
presentations. In addition to cutoff naturality, require

\[
C_{-,X}J_X^R
=
J_X^QC_{+,X}.
\]

Together, cutoff and reciprocal maps form a commuting cube with the comparison
maps \(C_X\).

The polar frames must descend through this cube. An equality of final scalar
determinants is only a shadow of the cube and does not authorize its phase.

## Relative determinant alternative

If \(P_X-I\) is not trace class, the comparison may still admit a higher-order
relative determinant compatible with the third-order boundary packet.

Then the first two comparison traces must be retained as anomaly-line data,
and the connected comparison must lie in the corresponding Schatten ideal.

The admissible condition is not an arbitrary renormalized number. It is a
relative determinant functor whose transition maps commute with the cutoff and
reciprocal cube.

## Determinant density alternative

A normalized density

\[
\frac1{\dim R_X}\log\det P_X
\]

may converge even when \(\det P_X\) collapses. Such a density records extensive
metric distortion but does not by itself provide an invertible determinant-line
multiplier.

It is sufficient for an RH bridge only if the source determinant is itself
defined as a density and the missing extensive normalization is independently
trivialized. Otherwise density convergence is weaker than line descent.

## Interaction with spectral exactness

The ordered audit is now:

1. positive Friedrichs angle;
2. natural comparison of reduced bundles;
3. determinant-class control of the polar defect;
4. coherent unitary orientation;
5. norm-resolvent or collectively compact spectral exactness;
6. compact-local separation from generalized eigenvalue one;
7. completed determinant-line identification with \(\Xi\).

Spectral convergence before determinant-frame control can prove stable zero
sets while still fail to produce an invertible \(\Xi\)-comparison unit.

## Hostile tests

1. \(C_n=\alpha I_n\) has uniform angle but exponentially collapsing
   determinant.
2. Uniform inverse bounds do not control \(\operatorname{Tr}|\log P_X|\).
3. Independent unitary polar factors can rotate determinant phase.
4. Finite congruent pencils can have determinant sections related by a
   vanishing multiplier.
5. A nonnatural comparison does not define one map of cutoff systems.
6. Determinant density convergence does not imply determinant-line descent.
7. Renormalizing the comparison without anomaly-line provenance changes the
   source frame.

## Consequence for categorical RH

The bridge between reachable restriction and Green quotient now has two
independent quantitative layers:

- Friedrichs angle controls operator geometry;
- polar relative determinant controls determinant-line geometry.

Both must be natural under cutoff inclusion and reciprocal congruence. Only
then may spectral exactness and the gap at one be promoted to a completed
\(\Xi\)-line statement.

## Verdict

Uniform transversality is necessary but not sufficient for categorical RH.
Growing rank can collapse the determinant comparison while every operator norm
remains controlled. The missing determinant coherencer is a natural,
reciprocal, determinant-class polar comparison with an invertible completed
relative determinant.
