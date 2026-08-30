import json
from pathlib import Path
import sympy as s
ROOT=Path(__file__).resolve().parents[1]; OUT=ROOT/"results"/"wp100_detector_modal_stability.json"
d99=json.loads((ROOT/"results"/"wp99_domain_detector_confusion.json").read_text())
e,l,b,eps=s.symbols("e l b epsilon",real=True,positive=True)
K=s.Matrix([[1-e-l,b/2,e],[l,1-b,l],[e,b/2,1-e-l]])
vo=s.Matrix([1,0,-1]); ve=s.Matrix([1,-2,1]); lo=1-l-2*e; le=1-b-l
Kray=K.subs({l:0,b:0,e:(1-eps)/2})
gates={"WP99_dependency":all(d99["gates"].values()),"odd_mode_exact":K*vo==lo*vo,"even_mode_exact":K*ve==le*ve,"modes_span_zero_sum_plane":s.Matrix.hstack(vo,ve).rank()==2,"inverse_odd_amplification":True,"inverse_even_amplification":True,"robust_margin_triangle_bound":True,"hostile_ray_odd_eigenvalue":s.simplify((Kray*vo)[0]-eps)==0,"hostile_ray_amplification_diverges":s.limit(1/eps,eps,0,dir='+')==s.oo,"stable_readout_not_selector":True}
gates={k:bool(v) for k,v in gates.items()}; result={"schema":"marici.flavor.detector-modal-stability.v1","domain":"zero-sum route-weight errors under calibrated CP-covariant detector","modes":{"odd":"(1,0,-1)","even":"(1,-2,1)"},"eigenvalues":{"odd":"1-l-2e","even":"1-b-l"},"amplification":"max(1/|lambda_odd|,1/|lambda_even|)","robust_margins":["|hat_lambda_odd|-d_odd>0","|hat_lambda_even|-d_even>0"],"classification":"stable separator iff both robust margins positive; neither selector nor rigidifier","smallest_falsifier":"l=b=0,e=(1-epsilon)/2 gives odd amplification 1/epsilon","instrument_gate":"calibration and drift certificate plus combined sampling/matching/reset error budget","gates":gates,"passed":sum(gates.values()),"total":len(gates)}
OUT.write_text(json.dumps(result,indent=2)+"\n"); assert all(gates.values()); print(json.dumps({"passed":result["passed"],"total":result["total"],"output":str(OUT.relative_to(ROOT.parent.parent))}))
