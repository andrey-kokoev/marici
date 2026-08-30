# Feedback scaling is not yet an authorized theta homotopy

## Question

Does the interpolation

\[
S_\tau=D-\tau C(I-K)^{-1}B
\]

come from an admitted theta/Tate source operation, or is it only a useful
mathematical deformation?

## What scalar source scaling does

The Schwartz–Bruhat source is a vector space, so multiplication of a test
function by a scalar is authorized. The Tate integral and its linear output
channels scale accordingly.

But scaling the source generally changes every source-dependent channel at
once. It does not selectively hold \(K\) and \(D\) fixed while multiplying
only the returned feedback term by \(\tau\).

Therefore ordinary source linearity does not derive the proposed feedback
homotopy.

## What selective feedback scaling requires

To obtain

\[
B_\tau=\sqrt{\tau}\,B,
\qquad
C_\tau=\sqrt{\tau}\,C,
\]

with \(A=I-K\) and \(D\) fixed, the theory needs an independently controllable
port coupling. In a conservative realization the canonical construction is
an auxiliary vacuum port mixed by

\[
U_\tau=
\begin{pmatrix}
\sqrt{\tau}&\sqrt{1-\tau}\\
-\sqrt{1-\tau}&\sqrt{\tau}
\end{pmatrix}.
\]

The enlarged transformation is unitary. Compression to the original port
produces attenuation by \(\sqrt{\tau}\), and a round trip produces the factor
\(\tau\).

This is an algebraic template, not yet a theta constructor.

## Compression warning

The full vacuum-dilated system and its compressed visible subsystem have
different determinant and kernel data. Discarding the auxiliary port can
create apparent loss, zeros, or strict contraction that are absent from the
conservative dilation.

Hence an authorized attenuation proof must state:

1. the auxiliary unit or vacuum object;
2. the coherent mixing map;
3. the full enlarged colligation;
4. which compression defines the physical scalar readout;
5. why the zero index of the compressed Schur complement is the relevant
   invariant.

One may not use the full unitary system to claim invertibility of a
compression without an additional theorem.

## Present theta/Tate authority

The pinned source provides:

- linear scaling of test functions;
- global Fourier–Poisson sewing;
- reciprocal sheet exchange;
- finite prime incidence;
- a distinguished local unramified vector;
- a candidate vacuum or tensor-unit normalization.

It does not yet provide an independently tunable seam-feedback coupling that
leaves the open bulk and direct boundary block fixed.

Moreover, global Poisson sewing has no finite-Euler constructor analogue.
Any cutoffwise \(\tau\)-homotopy that attenuates a finite Euler feedback loop
cannot be promoted to source authority merely by taking the cutoff limit.

## Mathematical versus explanatory use

Once \(B,C,D,K\) are independently derived, \(S_\tau\) is a legitimate
mathematical homotopy of typed operators. If one can prove its contour gap,
it proves equality of winding numbers regardless of whether a laboratory
actuator realizes \(\tau\).

But it is not yet a source-native explanation. The gap theorem might rely on
special properties of an interpolation with no meaning in the admitted
constructor category.

The programme should therefore label conclusions separately:

- mathematical index homotopy;
- source-authorized constructor homotopy;
- physically executable attenuation.

The first does not imply the latter two.

## Minimal hostile

Let all four colligation blocks depend on one scalar source amplitude
\(\lambda\):

\[
A_\lambda=A_0+\lambda A_1,\quad
B_\lambda=\lambda B_1,\quad
C_\lambda=\lambda C_1,\quad
D_\lambda=D_0+\lambda D_1.
\]

Source scaling changes the Schur complement as

\[
S_\lambda
=D_0+\lambda D_1
-\lambda^2C_1(A_0+\lambda A_1)^{-1}B_1.
\]

This is not

\[
D_1-\tau C_1A_1^{-1}B_1.
\]

The example falsifies the inference from source linearity to selective
feedback scaling.

## Possible source-native replacements

Three routes remain:

1. derive a vacuum-port dilation from the distinguished Tate or Fock unit;
2. find an existing source parameter that genuinely controls only the
   boundary incidence;
3. avoid interpolation and compute the physical Schur index directly from
   its contour data.

The third route needs no constructor homotopy, but still needs the full
operator family and a contour gap.

## Relation to the tensor-unit result

The tensor unit can canonically fix a frame without implementing a controlled
operation. The same distinction appears here. A distinguished vacuum is the
right reference object for attenuation, but possessing it does not construct
the beam-splitter-like coupling \(U_\tau\).

Thus the missing attenuation arrow is another instance of:

> canonical reference does not imply executable transport.

## Disposition

The anchor–homotopy–gap theorem remains mathematically valid. Its naive
feedback path is not yet source-authorized for theta/Tate. The cleanest next
question is whether the distinguished Fock vacuum supports a coherent
two-port dilation whose visible compression is the desired boundary
attenuation.

Until then, the winding argument must be reported as conditional on an
operator homotopy, not as an intrinsic consequence of source scaling.

## Claim boundary

This packet classifies authority and gives a conservative dilation template.
It does not prove that theta/Tate has the auxiliary port, mixing constructor,
or compressed-index theorem.
