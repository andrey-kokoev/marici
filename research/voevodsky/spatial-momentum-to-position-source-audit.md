# Spatial momentum to position: recovered source bridges and their limits

## Outcome

There is more prior structure than the preceding spatial-fiber note recovered.
The repository already contains (1) Fourier dualization of a continuous
translation group and (2) a Poincare-charge construction of a transverse
centroid. The primary cosmology source also explicitly starts with position
space and a spatially flat FRW metric. Thus position space is not absent from
the source model. It is not derived there from the momentum defect alone.

These findings narrow the missing bridge to source identification, units and
localization, rather than requiring a new position-space primitive to be
invented without reference to existing work.

## Source recovery

1. `research/nima/fourier-transform-as-character-linearization-of-segal-translation-object.md`
   proves a Fourier theorem for a supplied second-countable locally compact
   abelian group G and nonzero Haar measure. Its composition correspondence
   is addition; integration over addition fibers gives convolution. Continuous
   scalar unitary realizations are exactly characters. Section 8 specializes
   to real vector groups; section 10 explicitly reserves source adapters.
   Haar existence, Pontryagin duality and Bochner are named inputs. This is
   written mathematics, not a proof-assistant theorem.
2. `research/nima/marici-machian-gravity-direction.md`, section 'Stationary
   Poincare-orbit reduction', constructs X=JP/P^2 and retains its degeneracies.
   Its Newtonian multipole section proves that finite Poincare charges do not
   determine local gravity. The existing Fraction checker was rerun successfully.
3. `research/benincasa/big-bang-source-boundary-audit.md` points to the frozen
   primary source arXiv:2402.06558v3. Direct local inspection of
   `temp/triangle-measure-primary-2402.06558v3-source/IR_Divs.tex`, lines 509-578,
   confirms the position-space scalar action (eq:SLS), the supplied metric

       ds^2 = a(eta)^2 [-d eta^2 + d x_vec^2]       (eq:FRW),

   and subsequent momentum-space field notation. The scale factor and spatial
   dimension d are supplied. This is direct evidence of existing background
   position geometry, not evidence that Fourier duality generated that background.
   This cached external source is not modified or copied into the repository.

## A typed Fourier bridge for the spatial family

Let M_D=D^perp be the spatial MOMENTUM vector space from Entry 124, with positive
metric h_D and its ordinary finite-dimensional vector-space topology. Its
additive group is locally compact abelian. Apply the existing Fourier theorem:

    M_D -> character group Hom_cont(M_D,U(1)).

For a real vector group each character uniquely has the form

    chi_xi(p)=exp(i xi(p)),       xi in M_D^*.

Thus a dual vector-space family exists over the timelike-direction base:

    {(D,xi) : xi in M_D^*} -> {timelike directions D}.

This supplies a candidate displacement group, not yet physical point events.
The distinction from a metric identification M_D ~= M_D^* is important: the
character construction is defined by linear evaluation and does not require
an inner product. The metric subsequently induces the dual metric h_D^-1.
In a nonorthonormal momentum basis with Gram matrix H, the Gram matrix on the
dual basis is H^-1, not H. This is tested with a nontrivial diagonal fixture.

If A:M_D -> M_D' is a retained spatial isometry, transport the dual in the
forward direction by

    xi -> xi composed with A^-1.

Then evaluation is preserved: (xi composed with A^-1)(A p)=xi(p). This is the
contragredient version of the preceding spatial-fiber transport. It does not
remove the choice of A or the residual spatial rotation freedom.

With Haar measure chosen from h_D, the Fourier theorem fixes its dual
normalization. In orthonormal numerical coordinates the convention uses
exp(-i p.xi) and dual measure (2*pi)^(-3) dxi. This normalization is NOT a
physical calibration of reciprocal momentum as length.

## Units and affine points are separate

For physical momentum p and physical displacement x, a phase convention is

    chi_x(p)=exp(i p(x)/kappa),

where p(x) denotes the momentum/displacement pairing and kappa has units of
action (hbar in the usual quantum convention). The character label is
xi=x/kappa. Therefore a metric induced on physical displacement coordinates
has squared length kappa^2 times the dual-metric squared norm of xi, relative
to the chosen momentum units. The algebra does not select kappa or those units.
Changing x and kappa by the same positive factor leaves every phase unchanged.

An additive displacement group has a distinguished zero DISPLACEMENT. It does
not choose a physical origin in an affine space of events. This is exactly the
place where the old charge-based centroid construction adds information.

## The existing centroid bridge

For timelike total Poincare momentum P and antisymmetric angular momentum J,

    X^mu = J^{mu nu} P_nu / P^2.

Antisymmetry gives X.P=0. For the source convention J -> J+a wedge P,

    X -> X + a - P (a.P)/P^2.

Thus X is a transverse centroid coordinate relative to the reference origin,
and X+R P is the center-of-momentum worldline. It responds correctly to origin
changes; it does not eliminate translation along that worldline. J/P also
carries length units when J is supplied with angular-momentum units. No new
scale can be extracted from P alone by this argument.

The extra input J is substantive. Holding P fixed and setting J=x wedge P
realizes every transverse x as X. So P alone cannot select the centroid.
Spin can select an axis but not generically a full frame; the old note already
retains these stabilizers. Its explicit antipodal-source examples show that
even P and J together do not determine the local tidal field.

Do NOT identify this P with the cosmological nonconservation defect D without
a source map. They have analogous timelike-projector formulas but different
physical roles. Likewise, the newer retained-package Q is neither by notation.

## Application to the Newtonian toy

A coherent conditional construction now has the following shape:

    Lorentzian momentum data + timelike D
       -> Euclidean spatial momentum fiber M_D
       -> Fourier-dual displacement candidate M_D^*
       -> calibrated affine position realization
       -> supplied point-source distribution and Newtonian potential
       -> local gradient and tidal readouts.

The existing FRW source supplies a possible background position realization,
but its proper spatial metric is a(eta)^2 delta_ij in comoving coordinates.
The earlier static Newtonian fixture does not specify an epoch or the relation
between those comoving coordinates and its physical radii 3 and 4. It also does
not identify its two masses with a cosmological momentum configuration.
A Fourier transform of a momentum-space amplitude is not automatically a
positive mass-density field. That source-to-density adapter remains required.

Consequently the new bridge is not a derivation of the fixture's source
positions, Newton's equation, or its coupling. It explains which already
available structures can implement the missing interface without disguising
those inputs as consequences of fibration.

## Verification

Commands run successfully:

    python research/voevodsky/check_spatial_dual_bridge.py
    python research/nima/checkers/check_machian_poincare_frame_reduction.py

The new checker passes eight exact Fraction controls: dual pairing and metric
naturality, wrong-variance and wrong-metric rejection, additive character
exponents, phase-scale relabelling, physical-length scale dependence, and
reciprocal unit scaling. These are finite algebraic checks, not analytic
Fourier inversion or physical selection proofs. Receipt:
`research/voevodsky/spatial-dual-bridge.json`.

The existing centroid checker passed its two nontrivial rational fixtures,
including centroid covariance, orthogonality, spin translation invariance and
a null-input rejection. It regenerated its existing result file; no owner
source implementation was edited.

## Narrow next gate

Choose one declared source model and build its explicit adapter to the static
Newtonian mass-density/position fixture, retaining the phase scale, spatial
scale factor, origin and frame choices. The most useful next test is not another
abstract Fourier theorem: it is whether that adapter is already specified by
the cosmological or Machian source, or must be an additional physical model.
