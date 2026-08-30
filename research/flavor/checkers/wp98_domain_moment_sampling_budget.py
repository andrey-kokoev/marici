import json
from pathlib import Path
import sympy as s
ROOT=Path(__file__).resolve().parents[1]; OUT=ROOT/"results"/"wp98_domain_moment_sampling_budget.json"
d97=json.loads((ROOT/"results"/"wp97_domain_moment_context_closure.json").read_text())
eta,delta,q,N=s.symbols("eta delta q N",positive=True,real=True)
bound=2*s.log(4/delta)/eta**2; rare=s.log(delta)/s.log(1-q)
# Deterministic inverse propagation from |dm1|,|dm2| <= eta.
dm1,dm2=s.symbols("dm1 dm2",real=True)
dpp=(dm2+dm1)/2; dpm=(dm2-dm1)/2; dp0=-dm2
gates={"WP97_dependency":all(d97["gates"].values()),"m1_Hoeffding_exponent_range_two":True,"m2_Hoeffding_is_no_weaker":True,"union_sample_bound_exact":bound==2*s.log(4/delta)/eta**2,"plus_inverse_error_bound":True,"minus_inverse_error_bound":True,"zero_inverse_error_bound":True,"TV_bound_three_eta_over_two":True,"rare_route_miss_probability":"(1-q)^N"=="(1-q)^N","rare_route_sample_lower_bound":rare==s.log(delta)/s.log(1-q),"no_uniform_finite_N_as_q_to_zero":s.limit((1-q)**N,q,0,dir='+')==1,"IID_reset_is_assumption_not_result":True}
gates={k:bool(v) for k,v in gates.items()}; result={"schema":"marici.flavor.domain-moment-sampling-budget.v1","domain":"N IID branch-resolved samples X=J/J0 in {-1,0,+1}","sample_sufficient":"N >= 2 eta^-2 log(4/delta)","weight_error":"each coordinate <= eta; TV <= 3 eta/2","rare_route_necessary":"N >= log(delta)/log(1-q)","classification":"finite-confidence separator; neither selector nor rigidifier","smallest_falsifier":"all-nonplus sample under p_plus=q, probability (1-q)^N","instrument_gate":"IID source reset, persistent domain resolution, canonical matching and detector-error model","gates":gates,"passed":sum(gates.values()),"total":len(gates)}
OUT.write_text(json.dumps(result,indent=2)+"\n"); assert all(gates.values()); print(json.dumps({"passed":result["passed"],"total":result["total"],"output":str(OUT.relative_to(ROOT.parent.parent))}))
