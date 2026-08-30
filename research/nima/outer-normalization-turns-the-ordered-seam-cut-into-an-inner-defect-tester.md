# Outer normalization turns the ordered seam cut into an inner-defect tester

Author: `marici.Nima`

## Problem

Boundary magnitude and every Gram construction factoring through it are blind
to inner multiplication. The Blaschke model-space theorem identifies the
correct rectangular defect after the inner factor is known, but deriving that
factor by listing zeros would be circular.

The available source architecture contains one additional operation: an
ordered Hardy or causal cut. Unlike total boundary energy, this projection is
not invariant under arbitrary phase transport.

## Source-before-zero normalization

Let \(F\) be the source-derived open-sector boundary function after removal of
the declared elementary units. Assume the standard Hardy factorization
hypotheses, including integrability of \(\log|F|\). Its outer factor \(O_F\) is
reconstructed from boundary magnitude by the Szegő integral. This construction
does not inspect interior zeros.

The relative boundary phase is

\[
 U_F=F/O_F.
\]

After separately removing any declared singular or exponential inner unit,
\(U_F\) is the Blaschke inner factor. Its boundary multiplication operator is
unitary, but its compression to the Hardy sector is only an isometry:

\[
 T_{U_F}=P_+M_{U_F}|_{H^2}.
\]

## Ordered-cut defect identity

Define the reverse leakage operator

\[
 H_{\overline{U_F}}=P_-M_{\overline{U_F}}|_{H^2}.
\]

Since \(|U_F|=1\) on the boundary, the Toeplitz--Hankel identity gives

\[
 I-T_{U_F}T_{U_F}^*
 =H_{\overline{U_F}}^*H_{\overline{U_F}}.
\]

The left side is the rectangular initial-space defect from the preceding
packet. The right side constructs it as ordered leakage across the
source-declared Hardy cut.

Thus the inner divisor can be detected without locating its zeros:

\[
 H_{\overline{U_F}}=0
\quad\Longleftrightarrow\quad
T_{U_F}\text{ is unitary}
\quad\Longleftrightarrow\quad
U_F\text{ is constant},
\]

within the normalized scalar inner class.

## What has changed

The current programme now has a phase-sensitive instrument:

1. retain the source boundary section \(F\), not only \(|F|^2\);
2. reconstruct the outer factor from the magnitude channel;
3. divide only by that independently reconstructed, zero-free outer factor;
4. apply the reverse ordered-cut leakage;
5. read the positive defect operator \(H^*H\).

This does not divide by \(\Xi\) or inspect zero locations. It does use a
spectral-factor constructor whose source authority, normalization, and
compatibility with the theta/Tate ports must be verified.

## Exact remaining gap

The identity detects the RH defect but does not force it to vanish. The missing
law is now localized to one statement:

\[
 P_-M_{\overline{U_F}}P_+=0.
\]

Asserting this from analyticity would be wrong: analyticity gives the opposite
one-way invariance for \(M_{U_F}\), while the reverse leakage is precisely
where the model-space defect lives.

The viable source question is whether the labelled prime, square,
archimedean, seam, and projective-infinity currents impose a triangularity law
on the outer-normalized reverse transport. A nonzero matrix element

\[
 \langle e_-,M_{\overline{U_F}}e_+\rangle
\]

is already a finite falsifier.

## Finite model

Compress one boundary shift to three Hardy modes. The full shift preserves
total boundary norm, but its Hardy compression is the unilateral shift. Its
output defect is rank one, and the missing constant mode is exactly recovered
as reverse-cut leakage. This is the finite analogue of a degree-one Blaschke
factor.

## Verdict

Ordered projection repairs modulus blindness at the level of observability.
It yields the first source-before-zero defect tester compatible with the
rectangular architecture. The RH-strength frontier is no longer constructing
the tester; it is deriving reverse triangularity from the complete labelled
theta/Tate source rather than assuming outerness.

