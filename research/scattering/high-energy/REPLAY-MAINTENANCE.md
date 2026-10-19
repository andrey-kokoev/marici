# Replay and maintenance

## Durable source cache

`results/scattering-replay-cache.v1.zip` preserves 709 source/cache assets from the H6/H7 reconstruction, including raw fields, frames, model cache, source scripts and the inspected radial-source copy. `results/scattering-replay-cache.v1.json` records the archive SHA-256 and every member SHA-256. This is a local repository artifact, not evidence of remote backup or publication.

Verify all members:

    python research/scattering/high-energy/preserve_replay_cache.py check

Restore missing scratch assets (existing differing files are refused):

    python research/scattering/high-energy/preserve_replay_cache.py restore

The machine-specific engine_path.txt is normalized to the restored repository. No scientific receipt currently binds that locator. The other scratch paths remain stable for compatibility; deletion is now recoverable without rerunning the stationary solve. Preserve the ZIP and manifest together when moving/backing up the repository. A full operator/inverse certificate is not contained in the cache.

## Complete receipt checks

The H6 quadrature review and three H7 follow-up checkers now compare **every** freshly computed receipt field. Dictionaries, list shapes, strings, integers, flags and hashes must match exactly; finite floating diagnostics use rtol=1e-8, atol=1e-10. These accommodate replay-level floating variation, not proof-level error. The shared comparator is itself source-hash-bound. Missing assets and stale hashes fail rather than silently downgrade a check.

Run in dependency order, with NumPy/SciPy available:

    python research/scattering/high-energy/check_quadrature_review.py --check
    uv run --with numpy --with python-flint python research/scattering/high-energy/check_peak_enclosure.py --check
    uv run --with numpy --with python-flint python research/scattering/high-energy/check_readout_enclosures.py --check
    uv run --with numpy --with scipy --with python-flint python research/scattering/high-energy/check_preparation_enclosure.py --check
    uv run --with numpy --with python-flint python research/scattering/high-energy/check_prepared_readouts.py --check
    python research/scattering/high-energy/check_finite_preconditioner.py --check
    python research/scattering/high-energy/check_polynomial_preconditioner.py --check
    python research/scattering/high-energy/check_verified_factor_controls.py --check
    python research/scattering/high-energy/check_verified_d_blocks.py --check
    python research/scattering/high-energy/check_verified_inverse_factor.py --check
    python research/scattering/high-energy/check_verified_binary_inertia.py --check
    uv run --with numpy --with python-flint python research/scattering/high-energy/check_exact_pose_reference.py --check
    python research/scattering/high-energy/check_ground_frame_bridge.py --check
    python research/scattering/high-energy/check_terminal_assembly.py --check
    python research/scattering/high-energy/check_native_geometry_bridge.py --check
    python research/scattering/high-energy/check_exact_vertex_bridge.py --check
    python research/scattering/high-energy/check_corrected_native_leakage.py --check
    python research/scattering/high-energy/check_radial_envelope.py --check
    python research/scattering/high-energy/check_corrected_matching_residual.py --check
    python research/scattering/high-energy/check_inertia_margin.py --check
    python research/scattering/high-energy/check_inertia_thresholds.py --check
    python research/scattering/high-energy/check_inertia_roundoff_screen.py --check
    python research/scattering/high-energy/check_inverse_factor_reconstruction.py --check
    uv run --with numpy --with scipy --with sympy --with threadpoolctl --with python-flint python research/scattering/high-energy/check_ball_factor_residual.py --check
    python research/scattering/high-energy/check_resolvent_certificate.py --check
    python research/scattering/high-energy/check_high_energy_net_v2.py --check

The net validator checks receipt/source bindings and dispositions; it does not replace the raw replay or analytic proof review.

## H6 budget

The six-cycle H6 attempt is exhausted: localization, readouts, preparation, propagation, preconditioner and polynomial screening. Outcome: inconclusive; final 0.05/0.02/0.93 forecast is historical. Prepared stored-kernel comparisons remain certified, but solver/kernel/reference bounds require a costed successor using a different approach. Active cost/forecast are unknown; no budget is automatically renewed. H7's budget is not renewed.

## H7 budget

The original eight-cycle attempt is exhausted: three native/norm/matching cycles and five inertia-margin, threshold-search, roundoff-screen, inverse-reconstruction and ball-factor cycles. Outcome: inconclusive. The final 0.05/0.05/0.90 forecast is historical, not active ranking evidence. Factor residual is now ball-enclosed only for the binary reference; the remaining source/frame/inverse obligations require an explicitly specified and costed successor. No budget is automatically renewed.

### Explicit successor VB1

VB1 has an explicit two-cycle allowance; one spent on exact radical vertex/centering propagation, one remains for ground/frame coverage audit or pilot. The pinned geometry input is preserved in results/source-geometry.v1.json. Forecast 0.00/0.01/0.99 concerns full H7, not the successful exact native assembly subgate. Ground/frame and coupled inverse remain uncertified; prior budgets stay exhausted.

### Explicit successor AB1

AB1's two cycles are exhausted (terminal assembly and native geometry enclosure). Full-H7 outcome is inconclusive; final 0.00/0.01/0.99 forecast is historical. Samples and centered vertices/Pauli constants are durably preserved. Native/terminal assembly is certified on those binary vertices; upstream vertex/centering reference, frame and coupled inverse remain missing. Active successor cost/forecast are unknown; no budgets renewed.

### Explicit successor RB1

RB1's two cycles are exhausted (exact pose transfer and source/frame audit with binary eigenpair proximity). Full-H7 outcome: inconclusive; 0.00/0.01/0.99 forecast is historical. Source assembly, ground identity/frame and coupled inverse remain uncertified. Active successor cost/forecast are unknown; neither RB1 nor VF1 is renewed.

### Explicit successor VF1

VF1 is separately specified in H7-VERIFIED-FACTOR-SUCCESSOR.md, with three execution cycles now exhausted. Final 0.01/0.02/0.97 forecast is historical; the full-H7 outcome is inconclusive. The frontier has been resumed to certify all 49 inverse rows and link the factor residual: full binary shifted native inertia is certified. Source/frame and full-band coupled inverse still need a costed successor, so active H7 cost/forecast are unknown. All 49 binary D-block inertias/separations are now certified; their factor/eigenframe witness is preserved in results/verified-factor-witness.v1.npz. The design/control-validation turn is recorded separately. Only verified subgate progress is expected; it cannot promote H7. The original eight-cycle record remains exhausted. H6's successor remains unspecified. Maintenance does not restart the budget. These numbers are planning judgments, not calibrated probabilities of mathematical truth.
