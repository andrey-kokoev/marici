# Prior research corrects the relative-Haar domain route

Date: 2026-09-08

## Local domain theorem

For a regular function near the singular multiplicative endpoint,

\[
\int_0^1|f(x)|^2\frac{dx}{x}<\infty
\]

holds when `f(0)=0`; a continuous nonzero endpoint value causes logarithmic divergence.  Scalar finite-part subtraction has the exact anomaly

\[
\mathcal E_{\rm fp}(U_a(p)f)
=p\mathcal E_{\rm fp}(f)-p|f(0)|^2\log p
\]

and becomes negative under sufficiently many dilations.  It cannot serve as a positive covariant replacement.

## Coordinate correction

The theta tail coordinate is `q≥0`.  Under `x=e^{-q}` or `x=e^q`, the sewing point `q=0` maps to `x=1`, not the singular endpoint `x=0`.  Therefore the Xi zero condition at the seam does not establish the relative-Haar Dirichlet condition.

Relative Haar energy is simply the already known positive tail norm

\[
\int_0^\infty|G(q)|^2\,dq.
\]

It explains the critical modular coefficient but does not remove the forcing polarization.

## Actual domain defect

The augmented tail system contains a constant source coordinate:

\[
\mathcal D_z
\binom{G}{c}
=
\begin{pmatrix}
\partial_q+z&f(q)\\
0&\partial_q
\end{pmatrix}
\binom{G}{c},
\qquad c=1.
\]

The response `G` can have finite relative-Haar energy, but the constant channel is non-normalizable.  The unresolved term is exactly its interaction work with `G`, not a defect in positivity of the tail norm.

The required object is therefore a conservative reservoir or boundary-control dilation in which the constant drive acquires a finite-energy partner and

\[
2\operatorname{Re}z\,
\widetilde{\mathcal E}(G,r)
=-\partial_q\widetilde J(G,r).
\]

Eliminating the reservoir must recover the original forced equation, and the scalar zero must select a nonzero two-ended state without reconstructing the reservoir from Xi.

## Disposition

The relative-Haar route does not close the shell crossing or zero-to-flux bridge.  Its source contribution is narrower: it identifies the positive tail bulk and types the obstruction as work by a non-normalizable constant channel.  The missing conservative reservoir is the same physical datum sought by the bordered radial response construction.

## Evidence

- `research/nima/theta-relative-haar-domain-has-a-dirichlet-or-anomaly-dichotomy.md`
- `research/nima/theta-relative-haar-coordinate-audit-identifies-the-constant-channel-defect.md`
- `research/nima/theta-relative-haar-operator-has-the-exact-critical-energy-cocycle.md`
