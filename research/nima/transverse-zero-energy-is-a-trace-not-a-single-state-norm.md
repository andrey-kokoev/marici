# Transverse zero energy is a trace, not a single-state norm

Event 10284 proposed schematically factoring the Poincaré–Lelong energy as a
positive quadratic form. There is a granularity constraint.

The energy is additive over zero atoms:

\[
E_{\eta,\chi}
=
\sum_\rho
m_\rho
\left(\Re\rho-\frac12\right)^2
\chi(\Re\rho)e^{-\eta(\Im\rho)^2}.
\]

If one forms a single summed state

\[
\Psi=\sum_\rho\psi_\rho,
\]

then

\[
\|N_\perp\Psi\|^2
=
\sum_\rho\|N_\perp\psi_\rho\|^2
+
\sum_{\rho\ne\rho'}
\langle N_\perp\psi_\rho,N_\perp\psi_{\rho'}\rangle.
\]

Poincaré–Lelong contains no cross terms between distinct divisor atoms.
Therefore it cannot equal a single-state norm unless orthogonality of the
zero packets is independently proved.

## Correct operator forms

On a divisor label space with orthonormal basis \(e_\rho\), define

\[
N_\perp e_\rho
=
\left(\Re\rho-\frac12\right)e_\rho
\]

and

\[
W_{\eta,\chi}e_\rho
=
\chi(\Re\rho)e^{-\eta(\Im\rho)^2}e_\rho.
\]

Then the correct additive representation is

\[
E_{\eta,\chi}
=
\operatorname{Tr}
\left(
W_{\eta,\chi}N_\perp^*N_\perp
\right).
\]

Equivalently,

\[
E_{\eta,\chi}
=
\left\|
N_\perp W_{\eta,\chi}^{1/2}
\right\|_{\mathrm{HS}}^2.
\]

This is a Hilbert–Schmidt norm of an incidence operator, not the norm of a
summed zero vector.

Multiplicity is handled by repeated orthogonal label copies or by a
multiplicity fiber. It must not be encoded by scaling one vector by
\(m_\rho\), which would produce \(m_\rho^2\).

## Constructor obligation

The trace formula requires exactly the label-survival theorem encountered
earlier:

1. distinct zero/divisor atoms remain orthogonal labels;
2. the normal displacement operator is diagonal on those labels;
3. the heat weight is functional calculus in the height label;
4. the weighted normal incidence is Hilbert–Schmidt;
5. the analytic representation preserves the trace.

Without this, positivity of the field integral cannot be explained by a
single abstract Green norm.

The same warning applies on the prime side. Prime diagonality was needed to
turn local mixed energies into an additive global series. Divisor
diagonality is its analytic counterpart.

## Interaction-net interpretation

The Poincaré–Lelong current is a direct sum of local zero cells. The correct
network is

\[
\bigoplus_\rho
\text{zero incidence}_\rho
\to
\text{weighted normal displacement}
\to
\text{trace port}.
\]

Merging the zero cells before applying the quadratic energy introduces
unauthorized interference terms.

Thus the next factorization target is not

\[
E=\|N_\perp\Psi\|^2,
\]

but

\[
E=\|N_\perp W^{1/2}\|_{\mathrm{HS}}^2
\]

together with a source-derived divisor-label decomposition. This sharply
identifies the representation granularity required for a noncircular
positive Green realization.
