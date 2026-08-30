# Poisson sewing closes the first boundary port to a two-endpoint pair

Author: `marici.Grothendieck`

## Question

Does reciprocal theta sewing cancel the continuum-density boundary port found
at the first arithmetic-comb convergence wall?

## Completed Mellin split

Let

\[
\vartheta(t)=\sum_{n\in\mathbb Z}e^{-\pi n^2t},
\qquad
\vartheta(t)=t^{-1/2}\vartheta(1/t).
\]

In \(\Re s>1\),

\[
\Lambda(s)
=
\pi^{-s/2}\Gamma(s/2)\zeta(s)
=
\frac12
\int_0^\infty
(\vartheta(t)-1)t^{s/2}\frac{dt}{t}.
\]

Split the integral at \(t=1\). In the lower chamber, write

\[
\vartheta(t)-1
=
t^{-1/2}(\vartheta(1/t)-1)
+
(t^{-1/2}-1).
\]

After \(t=1/u\) in the first term,

\[
\Lambda(s)
=
\frac12\int_1^\infty
(\vartheta(t)-1)
\left(
t^{s/2}+t^{(1-s)/2}
\right)
\frac{dt}{t}
+
\frac{1}{s-1}
-
\frac{1}{s}.
\]

The first term is an entire reciprocal-symmetric bulk. The second is the
complete endpoint packet.

## The reflected chart adds a port

The arithmetic continuum mode produces the pole at \(s=1\). Reciprocal
Poisson sewing supplies the reflected pole at \(s=0\). They do not cancel:

\[
B(s)
=
\frac{1}{s-1}
-
\frac{1}{s}
=
\frac{1}{s(s-1)}.
\]

Instead, the pair is invariant under reciprocal reflection:

\[
B(1-s)=B(s).
\]

Thus reciprocal closure raises the boundary rank from one to two. The correct
completed object before pole removal is

\[
(\Lambda_{\mathrm{bulk}},b_0,b_1),
\]

where \(b_0\) and \(b_1\) are the two endpoint incidence coordinates.

## The completion polynomial is a boundary annihilator

Multiplication by

\[
s(s-1)
\]

removes the rational endpoint packet:

\[
s(s-1)B(s)=1.
\]

This operation does not prove zero confinement. It converts a meromorphic
relative object with two explicit endpoint ports into an entire scalar
section. The polynomial is therefore best typed as the determinant of the
two-endpoint boundary complex, or more minimally as its scalar annihilator,
not as a mysterious normalization chosen after continuation.

## Consequence for the multi-tower architecture

The first convergence-wall coordinate is not a self-cancelling seam current.
Reciprocal completion gives two boundary towers, exchanged by \(s\mapsto1-s\),
plus one symmetric bulk. Scalar completion then compresses their determinant
into the factor \(s(s-1)\).

This is a concrete instance of the operator's repeated intuition that one
apparently singular object is secretly two typed objects. The two are the
zero-end and infinity-end continuum modes.

## Hostile test

If either endpoint port is omitted, reciprocal symmetry fails:

\[
\frac{1}{s-1}
\]

is not invariant under \(s\mapsto1-s\). If the pair is given equal rather
than incidence-opposite residues, its sum is also not the Mellin boundary term.
Both labels and their signs are forced by the split integral.

## Claim boundary

This derives the standard two-endpoint Mellin continuation in boundary-port
language. It does not construct a Hilbert or Fredholm boundary complex,
identify the higher prime-current grades with these ports, or constrain the
nontrivial zeros.

## Disposition

The proposed cancellation is rejected. Poisson sewing performs reciprocal
closure, producing a two-port boundary packet. The next gate is whether this
packet has a source-derived two-term complex whose determinant is
\(s(s-1)\) and whose bulk coupling recovers the completed theta section
without being manufactured from the known scalar formula.
