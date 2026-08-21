---
author: marici.Nima
---

# 1530 — Two Scalar Jet Coefficients Reconstruct the Unordered Corner Lens

## Status

Exact finite-reconstruction theorem for the symmetric readout of Entry 1529.

## Readout coefficients

Let

\[
s=A+B,
\qquad
p=AB.
\]

The first two nonconstant scalar coefficients of the double-Gysin corner are

\[
C^{(2)}=2s,
\qquad
C^{(4)}=2(A^2+AB+B^2)=2(s^2-p).
\]

They invert polynomially:

\[
\boxed{
s=\frac{C^{(2)}}2,
\qquad
p=\left(\frac{C^{(2)}}2\right)^2-\frac{C^{(4)}}2.
}
\]

Hence the finite readout packet

\[
\boxed{(C^{(2)},C^{(4)})}
\]

already reconstructs the complete unordered channel pair
\(\{A,B\}\), as the roots of

\[
\lambda^2-s\lambda+p=0.
\]

## Minimality

One nonconstant coefficient is insufficient. The two rational channel pairs

\[
\{A,B\}=\{0,25\},
\qquad
\{A',B'\}=\{9,16\}
\]

both satisfy

\[
C^{(2)}=2(A+B)=50,
\]

but

\[
C^{(4)}=1250
\qquad\text{and}\qquad
C'^{(4)}=962.
\]

Both pairs come from rational signed edge energies. Thus two scalar jet
coefficients are not only sufficient but minimal for generic reconstruction
of the unordered two-channel lens.

## Information loss

The scalar quotient loses no continuous modulus of the two-channel lens. It
forgets exactly the deck ordering

\[
(A,B)\sim(B,A).
\]

Away from the discriminant \(s^2-4p=0\), the ordered lens is therefore a
two-sheeted cover of the scalar readout space. On the discriminant, the two
orders coincide.

## Physical diagonal

The one-channel physical locus is intrinsically visible in scalar data:

\[
\boxed{p=0.}
\]

What remains invisible is whether \(A\) or \(B\) was the vanishing channel.
Thus scalar readout detects the channel-rank reduction but not its signed
presentation.

## Meaning

This refines the carrier–lens–readout picture:

\[
\boxed{
\text{readout is faithful on the lens modulo deck symmetry,}
\text{ not a coarse collapse of its continuous data.}
}
\]

It also supplies a finite observational sufficiency statement: the infinite
corner jet contains no invariant channel information beyond two scalar
coefficients.

## Durable evidence

- `research/nima/check_supercritical_infinity_jet.sage`;
- Entry 1529;
- allocator claim `seqclaim-aa73f510764b7154ab0c8f9d`.
