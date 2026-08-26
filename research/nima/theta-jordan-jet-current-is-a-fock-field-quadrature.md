# The Jordan jet current is a Fock field quadrature

## Status

Exact algebraic identification. After factorial normalization of the spectral
jet tower, the adjacent-level Jordan coefficients become the standard bosonic
ladder coefficients. The prolonged Green residual is the expectation of a
field quadrature on a one-mode Fock module.

The factorially weighted Green diagonal is the Fock identity, not the number
operator. Therefore the native prolonged form is an identity-plus-field form,
which is unbounded below for every nonzero field coefficient. A positive
oscillator square requires both an additional source-derived number energy and
the matching vacuum reservoir.

## Factorially normalized jets

Let

\[
g_m=\partial_z^mG,
\qquad
h_m=\frac{g_m}{\sqrt{m!}}.
\]

Collect the normalized jets into

\[
h=(h_0,h_1,h_2,\ldots).
\]

The natural factorially weighted adjacent-level Jordan sum is

\[
\mathcal J(h)
=
2\sum_{m\geq1}
\frac{m}{m!}
\operatorname{Im}\langle g_{m-1},g_m\rangle.
\]

Substitution gives

\[
\mathcal J(h)
=
2\sum_{m\geq1}
\sqrt m\,
\operatorname{Im}\langle h_{m-1},h_m\rangle.
\]

The coefficient \(m\) from the Green product rule has become the canonical
ladder coefficient \(\sqrt m\).

## Creation and annihilation operators

On the filtered jet module define

\[
ae_m=\sqrt m\,e_{m-1},
\qquad
a^*e_{m-1}=\sqrt m\,e_m.
\]

They satisfy the canonical commutation relation

\[
[a,a^*]=I
\]

on the finite-jet core.

Up to the inner-product sign convention, the Jordan sum is the quadratic form
of the self-adjoint field quadrature

\[
P=i(a^*-a).
\]

Thus

\[
\mathcal J(h)=\langle h,Ph\rangle
\]

with the orientation fixed by the Green identity.

The spectral jet filtration is therefore not merely analogous to a positive
Fock construction. Its product-rule residual carries the exact bosonic ladder
algebra.

## Native diagonal is the identity

With the same factorial weight, the diagonal jet energy is

\[
\sum_{m\geq0}\frac1{m!}\lVert g_m\rVert^2
=
\sum_{m\geq0}\lVert h_m\rVert^2
=
\langle h,Ih\rangle.
\]

It is not

\[
\langle h,Nh\rangle
=
\sum_{m\geq0}m\lVert h_m\rVert^2.
\]

Thus the native factorially prolonged Green form supplies \(I+\lambda P\), not
\(N+\lambda P\).

Because \(P\) is unbounded above and below, no finite scalar \(c\) makes

\[
cI+\lambda P
\]

positive for \(\lambda\neq0\). A vacuum constant alone cannot repair the
field quadrature.

## Number energy and square completion

Let

\[
N=a^*a.
\]

For a real coefficient \(\lambda\),

\[
N+\lambda P
=
(a+i\lambda I)^*(a+i\lambda I)
-\lambda^2I.
\]

Therefore

\[
N+\lambda P+\lambda^2I
\geq0
\]

on the finite-jet core.

This square remains a valid target identity, but \(N\) is additional structure.
It is not supplied by the native factorial Green diagonal. Both \(N\) and the
vacuum term \(\lambda^2I\) must be derived from source currents before this
completion can be used.

## Source interpretation

The required pieces have distinct types:

- \(N\) is the positive jet-number energy;
- \(P\) is the oriented adjacent-jet current;
- \(I\) is the vacuum reservoir channel.

The primitive forcing-norm reservoir is a natural candidate for the vacuum
term. A separate weighted source current must supply \(N\); the prime-square
channel is a candidate because it is the first Hilbert-level non-trace-class
current. Seam and archimedean channels may fix the displacement coefficient
\(\lambda\).

This is only a candidate matching. The exact Green prolongation must derive all
three coefficients before square completion. Choosing \(\lambda\) to make the
form positive would be fitted and invalid.

## Reciprocal-sector behavior

The field quadrature changes orientation under exchange of creation and
annihilation. Reciprocal Tate sewing must specify whether it:

1. sends \(a\) to \(a^*\), reversing \(P\);
2. conjugates the jet amplitudes while retaining \(P\);
3. or couples two independent Fock modules through a Bogoliubov transform.

Unitarity of the scalar gamma factor does not decide among these operator
actions. The exact source sewing map is required.

If the two sectors reverse \(P\), the Jordan currents can cancel. If they
retain it, the currents add and a source-derived number energy plus vacuum
completion becomes mandatory.

## Link to macroscopic band coherence

The growing-band asymptotic extracts the terminal separation current

\[
Q_a(R)=J_a'(R)-aR W_a(R).
\]

This is another boundary quadrature produced by retaining macroscopic source
scale while microscopic bands proliferate.

A sharp cross-filtration test is whether \(Q_a(R)\) is the coherent-state
symbol of the jet-Fock field operator \(P\) after the band-to-jet bonding map.
The exact endpoint-sign census proves \(Q_a(R)<0\) for every \(a,R>0\), so no
finite macroscopic coherence length exists in the consecutive-band model. If
the symbol identification holds, those coherent states sample only the
negative field-quadrature sector.

The identification must be proved from the common source kernel. Similar
formulas alone are insufficient.

## Two-dimensional filtration

Let \(m\) index jet order and \(M\) index phase-band resolution. The source
packet should provide bonding maps

\[
V_{(m,M),(m',M')}
\]

for \(m\leq m'\) and \(M\leq M'\), together with compatibility of:

- the ladder operators in \(m\);
- the terminal separation current in \(M\);
- reciprocal sewing;
- primitive and square reservoirs;
- the ordered endpoint/source flag.

The relevant completion is a filtered graph topology controlling \(N\), \(P\),
and the band generator. Ordinary unweighted sequence norm is not sufficient.

## Finite falsifiers

The Fock identification fails if factorial normalization does not convert the
Jordan coefficient to \(\sqrt m\), or if a non-adjacent jet coupling survives
the exact product rule.

The positive-square route fails if the source-derived coefficients do not
match

\[
N+\lambda P+\lambda^2I.
\]

The cross-filtration interpretation fails if the coherent-state symbol of
\(P\) differs from \(Q_a(R)\) at the first finite source order where both are
defined.

## Decisive conclusion

The adjacent-jet Jordan residual has a canonical operator identity: it is a
bosonic field quadrature on the factorially normalized spectral-jet Fock
module. This supplies the first principled algebra for organizing the infinite
jet tower.

The RH-bearing question is now stronger than coefficient matching. Does
Fourier--Tate sewing and the boundary-current hierarchy supply the missing
number energy as well as the exact vacuum reservoir required by the oscillator
square? If not, the Fock organization explains the grammar of the residual but
also proves that the native identity-plus-field completion is unbounded below.
