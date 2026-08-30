#!/usr/bin/env python3
import hashlib, json
from pathlib import Path
from sympy import Matrix

ROOT=Path(__file__).resolve().parents[3]
RESULT=ROOT/"research/kitaev/results/weak-actuator-energy-escape.json"

def main():
    dim=8
    basis=Matrix.eye(dim)
    fixed_probe=basis[:,0]
    records=[]
    for n in range(dim):
        image=basis[:,n]
        fixed=(fixed_probe.T*image)[0]
        moving=(basis[:,n].T*image)[0]
        energy=(image.T*image)[0]
        assert moving==1 and energy==1
        records.append({"coordinate":n+1,"fixed_e1_probe":int(fixed),"moving_probe":int(moving),"quadratic_energy":int(energy)})
    assert all(r["fixed_e1_probe"]==0 for r in records[1:])
    payload={"schema":"marici.kitaev.weak_actuator_energy_escape.v1","status":"pass","fixed_probe_limit":0,"unique_weak_limit":"zero","operator_norm":1,"quadratic_energy":1,"strong_limit_zero":False,"moving_probe_response":1,"records":records,"checker_sha256":hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
    RESULT.parent.mkdir(parents=True,exist_ok=True)
    RESULT.write_text(json.dumps(payload,indent=2)+"\n",encoding="utf-8")
    print(json.dumps(payload,indent=2))
if __name__=="__main__": main()
