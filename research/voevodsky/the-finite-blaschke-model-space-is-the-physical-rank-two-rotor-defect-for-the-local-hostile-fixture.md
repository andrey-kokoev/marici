# The finite Blaschke model space is the physical rank-two rotor defect for the local hostile fixture

## Objective

Transport the canonically normalized Cauchy rotor line from phase energy into an actual projection-defect space.

For the local hostile fixture this can be done exactly: a simple Blaschke crossing produces a rank-one Hardy projection defect, and the symmetry-completed pair produces a rank-two model space.

This closes the local Hardy/projection realization gate. It does not yet identify the same defect inside the full semilocal prolate cutoff pair.

## Hardy projection pair

Let

\[
H^2_+
\subset
L^2(\mathbb R)
\]

be the upper-half-plane Hardy space and let

\[
\Pi
:
L^2(\mathbb R)
\to
H^2_+
\]

be its orthogonal projection.

For \(b>0\) and \(\gamma\in\mathbb R\), define the elementary upper-half-plane Blaschke factor

\[
b_{\gamma,b}(z)
=
\frac{
z-\gamma-ib
}
{
z-\gamma+ib
}.
\]

Multiplication by \(b_{\gamma,b}\) is unitary on boundary \(L^2\) and isometric on \(H^2_+\). Hence

\[
b_{\gamma,b}H^2_+
\subset
H^2_+.
\]

Define

\[
Q_{\gamma,b}
=
M_{b_{\gamma,b}}
\Pi
M_{b_{\gamma,b}}^*.
\]

Then \(Q_{\gamma,b}\) is the projection onto

\[
b_{\gamma,b}H^2_+.
\]

Therefore

\[
\boxed{
\Pi-Q_{\gamma,b}
=
P_{K_{b_{\gamma,b}}},
}
\]

where

\[
K_{b_{\gamma,b}}
=
H^2_+
\ominus
b_{\gamma,b}H^2_+
\]

is the degree-one model space.

## Normalized defect vector

The model space is spanned by

\[
e_{\gamma,b}(t)
=
\sqrt{
\frac b\pi
}
\frac1{
t-\gamma+ib
}.
\]

Its boundary norm is one:

\[
\int_{
\mathbb R
}
|e_{\gamma,b}(t)|^2dt
=1.
\]

Moreover,

\[
\boxed{
|e_{\gamma,b}(t)|^2dt
=
\frac1\pi
\frac b{(t-\gamma)^2+b^2}
\,dt
=
d\mu_{b,\gamma}(t).
}
\]

Thus the squared modulus of the normalized Hardy defect vector is exactly the crossing phase-energy measure.

Consequently

\[
\Pi-Q_{\gamma,b}
=
|
e_{\gamma,b}
\rangle
\langle
e_{\gamma,b}
|.
\]

## Exact rotor transport

Define

\[
W_{\gamma,b}:
\mathbb C
\longrightarrow
K_{b_{\gamma,b}},
\qquad
W_{\gamma,b}c
=
ce_{\gamma,b}.
\]

This is unitary.

For every bounded source multiplier \(m\), the compressed multiplication matrix coefficient is

\[
\langle
M_m
e_{\gamma,b},
e_{\gamma,b}
\rangle
=
\int
m(t)
\,d\mu_{b,\gamma}(t).
\]

As \(b\downarrow0\),

\[
\langle
M_m
e_{\gamma,b},
e_{\gamma,b}
\rangle
\longrightarrow
m(\gamma).
\]

Therefore \(W_{\gamma,b}\) realizes exactly the Cauchy-averaging rotor extraction inside the rank-one Hardy projection defect.

## Symmetry-completed product

Define

\[
B_{b,\gamma}(z)
=
b_{\gamma,b}(z)
b_{-\gamma,b}(z).
\]

Its model space

\[
K_{B_{b,\gamma}}
=
H^2_+
\ominus
B_{b,\gamma}H^2_+
\]

has dimension two, and

\[
\boxed{
\Pi-
M_{B_{b,\gamma}}
\Pi
M_{B_{b,\gamma}}^*
=
P_{K_{B_{b,\gamma}}}.
}
\]

Use the ordered Takenaka basis

\[
e_{+,b}
=
e_{\gamma,b},
\]

\[
e_{-,b}
=
b_{\gamma,b}
e_{-\gamma,b}.
\]

These vectors are orthonormal. Since the Blaschke factor is unimodular on the boundary,

\[
|e_{+,b}(t)|^2dt
=
d\mu_{b,+\gamma}(t),
\]

\[
|e_{-,b}(t)|^2dt
=
d\mu_{b,-\gamma}(t).
\]

Thus

\[
W_{b,\gamma}:
\mathbb C^2
\longrightarrow
K_{B_{b,\gamma}},
\]

\[
W_{b,\gamma}(c_+,c_-)
=
c_+
e_{+,b}
+
c_-
e_{-,b}
\]

is unitary and transports the discrete rotor plane into the exact rank-two projection defect.

## Source matrix limit

For a bounded continuous multiplier \(m\), the compressed matrix is

\[
G_{b,\gamma}(m)
=
W_{b,\gamma}^*
M_m
W_{b,\gamma}.
\]

Its diagonal entries satisfy

\[
G_{b,\gamma}(m)_{++}
\longrightarrow
m(\gamma),
\]

\[
G_{b,\gamma}(m)_{--}
\longrightarrow
m(-\gamma).
\]

For \(\gamma>0\), the off-diagonal entries tend to zero on the Mellin--Schwartz source core because the two normalized defect packets concentrate at distinct points.

Hence

\[
\boxed{
G_{b,\gamma}(m)
\longrightarrow
\begin{pmatrix}
m(\gamma)&0\\
0&m(-\gamma)
\end{pmatrix}.
}
\]

This is the discrete character representation previously derived by faithful horn recovery.

## Dagger

Centered reflection exchanges the two divisor centers. With the corresponding antiunitary action on \(H^2_+\), it sends the ordered model-space basis to the opposite ordered basis up to unimodular phase.

Those phases can be fixed by the Takenaka basis convention so that the limiting action is

\[
D(c_+,c_-)
=
(
\overline{c_-},
\overline{c_+}
).
\]

Thus the physical defect plane carries the required rotor dagger.

## Orientation and hostile passage

The positive projection defect depends on

\[
b=|a|
\]

and is the same on both sides of the crossing.

The crossing orientation is carried by which projection difference is read:

\[
a<0:
\qquad
+
(
\Pi-Q_{b,\gamma}
),
\]

\[
a>0:
\qquad
-
(
\Pi-Q_{b,\gamma}
).
\]

Thus the same positive rank-two rotor plane underlies both polarities, while the signed current reverses.

The affine index row records the change of orientation:

\[
-
P_{K_B}
+2P_{K_B}
=
+
P_{K_B}.
\]

This is the operator version of

\[
\nu+2I.
\]

## Uniform trace control

Unlike the Paley--Wiener approximate evaluation operator, the exact Hardy model-space projection satisfies

\[
\|P_{K_{B_{b,\gamma}}}
\|_1
=
\operatorname{Tr}
P_{K_{B_{b,\gamma}}}
=2
\]

for every \(b>0\).

Therefore the rotor defect is uniformly trace class before taking the crossing limit.

The prior \(2L/\pi\) divergence arose from realizing point evaluation as a rank-one form inside an expanding bandlimited carrier. The model-space realization instead uses the correct relative projection defect and retains its topological rank.

## Multiplicity

For a finite Blaschke product of degree \(N\),

\[
\Pi-
M_B
\Pi
M_B^*
=
P_{K_B}
\]

has rank and trace \(N\).

An ordered Takenaka basis splits it into \(N\) elementary rotor lines. This agrees with strict divisor telescoping and with the Krein--Langer index count.

## Tetrahedral placement

The rank-two model-space projection supplies an exact local operator on the spectral--trace face:

\[
H_{134}^{rot}:
\mathcal R_\gamma
\xrightarrow[
\cong
]{W_{b,\gamma}}
K_{B_{b,\gamma}}.
\]

It also supplies the local projection-pair geometry expected on \(H_{234}\):

\[
P_{K_B}
=
\Pi-
M_B
\Pi
M_B^*.
\]

Thus the hostile rotor is physically realized for the local Hardy scattering pair.

## Remaining semilocal gate

The full geometric edge uses the transported semilocal prolate/cutoff pair rather than only the local Hardy pair. One still must construct an intertwiner carrying

\[
P_{K_{B_{b,\gamma}}}
\]

into the corresponding finite-rank defect of that transported cutoff geometry.

The desired comparison must preserve:

1. rank and trace two;
2. dagger symmetry;
3. source compressed multipliers;
4. affine orientation;
5. successor naturality;
6. cutoff removal.

No scalar volume subtraction is needed for the model-space rotor itself.

## Disposition

For the local hostile fixture, the physical rotor is the finite Blaschke model space:

\[
\boxed{
\mathcal R_{\gamma}^{phys}
=
K_{B_{b,\gamma}},
\qquad
P_{\gamma}^{phys}
=
\Pi-
M_{B_{b,\gamma}}
\Pi
M_{B_{b,\gamma}}^*.
}
\]

Its normalized defect vectors have squared moduli equal to the crossing phase-energy measures, and its trace is uniformly the divisor degree. The remaining comparison is from this exact local Hardy defect to the global semilocal cutoff defect.
