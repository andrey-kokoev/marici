# Every Prime Shift Is a Positive Green Repair Current

## Exact source recursion

For each prime \(p\), the labelled theta source satisfies

\[
\Phi(u)=\Phi_{p\nmid}(u)+p^{-1/2}\Phi(u+\log p).
\]

The centered Green operator

\[
L=D^2-\frac14
\]

commutes with translation and label exclusion. Hence, with \(F=L\Phi\),

\[
F(u)=F_{p\nmid}(u)+C_p(u),
\]

where the prime repair current is independently defined by

\[
C_p(u)=p^{-1/2}F(u+\log p).
\]

No Schur complement or desired scalar identity enters this definition.

## Positivity from defect localization

Entry 3263 proved

\[
F(u)>0
\qquad(u>u_*),
\]

with \(u_*<0.239\). Since

\[
\log p\ge\log2>0.693>u_*,
\]

we obtain the pointwise source theorem

\[
C_p(u)>0
\qquad(p\in\mathbb P,\ u\ge0).
\]

Thus every prime-divisible branch of the Green source is already wholly in
the positive repair sector. The unique negative band remains in the primitive
exclusion remainder.

## Transform and mandatory moving seam

Let

\[
\mathcal F(z)=\int_0^\infty F(u)e^{zu}\,du,
\qquad
B_p(z)=\int_0^{\log p}F(u)e^{zu}\,du.
\]

Changing variables gives the exact transformed repair current

\[
\widehat C_p(z)
=p^{-1/2-z}\bigl(\mathcal F(z)-B_p(z)\bigr).
\]

The finite seam \(B_p\) is therefore forced by the source translation. It
cannot be omitted, reconstructed from the tail, or selected after forming a
Schur complement.

## Consequence

This is the first arithmetic discriminator that the hostile two-Gaussian
source of entry 3266 lacks. The theta repair is not merely a positive tail; it
is a compatible family of positive currents indexed by every prime, each with
its own source-fixed moving seam.

The next finite residual audit should construct the primitive, square,
archimedean, and mixed-seam currents independently and compare their sum with
the doubled Green defect. Any mismatch must remain visible as a typed residual.
