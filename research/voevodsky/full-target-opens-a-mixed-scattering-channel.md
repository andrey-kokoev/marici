# The full target opens a mixed scattering channel

Fresh resume selected `full-target-mixed-channel-readout:v1`.

## Result

For Nima's declared full normalized-probe target and counting-metric kinetic
prescription, the massive scalar can scatter into either of the two massless
modes:

    M(phi phi -> chi_a chi_b) = (s/F^2) delta_ab.

The Feynman vertex is i*M; signature is +--- and momenta are taken incoming in
the vertex calculation. Here s is the center-of-mass energy squared, not a
source label. For physical pair production s>=4m2, with m2=2U/F^2. The amplitude
is nonzero above threshold for identical outgoing species.

This is a complete tree four-point calculation in the supplied model, checked
in TWO full-target coordinate systems. It is not an inference from counting
extra tangent directions alone.

## Derivation from the actual source

The checker imports the owner's recorded swap images and verifies its action
on the selected even vector v0, odd vector w, and two remaining orthonormal even
vectors e1,e2. Parameterize a local unit probe by

    n = cos(phi/F) e(chi) + sin(phi/F) w,
    e(chi) = sqrt(1-|chi|^2/F^2) v0 + (chi_a/F) e_a.

On |phi/F|<pi/4 and |chi|<F this is the positive-overlap, positive-square-root
patch. Direct source evaluation gives

    <n,Pn> = cos(2phi/F),
    V = -U/2 log(cos(2phi/F)),
    ds^2 = dphi^2 + cos(phi/F)^2 h_ab(chi) dchi_a dchi_b,
    h_ab = delta_ab + chi_a chi_b/(F^2-|chi|^2).

The vacuum kinetic metric is identity and the mass-squared matrix is

    diag(2U/F^2, 0, 0).

Expanding the kinetic action produces

    L_mixed = -phi^2 [(dchi_1)^2+(dchi_2)^2]/(2F^2).

There is no mixed potential term in this chart. Four species-compatible
assignments of the differentiated legs give the vertex

    (2i/F^2) k1.k2 = i s/F^2

for two identical massless outgoing particles. All cubic vertices vanish at the
vacuum, so there are no exchange diagrams for this four-point process. Terms
with two different outgoing massless species vanish.

## Independent chart check

Use tangent Cartesian coordinates q=(psi,xi1,xi2) on the same unit sphere:

    n = sqrt(1-|q|^2/F^2) v0 + (psi/F)w + (xi_a/F)e_a.

Their metric and potential are

    G_ij = delta_ij + q_i q_j/(F^2-|q|^2),
    V = -U/2 log(1-2psi^2/F^2).

The exact transition is

    psi=F sin(phi/F), xi_a=cos(phi/F) chi_a.

The checker verifies the full metric pullback, not just its vacuum value.
In these coordinates the relevant interaction is instead

    L_mixed = psi xi_a (dpsi.dxi_a)/F^2.

Summing its four differentiated cross-pairs gives

    -i (p1+p2).(k1+k2)/F^2 = i s/F^2.

The two representations therefore agree after transporting the kinetic data,
despite different-looking interaction vertices. Both coordinate transformations
have identity linear part at the vacuum, so they use the same asymptotic field
normalizations and species.

## Why this does not contradict classical consistency

The normal force and normal geodesic acceleration vanish when chi=0. Thus
setting chi identically to zero is a consistent classical restriction. The
checker verifies these conditions directly.

That assertion does NOT say that every amplitude with external chi particles
vanishes. A phi^2(dchi)^2 interaction is compatible with both facts. Consequently
agreement of the pure-scalar tree readings does not authorize promotion to a
profile containing ALL scattering channels of the full target.

This gives a concrete physical refinement boundary: the scalar-only theory
omits an allowed final-state channel. It is not a claim that source states or
classical scalar solutions must be deleted.

## Verification and scope

    uv run --with sympy python research/voevodsky/check_full_target_mixed_channel.py

All 137 exact symbolic/provenance checks pass. They cover the source eigenspaces,
unit norm, overlap, both metrics, their full pullback, mass matrix, classical
restriction, absence of cubic vertices, differentiated-leg multiplicities and
both channel calculations.

An exact real on-shell 2->2 control at F=1,U=1/2 uses incoming energies 2 and
opposite spatial momenta sqrt(3), and outgoing massless energies 2 with opposite
transverse momenta 2. It conserves four-momentum and gives s=16 and M=16.

Receipt: `full-target-mixed-channel.json`. No owner artifact was changed.
This is symbolic geometry and a conditional bosonic tree calculation, not a new
Agda proof, a loop evaluation or a UV completion. The neighboring-probe kinetic
interpretation, Lorentzian spacetime, statistics and scales remain supplied.
The tree result is a perturbative statement, not a claim of validity at
arbitrarily high energies in this nonlinear sigma model.

## Next question

Test the corresponding two-massless-particle contribution to the forward
elastic unitarity cut. It should expose whether omitting these channels changes
a pure-scalar LOOP-level observable, even though the pure-scalar tree results
agreed. Derive the phase-space and identical-species factors explicitly; do not
infer a complete renormalized loop amplitude or quantum completion merely from
a nonzero tree channel.
