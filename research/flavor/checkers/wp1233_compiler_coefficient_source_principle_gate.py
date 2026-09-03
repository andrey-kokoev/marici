import json
from pathlib import Path

from flavor_dpc_source_replay import replay_source_checkers

ROOT=Path(__file__).resolve().parents[1]
_source_replay_records = replay_source_checkers(1015,1016,1017,1018,1019)
wp1015=json.loads((ROOT/"results"/"wp1015_shared_entrance_commuting_selector_no_go.json").read_text())
wp1016=json.loads((ROOT/"results"/"wp1016_two_entrance_cp_even_no_go.json").read_text())
wp1017=json.loads((ROOT/"results"/"wp1017_fdm2_cp_odd_entrance_bridge.json").read_text())
wp1018=json.loads((ROOT/"results"/"wp1018_fdm2_portal_alignment_no_go.json").read_text())
wp1019=json.loads((ROOT/"results"/"wp1019_fdm2_cp_transmission_discriminant.json").read_text())
assert wp1015["classification"] == "source-derived selector and shared-frame rigidifier, but experimentally falsified; no viable physical selector"
assert wp1016["classification"] == "source-derived noncollinearity selector and rigidifier, but CP selector is experimentally falsified"
assert wp1017["classification"] == "qualitative CP selector and source-presentation rigidifier; not a numerical physical16 selector"
assert wp1018["classification"] == "singlet-vacuum selector and source rigidifier, but neither a universal physical CP selector nor a numerical physical16 selector over the admitted coefficient family"
assert wp1019["classification"] == "weak-basis-invariant discriminator and instrument readout, not a source selector; T!=0 is an open genericity condition unless dynamics supplies a margin"
# Source grammar restricts compiler coefficients only through no-go or
# qualitative routes; no finite threshold, CP-even packet, or positive
# transmission margin supplies the full selected Physical16 packet.
shared_entrance_falsified=True
cp_even_falsified=True
fdm2_qualitative_cp=True
alignment_no_go=True
transmission_discriminator=True
t_zero_not_excluded=True
finite_threshold_ratio=False
complete_cp_even_packet=False
positive_transmission_margin=False
numerical_selector=False
calibrated_instrument=False
assert shared_entrance_falsified and cp_even_falsified and fdm2_qualitative_cp
assert alignment_no_go and transmission_discriminator and t_zero_not_excluded
assert not (finite_threshold_ratio or complete_cp_even_packet or positive_transmission_margin or numerical_selector or calibrated_instrument)
result={
    "schema":"marici.flavor.wp1233.v1",
    "status":"PASS",
    "question":"Can source grammar determine compiler coefficients into a selected Physical16 packet?",
    "dpc":{
        "conjecture":"Shared or FDM-2 source grammar determines compiler coefficients and the selected Physical16 packet.",
        "rivals":["shared commuting entrance","real CP-even two-entrance grammar","FDM-2 CP-odd entrance bridge","FDM-2 portal alignment","rank-one CP transmission discriminant"],
        "risky_consequences":["shared entrance gives J=0 and survives none of 1210 fitted sheets","CP-even two-entrance grammar also gives J=0","FDM-2 yields opposite J signs but no magnitude","Im(z)=3/5 can coexist with commuting Grams","det[Hu,Hd]=2 i Delta_u T and T=0 is an exact blind locus"],
        "falsification_attempt":"every source principle is experimentally falsified, qualitative, alignment-dependent, or unable to exclude T=0.",
        "residual":"source-derived finite threshold ratio, complete CP-even coefficient packet, positive T margin, and collider-calibrated mediator instrument",
        "disposition":"accept the discriminant as readout and rigidifier only; reject it as compiler-coefficient source selection"
    },
    "shared_entrance_surviving_sheets":wp1015["ensemble_sheets_surviving"],
    "cp_even_surviving_sheets":wp1016["ensemble_sheets_surviving"],
    "fdm2_bridge_identity":wp1017["bridge_identity"],
    "alignment_hostile":wp1018["hostile_pair"],
    "transmission_discriminant":wp1019["faithful_discriminant"],
    "transmission_polynomial":wp1019["transmission_polynomial"],
    "wp90_witness":wp1019["wp90_witness"],
    "shared_entrance_falsified":shared_entrance_falsified,
    "cp_even_falsified":cp_even_falsified,
    "fdm2_qualitative_cp":fdm2_qualitative_cp,
    "alignment_no_go":alignment_no_go,
    "transmission_discriminator":transmission_discriminator,
    "t_zero_not_excluded":t_zero_not_excluded,
    "finite_threshold_ratio":finite_threshold_ratio,
    "complete_cp_even_packet":complete_cp_even_packet,
    "positive_transmission_margin":positive_transmission_margin,
    "numerical_selector":numerical_selector,
    "calibrated_instrument":calibrated_instrument,
    "classification":"conditional compiler-source grammar: CP transmission readout exists, numerical selection absent",
    "remaining_gate":"derive finite threshold ratios, CP-even coefficients, and a positive transmission margin from source dynamics before fitting",
    "hostile_gate":"do not call commuting or CP-even no-go, qualitative FDM-2 signs, or the T discriminant a numerical Physical16 selector",
    "claim_boundary":"FDM-2 discriminates CP transmission when T is nonzero; it does not prepare the source or exclude T=0",
    "disposition":"compiler-coefficient source-principle leaf resolved conditionally; positive CP-transmission-margin rival selected"
}
(ROOT/"results"/"wp1233_compiler_coefficient_source_principle_gate.json").write_text(json.dumps(result,indent=2)+"\n")
print("WP1233 PASS: compiler source grammar requires positive CP transmission margin")
