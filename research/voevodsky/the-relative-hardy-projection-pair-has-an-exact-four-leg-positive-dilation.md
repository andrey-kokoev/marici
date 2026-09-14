# The relative Hardy projection pair has an exact four-leg positive dilation

## Projection feature

Let `Q` be any orthogonal projection on a Hilbert space `H`. Define

\[
\boxed{
F_Q:
H
\longrightarrow
H\oplus H,
\qquad
F_Qx
=(Qx,
(I-Q)x).
}
\]

Because the two components are orthogonal,

\[
\boxed{
F_Q^*F_Q
=Q+(I-Q)
=I.
}
\]

Thus `F_Q` is an isometry.

Let

\[
J_2
=
\begin{pmatrix}
I&0\\
0&-I
\end{pmatrix}.
\]

Then

\[
\boxed{
F_Q^*J_2F_Q
=Q-(I-Q)
=2Q-I.
}
\]

Every projection therefore has a canonical positive two-leg feature whose signed readout is its associated reflection.

## Tate and reference projections

On one Hardy/angular fiber, let

\[
Q_{L,\chi}^T
=
M_{e^{2iLs}\gamma_\chi}
\Pi
M_{e^{2iLs}\gamma_\chi}^*,
\]

and let

\[
Q_L^0
=
M_{e^{2iLs}}
\Pi
M_{e^{2iLs}}^*.
\]

The first is the Tate-scattered cutoff projection; the second is the pure translated Hardy reference.

Both act on the same fiber and differ only by the gamma scattering conjugation after common translation.

## Four-leg feature

Define

\[
\boxed{
\Psi_{L,\chi}x
=
\frac1{\sqrt2}
\left(
Q_{L,\chi}^T x,
(I-Q_{L,\chi}^T)x,
Q_L^0x,
(I-Q_L^0)x
\right).
}
\]

This maps into

\[
H^{\oplus4}.
\]

Its ordinary positive Gram is

\[
\begin{aligned}
\Psi_{L,\chi}^*
\Psi_{L,\chi}
&=
\frac12
\left[
Q_{L,\chi}^T
+(I-Q_{L,\chi}^T)
+Q_L^0
+(I-Q_L^0)
\right]\\
&=I.
\end{aligned}
\]

Hence

\[
\boxed{
\Psi_{L,\chi}^*
\Psi_{L,\chi}
=I.
}
\]

The feature is an exact isometry for every cutoff and character.

## Relative signed readout

Define the four-leg fundamental symmetry

\[
\boxed{
J_4
=
\operatorname{diag}
(I,-I,-I,I).
}
\]

Then

\[
\begin{aligned}
\Psi_{L,\chi}^*
J_4
\Psi_{L,\chi}
&=
\frac12
\left[
(2Q_{L,\chi}^T-I)
-(2Q_L^0-I)
\right]\\
&=
Q_{L,\chi}^T-Q_L^0.
\end{aligned}
\]

Therefore

\[
\boxed{
\Psi_{L,\chi}^*
J_4
\Psi_{L,\chi}
=Q_{L,\chi}^T-Q_L^0.
}
\]

This is the exact relative Hardy projection pair.

## Observer localization

Let `M_(m_g)` be the observer multiplier and define

\[
\boxed{
\Psi_{L,\chi}(g)
=
\Psi_{L,\chi}
M_{m_{g,\chi}}.
}
\]

Whenever the observer makes the relevant products Hilbert--Schmidt or relatively traceable,

\[
\boxed{
\langle
\Psi_{L,\chi}(g),
J_4
\Psi_{L,\chi}(h)
\rangle_{rel}
=
\operatorname{Tr}_{rel}
\left(
M_{m_h}^*
(Q_{L,\chi}^T-Q_L^0)
M_{m_g}
\right).
}
\]

The right side is the localized Tate projection-pair functional.

## Gamma derivative

The common translation cancels in the projection difference. The relative trace formula gives

\[
\boxed{
\operatorname{Tr}_{rel}
\left(
M_{|m|^2}
(Q_{L,\chi}^T-Q_L^0)
\right)
=
\frac1{2\pi i}
\int
|m(s)|^2
\partial_s
\log\gamma_\chi(s)ds
+
e_{end,\chi}(m).
}
\]

The expression is independent of `L`, apart from endpoint conventions transported by the common translation.

Thus the signed readout of the four-leg positive feature is exactly the Tate connection.

## No positive subtraction

Each two-leg projection feature has Gram `I`:

\[
F_{Q^T}^*F_{Q^T}
=F_{Q^0}^*F_{Q^0}
=I.
\]

The construction does not subtract one positive Gram from another before feature formation. It takes their orthogonal direct sum and applies the signed readout only afterward.

Therefore:

\[
\boxed{
\text{positive completion first},
\qquad
\text{relative cancellation second}.
}
\]

This is exactly the required order for a positive realization functor.

## Location of the pure mismatch strip

For the pure reference `Q_L^0`, the pair with the base Hardy projection is nested. Its `2L` boundary-crossing mass lies in an exact `H_10/H_01` mismatch sector.

The four-leg feature retains that sector inside the reference projection/complement rows. It never mislabels it as a generic `B(I-B)` defect.

The Tate rows may contain both exact mismatches and generic angle mass. The formula remains valid without decomposing either projection pair into Halmos sectors.

## Relation to Halmos decomposition

If desired, decompose each pair into:

- `H_11`;
- `H_10`;
- generic `K \oplus K`;
- `H_01`;
- `H_00`.

The four-leg feature is defined before this decomposition and therefore automatically includes every exact atom and generic component with correct multiplicity.

Halmos decomposition refines the feature; it is not needed to make the relative projection difference well typed.

## Angular assembly

Define

\[
\boxed{
\Psi_{L,S}
=
\bigoplus_\chi
\Psi_{L,\chi}.
}
\]

Smooth observer coefficients decay rapidly in `chi`, while the gamma logarithmic derivatives have controlled conductor/polynomial growth. Hence the signed relative readout is angularly summable on the declared observer core.

The ordinary norm of the unlocalized full feature remains infinite on the noncompact carrier. Positivity is interpreted observerwise or with the finite `(R,N)` regulator retained before limit.

## Conductor filtration

Because the four-leg construction is diagonal in angular character, conductor projections commute with it. At level `F`, use

\[
\Psi_{L,S,F}
=Z_F\Psi_{L,S}.
\]

The resulting features restrict exactly under `F<=F'`. The relative signed readout converges on the conductor-filtered core to the global Tate multiplication form.

Unlike the common-Gram Jordan removal, the four-leg positive dilation itself requires no lower-semiboundedness of the Tate connection: `J_4` is bounded and each projection row is contractive.

## Important distinction

The feature norm is

\[
\|\Psi_{L,\chi}x\|^2
=
\|x\|^2.
\]

It does not converge to the absolute Tate norm

\[
\langle x,
|A_S|x\rangle.
\]

Thus the four-leg construction is a positive **dilation of the signed relative form**, not the minimal Jordan realization of that form.

Minimalizing the limiting signed form recovers the two legs

\[
(A_{S,+}^{1/2},
A_{S,-}^{1/2}),
\]

but the quotient/minimalization map is unbounded or filtered when the Tate connection is unbounded.

## Exact finite-regulator version

At finite outer cutoff `R` and angular cutoff `N`, let `Z_(R,N)` be the common regulator projection. Define

\[
\boxed{
\Psi_{L,R,N}x
=
\frac1{\sqrt2}
\left(
Q_L^T Z_{R,N}x,
(I-Q_L^T)Z_{R,N}x,
Q_L^0Z_{R,N}x,
(I-Q_L^0)Z_{R,N}x
\right).
}
\]

Then all four legs are ordinary Hilbert-space vectors/operators in the regulated carrier and

\[
\boxed{
\Psi_{L,R,N}^*
\Psi_{L,R,N}
=Z_{R,N}
}
\]

on the regulator range, while

\[
\boxed{
\Psi_{L,R,N}^*
J_4
\Psi_{L,R,N}
=Z_{R,N}
(Q_L^T-Q_L^0)
Z_{R,N}.
}
\]

This is the exact finite `(L,R,N)` positive regulator identity needed before taking limits.

## Coherence

The construction is functorial under any unitary intertwining both projection pairs. It is also strict under:

- angular direct sums;
- conductor restriction;
- finite regulator inclusion when the regulator projections are nested;
- exchange of Tate and reference rows together with `J_4 -> -J_4`.

No spectral threshold or dyadic depth is required to define this relative boundary feature.

Dyadic refinement can subsequently be applied to the Tate pair's generic angle block without changing the four-leg relative identity.

## Consequence for `C_34`

At the localized relative-Hardy level, the positive boundary sewing is now explicit:

\[
\boxed{
\text{four positive projection/complement legs}
\xrightarrow{J_4}
Q_{L,\chi}^T-Q_L^0
\xrightarrow{\operatorname{Tr}_{rel}}
\frac1{2\pi i}
\partial_s\log\gamma_\chi.
}
\]

This realizes the Tate scattering connection as a signed readout of an exact positive feature.

## Remaining comparison

What remains is not positivity of the Hardy boundary feature. It is comparison with Connes's physical product cutoff:

1. transport the exact finite `(Lambda,R,N)` cutoff pair to the Hardy pair with the observer in the same positions;
2. verify the centered product trace equals the four-leg signed readout in the regulator limit;
3. track endpoint and opposite-polarity conventions;
4. relate the Tate generic dyadic refinement to the same four-leg carrier.

The scalar limit is already known; the missing theorem is equality/convergence of the regulated operator placements.

## Disposition

The relative Hardy pair has the exact positive dilation

\[
\boxed{
\Psi_Lx
=
\frac1{\sqrt2}
(Q_L^Tx,
(I-Q_L^T)x,
Q_L^0x,
(I-Q_L^0)x),
}
\]

with

\[
\boxed{
\Psi_L^*
\Psi_L
=I,
\qquad
\Psi_L^*
J_4
\Psi_L
=Q_L^T-Q_L^0.
}
\]

This is a complete positive realization of the Tate--Hardy relative boundary at every finite regulator. It retains exact mismatch, generic prolate, and intersection sectors without conflation. The unresolved `C_34` gate is solely the operator-placement comparison with Connes's exact product-cutoff regulator.
