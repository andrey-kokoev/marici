# The symmetric-Fock trace is the source multiplicative Euler state before scalar readout

> **Completion correction.** The successor packet
> `no-equivalent-hilbert-fock-topology-extends-the-euler-trace-to-the-critical-strip.md`
> proves that this exact finite/Euler-domain construction cannot become an
> ordinary critical-strip Hilbert-Fock trace in any equivalent topology. Its
> role is finite multiplicative provenance, not the completed kernel carrier.

## Finite prime carrier

Fix a finite prime set \(X\) and let

\[
E_X=\operatorname{span}\{e_p:p\in X\}.
\]

On the Euler domain define

\[
L_X(s)e_p=p^{-s}e_p.
\]

The bosonic symmetric-Fock carrier is

\[
\mathcal F_X=\operatorname{Sym}^{\bullet}E_X
=
\bigoplus_{n\ge0}\operatorname{Sym}^nE_X.
\]

Second quantization gives

\[
\Gamma_X(L_X)ig|_{\operatorname{Sym}^nE_X}
=
\operatorname{Sym}^nL_X.
\]

For \(\operatorname{Re}s>0\), every eigenvalue of \(L_X(s)\) has modulus less
than one, so \(\Gamma_X(L_X(s))\) is trace class on the finite-prime Fock
carrier.

## Exact multiplicative readout

The symmetric-algebra trace identity gives

\[
\operatorname{Tr}_{\mathcal F_X}\Gamma_X(L_X(s))
=
\det(I-L_X(s))^{-1}
=
\prod_{p\in X}(1-p^{-s})^{-1}.
\]

This constructs the finite Euler product as an ordered state--observer pairing:

\[
u_{\Delta,X}(s)=\Gamma_X(L_X(s)),
\qquad
y_{\Delta,X}=\operatorname{Tr}_{\mathcal F_X},
\]

\[
y_{\Delta,X}u_{\Delta,X}(s)=\zeta_X(s).
\]

Neither map is defined from the already aggregated scalar \(\zeta_X\).

## Prime-power grades

Taking the logarithm of the Fock trace recovers

\[
\log\operatorname{Tr}_{\mathcal F_X}\Gamma_X(L_X)
=
\sum_{k\ge1}\frac1k\operatorname{Tr}L_X^k
=
\sum_{p\in X}\sum_{k\ge1}\frac1k p^{-ks}.
\]

Thus primitive, square, and connected prime-power grades are cyclic returns of
one source operator.  The symmetric-Fock construction totalizes them
multiplicatively without first adding their endpoint currents as a scalar.

## Multiplicative border

Define the finite bordered operator on the trace-class state space
\(\mathcal T_1(\mathcal F_X)\oplus\mathbb C\):

\[
D_{\Delta,X}(s)
=
\begin{pmatrix}
I&u_{\Delta,X}(s)\\
y_{\Delta,X}&0
\end{pmatrix}.
\]

Its Schur determinant is

\[
\det D_{\Delta,X}(s)=-\zeta_X(s),
\]

and a zero, if one existed in a continued typed completion, would have the
forward-derived kernel state

\[
\binom{-u_{\Delta,X}(s)}{1}.
\]

At finite cutoff and \(\operatorname{Re}s>0\), the Euler product is nonzero;
the border is therefore invertible.  The construction supplies provenance,
not a finite zero mechanism.

## Archimedean completion

The Gaussian Mellin, reciprocal endpoint, and completion-polynomial factors
form a separate one-dimensional source line \(\mathcal L_{\infty,X}\).  Tensoring
that line with the Fock state gives the finite completed state

\[
\widetilde u_{\Delta,X}(s)
=u_{\Delta,X}(s)\otimes b_\infty(s),
\]

whose source observer has readout

\[
B_\infty(s)\zeta_X(s).
\]

The archimedean factor is retained as a line vector rather than inserted as a
fitted scalar block.

## Relation to det3

The Fock trace and determinant-three compiler are two presentations of the
same finite Euler character:

\[
\operatorname{Tr}_{\mathcal F_X}\Gamma_X(L_X)
=
\exp\left(
\operatorname{Tr}L_X+
\frac12\operatorname{Tr}L_X^2
\right)
\det_3(I-L_X)^{-1}.
\]

This equality supplies the finite comparison cell between the multiplicative
Fock presentation and the three-stratum determinant-line presentation.

## Completion boundary

The infinite-prime Fock trace exists as an ordinary trace only where
\(L(s)\in\mathcal S_1\), namely \(\operatorname{Re}s>1\).  It cannot be
continued to the critical strip merely by continuing its scalar trace.

The admissible completion target is a rigged or relative Fock determinant
line whose three strata are completed by the already constructed
primitive-distributional, square-Hilbert, connected-\(\mathcal S_3\), seam,
and Fourier--Poisson data.  The theta Mellin--Poisson functional supplies its
scalar trivialization, but a completed Fock state and trace observer have not
yet been constructed.

## G4 consequence

The previously missing finite multiplicative state--observer factorization is
now explicit and noncircular.  It also fixes the inverse Euler variance:
symmetric powers produce \(\det(I-L)^{-1}\) directly.

The remaining operator theorem is completion of this Fock state through the
three-stratum boundary category and comparison of its completed kernel with
the maximal-isotropic closed-loop cone.  No RH conclusion is authorized.
