#!/usr/bin/env python3
import hashlib, json
from pathlib import Path
from sympy import Rational

ROOT=Path(__file__).resolve().parents[3]
RESULT=ROOT/"research/kitaev/results/uniform-affine-compatibility.json"

def main():
    rows=[]
    for n in [1,2,4,8,16]:
        phi=Rational(1,n); defect=1; solution=Rational(defect,1)/phi
        assert phi*solution==defect
        rows.append({"N":n,"phi":str(phi),"defect":"1","unique_solution":str(solution),"least_correction_norm":str(abs(solution))})
    payload={"schema":"marici.kitaev.uniform_affine_compatibility.v1","status":"pass","every_cutoff_solvable":True,"uniform_solution_bound":False,"smallest_singular_value":"1/N -> 0","records":rows,"checker_sha256":hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
    RESULT.parent.mkdir(parents=True,exist_ok=True)
    RESULT.write_text(json.dumps(payload,indent=2)+"\n",encoding="utf-8")
    print(json.dumps(payload,indent=2))
if __name__=="__main__": main()
