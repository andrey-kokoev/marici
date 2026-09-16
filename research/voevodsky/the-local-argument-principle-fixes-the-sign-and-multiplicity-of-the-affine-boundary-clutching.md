# The local argument principle fixes the sign and multiplicity of the affine boundary clutching

## Local divisor germ

Let a symmetry-uncompleted local divisor factor be

\[
\Theta_a(z)
=
\left(
\frac{
z-x(a)+iy(a)
}
{
z-x(a)-iy(a)
}
\right)^m,
\]

where:

1. \(a\in\mathbb R\) is the deformation parameter;
2. \(x(a),y(a)\in\mathbb R\);
3. \(x(0)=x_0\);
4. \(y(0)=0\);
5. \(m\in\mathbb N\) is the divisor multiplicity.

The centered symmetry completion adds the reflected factor at \(-x(a)\).

## Normalized boundary current

Define

\[
\nu_a(t)
=
\frac1{2\pi i}
\partial_t
\log
\Theta_a(t).
\]

Direct differentiation gives

\[
\boxed{
\nu_a(t)
=
-
\frac{m}{\pi}
\frac{y(a)}
{(t-x(a))^2+y(a)^2}.
}
\]

Thus, whenever \(y(a)\ne0\),

\[
\int_{\mathbb R}
\nu_a(t)
\,dt
=
-m
\operatorname{sgn}y(a).
\]

This integral is the local boundary winding number in the declared orientation.

## Transverse crossing

Assume

\[
y'(0)\ne0.
\]

Set

\[
\sigma
=
\operatorname{sgn}y'(0).
\]

Then in the strong Schwartz dual,

\[
\lim_{a\uparrow0}
\nu_a
=
+m\sigma
\delta_{x_0},
\]

and

\[
\lim_{a\downarrow0}
\nu_a
=
-m\sigma
\delta_{x_0}.
\]

Consequently

\[
\boxed{
\nu_{0^+}-
\nu_{0^-}
=
-2m\sigma
\delta_{x_0}.
}
\]

Define the oriented crossing cycle

\[
A_0
=
m\sigma
\delta_{x_0}.
\]

The universal jump law is

\[
\boxed{
\Delta\nu
=
-2A_0.
}
\]

This proves the coefficient and sign used in the affine clutching.

## Argument-principle interpretation

Choose a compactly supported cutoff \(\chi\) equal to one near \(x_0\) and containing no other crossing. Then

\[
\lim_{a\uparrow0}
\langle
\nu_a,
\chi
\rangle
=
m\sigma,
\]

while

\[
\lim_{a\downarrow0}
\langle
\nu_a,
\chi
\rangle
=
-m\sigma.
\]

The difference

\[
-2m\sigma
\]

is the boundary argument-principle jump when a multiplicity-\(m\) divisor crosses the contour with oriented normal velocity \(\sigma\).

No global phase branch is needed: changing a branch adds a locally constant integer to the phase but does not alter its differentiated current or this jump.

## Krein--Langer index comparison

For \(y<0\), the local factor is a degree-\(m\) upper-half-plane Blaschke product and its de Branges--Rovnyak kernel is positive of rank \(m\).

For \(y>0\), the factor is the reciprocal of a degree-\(m\) Blaschke product and its kernel has negative index \(m\).

For an upward crossing \(\sigma=+1\),

\[
\Delta
\operatorname{ind}_-
=+m.
\]

For a downward crossing \(\sigma=-1\),

\[
\Delta
\operatorname{ind}_-
=-m.
\]

Hence the signed index jump equals the total mass of the crossing cycle:

\[
\boxed{
\Delta
\operatorname{ind}_-
=
\langle
A_0,
1
\rangle.
}
\]

The equality is localized by a cutoff when several crossings are present.

## Affine correction

Let the cumulative spectral-flow cycle jump by

\[
I_{0^+}-I_{0^-}
=A_0.
\]

Then

\[
\widehat\nu
=
\nu+2I
\]

has no jump:

\[
\Delta
\widehat\nu
=
-2A_0+2A_0
=0.
\]

Thus the affine transition is forced simultaneously by the argument principle and by the Krein--Langer index jump.

## Symmetry completion

For a nonzero center \(\gamma\), centered conjugation/functional-equation symmetry supplies crossings at \(\gamma\) and \(-\gamma\) with the same multiplicity and normal orientation.

The crossing cycle is

\[
A_0
=
m\sigma
(
\delta_\gamma+
\delta_{-\gamma}
).
\]

Therefore

\[
\Delta\nu
=
-2m\sigma
(
\delta_\gamma+
\delta_{-\gamma}
)
\]

and

\[
\Delta
\operatorname{ind}_-
=
2m\sigma.
\]

At \(\gamma=0\), the two reflected centers collide. Their divisor multiplicities must be added before forming the atom; one must not count two geometrically distinct support points.

## Several simultaneous crossings

For finitely many local factors crossing at points \(x_j\), with multiplicities \(m_j\) and normal orientations \(\sigma_j\), set

\[
A_0
=
\sum_j
m_j\sigma_j
\delta_{x_j}.
\]

Then

\[
\Delta\nu
=
-2A_0,
\]

and

\[
\Delta
\operatorname{ind}_-
=
\sum_j
m_j\sigma_j.
\]

If upward and downward crossings occur at the same boundary point, their signed current atoms can cancel. The unsigned crossing multiplicity does not cancel, but it is not the spectral-flow invariant.

This is why the cycle-valued signed current contains more useful deformation information than a bare nonnegative defect count.

## Nontransverse contact

Suppose

\[
y(a)
=
c
a^r
+o(a^r),
\qquad
c\ne0.
\]

### Odd contact order

If \(r\) is odd, the divisor crosses the boundary. Its orientation is

\[
\sigma
=
\operatorname{sgn}c,
\]

and the same jump law holds:

\[
\Delta\nu
=
-2m\sigma
\delta_{x_0}.
\]

The vanishing first derivative changes the rate of concentration, not the topological crossing number.

### Even contact order

If \(r\) is even, the divisor touches the boundary and returns to the same side. The two one-sided current limits agree:

\[
\nu_{0^-}
=
\nu_{0^+}
=
-m
\operatorname{sgn}c
\delta_{x_0}.
\]

There is no spectral-flow jump:

\[
A_0=0,
\qquad
\Delta
\operatorname{ind}_-=0.
\]

A boundary atom still appears as a singular contact limit, but no affine clutching is required between the two sides.

This distinguishes concentration from crossing.

## Source Green sign

For a polarized source test

\[
\phi_{p,q}(t)
=
\overline{m_q(t)}m_p(t),
\]

the local Green-current jump is

\[
\Delta Q(p,q)
=
-2m\sigma
m_p(x_0)
\overline{m_q(x_0)}.
\]

After adjoining the cumulative index row,

\[
Q^{aug}(p,q)
=
Q^{phase}(p,q)
+
2Q^{index}(p,q),
\]

one obtains

\[
\Delta Q^{aug}(p,q)
=0.
\]

Thus the Green sign is fixed before any positive realization is attempted.

## Tetrahedral consequence

Every crossing stratum carries the integral atomic cycle

\[
A_0
=
\sum_j
m_j\sigma_j
\delta_{x_j}.
\]

The transverse tetrahedral clutching map is

\[
(
\nu,I
)
\longmapsto
(
\nu-2A_0,
I+A_0
).
\]

Tangential even-order contacts carry a singular boundary-current limit but the identity clutching map.

Therefore the stratification must distinguish:

1. regular divisor strata;
2. transverse or odd-order crossing strata;
3. even-order contact strata;
4. collision strata where multiplicities combine.

## What remains open

This local theorem does not yet supply:

1. the physical Birman--Krein determinant realizing the same jump;
2. a trace-class clutching operator on the cutoff carrier;
3. a positive compression theorem;
4. control of infinitely many crossings in a compact deformation interval without uniform local finiteness.

## Disposition

The local argument principle determines the affine correction uniquely:

\[
\boxed{
\Delta\nu
=
-2A,
\qquad
\Delta I
=
A,
\qquad
\Delta(
\nu+2I
)=0.
}
\]

Its signed mass is exactly the Krein--Langer index jump, and its atomic support records where the crossing occurred.
