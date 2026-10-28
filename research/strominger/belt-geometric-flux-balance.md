# Weighted geometric balance of the current belt

## Central exchange update

L3/L3′ now use complete directed star-to-star exchange: each of the three stars sends one satellite to each opposite minority centre, in both directions (nine links per direction). Arm k feeds opposite centre k. The receipt has been regenerated for this wiring. The central gap still has vanishing twist, transverse angular transport and anisotropy within 1e-10. The separate L1′/L2′ address mismatch has now been fixed in production: star bundles use their unrotated symbolic arm addresses, while rotation remains geometric. All five gaps pass the moment and anisotropy checks; the diagnostic control now changes zero endpoints.

## Audit contract

The audit reads the existing six-layer model and all 74 directed links without changing the viewer. Each outer majority arrow supplies one flux unit; each junction splits its incoming flux equally among outgoing links. Boundary minority arrows receive the transported flux. This uniquely propagates positive steady rates through the acyclic graph.

Rates are normalized, not physical units. Multiplying all rates by four gives 48 units per direction instead of 12, without changing any cancellation or normalized anisotropy result.

Two distinct diagnostics are retained:

1. Axial node arrows: signed rates, signed position moments and unsigned transverse position second moments.
2. Straight-wire transport: each edge carries momentum proxy `q * unit(target-source)`. Across each layer gap, sum vector transport, `cross(midpoint-origin, momentum)` and transverse tangent second moments. Junction turning reactions are incoming minus outgoing momentum, including axial boundary injection/extraction.

This equal-momentum-per-flux convention is declared for the geometric test. It does not derive momentum from native fibers. No inertia, elastic stiffness, physical time evolution or dynamical no-wobble theorem is assumed.

## Conserved rates

| Layer | Rate per P arrow | Rate per E arrow | Total P/E |
|---|---:|---:|---|
| L1 | 3 | 1 | 12 / 12 |
| L2 | 12 | 4 | 12 / 12 |
| L3 | 4 | 4/3 | 12 / 12 |
| L3′ | 4/3 | 4 | 12 / 12 |
| L2′ | 4 | 12 | 12 / 12 |
| L1′ | 1 | 3 | 12 / 12 |

Every star's minority centre therefore carries three times one majority satellite's flux. Total external injection and extraction are both 24. Maximum node conservation residual is 4.45e-16. Every layer has balanced axial arrows, vanishing axial-arrow moment and isotropic transverse position second moments to tolerance 1e-10.

## Historical defect: local primed-side asymmetry

Before the fix, the first four gaps had vanishing transverse vector transport, axial/transverse angular transport and tangent second-moment anisotropy within 1e-10. L2′/L1′ instead had:

- axial angular transport: −0.02804462691;
- transverse angular-transport magnitude: 0.11936876405;
- normalized tangent eigenvalue gap: 0.01635409063 (1.6354%).

The associated layer turning moments are equal and opposite. Whole-belt net reaction and moment vanish, but that global cancellation hides the local couple. Junction turning loads also remain nonzero in otherwise balanced layers.

The asymmetry is in the outer primed connection, not in the central exchange. Star presentation retained grid-address wiring; the outer half-turn changes perimeter grouping, so primed satellites no longer consistently feed the corresponding inner-star arm.

## Correction applied and verified

An in-memory control reattaches each primed outer satellite to its matching inner star arm using the retained `arm` identity, with minority centres still attached to the inner centre. It changes 12 edge endpoints, preserving node geometry, all 74 links, directions and branch counts.

All five gaps then have angular transport and tangent anisotropy below 1e-10; every layer's net turning moment also vanishes. Axial turning loads remain, including balanced opposite-side loads. This is a positive geometric balance control, not a claim of dynamical stability. The production wiring now implements this correction and the viewer has been rebuilt. The audit receipt reflects the corrected layout. A negative-control regression deliberately reinstates the legacy rotated-grid wiring and confirms that it reproduces the defect before arm alignment removes it.

## Reproduction and evidence

- `node scripts/audit-belt-flux.mjs`
- `node --test tests/belt-flux-audit.test.mjs`
- Receipt: `results/belt-flux-audit.json`
- Implementation: `../realization-tower/belt-flux-audit.mjs`

Tests cover local conservation, exact expected rate ratios, the local/global distinction, the control, deliberately corrupted edge rates, covariance under a translated/rotated frame, and linear scaling with injected flux. No browser rebuild is required because this audit does not modify rendering or production wiring.
