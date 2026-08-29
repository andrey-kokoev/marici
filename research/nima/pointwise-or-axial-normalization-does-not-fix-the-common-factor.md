# Pointwise or axial normalization does not fix the common factor

## Claim under test

Suppose two determinant charts have a fixed reciprocal transition. Multiplying both chart sections by the same entire function preserves that transition. The question is whether a value normalization and asymptotic normalization on the imaginary axis force the common factor to be trivial.

They do not.

## Exact hostile

For any real parameter satisfying

\[
0<\varepsilon<1,
\]

define

\[
h_\varepsilon(\lambda)=1+\varepsilon e^{\lambda^2}.
\]

This factor is entire. On the imaginary axis,

\[
h_\varepsilon(iy)=1+\varepsilon e^{-y^2}\longrightarrow 1
\]

as either end of the axis is approached. It can also be rescaled to take any prescribed nonzero value at one chosen point without changing its divisor.

Nevertheless it has nonreal zeros. They satisfy

\[
\lambda^2=\log(1/\varepsilon)+(2k+1)\pi i,
\qquad k\in\mathbb Z.
\]

Thus a common multiplication

\[
(D_+,D_-)\longmapsto(h_\varepsilon D_+,h_\varepsilon D_-)
\]

preserves the transition quotient and the axial asymptotic normalization while inserting a common off-axis divisor.

## Consequence

The chart transition, one-point normalization, and asymptotics along one line do not determine the determinant divisor. The missing datum is a source-derived function class with a uniqueness theorem.

A sufficient strong gate is that the admissible common factor be entire and bounded in both open half-planes, with compatible boundary control. It is then bounded on the plane and hence constant by Liouville's theorem. A single normalization fixes that constant. Weaker Hardy, Smirnov, Cartwright, or outer-function gates may suffice, but their hypotheses must be derived from the theta/Tate construction rather than imposed after the desired divisor is known.

Boundary modulus alone must also be audited for inner-factor ambiguity. The source must fix not only a transition law but the admissible determinant-line section class.

## Finite falsifier

Take \(\varepsilon=1/2\) and

\[
w=\log 2+\pi i,
\qquad
\lambda_0=\sqrt w.
\]

Then \(\operatorname{Im}\lambda_0\ne0\) and

\[
h_{1/2}(\lambda_0)=0.
\]

Any proposed normalization theorem admitting this factor is too weak to carry zero-confinement information.

