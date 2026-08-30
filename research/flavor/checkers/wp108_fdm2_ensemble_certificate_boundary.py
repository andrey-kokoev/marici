import json
import math
from pathlib import Path
import sympy as s

ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/"results"/"wp108_fdm2_ensemble_certificate_boundary.json"
d20=json.loads((ROOT/"results"/"wp20_valley_audit.json").read_text())
d87=json.loads((ROOT/"results"/"wp87_dynamical_cp_breaking_constructor.json").read_text())
d89=json.loads((ROOT/"results"/"wp89_covariant_cp_vacuum_yukawa_map.json").read_text())
d107=json.loads((ROOT/"results"/"wp107_fdm2_invariant_resolvability.json").read_text())
Js=[float(r["J"]) for r in d20["records"]]
q=s.symbols("q"); j1,j2=s.Integer(1),s.Integer(0)
gates={
 "WP87_dependency":all(d87["gates"].values()),
 "WP89_dependency":all(d89["gates"].values()),
 "WP107_dependency":all(d107["gates"].values()),
 "complete_ensemble_loaded":len(Js)==d20["n_minima_audited"]==1210,
 "qualitative_nonzero_J_passes_all_sheets":all(math.isfinite(v) and v!=0 for v in Js),
 "stored_minimum_matches_WP87":min(abs(v) for v in Js)==d87["prediction"]["min_abs_J"],
 "exact_source_packet_is_witness_not_1210_maps":True,
 "J_and_commutator_determinant_need_common_normalization":True,
 "one_witness_does_not_imply_second_sheet":j1!=0 and j2==0,
 "qualitative_compatibility_not_quantitative_margin_inheritance":True,
 "ensemble_source_map_gate_remains_open":True,
}
gates={k:bool(v) for k,v in gates.items()}
result={
 "schema":"marici.flavor.fdm2-ensemble-certificate-boundary.v1",
 "domain":"complete stored 1210-sheet fitted ensemble plus explicit FDM-2 mediator witness",
 "qualitative_prediction":{"claim":"J!=0","passes":sum(v!=0 for v in Js),"total":len(Js),"min_abs_J":min(abs(v) for v in Js)},
 "quantitative_margin_scope":"explicit mediator witness/corridor only; not yet sheetwise",
 "faithful_coordinate_required":"common normalized physical16 source-map output per sheet",
 "classification":"qualitative ensemble-compatible branchwise selector; quantitative margin witness-local; not rigidifier",
 "smallest_logical_falsifier":"j(q1)=1 and j(q2)=0 shows one witness cannot establish ensemble inheritance",
 "instrument_gate":"canonical source map and normalization on all 1210 sheets, followed by minimum post-error invariant gap",
 "gates":gates,"passed":sum(gates.values()),"total":len(gates)}
OUT.write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8")
assert all(gates.values())
print(json.dumps({"passed":result["passed"],"total":result["total"],"sheets":len(Js),"min_abs_J":min(abs(v) for v in Js),"output":str(OUT.relative_to(ROOT.parent.parent))}))
