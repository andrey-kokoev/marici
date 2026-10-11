# Prior clues after the relative-anchor canonical chart

**Current disposition (7 October 2026):** the proposed all-port comparison
below was completed in `shared-recoil-cotangent-binding.md`; it is not an open
task. The further question of canonically combining its recoil momenta with
the old A*q spatial reading is now excluded by the full-source rank bound in
`old-spatial-recoil-poisson-obstruction.md`. This prior-search record is retained
as history; neither closure supplies a physical localization criterion.

## Question and scope

Operator request: search prior research for clues to the remaining spatial,
charge and inertia interpretation. The current six-port pulse law, metric,
preparation and retained histories stay fixed. The relevant follow-up SCC
obligations are attachment transport and readout descent, not construction of
another dynamics. This turn inspected packets, selected implementations and
an existing receipt; it ran no mathematical checker or formal proof root.

## 1. Zero endpoint momentum is a chart statement, not a recoil obstruction

`exchange-to-mechanical-recoil.md` and its inspected
`checkers/check_exchange_recoil_readout.py` use REAL exchange amplitudes as
momentum coordinates. The isolated pair (a,b)->(b,a) becomes an elastic
collision through a declared mass-dependent linear map. Its cotangent lift
also supplies the conjugate position transformation; on the stated contact
subspace the positions are unchanged. Every positive mass pair admits the
mixed reading, so that result does not select masses.

Our new `relative-anchor-canonical-chart.md` instead names the reference-relative
real quadrature q and its metric-weighted imaginary quadrature p. Its existing
checker and 882-control receipt ALREADY test the symplectic frame change

    q_tilde=-K^-1*p/2,
    p_tilde=2*K*q,

and preservation of every port Hamiltonian

    h_i=(K*q)_i^2/2+p_i^2/8.

Thus real exchange endpoints with p=0 can have p_tilde!=0. In the rotated
chart q_tilde=0 there instead. The previous endpoint census is correct, but
cannot be used as an invariant argument against all recoil readings.

This is a reason to compare with the OLD real-amplitude recoil adapter,
not evidence that the rotated momentum has become physical. Under a passive
chart change the old readings must be transported: the previous spatial
reader X*q becomes X*K^-1*p_tilde/2, not X*q_tilde. Renaming the quadratures
cannot simultaneously retain that reader and change its physical meaning.

## 2. The all-port compatibility test must survive that comparison

`multiport-mechanical-binding-gate.md` tests ONE shared scalar carrier body
and six scalar partners. The reflection-normal Gram is

    C_ij=(delta_ij+f_i^T H f_j)/2=K_ij/2.

The scalar-star model requires off-diagonal factorization C_ij=v_i*v_j.
The source quartet AB,BC,AD,DB instead has tetrad -5/29282. Independent normal
signs and inactive spectators cannot remove it. A quadrature relabelling does
not undo this fixed-operation obstruction.

The excluded architecture is not every collective mechanics. Vector-valued
bodies, additional interacting internal modes and different shared-body
incidences were expressly left unclassified. The relative-anchor calculation
now supplies a common canonical carrier on which to test such a map, rather
than separately fitting a momentum basis at each port.

`../aspect/optical-material-hamiltonian-equivalence.md` gives the corresponding
methodological control: separately fitted channels can all pass while one
shared transport fails. Apply the same requirement to position, momentum,
kinetic pairing and all six labelled operations together.

## 3. Spatial covariance alone does not select displacement or localization

`../voevodsky/spatial-momentum-to-position-source-audit.md` recovers an existing
continuous-translation/Fourier bridge. Its characters have the form
exp(i*p(x)/kappa), with an action scale kappa and contragredient spatial
transport. The dual metric is the inverse metric in a nonorthonormal basis.
These facts do not create an affine origin, physical length scale or position
state from a momentum marginal. Its small exact implementation was inspected,
not rerun.

`../voevodsky/particle-source-to-newtonian-spatial-adapter.md` makes the last
point concrete: sources with identical COMPLETE particle momentum measures,
total momentum and angular momentum can have different positions and tides.
It gives an adapter only after retaining the positions, masses and field law
of its own Newtonian fixture. Those inputs are not supplied by our chart.

`photon-spatial-phase-return.md` tests the actual prior finite spatial atlas:
its S4 actions rotate or exchange bodies about a common center, but do not
produce accumulated translation. Native endpoint words also need their actual
comparison witnesses; endpoint labels do not choose those witnesses.

Reusable question: what existing source operation represents physical
configuration change, and which proposed momentum generates it? Our current
24-frame covariance tests alone cannot answer that. No continuous spatial
translation/localization map for the six-port state was located in this search.

## 4. Charge work already separates global phase from a local matter/field law

`137-gauge-adapter-and-complex-lift.md` supplies the complex pulse and global
phase symmetry underlying the current model. It also rejects a product of
two four-component amplitude vectors as a closed substitute for the full
tensor state: an allowed comparison raises tensor rank. Its implementation
was inspected; its NumPy tests were not rerun.

Its proposed next adapter retains the full tensor and records, and tests local
endpoint phase covariance while transporting operation/connection data. It
must not require a nontrivial local phase action to commute with every frozen
matrix, nor mistake passive covariance for a new physical gauge field.

`record-charge-and-phase-transport.md` and `record-gauge-feedback-loop.md`
already provide separate trial continuity, current, field-response and Gauss
interfaces. They supply hopping strengths, field coefficients, geometry and
background charge; the latter is needed by that compact closed-graph fixture.
They explicitly lack the comparison-model adapter. Their existence supplies
acceptance tests, not permission to replace the current interaction with them.

`continuation-charge-character.md` forces inverse phase character only in the
specified neutral-answer linear-dual sector. An effect is not thereby a
persistently interacting charged body. Likewise the reference momentum -Q
in our chart is not a negatively charged species.

## 5. Phase-frame transport constrains the eventual momentum interpretation

`retained-hamilton-jacobi.md` already derives, for supplied smooth trajectory
branches and phase scale hbar,

    H_a(x,p,t)=H_b(x,p-hbar*d_x chi,t)-hbar*d_t chi.

Endpoint-dependent rephasing transports momentum and energy. It is not merely
an extra scalar phase and is not itself a force. Our newly retained action
endpoint term is compatible with this discipline; it is not a derivation of
an electromagnetic potential or an action/Bargmann-phase identification.

`../sontag/rigidity-modulo-authorized-gauge.md` adds a useful selection test:
freeze which differences are authorized presentation changes, then compare
rival physical readings on the independently admitted source interface. Do
not quotient away a rival simply because the equations admit both choices.

## Bounded next test and stopping conditions

Compare the existing real-amplitude recoil reading with the new reference-relative
canonical chart, including its cotangent position map. Require ONE shared map
across all six ports, preserving the fixed kinetic pairing, source record,
intermediate pulse and endpoint maps. Keep the three internal pairs; allow
vector/internal-body candidates only with their body incidence stated before
testing. Reuse the reflection Gram as a falsifier instead of fitting masses.

A passing algebraic comparison would still need an independently sourced
configuration/localization reading and dimensional normalization. For electric
charge, current, matter/field identification and field normalization remain
separate missing maps. Neither another freely chosen gauge Hamiltonian nor
another abstract Fourier transform supplies those maps.

The search's main change is therefore specific: the old recoil adapter and
the new canonical chart should be compared directly. Zero momentum at real
endpoints does not close that route, while the scalar-body Gram obstruction
and the absence of physical source selection still do.
