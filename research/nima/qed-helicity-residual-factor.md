# The residual is a four-coordinate boundary jet, then identity

Owner: marici.Nima

Assemble the Bose-reduced helicity vector

\[
\mathbf\Phi=(\Phi_1,\Phi_2,\Phi_5)^T.
\]

Before boundary completion, the exact-minus-dispersive residual is

\[
\mathbf P(\nu,T)=
\begin{pmatrix}
a(T)+b(T)\nu\\
c_2(T)\\
c_5(T)
\end{pmatrix}.
\]

This is the complete crossing-authorized first-jet packet:

\[
a=\Phi_1(0,T),\qquad
b=\partial_\nu\Phi_1(0,T),\qquad
c_2=\Phi_2(0,T),\qquad
c_5=\Phi_5(0,T).
\]

It is four-dimensional at fixed transfer. Crossing and Bose symmetry prohibit
all other degree-at-most-one directions.

After adding this packet, define the multiplicative residual factor on the
three independent channels by

\[
R_i(\nu,T)=
\frac{\Phi_i^{\rm exact}}
{\Phi_i^{\rm dispersive}+P_i}.
\]

Across the certified real and complex hostile points,

\[
\max|R_1-1|=1.69\times10^{-6},
\]

\[
\max|R_2-1|=1.34\times10^{-7},
\]

\[
\max|R_5-1|=2.36\times10^{-5}.
\]

Thus the residual matrix is numerically the identity within the independently
measured integration error.

## Classification

- The surviving subtraction freedom is finite additive boundary data.
- Its helicity type and jet degree are fixed by crossing.
- Its leading transfer grades are fixed by gauge softness.
- No additional polynomial direction is detected.
- No nontrivial inner/CDD factor is detected on the tested analytic domain.

This is stronger than saying that a fitted phase happens to work. The
inclusive Cut loses a source boundary jet; once that typed jet is restored,
the exact source amplitude contains no further observed freedom.

The bounded census alone cannot exclude an inner factor outside the sampled
domain.  That global gate is now closed by the source growth and singularity
audit in `qed-oriented-cut-uniqueness.md`.
