# Gauge-complete SM portal and accessibility audit (WP131)

Owner: `marici.Figueiredo`.

## Bounded question

Can WP128's mediator/flavon sector be connected to physical Standard Model
external states by a gauge-, Lorentz-, and weak-basis-complete portal, and does
that source determine whether the WP130 threshold experiment is accessible?

Pre-objective process report: excitement `9/10`, confidence `8/10` that a
complete EFT portal exists and `3/10` that accessibility follows from the
current source, expected information gain `9/10`. The immediate reason is that
the same flavons used to define Yukawas provide the natural bridge to quark--
Higgs states. Confounds are the dimension-five portal, unspecified absolute
flavor scale, confinement/detector realization, and simplified widths. These
reports are non-evidential.

Frozen optionality snapshot: one up portal and one down portal; canonical
dimension and hypercharge checks; two derived reduced widths; one reachable
benchmark; one exact source-scale hostile pair; twelve exact checks. No
threshold mass is fitted to detector reach.

## Frozen physical portal

Take `Phi_u` and `Phi_d` in the bifundamental representations already used by
WP128 and declare

\[
\mathcal L_{\rm portal}=
-\frac{c_u}{\Lambda}\bar Q_L\widetilde H\Phi_u u_R
-\frac{c_d}{\Lambda}\bar Q_L H\Phi_d d_R+\text{h.c.}
\]

The Lorentz spinors contract to scalars. The Standard Model gauge checks are

\[
-\frac16-\frac12+\frac23=0,
\qquad
-\frac16+\frac12-\frac13=0,
\]

and the `SU(2)` doublets contract in the usual up/down Yukawa channels. Under
the full weak-basis group,

\[
\bar Q_L\to\bar Q_LU_Q^\dagger,quad
\Phi_u\to U_Q\Phi_uU_u^\dagger,quad u_R\to U_u u_R,
\]

with the analogous down transformation, so both portals descend exactly.
Their canonical field dimension is five; `1/Lambda` makes the Lagrangian
dimension four. This is a gauge- and Lorentz-complete EFT portal, not a
renormalizable fundamental Yukawa interaction.

## From the portal to pole widths

After `Phi_a=V_a+phi_a`, the vacuum term gives

\[
Y_a=\frac{c_aV_a}{\Lambda}.
\]

The WP128 sources `mu_u Tr(A H_u)+mu_d Tr(D H_d)` mix the adjoints with
Hermitian flavon fluctuations. If `zeta_i` is the overlap of a scalar mass
eigenstate with the portal-active fluctuation, its effective quark--Higgs
coupling is

\[
y_i=\frac{c,v_H}{\Lambda}\zeta_i.
\]

For negligible final-state masses, define the exact reduced width

\[
\widehat\Gamma_i=\frac{8\pi\Gamma_i}{N_cM_i}=|y_i|^2.
\]

The benchmark `c=v_H=Lambda=1`, with source mixing overlaps
`(zeta_1,zeta_2)=(1/5,1/4)`, gives reduced widths `(1/25,1/16)`.
Thus masses, residues, and widths are functions of a single declared source
packet rather than independent formal pole labels. A complete phenomenology
would restore phase space, competing channels, running, and the full scalar
mixing matrix.

## Accessibility hostile pair

The current source does not select its absolute flavor scale. Let every
dimension-one flavor-sector input, including `V_a`, `Lambda`, and mediator
pole masses, scale by a common positive `s`; scale the dimensionful scalar
couplings coherently. Then

\[
\frac{V_a}{\Lambda}\longmapsto\frac{sV_a}{s\Lambda}
=\frac{V_a}{\Lambda},
\]

so all dimensionless low-energy Yukawa data and normalized selector
coordinates remain fixed. The mediator thresholds instead obey `M_i->sM_i`,
and the portal fluctuation residues decrease as `1/s` at fixed electroweak
scale.

With detector reach `E_max=5`, the benchmark masses `(1,2)` give two
accessible poles. The exact scale-related source with `s=10` has masses
`(10,20)`, zero accessible poles, the same low Yukawa, and smaller portal
residues. These are physically different sources, not weak-basis
presentations, collapsed by the low-energy flavor experiment.

Therefore accessibility is not a consequence of WP128's selector geometry.
It requires a new source operation fixing the absolute flavor scale relative
to the electroweak and detector scales.

## Instrument and groupoid disposition

WP131 supplies the missing gauge/Lorentz-complete portal at EFT level and
derives a conditional width map. It still does not establish an executable
instrument. That would require a UV completion of the dimension-five portal,
an independently selected absolute scale, complete production and decay
rates, collider initial states, backgrounds, luminosity, and a calibrated
detector likelihood.

The reference apparatus creates a relational energy observable `M_i/E_max`
and changes the physical groupoid to the stabilizer of the SM clock, beam, and
detector calibration. It does not reveal an absolute threshold belonging to
the original flavor-only experiment.

Classification: **gauge/Lorentz-complete conditional SM portal; accessibility
not source-selected**. The smallest exact falsifier of accessibility authority
is the `s=10` pair: identical dimensionless low-energy flavor packet, but two
versus zero accessible poles. The first nonfaithful arrow is now upstream of
detector convolution:

\[
\text{dimensionless flavor source}
\longrightarrow
\boxed{\text{absolute-scale embedding}}
\longrightarrow
\text{threshold detector records}.
\]

Post-objective process report: excitement `9/10`, confidence `10/10` in the
bounded portal/descent and scale obstruction, realized information gain
`10/10`. Raw delta: one complete EFT portal is constructed; two reduced widths
are derived; one accessible benchmark is opened; an exact scale-related
hostile source removes both accessible poles while preserving the low packet;
twelve of twelve checks pass; no absolute-scale selector or executable
instrument is added. These reports are non-evidential.
