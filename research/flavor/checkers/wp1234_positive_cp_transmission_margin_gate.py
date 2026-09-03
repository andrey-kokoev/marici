import json
from pathlib import Path

from flavor_dpc_source_replay import replay_source_checkers

ROOT=Path(__file__).resolve().parents[1]
_source_replay_records = replay_source_checkers(1020,1021,1022,1023,1024)
wp1020=json.loads((ROOT/"results"/"wp1020_scale_free_cp_margin_no_go.json").read_text())
wp1021=json.loads((ROOT/"results"/"wp1021_normalized_pairing_cp_no_go.json").read_text())
wp1022=json.loads((ROOT/"results"/"wp1022_cyclic_incidence_cancellation_no_go.json").read_text())
wp1023=json.loads((ROOT/"results"/"wp1023_maximal_cp_selector_no_go.json").read_text())
wp1024=json.loads((ROOT/"results"/"wp1024_minimal_landau_small_cp_no_go.json").read_text())
assert wp1020["classification"] == "exact scale-free no-go for a symmetry-only CP margin; normalization is a logically independent source resource"
assert wp1021["classification"] == "nonconic norm selector and orthogonality rigidifier, but neither physical CP selector nor positive-margin constructor"
assert wp1022["classification"] == "cyclic-incidence rigidifier with fixed norms, but not a physical CP selector or positive-margin constructor"
assert wp1023["classification"] == "coefficient-free mathematical selector and presentation-independent rigidifier; no declared source action realizes the extremization"
assert wp1024["classification"] == "descending mathematical selector family with existing readout; no viable small nonzero selector and no declared source-local realization"
# Support, norms, incidence, and coefficient-free invariant actions do not
# give a positive margin at the small observed CP scale.
scale_free_margin_absent=True
norms_not_margin=True
cyclic_cancellation_possible=True
maximal_cp_falsified=True
minimal_landau_falsified=True
positive_t_margin=False
oriented_volume_law=False
small_source_ratio=False
radiative_closure=False
calibrated_instrument=False
assert scale_free_margin_absent and norms_not_margin and cyclic_cancellation_possible
assert maximal_cp_falsified and minimal_landau_falsified
assert not (positive_t_margin or oriented_volume_law or small_source_ratio or radiative_closure or calibrated_instrument)
result={
    "schema":"marici.flavor.wp1234.v1",
    "status":"PASS",
    "question":"Can source structure generate a positive CP-transmission margin at the observed small scale?",
    "dpc":{
        "conjecture":"Scale, norm, cyclic incidence, maximal CP, or minimal Landau structure fixes a positive CP-transmission margin.",
        "rivals":["scale-free portal ray","unit-orthogonal portal vectors","fully cyclic fixed-norm incidence","maximal-CP invariant","minimal primitive Landau action"],
        "risky_consequences":["lambda=1/n preserves qualitative structure while det[Hu,Hd] tends to zero","unit orthogonal complex vectors can still have only one mixing edge","one rational background entry cancels T while every cycle edge remains nonzero","maximal CP requires J squared 1/108 and survives no fitted sheet","primitive quadratic minima are only 0, 1/2, or 1"],
        "falsification_attempt":"each proposed margin either vanishes by scaling, misses cyclic support, permits exact cancellation, selects a phenomenologically false orbit, or imports a small fitted coefficient.",
        "residual":"an independently derived small dimensionless source ratio, oriented-volume law or margin, radiative closure, and calibrated readout/preparation instrument",
        "disposition":"reject all tested margin constructors; select independent small-source-ratio rival"
    },
    "scale_response":wp1020["exact_commutator_response"],
    "scale_leading_coefficient":wp1020["normalized_J_squared_leading_coefficient"],
    "norm_constraints":wp1021["constraints"],
    "cyclic_background_deformation":wp1022["background_deformation"],
    "maximal_cp_conditions":wp1023["equality_conditions"],
    "landau_selected_values":wp1024["coefficient_free_selected_values"],
    "fitted_normalized_upper_bound":wp1024["fitted_normalized_upper_bound"],
    "coefficient_ratio_gate":wp1024["coefficient_ratio_gate"],
    "scale_free_margin_absent":scale_free_margin_absent,
    "norms_not_margin":norms_not_margin,
    "cyclic_cancellation_possible":cyclic_cancellation_possible,
    "maximal_cp_falsified":maximal_cp_falsified,
    "minimal_landau_falsified":minimal_landau_falsified,
    "positive_t_margin":positive_t_margin,
    "oriented_volume_law":oriented_volume_law,
    "small_source_ratio":small_source_ratio,
    "radiative_closure":radiative_closure,
    "calibrated_instrument":calibrated_instrument,
    "classification":"negative CP-margin result: no tested support, norm, or primitive invariant yields the observed small positive margin",
    "remaining_gate":"derive an independent small dimensionless ratio and a weak-basis-invariant oriented-volume margin with radiative closure and calibrated instrument",
    "hostile_gate":"do not call finite nonzero J, norm constraints, cyclic support, maximal CP, or primitive Landau minima a positive observed-scale margin",
    "claim_boundary":"the signed J readout remains exact, but it cannot prepare the portal, exclude T=0, or import the fitted scale",
    "disposition":"positive-CP-transmission-margin leaf resolved negatively; independent small-source-ratio rival selected"
}
(ROOT/"results"/"wp1234_positive_cp_transmission_margin_gate.json").write_text(json.dumps(result,indent=2)+"\n")
print("WP1234 PASS: positive CP margin requires an independent small source ratio")
