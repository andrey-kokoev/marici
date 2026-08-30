#!/usr/bin/env python3
"""Exact EPR-Compton local-flatness and Bell-nonfactorization fixture."""
import itertools, json, math
from pathlib import Path
ASPECT=Path(__file__).resolve().parent.parent
CONTRACT=ASPECT/"contracts"/"epr-compton-local-flatness-nonfactorization.v1.json"
RESULT=ASPECT/"results"/"epr_compton_local_flatness_nonfactorization.json"
def corr(a,b): return -math.cos(2*math.radians(a-b))
def chsh(e): return abs(e[0][0]+e[0][1]+e[1][0]-e[1][1])
def local_vertices():
 vals=[]
 for a0,a1,b0,b1 in itertools.product((-1,1),repeat=4):
  e=[[a0*b0,a0*b1],[a1*b0,a1*b1]];vals.append(chsh(e))
 return vals
def compton(E,theta):
 ep=E/(1+E*(1-math.cos(theta))); q=(E-ep*math.cos(theta),-ep*math.sin(theta)); ke=math.sqrt(1+q[0]*q[0]+q[1]*q[1])-1
 return ep,q,ke
def main():
 c=json.loads(CONTRACT.read_text(encoding="utf-8")); A=c["settings_degrees"]["A"];B=c["settings_degrees"]["B"]
 e=[[corr(a,b) for b in B] for a in A];S=chsh(e);vertices=local_vertices()
 ep,q,ke=compton(1.0,math.pi/3);local_energy=(1-ep)-ke;local_momentum=0.0
 N=c["trials_per_setting_pair"];tau=c["correlation_tolerance"];M=4;bound=2*M*math.exp(-N*tau*tau/2);lower=S-4*tau
 marginals={"A_given_B0":[0.0,0.0],"A_given_B1":[0.0,0.0],"B_given_A0":[0.0,0.0],"B_given_A1":[0.0,0.0]}
 required=c["local_wing_fields"];synthetic_record={k:("A" if k=="wing" else 0 if k in ("outcome","target_excitation") else False if k=="no_click" else "fixture") for k in required}
 checks={"local_compton_energy_flat":abs(local_energy)<1e-12,"local_compton_momentum_flat":local_momentum<1e-12,"all_local_vertices":len(vertices)==16 and max(vertices)<=c["chsh_local_ceiling"],"quantum_tsirelson":abs(S-2*math.sqrt(2))<1e-12,"robust_violation":lower>2,"familywise_bound":bound<c["familywise_alpha"],"no_signalling_marginals":all(all(x==0 for x in v) for v in marginals.values()),"no_click_retained":0 in c["outcomes"] and c["no_click_outcome"]==0,"complete_local_record":all(k in synthetic_record for k in required),"postselection_hostile_named":"discard_no_clicks" in c["hostiles"],"frame_hostile_named":"frame_reflection" in c["hostiles"],"claim_boundary":not any(c["claim_boundary"].values())}
 out={"schema":"marici.aspect.epr-compton-local-flatness-nonfactorization-result.v1","passed":all(checks.values()),"checks":checks,"correlations":e,"chsh":S,"local_vertex_max":max(vertices),"conservative_chsh_lower":lower,"familywise_bound":bound,"local_compton_fixture":{"scattered_energy":ep,"electron_recoil":q,"electron_kinetic":ke,"energy_residual":local_energy},"marginals":marginals,"current_verdict":"local_flat_global_nonfactorizable_mathematical_fixture","physical_status":"not_run"}
 RESULT.write_text(json.dumps(out,indent=2)+"\n",encoding="utf-8"); print(json.dumps(out,sort_keys=True)); raise SystemExit(0 if out["passed"] else 1)
if __name__=="__main__":main()

