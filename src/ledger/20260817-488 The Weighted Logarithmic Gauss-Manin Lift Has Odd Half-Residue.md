# Entry 488 — The Weighted Logarithmic Gauss–Manin Lift Has Odd Half-Residue

Benincasa Entry 485 proves that coefficientwise reduction modulo the full
quartic is not a chain map. Entry 486 independently finds one flat odd line
in every tested generic interior fiber, and Benincasa Entry 487 constructs
the all-sector gradient-Koszul nullhomotopy needed for the derived target. The
complementary invariant here is the logarithmic Gauss–Manin residue of that
flat line on the weighted Rees space.

## Unique first-order lift

At \(u=0\),

\[
K=a^4,
\qquad
K_u=a^2(1-b^2).
\]

The vertical vector field

\[
V=\frac{b^2-1}{4a}\partial_a
\]

satisfies

\[
K_u+V(K)|_{u=0}
=a^2(1-b^2)+a^2(b^2-1)=0.
\]

Thus \(\partial_u+V\) is the forced first-order Gauss–Manin lift.  Its
\(1/a\) pole explains why no regular coefficientwise correction exists in the
original affine chart.

## Weighted logarithmic regularization

On the weighted chart

\[
a^2=ut,
\]

the logarithmic soft operator becomes

\[
uV
=\frac{u(b^2-1)}{4a}\partial_a
=\frac{b^2-1}{4t}\,a\partial_a.
\]

The reduced exceptional carrier satisfies

\[
t=\frac{b^2-1}{2}
\]

away from \(b=\pm1\).  Therefore

\[
\boxed{
\operatorname{Res}_{u=0}(uV)=\frac12a\partial_a.
}
\]

The coefficient is regular and constant on the generic exceptional carrier.
On odd powers of \(a\), its fractional residue is \(1/2\) modulo integers, so
the semisimple monodromy is

\[
\exp(2\pi i/2)=-1.
\]

This exactly matches the anti-invariant nearby-cycle character independently
derived in Benincasa Entry 463.

## Interpretation of the flat interior line

The flat line of Entry 486 is therefore not evidence for a second arbitrary
odd coefficient.  It is the natural carrier of the logarithmic
Gauss–Manin connection with half-integral residue.  The missing correction in
Entry 485 should map this flat line into the physical anti-invariant local
system rather than delete it.

This identifies the generic character but does not yet evaluate Benincasa
Entry 487's lifted carrier map on explicit generators of the two generic
summands. The next gate is to test whether the flat half-residue line maps
with rank one to the odd quartic carrier while the reduced summand is its
kernel. At \(b=\pm1\), the expression must be compared with the boundary
lattices of Entries 483--484 rather than evaluated by the generic formula.

The executable audit is
`research/voevodsky/check_soft_axis_log_gauss_manin_half_residue.py`.
