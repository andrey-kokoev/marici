---
author: marici.Nima
---

# 1527 — Edge-Sign Reversal Exchanges the Two Corner-Jet Channels

## Status

Exact equivariance statement for the two-channel recurrence module of Entry
1525.

## Involution

The signed edge involution

\[
\sigma:y_2\longmapsto-y_2
\]

exchanges the two quadratic generators

\[
A=(y_1+y_2)^2,
\qquad
B=(y_1-y_2)^2:
\]

\[
\boxed{\sigma(A)=B,\qquad\sigma(B)=A.}
\]

The full corner source

\[
I_{\rm corner}(X)=\frac{2X}{(X^2-A)(X^2-B)}
\]

is invariant. Consequently every jet coefficient
(C^{(2m)}=2h_m(A,B)) is invariant, even though its two generating channels
are exchanged.

## Conjugate one-channel loci

The two signed diagonals select opposite channels:

\[
\begin{array}{c|cc}
&A&B\\
\hline
y_2=y_1=y&4y^2&0\\
y_2=-y_1=-y&0&4y^2
\end{array}
\]

Both yield the same scalar source and the same one-channel jet,

\[
\boxed{
I_{\rm diag}(X)=\frac{2}{X(X^2-4y^2)},
\qquad
C^{(2m)}=2(4y^2)^m.
}
\]

## Meaning

The two-channel corner lens is naturally (mathbb Z_2)-equivariant. The
physical equal-edge diagonal is selection of one member of a conjugate pair,
not an invariantly preferred quotient of the abstract corner module. The
scalar readout forgets which signed channel was selected.

This supplies a precise distinction between:

\[
\boxed{
\text{equivariant coefficient lens}
\quad\text{and}\quad
\text{deck-invariant scalar readout}.
}
\]

## Durable evidence

- `research/nima/check_supercritical_infinity_jet.sage`;
- Entries 1525–1526;
- allocator claim `seqclaim-75fd4a928206d85a6bc65331`.
