# The physical x derivative closes only on the augmented H--Phi jet system

Let

\[
H(t)=e^{x/2}e^{X(t-1)},\qquad
A=4\partial_t^2-6\partial_t,\qquad
\Phi(t)=AH(t).
\]

The labelled generating section obeys

\[
\partial_xH=LH,
\qquad
L=\frac12+2(t-1)\partial_t.
\]

The physical source is `Phi(0)`.  Since `A` does not commute with `L`, its
transport is not a closed equation on `Phi` alone.  The exact commutator is

\[
[A,L]=16\partial_t^2-12\partial_t,
\]

so

\[
\partial_x\Phi
=L\Phi+(16\partial_t^2-12\partial_t)H.
\]

At the coefficient level,

\[
\partial_x(4h_2-6h_1)=30h_2-15h_1-8h_3.
\]

Thus differentiating the physical forcing along the shell/history coordinate
requires the augmented pair `(H,Phi)`, not only the `Phi` jet tower.

After summing labels, the Poisson zero-mode components are

\[
H_{\rm bd}(t)=\frac12(1-t)^{-1/2}e^{-x/2},
\qquad
\Phi_{\rm bd}(t)=AH_{\rm bd}(t)
=\frac32t(1-t)^{-5/2}e^{-x/2}.
\]

Although `Phi_bd(0)=0`, the term `L Phi_bd|_(t=0)` samples
`partial_t Phi_bd(0)` and equals

\[
L\Phi_{\rm bd}|_{t=0}=-3e^{-x/2}.
\]

The commutator contribution is exactly

\[
(16\partial_t^2-12\partial_t)H_{\rm bd}|_{t=0}
=+3e^{-x/2}.
\]

The two non-L2 terms cancel coefficientwise. Their sum is the actual derivative
`partial_x Phi(0)`, which is again rapidly decreasing. Therefore no endpoint
coordinate is added to the base physical state, but endpoint cancellation is
mandatory inside any differentiated Schur calculation.

The required completed carrier is consequently an augmented boundary-plus-bulk
jet graph retaining both `H` and `Phi=AH` until after applying the connection;
setting `t=0` or discarding the modular endpoint line before this cancellation
is not domain-safe.

This establishes the algebraic closure and location of the cancellation. A
full graph theorem still requires explicit Poisson bounds for the `H` boundary
term and continuity of the Schur incidence on the augmented pair.
