# Spin-memory contour complement theorem

## Two different ports

The grade-three incidence density and the spin-memory detector are not the
same map.

The local Bondi constraint port is

\[
\mathcal A_3C=\operatorname{Im}
\left[\partial_{\bar z}D_z^3C^{zz}\right].
\]

It relates shear to angular-momentum flux and has the smooth magnetic kernel
\(l=2,3,4\).

The physical spin-memory detector instead measures the time-integrated
contour holonomy

\[
\Delta_C
=
\int du\oint_C
\left(D^zC_{zz}\,dz+D^{\bar z}C_{\bar z\bar z}\,d\bar z\right),
\]

up to the fixed apparatus normalization. This is the counter-orbiting-light
time delay derived in equations (4.3)--(4.5) of *New Gravitational Memories*:
<https://doi.org/10.1007/JHEP12(2016)053>.

## Magnetic multiplier

Write a magnetic-parity shear in terms of its scalar potential \(\Psi\).
Spin-two construction contributes the two raising factors, and divergence
contributes one lowering factor. Taking the exterior derivative of the
resulting coexact one-form gives the scalar multiplier

\[
\mu_l=(l-1)l(l+1)(l+2).
\]

It is nonzero for every physical shear degree \(l\geq2\). In particular,

\[
\mu_2=24,\qquad \mu_3=120,\qquad \mu_4=360.
\]

Thus every nonzero member of the 21-dimensional \(\mathcal A_3\) kernel has a
nonzero contour-curvature density.

## Joint faithfulness of contours

Let \(\alpha(C)\) be the spin-memory one-form of the time-integrated magnetic
shear. If

\[
\oint_C\alpha=0
\]

for every contractible contour, Stokes' theorem gives \(d\alpha=0\).
Magnetic parity makes \(\alpha\) coexact. Since \(H^1(S^2)=0\), a closed
coexact one-form on the sphere vanishes. The nonzero multiplier \(\mu_l\)
then implies that the magnetic shear vanishes.

Therefore the complete labelled contour family is jointly faithful on the
smooth magnetic shear packet, including the low block:

\[
\ker\mathcal A_3\cap\ker\{\Delta_C:C\subset S^2\}=0.
\]

One fixed contour is not faithful; it supplies only one scalar functional.
The theorem requires the family of contours, or a separately constructed
finite family proved faithful on a declared finite harmonic block.

## Where the information goes

The 21 low coefficients are homogeneous or boundary data for the local
flux-incidence equation. They are not erased by magnetic transport and are
not invisible to the physical spin-memory experiment. The constraint port
cannot infer them from local angular-momentum flux, while contour holonomy
can measure them directly.

The first nonfaithful arrow is therefore contextual:

\[
\text{magnetic shear}
\longrightarrow
\begin{cases}
\text{grade-three flux incidence} & \text{blind on }l=2,3,4,\\
\text{complete contour family} & \text{faithful for }l\geq2.
\end{cases}
\]

The abstract 21 harmonic coefficient ports are a finite coordinate
presentation of this missing block. They are not needed to prove that a
physical complementary observable exists. Establishing a minimal finite
apparatus of 21 or more actual contours remains a separate design problem.

## Scope

This is a linear, time-integrated, smooth magnetic-sector theorem on the
unit sphere. It does not claim that one contour reconstructs the field, that
arbitrary hard-flux histories satisfy nonlinear energy conditions, or that
the previously proposed algebraic 24-port frame has a physical realization.
