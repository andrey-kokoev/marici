# Entry 497 — The Derived Endpoint Class Is a Single Invariant Conormal

Entry 496 shows that the generic Bockstein is divisible by the endpoint
equation

\[
c=1-b^2,
\qquad
\beta(a^3)=-{c\over8}[a^2e_a].
\]

Derived base change along \(c=0\) retains the quotient

\[
\delta_c\beta=-{1\over8}[a^2e_a]\otimes[c]
\]

in the conormal line \((c)/(c^2)\).  Since the endpoint divisor consists of
the two points \(b=\pm1\), its untwisted fiber has two components.  Deck
character determines the physical rank.

## Local residues and orientation

At the endpoint \(b=\epsilon\), use the local coordinate
\(t_\epsilon=b-\epsilon\).  Then

\[
{c\over t_\epsilon}\bigg|_{b=\epsilon}=-2\epsilon.
\]

Thus the two coordinate residues are

\[
\delta_{t_-}\beta=-{1\over4}[a^2e_a],
\qquad
\delta_{t_+}\beta=+{1\over4}[a^2e_a].
\]

Numerically they have opposite signs.  However the deck involution
\(b\mapsto-b\) also sends

\[
t_\epsilon\longmapsto-t_{-\epsilon},
\]

so it reverses the local conormal frame.  The sign of the coefficient and
the sign of the frame cancel.  Therefore

\[
\boxed{
\delta_c\beta\text{ is deck invariant and spans one global line.}
}
\]

## Consequence

The derived endpoint class has precisely the character and rank of the
cutoff-independent invariant defect in Entry 473.  It is not either ordinary
endpoint value; both ordinary values vanish by Entry 496.  It is the single
global conormal jet joining the two endpoint branches.

This closes the generic-to-boundary type chain:

\[
I/I^2
\xrightarrow{\text{derived }u\text{-specialization}}
[a^3e_u]
\xrightarrow{\text{derived }c\text{-specialization}}
\mathbb Q\langle\delta_c\beta\rangle_+.
\]

The agreement with Entry 473 is now structural, not merely numerical.  A
remaining comparison is needed to identify this derived endpoint line with
the explicit constant class in the complete filtered orbit cokernel.

## Next gate

Evaluate the complete orbit-cokernel projection of Entry 473 on the endpoint
jet representative \(-[a^2e_a]/8\).  Test whether it spans the unique plus
defect and whether its normalization agrees in both endpoint charts after
the conormal orientation is included.

The orientation and character audit is
`research/voevodsky/check_soft_axis_endpoint_conormal_orientation.py`.
