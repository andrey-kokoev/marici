# Clark-sheet swap natively reverses theta spin two

## Bounded native-frame test

The complementary-quadrature route must be tested before any
determinant/Fresnel lift. The completed Clark sheets already supply a
source-derived comparison in the Fourier-fixed theta frame.

Let

\[
 P_a=F+iaF',
 \qquad
 Q_a=F-iaF'.
\]

Reversing the Clark orientation sends `a` to `-a` and swaps the two sheets:

\[
 \boxed{P_{-a}=Q_a,\qquad Q_{-a}=P_a.}
\]

This swap, together with reciprocal endpoint orientation and the common
`q`-coordinate, is the native comparison `P_X` at every labelled cutoff. It
does not use a determinant phase.

## Trace and Wronskian transformation

Every symmetric quadratic trace in the two sheets is invariant under their
swap. By contrast, the oriented Wronskian

\[
 W_a=Q_aP_a'-P_aQ_a'
\]

changes sign:

\[
 \boxed{W_{-a}=-W_a.}
\]

Using the common source transform,

\[
 W_a=2ia\bigl(FF''-(F')^2\bigr),
\]

so the sign reversal is exact before diagonal restriction and before any
division by the horizontal spectral coordinate.

The full mixed-sheet kernel inherits the same orientation reversal because
its reflection quotient is the even combination of these Wronskians.

## Native complementary form

Let `T_X` denote the symmetric trace bulk and `S_X` the normalized oriented
Wronskian/spin-two bulk at cutoff `X`, both expressed in the common frame
defined by sheet swap. If the doubled Green normalization gives

\[
 Q_X^+=T_X+S_X,
 \qquad
 P_X^TQ_X^-P_X=T_X-S_X,
\]

then

\[
 \boxed{H_X=2T_X.}
\]

The null-line intersection is trivial whenever `T_X` is the faithful positive
Gram trace on the labelled amplitude packet.

This complementarity is native: it follows from sheet swap and Wronskian
orientation, not from opposite Maslov phases.

## Remaining coefficient gate

The transformation law proves

\[
 T_X\mapsto T_X,
 \qquad
 S_X\mapsto-S_X.
\]

It does not yet prove that the actual Green forms have equal trace
normalizations or unit spin-two coefficients. In general they may be

\[
 Q_X^+=c_X^+T_X+\lambda_X^+S_X,
\]

\[
 P_X^TQ_X^-P_X=c_X^-T_X-\lambda_X^-S_X.
\]

Then

\[
 H_X=(c_X^++c_X^-)T_X
 +(\lambda_X^+-\lambda_X^-)S_X.
\]

Exact complementarity requires

\[
 c_X^+=c_X^->0,
 \qquad
 \lambda_X^+=\lambda_X^-.
\]

Those equalities must be derived from the doubled-tail boundary orientation,
constant-channel normalization, and Mellin units.

## Kernel-level requirement

The spin-two term must be extracted from

\[
 \mathcal X_X(z,w)
 =(z+\bar w)\mathcal R_X(z,w)
\]

before setting `w=z`. Sheet swap reverses the oriented quotient
`R_X` while preserving the trace kernel. This avoids dividing by
`2 Re(z)` and hiding seam behavior.

## Falsifiers

The native route fails at the first cutoff where:

1. exact boundary normalization gives `c_X^+` different from `c_X^-`;
2. the spin coefficients differ after source comparison;
3. an off-diagonal labelled residual is neither trace nor Wronskian type;
4. the Gram trace has a nonzero null vector in the admissible endpoint domain;
5. sheet swap is incompatible with a primitive, square, or archimedean
   boundary channel.

The corresponding failure should be reported as a native shared-null or
normalization residual, with `determinant_phase_used=false`.

## Present result

Native Fourier-fixed theta geometry already supplies the correct
representation-theoretic sign reversal: symmetric trace is even and the
oriented Wronskian is odd under Clark-sheet exchange. The only remaining
finite algebra gate is equality of the source-fixed coefficients and absence
of additional bulk representation types.

