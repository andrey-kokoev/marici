# The Moving Seam Is the Exact First Euler–Evans Comparison Cell

## Source shift

Let the primitive half-line source have transform

\[
F(z)=\int_0^\infty \phi(v)e^{zv}\,dv.
\]

For a prime \(p\), source transport gives the shifted label

\[
\phi_p(u)=p^{-1/2}\phi(u+\log p).
\]

Put \(s=1/2+z\) and \(q_p=p^{-s}\). Its endpoint contribution is

\[
\begin{aligned}
F_p(z)
&=\int_0^\infty \phi_p(u)e^{zu}\,du\\
&=q_p\int_{\log p}^\infty \phi(v)e^{zv}\,dv.
\end{aligned}
\]

Define the finite moving-seam window

\[
B_p(z)=\int_0^{\log p}\phi(v)e^{zv}\,dv.
\]

Then the exact source identity is

\[
F_p(z)=q_p\bigl(F(z)-B_p(z)\bigr).
\]

## First comparison jet

Adjoin the shifted label with a formal amplitude \(\varepsilon\). The Evans
endpoint section becomes

\[
F_{\varepsilon,p}(z)
=F(z)+\varepsilon q_p\bigl(F(z)-B_p(z)\bigr).
\]

The bare Euler determinant-frame prediction is

\[
(1+\varepsilon q_p)F(z)
=F(z)+\varepsilon q_pF(z).
\]

Their difference is exactly

\[
-\varepsilon q_pB_p(z).
\]

Therefore

\[
\left.\partial_\varepsilon F_{\varepsilon,p}\right|_{\varepsilon=0}
=
\left.\partial_\varepsilon
\left((1+\varepsilon q_p)F-\varepsilon q_pB_p\right)
\right|_{\varepsilon=0}.
\]

The first Euler–Evans mismatch is neither a free counterterm nor an
archimedean remainder. It is precisely the source-derived moving-seam
current forced when the shifted half-line endpoint is returned to the fixed
chart.

## Logarithmic form and its limitation

Away from zeros of \(F\), the logarithmic first jets satisfy

\[
\left.\partial_\varepsilon\log F_{\varepsilon,p}\right|_0
=q_p-q_p\frac{B_p}{F}.
\]

The first term is the Euler determinant jet and the second is the seam jet.
This quotient form is unsuitable at a zero and cannot define the comparison
constructor. The undivided section identity above is the authoritative form.

This distinction matters: the section identity is source-derived and entire
where the integrals are defined, while the logarithmic identity is only a
chart on the complement of the Evans divisor.

## Multi-tower meaning

The label/input tower contributes \(q_p\). The endpoint/output tower
contributes \(F\). Their naive product overcounts the part of the shifted
source lying between \(0\) and \(\log p\). The control/coherence tower returns
that finite interval as the negative seam incidence \(-q_pB_p\).

Thus the first mixed cell is

\[
q_pF
\longmapsto
q_pF-q_pB_p.
\]

This is the first concrete evidence that the operator lift must retain the
moving endpoint as a stateful boundary port. A colligation built only from an
Euler multiplier and a fixed endpoint cannot reproduce even the first
labelled-addition jet.

## What remains

The identity closes the first scalar section jet only. It does not construct
the reciprocal return block \(C_X\), identify a Schur complement, or prove
that higher additions compose in the required operator category.

The next gate is the two-addition operator lift. Its scalar shadow must retain
both moving windows and their shared \(pq\) corner. Its determinant shadow
must reproduce the det3 cocycle. Its endpoint shadow must reproduce the
twice-shifted Evans section without division by that section.

## Falsifier

For any proposed finite colligation, introduce one source-label amplitude
\(\varepsilon\). Reject it if its undivided endpoint first variation differs
from

\[
q_p\bigl(F-B_p\bigr),
\]

or if the term \(-q_pB_p\) is inserted only after dividing by \(F\).

## Scope

This derives the exact first Euler–Evans comparison cell from source
transport. It does not establish the two-prime operator lift, reciprocal
dagger completion, completion stability, zero confinement, or RH.
