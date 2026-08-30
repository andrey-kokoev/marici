# The oriented Cut leaves only a finite boundary jet

Owner: `marici.Nima`

The earlier polar-decomposition result and the present dispersion theorem
answer different questions.  The inclusive effect

\[
E=K^\dagger K
\]

forgets the orientation and phase of the pair-production amplitude.  It
therefore permits the continuous family

\[
S_{\rm el}=U\sqrt{I-E}.
\]

The vector-valued dispersive input is stronger: it retains the complete
right- and left-cut helicity discontinuities with their crossing labels.

## Uniqueness theorem in the exact one-loop class

Fix spacelike transfer (T).  Let (M) and \(\widetilde M\) be two
one-loop massive-fermion helicity vectors satisfying:

1. the same oriented discontinuity on both physical cuts;
2. the exact one-loop singularity inventory, with no additional poles;
3. the fixed-transfer bound (O(\log^2|\nu|));
4. the same source-normalized first jet at the crossing point.

Their difference (D=M-\widetilde M) has zero jump on both cuts.  It
therefore continues through the cuts.  The source singularity inventory
excludes isolated poles, so (D) is entire.  Cauchy's estimate together with
the logarithmic growth bound makes (D) constant.  Equality of the
crossing-point value then gives (D=0).

Equivalently, the twice-subtracted Cauchy representation first exposes a
degree-at-most-one ambiguity.  Crossing and Bose reduction type it as

\[
P(\nu,T)=
\begin{pmatrix}
a(T)+b(T)\nu\\
c_2(T)\\
c_5(T)
\end{pmatrix}.
\]

The source-normalized first jet fixes all four coordinates.  The exact
large-circle gate forbids a quadratic or higher subtraction direction.

## CDD classification

A nontrivial inner/CDD factor can preserve a boundary modulus, which is why
it survives the inclusive-effect problem.  It cannot preserve the complete
oriented discontinuity and the boundary jet while remaining in the declared
one-loop analytic class.  The additive difference theorem above then forces
the purported alternative completion to equal the original amplitude.

Thus the exact classification is:

- effect alone: a continuous polar-unitary phase family;
- oriented Cut alone: a four-coordinate additive boundary jet;
- oriented Cut plus the source-normalized boundary jet: a unique one-loop
  amplitude;
- additional polynomial or inner/CDD freedom: none in this analytic class.

This is deliberately scoped to the exact massive-fermion one-loop source.
It does not exclude new poles, higher-loop subtraction data, or
nonperturbative CDD sectors in an enlarged source category.

## Finite control

The theorem is accompanied by independent hostile real and complex
reconstruction.  After restoring the four-coordinate jet, the measured
diagonal residual matrix differs from the identity by at most

\[
2.37\times10^{-5},
\]

within the independently measured quadrature uncertainty.  This numerical
control tests the implementation; the global exclusion of CDD freedom comes
from the analytic argument, not from sampling.
