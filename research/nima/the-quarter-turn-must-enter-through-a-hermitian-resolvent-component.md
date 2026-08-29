# The quarter-turn must enter through a Hermitian resolvent component

## Correction to the schematic return

The real complex structure

\[
J_{KV}=
\begin{pmatrix}
0&-I\\
I&0
\end{pmatrix},
\qquad
J_{KV}^{2}=-I,
\qquad
J_{KV}^{*}=-J_{KV}
\]

does select the reciprocal orientation. But for real endpoint incidence \(C_p\) and a real self-adjoint propagator \(R_p\), the raw return

\[
C_pR_pJ_{KV}C_p^{*}
\]

is real skew-adjoint, hence anti-Hermitian. It cannot itself be added to a Hermitian endpoint Gram. The Hermitian odd return requires the factor \(i\):

\[
i\,C_pR_pJ_{KV}C_p^{*}.
\]

Equivalently, the quarter-turn must occur as the imaginary Hermitian component of the auxiliary inverse used by the Schur complement.

## Correct auxiliary typing

Write the reduced tail/PV block as

\[
D_p=S_p+iT_p,
\]

where

\[
S_p^{*}=S_p,
\qquad
T_p^{*}=-T_p
\]

in the underlying real presentation. Then \(D_p\) is complex Hermitian. The source-oriented case has an odd component

\[
T_p=\tau_pJ_{KV}
\]

or its source-derived non-scalar analogue.

If

\[
D_p^{-1}=R_{p,\mathrm{ev}}+iR_{p,\mathrm{odd}},
\]

then Hermiticity forces

\[
R_{p,\mathrm{ev}}^{*}=R_{p,\mathrm{ev}},
\qquad
R_{p,\mathrm{odd}}^{*}=-R_{p,\mathrm{odd}}.
\]

For real \(C_p\), the Schur return decomposes as

\[
C_pD_p^{-1}C_p^{*}
=
C_pR_{p,\mathrm{ev}}C_p^{*}
+
iC_pR_{p,\mathrm{odd}}C_p^{*}.
\]

The first term changes real endpoint energy. The second is precisely the imaginary Hermitian orientation term. Thus the phase is source-authorized only if the Fourier convention places \(J_{KV}\) inside the auxiliary Hermitian block or its resolvent—not by appending an \(i\) to the endpoint plane after compression.

## Scalar commuting model

When \(S_p=s_pI\) and \(T_p=\tau_pJ_{KV}\),

\[
D_p=s_pI+i\tau_pJ_{KV}.
\]

Because \((iJ_{KV})^2=I\),

\[
D_p^{-1}
=
\frac{s_pI-i\tau_pJ_{KV}}{s_p^2-\tau_p^2},
\]

provided \(s_p^2\ne\tau_p^2\). Positivity requires

\[
s_p>|\tau_p|.
\]

The odd Schur return is then

\[
-\frac{i\tau_p}{s_p^2-\tau_p^2}
C_pJ_{KV}C_p^{*}.
\]

Changing the Fourier orientation \(J_{KV}\mapsto-J_{KV}\) reverses this term while preserving the even resolver and determinant magnitude.

This model also exposes a coercivity cost: the odd magnitude grows as the auxiliary block approaches the radical threshold \(s_p=|\tau_p|\). Hence matching the Euler odd coordinate must be accompanied by a uniform reduced-support gap.

## Domain and radical theorem

The finite formula extends to the analytic carrier only after proving:

1. \(K\) and \(V\) share a common invariant core.
2. \(J_{KV}\) is a unitary skew-adjoint complex structure on its closure.
3. \(S_p+iT_p\) is a closed Hermitian form or operator.
4. \(\operatorname{ran}C_p^{*}\) lies in the form domain of its reduced inverse.
5. \(\ker D_p\subseteq\ker C_p\).
6. The odd resolvent component preserves the prime spectral fiber.
7. The reduced spectral gap is uniform on compact off-seam regions.

The scoped matching law is

\[
-\operatorname{Im}
\left(C_pD_p^\dagger C_p^{*}\right)_{12}
=
h_p,
\]

where \(h_p\) is either the strict grade-\(1,2\) current or the all-grade current with an explicitly present connected-tail reservoir.

## New minimal hostile

Use the correct \(J_{KV}\) but place \(C_pR_pJ_{KV}C_p^{*}\) directly into a Hermitian Gram without the \(i\)-typing supplied by the auxiliary complexification. The sign and scalar magnitude may look correct, yet the full block is not Hermitian.

A second hostile drives the auxiliary gap to zero while scaling \(C_p\) so the compressed odd coordinate remains finite. The effective endpoint shadow converges, but the eliminated carrier and its inverse lose completion control.

## Resulting constructor chain

Real endpoint incidence leads to the Hermitian tail/PV block \(S+iT\); source orientation makes \(T\) proportional to \(J_{KV}\); the reduced Hermitian resolvent is then Schur-compressed to the imaginary Hermitian endpoint orientation.

The next source calculation is therefore not merely to exhibit \(J_{KV}\). It is to derive the Hermitian auxiliary block in which that quarter-turn occurs and prove a uniform reduced spectral gap.
