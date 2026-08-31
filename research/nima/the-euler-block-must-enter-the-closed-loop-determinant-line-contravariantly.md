# The Euler block must enter the closed-loop determinant line contravariantly

## Variance audit

In the Euler domain,

\[
A_0(s)=I-L(s)
\]

satisfies

\[
\det A_0(s)^{-1}=\zeta(s).
\]

The completed source section is

\[
\xi(s)=B_\infty(s)\det A_0(s)^{-1}.
\]

Therefore the arithmetic Euler block belongs contravariantly in the completed
determinant line.  An ordinary block determinant places \(\det A_0\) in the
numerator and has the wrong variance.

## Ordinary cone mismatch

For the ungraded closed-loop block

\[
\mathcal C(s)=
\begin{pmatrix}
A_0(s)&-B(s)^\dagger\\
-B(s)&D_0(s)
\end{pmatrix},
\]

finite Schur factorization gives

\[
\det\mathcal C
=
\det A_0\det D_0\det(I-K_{\rm rel}).
\]

Even before completion, this cannot be the Euler/Xi section: its open Euler
factor is \(\det A_0\), whereas Xi requires \(\det A_0^{-1}\).

This does not invalidate the cone kernel calculation.  It invalidates the
claim that the ordinary scalar determinant of that cone has the required
Euler character.

## Graded determinant line

Put the arithmetic prime-loop object in odd degree and the boundary-history
object in even degree.  The determinant line of the resulting two-term object
has variance

\[
\operatorname{Det}(D_0)
\otimes
\operatorname{Det}(A_0)^*.
\]

Its uncoupled finite character is

\[
\frac{\det D_0}{\det A_0}.
\]

After inserting the source archimedean and endpoint trivialization, the
arithmetic factor now has the required Euler orientation.

The coupled object must therefore be formulated as a graded boundary complex
or a bordered determinant-line morphism, not as an ungraded determinant of
\(\mathcal C\).

## Berezinian diagnostic

For an invertible even block \(D_0\), the finite-dimensional Berezinian with
\(A_0\) in odd degree has the form

\[
\operatorname{Ber}
\begin{pmatrix}
D_0&-B\\
-B^\dagger&A_0
\end{pmatrix}
=
\frac{
\det(D_0-BA_0^{-1}B^\dagger)
}{
\det A_0
}.
\]

Equivalently,

\[
\operatorname{Ber}
=
\frac{\det D_0}{\det A_0}
\det(I-GBA_0^{-1}B^\dagger).
\]

By the Sylvester identity, the relative factor has the same nonzero divisor as
\(I-K_{\rm rel}\).  Thus the graded character simultaneously retains:

- inverse Euler variance;
- the boundary factor;
- the relative closed-loop collision divisor.

The displayed Berezinian is only a finite-cutoff diagnostic.  The completed
construction must use determinant lines and regularized relative factors; no
infinite-dimensional ordinary Berezinian is being asserted.

## Kernel relation survives

The equations defining a coupled kernel are unchanged by assigning parity.
On an invertible open-loop chart, elimination still gives

\[
\ker\mathcal C(s)
\cong
\ker(I-K_{\rm rel}(s)).
\]

Parity changes determinant variance, not the Schur kernel state.

## Corrected G4 target

The completed comparison must be a morphism

\[
\mathcal L_{\partial,\mathrm{even}}
\otimes
\bigl(\mathcal L_{\mathrm{Euler}}^{(3)}\bigr)^*
\otimes
\mathcal L_{\mathrm{rel}}^{(2)}
\otimes
\mathcal L_\infty
\longrightarrow
\mathcal L_\Xi.
\]

The earlier ungraded cone determinant has the wrong Euler orientation and
cannot supply this morphism.

## Remaining obligation

One must construct the graded three-stratum boundary differential whose
determinant-line section has the finite Berezinian character above, then prove
that the theta Mellin--Poisson trivialization sends that section to \(\xi\)
without an additional divisor.  Only afterward does a Xi zero produce the
closed cone kernel already governed by maximal-isotropic Green flux.

No RH conclusion is authorized.
