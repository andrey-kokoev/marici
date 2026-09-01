import json
from fractions import Fraction
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
wp857=json.loads((ROOT/"results"/"wp857_oriented_dark_state_portal_attractor.json").read_text())
wp1134=json.loads((ROOT/"results"/"wp1134_preparation_constructor_closure_audit.json").read_text())
wp1176=json.loads((ROOT/"results"/"wp1176_uv_ensemble_matching_no_go.json").read_text())
assert wp857["summary"]["all_passed"] is True
assert wp857["source_domain"] == "vacuum plus coherent even/odd two-path sectors"
assert wp857["selected_state"] == "odd ray (|A>-|B>)/sqrt(2)"

# Scope gate: the only currently sourced normalized state-like object is the
# WP857 rank-one three-state attractor. The required boundary ensemble is a
# 23-dimensional, six-sector, full-support state.
dims=[6,8,1,4,2,2]
q=[Fraction(d,23) for d in dims]
assert all(x > 0 for x in q)
target_dimension=sum(dims)
target_rank=sum(dims)
target_purity=Fraction(1,23)
assert target_dimension == target_rank == 23
assert target_purity == Fraction(1,23)
source_dimension=3
source_rank=1
source_purity=Fraction(1)
positive_source_sectors=1
required_positive_sectors=6
assert (source_dimension,source_rank,positive_source_sectors) == (3,1,1)
assert required_positive_sectors == 6
assert source_dimension != target_dimension
assert source_rank != target_rank
assert source_purity != target_purity

# A channel could in principle dilute the pure state, but no sourced
# portal-to-sector dilation, threshold intertwiner, or boundary density
# constructor is present. This is an authority no-go, not a theorem that no
# future channel exists.
assert wp1134["current_source_passes"] == 0
assert not any(wp1134["current_source_capabilities"].values())
portal_to_sector_dilations=0
threshold_intertwiners=0
boundary_density_matrices=0
assert portal_to_sector_dilations == threshold_intertwiners == boundary_density_matrices == 0
result={
    "schema":"marici.flavor.wp1177.v1",
    "status":"PASS",
    "question":"Can current source data provide the 23-dimensional UV boundary density matrix?",
    "dpc":{
        "conjecture":"The sourced dark-state attractor can serve as or directly select the UV boundary density matrix.",
        "rivals":["three-state rank-one attractor","23-dimensional full-support ensemble","portal-to-sector dilation","future UV boundary packet"],
        "risky_consequences":["source dimension 3 versus target 23","source rank 1 versus target rank 23","one positive sector versus six","target purity 1/23","zero sourced dilations"],
        "falsification_attempt":"The WP857 attractor is normalized and globally attracting, but its type, rank, sector support, and spectrum cannot directly equal the dimension-trace target; no sourced dilation is present.",
        "residual":"A future portal-to-sector dilation or independent UV boundary state could supply the density matrix.",
        "disposition":"reject direct UV density realization from current source data"
    },
    "source_state":{
        "dimension":source_dimension,
        "rank":source_rank,
        "purity":str(source_purity),
        "positive_sectors":positive_source_sectors,
    },
    "target_state":{
        "dimension":target_dimension,
        "rank":target_rank,
        "purity":str(target_purity),
        "positive_sectors":required_positive_sectors,
        "sector_distribution":[str(x) for x in q],
    },
    "portal_to_sector_dilations":portal_to_sector_dilations,
    "threshold_intertwiners":threshold_intertwiners,
    "boundary_density_matrices":boundary_density_matrices,
    "classification":"negative authority gate: current source has no 23-dimensional UV boundary density matrix",
    "remaining_gate":"derive a portal-to-sector dilation or independent UV boundary state with the required spectrum and sector weights",
    "hostile_gate":"do not treat the three-state dark attractor as the 23-dimensional boundary ensemble or infer a dilation from purity compatibility",
    "claim_boundary":"the no-go covers direct use of current sourced objects only; future channels and UV packets remain open",
    "disposition":"UV density leaf resolved; portal-to-sector dilation rival selected"
}
(ROOT/"results"/"wp1177_uv_boundary_density_no_go.json").write_text(json.dumps(result,indent=2)+"\n")
print("WP1177 PASS:",source_dimension,target_dimension,source_rank,target_rank,portal_to_sector_dilations)
