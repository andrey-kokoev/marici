# Synthetic reuse assessment for radial bulk/Wilson coordinates

## Boundary

Both candidate families are reusable only as synthetic transport scaffolds. Neither supplies a source-derived map into radial bulk fields or Wilson coordinates, physical calibration, or quotient authority.

## Comparison-loop hardware binding and pushforward packet

Reusable fields:

- **Record map:** `run_id`, `compiler_id`, `coincidence_window_id`, per-event `event_id`, settings, outcomes, no-click flags, `time_tag`, setting-health flags, photon/electron bins, target classes, local frames, and `reset_id`.
- **Provenance:** the explicit `local_a`/`local_b` field lists, run/compiler/window identifiers, and `status=synthetic_reference`.
- **Uncertainty scaffold:** `rotation_systematic`, `terminal_phase`, `differential_loss`, `statistical_quadrature`, `total_fringe`, measured-angle/phase standard-error field declarations, and the stated additive error-bound derivation.
- **Units:** only discrete/index-like coordinates and dimensionless outcomes are safely reusable; `time_tag`, angle, phase, and loss have no complete unit declaration in the packet.
- **Covariance:** not supplied. Scalar error budgets and standard-error field names are not a covariance matrix or kernel.
- **Admitted quotient:** none. Coincidence windows, bins, reset grouping, and local A/B provenance are record partitions, not authorized equivalence relations.

Missing map: a typed, source-derived pushforward from these event records to a radial bulk field and Wilson observable, including event-to-radial-coordinate assignment, frame/gauge transport, unit conversion, covariance pushforward, and proof that any binning/coincidence quotient preserves the target observable.

## Optical pair stiffness/flux cell

Reusable fields:

- **Record/configuration map:** node count; TDGL-with-Peierls-phase equation label; `dt`, settling and measurement steps; deterministic seed; pair, stiffness, flux, transport, and environment port names; fixture parameters and expected synthetic classifications.
- **Provenance:** fixture IDs, seed, model label, and explicit claim boundary `dimensionless_optical_analogue_not_material_superconductivity`.
- **Units:** the noise and loop flux are explicitly synthetic/dimensionless. They cannot be interpreted as kelvin, magnetic flux, energy, or radial length.
- **Uncertainty scaffold:** fixture-level scalar `noise` and `loss_monitor` port. No covariance law, bath spectrum, cross-port covariance, or uncertainty pushforward is present.
- **Admitted quotient:** none. Winding sectors and loop closure do not authorize gauge quotienting by themselves.

Missing map: a typed comparison from the discrete complex ring field and Peierls twist to the proposed radial bulk field, plus a Wilson-coordinate map from synthetic loop flux/phase winding to a declared holonomy. It must specify lattice-to-radial interpolation, gauge group/action, orientation, normalization, continuum or retained-lattice status, covariance/noise transport, and the equivalence relation under which the Wilson observable descends.

## Exact reusable composite

A safe synthetic composite may reuse:

1. the hardware packet as an event/provenance envelope;
2. the comparison-loop budget as scalar tolerance metadata;
3. the optical fixture as a dimensionless synthetic field/loop generator;
4. a new explicit adapter slot whose output type is `unbound_radial_bulk_wilson_candidate`.

The adapter must remain empty until the record-to-bulk map and loop-to-Wilson map above are supplied. Calibration authority, physical binding, covariance, units conversion, and quotient descent all remain null. No RH, material, or hardware claim follows.
