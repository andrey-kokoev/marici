# The additive theta--Euler determinant comparison is canonical but divisor-neutral

## The comparison already exists before completion

Let

\[
\mathcal P=\bigoplus_p \mathbb C e_p
\]

be the primitive-prime space and let \(\operatorname{Sym}(\mathcal P)\)
carry the occupation basis \(e_{(k_p)}\), where only finitely many
\(k_p\) are nonzero. Give this basis the source Hamiltonian

\[
H e_{(k_p)}
=
\left(\sum_p k_p\log p\right)e_{(k_p)}.
\]

Unique factorization supplies the canonical basis identification

\[
e_{(k_p)}
\longleftrightarrow
e_n,
\qquad
n=\prod_p p^{k_p}.
\]

It intertwines \(H\) with the integer-label Hamiltonian
\(H e_n=(\log n)e_n\). Therefore, in \(\Re s>1\),

\[
\operatorname{Tr}_{\operatorname{Sym}(\mathcal P)}e^{-sH}
=
\sum_{n\ge1}n^{-s}
=
\prod_p(1-p^{-s})^{-1}.
\]

The nonlinear comparison between the multiplicative Euler object and the
additive integer-labelled object is thus the bosonic Fock expansion followed
by unique factorization. It is not an additional RH-bearing constructor.

## The determinant chart is its cyclic coordinate system

Taking the logarithm in the same convergence chamber gives

\[
\log\zeta(s)
=
\sum_p\sum_{k\ge1}\frac{p^{-ks}}{k}.
\]

Hence the primitive, square, and connected-tail currents are precisely the
first, second, and higher cyclic coordinates of this one Fock trace. The
valuation-filtration identity from the preceding result is the occupation
number shadow of the same comparison.

## Archimedean completion

For

\[
\vartheta(t)=\sum_{n\in\mathbb Z}e^{-\pi n^2t},
\]

termwise Mellin transformation in \(\Re s>1\) gives

\[
\pi^{-s/2}\Gamma(s/2)\zeta(s)
=
\int_0^\infty
\frac{\vartheta(t)-1}{2}t^{s/2}\frac{dt}{t}.
\]

Thus the complete comparison factors canonically through prime occupations,
positive integers, the Gaussian theta source, and finally the Mellin boundary
section.

Unique factorization supplies the first arrow, the Gaussian sampling law the
second, and Mellin transformation the third. Poisson sewing then supplies the
reciprocal continuation and the completion boundary terms.

## Canonical-section rigidity

Suppose a second completed section is obtained by multiplying the source
section by a holomorphic factor \(Q(s)\), while preserving this comparison
on the convergence chamber. There

\[
Q(s)\zeta(s)=\zeta(s).
\]

Since \(\zeta(s)\neq0\) for \(\Re s>1\), one has \(Q=1\) on a nonempty
open set. Analytic continuation forces \(Q=1\) throughout every connected
domain of continuation.

Therefore a hostile divisor-bearing multiplier cannot be a presentation
change of the same source object. It must change the prime Fock object, the
integer sampling law, the Mellin boundary map, or the continuation data.
Canonical-section rigidity is already a theorem once the comparison is
required to agree in the Euler chamber.

## Why this does not prove RH

The comparison determines which completed section is authorized, but it
places no restriction on where that section may vanish. Unique analytic
continuation preserves a divisor; it does not orient it. A canonically
constructed holomorphic function may have zeros anywhere allowed by its
actual dynamics.

This separates two questions that had remained entangled:

1. Which completed scalar section belongs to the theta/Euler source?
2. Why can that particular section vanish only on the reciprocal seam?

The first is answered by Fock expansion, unique factorization, Mellin
transformation, and Poisson continuation. The second remains RH.

## Consequence

The additive-theta/multiplicative-determinant comparison is not the missing
zero-selection force. It is a canonical but divisor-neutral equivalence of
presentations. Further work must act on the authorized section through a
source-derived dynamical, order, or intersection constraint; neither another
prime-current port nor another proof of presentation equivalence can supply
that force.
