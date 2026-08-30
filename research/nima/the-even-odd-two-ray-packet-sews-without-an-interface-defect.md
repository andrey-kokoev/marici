# The even–odd two-ray packet sews without an interface defect

## Exact two-ray packet

Let \(L>0\), and write the pretranslation prime-cell packet as the sum of
an even and an odd function,

\[
E_L
=
-2\pi L^2f_0+4\pi^2L^2f_2,
\]

\[
O_L
=
8\pi Lf_1-8\pi^2Lf_3,
\]

where

\[
f_j(x)=x^je^{-\pi x^2}.
\]

Thus

\[
E_L(-x)=E_L(x),
\qquad
O_L(-x)=-O_L(x).
\]

The two moving-center rays carry

\[
F_+(x)
=
U_L(E_L+O_L)(x)
=
(E_L+O_L)(x+L),
\]

and

\[
F_-(x)
=
U_{-L}(E_L-O_L)(x)
=
(E_L-O_L)(x-L),
\]

with \(x\ge0\) the outward coordinate on each ray.

## Value sewing

At the common moving cut,

\[
F_+(0)
=
(E_L+O_L)(L).
\]

Parity gives

\[
\begin{aligned}
F_-(0)
&=
(E_L-O_L)(-L)\\
&=
E_L(L)+O_L(L)\\
&=
F_+(0).
\end{aligned}
\]

Hence the two ray values agree exactly.

## Kirchhoff derivative sewing

Because \(E_L'\) is odd and \(O_L'\) is even,

\[
F_+'(0)
=
(E_L'+O_L')(L),
\]

whereas

\[
\begin{aligned}
F_-'(0)
&=
(E_L'-O_L')(-L)\\
&=
-E_L'(L)-O_L'(L)\\
&=
-F_+'(0).
\end{aligned}
\]

Therefore the outward derivatives satisfy the exact Kirchhoff law

\[
F_+'(0)+F_-'(0)=0.
\]

The sign statement uses the two outward ray coordinates. If both sides are
instead written in one global line coordinate, the corresponding normal sign
must be inserted when comparing derivatives.

## Distributional consequence

The value jump and the outward flux jump both vanish. Consequently, sewing
the two smooth ray packets across the moving cut introduces neither a delta
term nor a derivative-of-delta term when a second-order differential
constructor is applied distributionally.

This is stronger than scalar endpoint agreement: the complete first-order
trace pair

\[
\bigl(F(0),\partial_\nu F(0)\bigr)
\]

is compatible with defect-free two-ray sewing.

## Uniformity in the prime scale

The proof uses only the parity of \(E_L\) and \(O_L\). It therefore holds for
every \(L>0\), and in particular for every prime scale

\[
L=\log p.
\]

No small-\(L\), large-\(L\), or first-prime approximation enters the
argument.

## Constructor consequence

For \(p=2\), the exact four-grade packet

\[
U_L(E_L+O_L)
\oplus
U_{-L}(E_L-O_L)
\]

passes the moving-cut trace gate without an additional interface carrier.
More generally, every prime packet with the same source-derived even–odd
reciprocal decomposition passes this local sewing gate.

Thus the first Adams-edge comparison no longer needs to explain a
moving-center delta defect. The next unresolved arrow is the global theta
label synthesis and relative Green comparison between the sewn packet and

\[
d_2=W_{2\log2}-W_{\log2}.
\]

## Falsifier

If the reciprocal ray is assembled as \(U_{-L}(E_L+O_L)\), without reversing
the odd component, then the value traces generally disagree. If it is
assembled with an inconsistent ray orientation, the outward derivative sum
generally fails. Either error creates an interface distribution despite
preserving some scalar shadows.
