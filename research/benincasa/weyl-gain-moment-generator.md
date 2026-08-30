# Full Weyl moment generator for the trace-balanced creation channel

Use \([Q,P]=2i\) and the creation jump

\[
L=a^\dagger=\frac{Q-iP}{2}.
\]

For Weyl-ordered polynomial symbols, the trace-balanced adjoint generator

\[
\mathcal L^\dagger(O)
=L^\dagger O L-\frac12\{L^\dagger L,O\}
\]

is represented exactly by

\[
\boxed{
\mathcal L^\dagger
=
\frac12(Q\partial_Q+P\partial_P)
+\frac12(\partial_Q^2+\partial_P^2).
}
\]

On a Weyl monomial,

\[
2\mathcal L^\dagger(Q^mP^n)
=(m+n)Q^mP^n
+m(m-1)Q^{m-2}P^n
+n(n-1)Q^mP^{n-2}.
\]

Thus the generator preserves total degree at leading order and adds only
degree-minus-two diffusion terms.  It maps the unit to zero, encoding trace
preservation.

Because Weyl symbols are the canonical quotient of the operator algebra by
the exact CCR ordering relations, this differential operator is intrinsically
defined on the CCR quotient; it does not depend on a chosen normal-ordering
representative.

The checker audits every monomial through total degree eight.  Momentum- and
time-dependent source amplitudes multiply and mix labelled Kraus channels but
do not change the local one-mode degree statement.
