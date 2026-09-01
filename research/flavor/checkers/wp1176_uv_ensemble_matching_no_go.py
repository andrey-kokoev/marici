import json
from fractions import Fraction
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
wp1133=json.loads((ROOT/"results"/"wp1133_uv_boundary_state_matching_no_go.json").read_text())
assert wp1133["boundary_density_matrices"] == 0
assert wp1133["state_matching_maps"] == 0
assert wp1133["microstate_uniformity_proofs"] == 0

dims=[6,8,1,4,2,2]
q=[Fraction(d,23) for d in dims]
# General block state rho=oplus_b rho_b with Tr rho_b=q_b. Within each block,
# the conditional state has d_b^2-1 real parameters, independently of its
# fixed trace. The sector-weight fiber therefore has dimension 119.
fiber_dimension=sum(d*d-1 for d in dims)
assert fiber_dimension == 119
uniform_blocks=[Fraction(1,23) for d in dims]

# Explicit same-sector nonuniform alternative in the eight-dimensional block:
# shift two microstate eigenvalues by +/-epsilon around 1/23 while preserving
# positivity and block trace q_1=8/23. Other blocks retain the uniform value.
epsilon=Fraction(1,1000)
nonuniform_eight=[Fraction(1,23)+epsilon,Fraction(1,23)-epsilon]+[Fraction(1,23)]*6
assert sum(nonuniform_eight) == q[1]
assert all(x > 0 for x in nonuniform_eight)
assert nonuniform_eight != [Fraction(1,23)]*8
same_sector_distribution=True
microstate_uniformity_forced=False
boundary_state_available=False
assert same_sector_distribution and not microstate_uniformity_forced
assert not boundary_state_available
result={
    "schema":"marici.flavor.wp1176.v1",
    "status":"PASS",
    "question":"Can UV ensemble matching derive the dimension-trace state and microstate uniformity?",
    "dpc":{
        "conjecture":"Matching the sector distribution q derives the dimension-trace state.",
        "rivals":["normalized boundary state","sector-weight matching","uniform microstate state","119-dimensional density fiber"],
        "risky_consequences":["no boundary density matrix","sector weights q=d/23","general block-state fiber dimension 119","explicit nonuniform same-sector state"],
        "falsification_attempt":"WP1133 has zero boundary states and matching maps; even with q fixed, an eight-sector state can shift two eigenvalues by +/-1/1000 without changing sector weight.",
        "residual":"A boundary density matrix, trace functional, matching map, and uniformity law all remain absent.",
        "disposition":"reject UV ensemble matching for current source data"
    },
    "sector_dimensions":dims,
    "sector_distribution":[str(x) for x in q],
    "density_fiber_dimension":fiber_dimension,
    "uniform_microstate_eigenvalue":str(Fraction(1,23)),
    "explicit_nonuniform_eight_block":[str(x) for x in nonuniform_eight],
    "same_sector_distribution":same_sector_distribution,
    "microstate_uniformity_forced":microstate_uniformity_forced,
    "boundary_state_available":boundary_state_available,
    "classification":"negative identifiability gate: sector matching does not derive dimension-trace microstate uniformity",
    "remaining_gate":"derive a normalized UV boundary density matrix and its block-uniformity law",
    "hostile_gate":"do not infer rho=oplus I_db/23 from sector probabilities alone",
    "claim_boundary":"the no-go covers current source authority and q-only matching, not a future UV state with a uniformity proof",
    "disposition":"UV ensemble matching leaf resolved; boundary-density rival selected"
}
(ROOT/"results"/"wp1176_uv_ensemble_matching_no_go.json").write_text(json.dumps(result,indent=2)+"\n")
print("WP1176 PASS:",fiber_dimension,same_sector_distribution,microstate_uniformity_forced)
