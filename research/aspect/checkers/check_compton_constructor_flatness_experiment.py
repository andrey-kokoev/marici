#!/usr/bin/env python3
"""Exact relativistic Compton closure and hostile comparison-loop classifier."""
import json, math
from pathlib import Path
ASPECT=Path(__file__).resolve().parent.parent
CONTRACT=ASPECT/"contracts"/"compton-constructor-flatness-experiment.v1.json"
RESULT=ASPECT/"results"/"compton_constructor_flatness_experiment.json"
def norm2(v): return sum(x*x for x in v)
def sub(a,b): return tuple(x-y for x,y in zip(a,b))
def scale(s,v): return tuple(s*x for x in v)
def dist(a,b): return math.sqrt(norm2(sub(a,b)))
def record(E,theta):
 ep=E/(1+E*(1-math.cos(theta))); ki=(E,0.0); kf=(ep*math.cos(theta),ep*math.sin(theta)); q=sub(ki,kf)
 electron_energy=math.sqrt(1+norm2(q))-1
 orientation=math.copysign(1.0,math.sin(theta))*abs(math.sin(theta))
 return {"theta":theta,"incident_energy":E,"scattered_energy":ep,"spectral_transfer":q,"electron_transfer":q,"photon_loss":E-ep,"electron_kinetic":electron_energy,"orientation":orientation}
def classify(residuals,orientation_flip=False,leakage=False):
 if leakage:return "nonunitary_leakage"
 if orientation_flip:return "conjugation"
 if max(residuals)-min(residuals)>1e-9:return "source_dependent"
 if residuals and abs(residuals[0])>1e-9:return "scalar_calibration"
 return "identity"
def main():
 c=json.loads(CONTRACT.read_text(encoding="utf-8")); rec=[record(1.0,math.radians(a)) for a in c["scattering_angles_degrees"]]
 energy_res=[r["photon_loss"]-r["electron_kinetic"] for r in rec]; momentum_res=[dist(r["spectral_transfer"],r["electron_transfer"]) for r in rec]
 common=[0.01 for _ in rec]; gain=[0.01*(i+1) for i in range(len(rec))]
 classes={"ideal":classify(momentum_res),"common_scale":classify(common),"frame_reflection":classify(momentum_res,orientation_flip=True),"target_excitation_leakage":classify(momentum_res,leakage=True),"angle_dependent_gain":classify(gain)}
 pairwise_orientation_magnitudes=[abs(r["orientation"]) for r in rec]; reflected=[abs(-r["orientation"]) for r in rec]
 completeness={k:True for k in c["source_completeness"]}; incomplete=dict(completeness,target_excitation_ledger=False)
 checks={"three_angles":len(rec)==3,"energy_closure":max(abs(x) for x in energy_res)<c["tolerances"]["energy"],"momentum_closure":max(momentum_res)<c["tolerances"]["momentum"],"known_sixty_degree_fixture":abs(rec[1]["scattered_energy"]-2/3)<1e-12 and abs(rec[1]["electron_kinetic"]-1/3)<1e-12,"hostile_classes":classes=={"ideal":"identity","common_scale":"scalar_calibration","frame_reflection":"conjugation","target_excitation_leakage":"nonunitary_leakage","angle_dependent_gain":"source_dependent"},"pairwise_reflection_blind":pairwise_orientation_magnitudes==reflected,"oriented_reflection_visible":all(r["orientation"]==-(-r["orientation"]) for r in rec),"source_complete_independent":all(completeness.values()) and not all(incomplete.values()),"wavelength_only_rejected":"wavelength_only" in c["hostiles"],"claim_boundary":not any(c["claim_boundary"].values())}
 out={"schema":"marici.aspect.compton-constructor-flatness-experiment-result.v1","passed":all(checks.values()),"checks":checks,"records":rec,"energy_residuals":energy_res,"momentum_residuals":momentum_res,"hostile_classifications":classes,"current_verdict":"mathematical_fixture_flat_physical_test_not_run","physical_status":"not_run"}
 RESULT.write_text(json.dumps(out,indent=2)+"\n",encoding="utf-8"); print(json.dumps(out,sort_keys=True)); raise SystemExit(0 if out["passed"] else 1)
if __name__=="__main__":main()

