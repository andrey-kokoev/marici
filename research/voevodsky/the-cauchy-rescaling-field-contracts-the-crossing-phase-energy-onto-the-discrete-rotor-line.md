# The Cauchy rescaling field contracts the crossing phase energy onto the discrete rotor line

## Objective

Package the varying phase-energy spaces

\[
L^2(
\mathbb R,
\kappa_{a,\gamma}(t)dt
)
\]

into one explicit Hilbert field and identify the discrete rotor line as the strong source-reached limit.

## Crossing probability measure

For \(a\ne0\), define

\[
d\mu_{a,\gamma}(t)
=
\kappa_{a,\gamma}(t)dt
=
\frac1\pi
\frac{|a|}{(t-\gamma)^2+a^2}
\,dt.
\]

This is a probability measure.

Let

\[
d\mu_C(x)
=
\frac1\pi
\frac{dx}{1+x^2}
\]

be the standard Cauchy probability measure.

## Exact rescaling trivialization

Set

\[
t
=
\gamma+|a|x.
\]

Then

\[
d\mu_{a,\gamma}(t)
=
d\mu_C(x).
\]

Therefore

\[
U_{a,\gamma}:
L^2(
\mu_{a,\gamma}
)
\longrightarrow
L^2(
\mu_C
),
\]

\[
(
U_{a,\gamma}f
)(x)
=
f(
\gamma+|a|x
)
\]

is unitary.

Thus all nonzero crossing fibers are canonically trivialized by dilation around the crossing point.

## Source sections

For a continuous bounded source boundary value \(m\), define the rescaled section

\[
s_a(m)(x)
=
m(
\gamma+|a|x
).
\]

Pointwise,

\[
s_a(m)(x)
\longrightarrow
m(
\gamma
)
\]

for every fixed \(x\).

For Mellin--Schwartz \(m\), dominated convergence gives

\[
\boxed{
s_a(m)
\longrightarrow
m(
\gamma
)
\mathbf 1
}
\]

strongly in \(L^2(\mu_C)\).

Equivalently,

\[
\int
|m(t)-m(\gamma)|^2
\,d\mu_{a,\gamma}(t)
\longrightarrow
0.
\]

The source-reached part of the phase-energy fiber therefore collapses onto the constant line

\[
\mathbb C\mathbf 1
\subset
L^2(
\mu_C
).
\]

## Rotor extraction

Define the constant-line inclusion

\[
J:
\mathbb C
\longrightarrow
L^2(
\mu_C
),
\qquad
Jc
=
c\mathbf 1.
\]

Since \(\mu_C\) is a probability measure, \(J\) is an isometry.

Its adjoint is Cauchy averaging:

\[
J^*F
=
\int
F(x)
\,d\mu_C(x).
\]

Transported back to the \(a\)-fiber,

\[
J_{a,\gamma}c
=
c
\]

as a constant function in \(L^2(\mu_{a,\gamma})\), and

\[
J_{a,\gamma}^*f
=
\int
f(t)
\,d\mu_{a,\gamma}(t).
\]

The rank-one projection

\[
R_{a,\gamma}
=
J_{a,\gamma}
J_{a,\gamma}^*
\]

is the canonical rotor-line projection inside the full phase-energy fiber.

For source sections,

\[
\|(
I-R_{a,\gamma}
)m\|_{L^2(\mu_{a,\gamma})}
\longrightarrow
0,
\]

and

\[
J_{a,\gamma}^*m
\longrightarrow
m(\gamma).
\]

Thus rotor extraction is asymptotically lossless on the admitted source core.

## Positive form decomposition

The crossing energy splits orthogonally as

\[
\int
|m(t)|^2
\,d\mu_{a,\gamma}(t)
=
\left|
\int
m(t)
\,d\mu_{a,\gamma}(t)
\right|^2
+
\int
|m(t)-
\mathbb E_{a,\gamma}m|^2
\,d\mu_{a,\gamma}(t),
\]

where

\[
\mathbb E_{a,\gamma}m
=
\int
m(t)
\,d\mu_{a,\gamma}(t).
\]

For Mellin--Schwartz sections, the variance term tends to zero, while the first term tends to

\[
|m(
\gamma
)|^2.
\]

This gives an explicit positive contraction from the diffuse phase-energy packet to the discrete rotor line.

## Symmetry-completed field

For \(\gamma>0\), use

\[
\mathscr R_{a,\gamma}^{full}
=
L^2(
\mu_{a,+\gamma}
)
\oplus
L^2(
\mu_{a,-\gamma}
).
\]

After Cauchy rescaling, this becomes

\[
L^2(
\mu_C
)
\oplus
L^2(
\mu_C
).
\]

The source-reached limit is the constant two-plane

\[
\mathcal R_\gamma
=
\mathbb C\mathbf 1_+
\oplus
\mathbb C\mathbf 1_-.
\]

Its limiting norm is

\[
\|m\|_{
\mathcal R_\gamma
}^2
=
|m(
\gamma
)|^2
+
|m(-
\gamma
)|^2.
\]

This is the discrete hostile rotor plane with counting measure.

## Dagger

Centered dagger exchanges the two Cauchy fibers and conjugates values:

\[
D(
F_+,F_-
)
=
(
\overline{F_-},
\overline{F_+}
).
\]

It preserves the constant two-plane and induces

\[
D(
c_+,c_-
)
=
(
\overline{c_-},
\overline{c_+}
).
\]

Therefore rotor extraction commutes with dagger exactly.

## Crossing orientation

The positive measure \(\mu_{a,\gamma}\) depends on \(|a|\) and is insensitive to crossing orientation.

Orientation acts through the signed current multiplier

\[
-
\operatorname{sgn}(a)
\]

on the same rotor line. Hence the two one-sided current representatives are

\[
+
I_{
\mathcal R_\gamma
}
\]

and

\[
-
I_{
\mathcal R_\gamma
},
\]

while the positive rotor metric is unchanged.

The affine index clutching translates between these oriented representatives.

## Successor action

Let a source successor multiply boundary values by a continuous amplitude \(m_c(t)\). In the rescaled fiber it acts by

\[
F(x)
\longmapsto
m_c(
\gamma+|a|x
)
F(x).
\]

On source-reached sections, this converges strongly to scalar multiplication by

\[
m_c(
\gamma
).
\]

Therefore the limiting rotor successor is

\[
c
\longmapsto
m_c(
\gamma
)c.
\]

For the symmetry pair, the two rotor blades receive the amplitudes

\[
m_c(
\gamma
),
\qquad
m_c(-
\gamma
).
\]

Exact finite-\(a\) commutation with rotor averaging need not hold for nonconstant \(m_c\); the commutator tends strongly to zero on source sections as \(a\to0\).

## Continuous-field interpretation

Take the fixed generic fiber

\[
\mathscr H_C
=
L^2(
\mu_C
)
\]

for \(a\ne0\), and take the source-reached crossing fiber

\[
\mathscr H_0^{src}
=
\mathbb C.
\]

Declare a source section continuous when its rescaling converges to a constant as above.

This defines a canonical source-generated continuous field in which the generic diffuse Cauchy packet contracts to one discrete rotor line at the crossing.

The full generic fiber does not collapse in norm: nonconstant Cauchy modes remain. They are simply not reached by fixed smooth source sections in the \(a\to0\) limit. Therefore the reduction to \(\mathbb C\) is a source-generated quotient, not an isomorphism of the complete generic fibers.

## Hardy feature interpretation

The local Hardy difference row has positive Gram equal, up to its fixed normalization, to integration against \(\mu_{a,\gamma}\). The projection \(R_{a,\gamma}\) therefore defines a canonical rank-one quotient of that Hardy feature.

At the crossing, this quotient is exactly the discrete character line. For the symmetry pair, it is the rank-two rotor quotient.

Thus the rotor is not only a measure limit; it is an explicit asymptotically lossless quotient of the positive Hardy phase-energy feature on the source-generated sector.

## What this closes

The construction supplies:

1. an exact trivialization of all nonzero phase-energy fibers;
2. strong convergence of source sections;
3. a canonical contractive rotor extraction;
4. exact dagger compatibility;
5. limiting successor naturality;
6. an explicit positive-form decomposition into rotor mean and vanishing source variance.

## Remaining geometric gate

The extracted rotor currently lives in the Hardy phase-energy realization. One still needs a comparison map from this quotient to the physical prolate/cutoff defect feature.

The required map no longer has to discover the rotor norm. It must transport the already normalized constant Cauchy line:

\[
\mathbb C\mathbf 1_+
\oplus
\mathbb C\mathbf 1_-
\longrightarrow
\mathcal H_{
geom
}^{defect}.
\]

The comparison must preserve dagger, the limiting successor scalars, and affine orientation.

## Disposition

Cauchy rescaling gives an explicit continuous-field model of rotor formation. On every fixed smooth source section, the diffuse crossing phase energy contracts strongly and without loss onto the discrete rotor line.
