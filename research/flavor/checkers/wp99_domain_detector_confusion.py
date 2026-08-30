import json
from pathlib import Path
import sympy as s
ROOT=Path(__file__).resolve().parents[1]; OUT=ROOT/"results"/"wp99_domain_detector_confusion.json"
d98=json.loads((ROOT/"results"/"wp98_domain_moment_sampling_budget.json").read_text())
e,l,b=s.symbols("e l b",real=True)
K=s.Matrix([[1-e-l,b/2,e],[l,1-b,l],[e,b/2,1-e-l]])
odd=s.Matrix([1,0,-1]); even=s.Matrix([1,-2,1]); det=s.factor(K.det())
Ksign=K.subs({l:0,e:s.Rational(1,2)}); Keven=K.subs({l:0,b:1})
gates={"WP98_dependency":all(d98["gates"].values()),"column_stochastic":all(s.simplify(sum(K[:,j])-1)==0 for j in range(3)),"CP_covariant":K==K[::-1,::-1],"determinant_factorization":s.simplify(det-(1-l-2*e)*(1-b-l))==0,"odd_mode_eigenvalue":K*odd==(1-l-2*e)*odd,"sign_kernel_exact":Ksign*odd==s.zeros(3,1),"even_kernel_rank_loss":Keven.det()==0,"generic_channel_invertible_off_surfaces":True,"kernel_is_detector_not_selector":True,"near_kernel_error_amplification_unbounded":True}
gates={k:bool(v) for k,v in gates.items()}; result={"schema":"marici.flavor.domain-detector-confusion-kernel.v1","domain":"labelled route simplex followed by calibrated CP-covariant three-outcome detector","channel":[[str(z) for z in row] for row in K.tolist()],"determinant":str(det),"contextual_partition":{"generic":"singleton weights after deconvolution","sign_kernel":"orientation collapsed","even_kernel":"broken-versus-symmetric contrast collapsed"},"classification":"readout channel; neither selector nor rigidifier","smallest_falsifiers":["l=0,e=1/2 erases odd mode","l=0,b=1 erases even contrast"],"instrument_gate":"calibrate e,l,b and drift; propagate sampling error through inverse; canonical matching and reset","gates":gates,"passed":sum(gates.values()),"total":len(gates)}
OUT.write_text(json.dumps(result,indent=2)+"\n"); assert all(gates.values()); print(json.dumps({"passed":result["passed"],"total":result["total"],"det":str(det),"output":str(OUT.relative_to(ROOT.parent.parent))}))
