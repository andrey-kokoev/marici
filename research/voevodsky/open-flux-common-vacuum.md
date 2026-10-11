# A common zero-background Gauss model with retained exterior flux

## Result

We constructed one fixed selected-mode graph containing both carriers and an explicit exterior charge coordinate. The empty configuration and both unit internal-charge particle sectors satisfy the **same zero-background Gauss law**. Exterior flux and exterior charging energy are included rather than discarded.

For a declared cross-face boundary rule, minimizing the complete matter and electric energy gives a strictly higher belt energy than proton energy, even after the belt amplitudes relax.

A second common attachment rule reverses the ordering. Thus the common-vacuum gate has a mathematical completion, but a mass prediction still needs the physical boundary/field attachment to be selected. We did not tune that attachment to remove its counterexample.

## 1. Prior research and additional inputs

This reuses Nima's `record-gauge-feedback-loop.md` through our exact `weighted-matter-link-adapter.md`. The closed-graph obstruction was already known there. The reservoir discipline in `mass-history-retaining-locking-interaction.md` requires retaining both charge and energy outside the carrier.

The prior search also found `primitive-boundary-flux-needs-a-weighted-scale-energy-law.md`, but that concerns a Mellin/prime-counting boundary, not a particle Gauss construction. Its variables and energy law were not imported.

New declared inputs are:

- one identical electric lead from every endpoint of a geometrically cross-face contact to a common exterior coordinate;
- electric coefficient beta>0 on internal links and leads;
- exterior charging energy eta*q_ext^2/2, with eta>=0;
- comparison of fixed internal norm-charge one in each particle sector.

These are model inputs, not a derived electromagnetic boundary condition.

## 2. One graph, not separate backgrounds

The common graph has:

- 12 proton and 18 belt matter vertices;
- their existing 24 and 39 internal links;
- 12 exterior leads per carrier, read from the actual cross-face contact endpoints;
- one shared exterior charge coordinate.

There are 31 vertices and 87 links altogether. All remain present in the empty, proton and belt configurations. The inactive carrier has zero amplitudes and zero minimizing field, not a removed background.

With the prior incidence sign convention, impose

    B_full E = (rho_p, rho_b, q_ext),
    rho_i=n_i |a_i|^2,
    q_ext=-(Q_p+Q_b),
    Q_s=sum_(i in s) rho_i.

The background is identically zero. The Hamiltonian is

    H = H_matter,p + H_matter,b
        + beta/2 sum_links E_e^2 + eta/2 q_ext^2.

The empty configuration has a=0, E=0 and q_ext=0, with energy zero. The proton sector has (Q_p,Q_b,q_ext)=(1,0,-1); the belt sector has (0,1,-1). All three are checked on the same combined incidence matrix.

This is an **internal norm-charge**, not an electric-charge assignment. We do not assign positive electric charge to the proposed neutron. The exterior coordinate is a retained compensating resource; its eta/2 energy in either unit sector is included.

No creation protocol or charge quantization is inferred. The matter/link model is classical and conserves the specified norms. These are constrained sector minima, not yet quantum particle gaps. With no magnetic term the empty field also has unlifted connection directions; existence of this common empty reference is not a uniqueness theorem for the physical vacuum.

## 3. Eliminate the electric field without losing its energy

For prescribed density rho in either carrier, let

    L_boundary = B_internal B_internal^T + diag(boundary_ports).

The minimum-norm Gauss field is the potential-gradient field with

    phi=L_boundary^(-1) rho,
    E=B_full^T(phi,0).

Its energy is beta*rho^T L_boundary^(-1)rho/2. Exact checks retain the exterior divergence -sum(rho), and verify that the field norm equals rho^T phi. Circulation fields only increase the energy because they are orthogonal to this gradient solution.

This is a finite network energy, not a derived continuum Coulomb law.

## 4. Proton minimum

All twelve proton vertices have exterior leads. For unit charge, the twelve lead fluxes sum to one. Their squared norm is at least 1/12; internal field and matter energies are nonnegative.

The uniform coherent proton density rho_i=1/12 attains that lower bound: each lead carries 1/12, internal field is zero, and the matter energy is zero. Therefore

    E_p,min = beta/24 + eta/2.

No particle-specific additive energy was inserted.

## 5. Belt relaxation and its global minimum

The belt has twelve lead-bearing vertices and six middle vertices with no lead. The source mode norms are

    n_outer=2386/675,
    n_middle=4198/675.

Let y be the total density on the six middle vertices. The stationary density has outer values (1-y)/12 and middle values y/6. The exact potential is

    phi_outer=1/12,
    phi_middle=1/12+rho_middle/2.

Each exterior lead still carries 1/12. The extra field lies on the twelve links between middle and outer vertices. Its energy is beta*y^2/24 above the common beta/24 lead contribution.

The source matter energy for this profile is

    [sqrt(A)*sqrt(1-y)-sqrt(B)*sqrt(y)]^2,
    A=2099/3292, B=1193/1646.

Thus

    E_b,min = beta/24 + eta/2 + min_(0<=y<=1) F_beta(y),
    F_beta(y) = [sqrt(A)*sqrt(1-y)-sqrt(B)*sqrt(y)]^2
                + beta*y^2/24.

This reduction is not an assumed symmetry of the full graph. The checker verifies that the full density-gradient equations reduce to the displayed outer/middle equations, including native alignment links.

The complete density functional is convex: matter terms are linear densities minus positive multiples of geometric means, and the eliminated electric form is positive definite. Its interior stationary point is therefore the unique global density minimum **within the declared phase-selected matter model**.

For beta>0, the excess is strictly positive. Zero matter energy requires y=2099/4485>0, whereas zero excess field energy requires y=0; they cannot both hold. The minimizing y lies between these values. The belt moves some density toward the boundary, paying matter-deformation energy to reduce its internal field energy. Its dressed amplitudes are not exactly the original rank-one return.

For rational calculation set t=a_middle/a_outer. Its stationary equation is

    beta*n_middle*(n_outer+n_middle)*t^3
      =12(1-t)(2n_outer+n_middle*t)(2n_outer+n_middle*t^2).

The root lies in (0,1). Exact rational brackets and convex supporting tangents certify the minimum; a numerical local minimum is not substituted for a global argument.

## 6. Illustrative minima, not mass fits

With the same exterior coefficient eta=1/5:

| beta | Proton energy | Belt energy | Difference |
|---|---:|---:|---:|
| 3/5 | 0.125000000000 | 0.130377543107 | 0.005377543107 |
| 1 | 0.141666666667 | 0.150523604562 | 0.008856937895 |
| 6 | 0.350000000000 | 0.396399064627 | 0.046399064627 |

The first beta value reuses the preceding feedback fixture. None is selected from a measured mass. The exterior charge is -1 and its energy is 1/10 in every row for both carriers.

Minimizing an energy does not show that the conservative dynamics automatically relaxes there. Preparation, changes of flux sector and any dissipation require their own retained resource account.

## 7. Discriminating boundary control

Now apply another rule equally to both carriers: attach one identical lead at **every** mode vertex. The proton still has twelve leads and its minimum remains beta/24+eta/2. The belt now has eighteen.

Use the original coherent belt density as a feasible trial, with zero internal electric field and boundary flux equal to each vertex density. It satisfies the same zero-background Gauss condition. Its matter energy is zero and its electric coefficient is

    805811/26820300 < 1/24.

Therefore the belt's optimized energy is already bounded strictly below the proton's under this alternative attachment, for every beta>0. This is a rigorous feasible-energy bound, not a claimed exact alternative minimum.

The alternative changes the physical boundary rule; it is not a coordinate transformation. It demonstrates that the observed mass ordering cannot be attributed to the retained matter geometry alone. The actual field must select how the carrier is exposed to the exterior.

## 8. Status

Completed in this declared model:

- one common graph, one zero background and an admissible empty reference;
- explicit internal and exterior Gauss accounting;
- exterior and field energy retained;
- relaxed, globally certified fixed-norm sector minima;
- a boundary-attachment control that reverses the ordering.

Still missing for physical neutron mass: the field's physical identity, selected exterior attachment, energy normalization, quantum/relativistic particle interpretation, and the relation to the electron and atomic-mass reference. The orthogonal carrier sectors beyond the current selected-mode field adapter are not included in this minimization.

## Verification

    python research/voevodsky/checkers/check_open_flux_common_vacuum.py

Results: `research/voevodsky/results/open_flux_common_vacuum.json`.

The checker uses exact rational field solutions, full-graph Gauss identities, stationarity equations and energy bounds. No measured mass enters the construction.
