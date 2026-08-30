import json
from pathlib import Path
import sympy as sp

ROOT=Path(__file__).resolve().parents[1]
wp507=json.loads((ROOT/"results"/"wp507_complete_gauge_gram_rank.json").read_text())
wp772=json.loads((ROOT/"results"/"wp772_su4_gauge_link_boundary_normalization_fiber.json").read_text())
wp773=json.loads((ROOT/"results"/"wp773_su4_localization_normalization_trilemma.json").read_text())
wp775=json.loads((ROOT/"results"/"wp775_su6_anomaly_family_spectral_generation_gate.json").read_text())
assert wp507["passed"] and wp772["status"]=="PASS"
assert wp773["status"]=="PASS" and wp775["status"]=="PASS"

g2,gy,v2=sp.symbols("g2 gy v2",positive=True)
ew=v2*sp.Matrix([
 [g2**2/4,0,0,0],[0,g2**2/4,0,0],
 [0,0,g2**2/4,-g2*gy/4],[0,0,-g2*gy/4,gy**2/4]])
eigs=ew.eigenvals()
nonzero=set(x for x in eigs if x!=0)
expected={g2**2*v2/4,v2*(g2**2+gy**2)/4}
assert nonzero==expected
splitting=sp.factor(v2*(g2**2+gy**2)/4-g2**2*v2/4)
assert splitting==gy**2*v2/4
assert splitting>0

seventeens={
 "WP507 complete gauge tangent Gram":"rank",
 "WP468 common-dilaton Hessian":"rank at a frozen benchmark",
 "WP635 charged messenger incidence":"field-label count",
 "WP772 SU(4) half-twist packet":"spectral index",
 "WP773 boundary localization branch":"spectral index",
 "WP775 two-bulk-family branch":"negative spectral index",
}
assert len(seventeens)==6

# Deliberate obstruction: rank only counts support. The visible electroweak
# subblock already contains unequal positive eigenvalues, so it cannot be the
# equal-norm projector required by M^2=17 f^2.
assert wp507["tangent_gram"]["rank"]==17
assert len(nonzero)==2

result={
 "schema":"marici.flavor.wp1029.v1","status":"PASS",
 "question":"Does an independently derived source seventeen realize the equal-norm mass constructor required by WP1028?",
 "source_seventeen_inventory":seventeens,
 "independent_seventeen_objects":len(seventeens),
 "typed_mass_norm_interfaces":0,
 "closest_candidate":"WP507 rank-17 complete gauge tangent Gram",
 "electroweak_positive_eigenvalue_classes":[str(x) for x in sorted(nonzero,key=str)],
 "exact_nonzero_splitting":str(splitting),
 "classification":"all seventeens are differently typed; gauge rank is a support rigidifier and fails the equal-norm condition, so none derives M^2=17 f^2",
 "smallest_exact_falsifier":"inside WP507 alone, the neutral and charged electroweak mass-Gram eigenvalues differ by gy^2*v^2/4",
 "instrument":"WP507 has no pole instrument, and no admitted source object couples its rank or spectral index to the WP90 messenger mass",
 "claim_boundary":"bounded inventory of six existing exact seventeens; does not exclude a new representation whose canonical mass Gram is a rank-17 projector",
 "disposition":"negative: WP1028 remains a data-compatible normal form, not a lifted source theorem"
}
(ROOT/"results"/"wp1029_source_seventeen_type_audit.json").write_text(
 json.dumps(result,indent=2)+"\n")
print("WP1029 PASS: six seventeens, zero interfaces, splitting",splitting)
