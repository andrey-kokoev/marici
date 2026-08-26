#!/usr/bin/env python3
import hashlib, json
from pathlib import Path
from sympy import Matrix

ROOT=Path(__file__).resolve().parents[3]
RESULT=ROOT/"research/kitaev/results/pointwise-vs-uniform-closure.json"

def main():
    dim=10; I=Matrix.eye(dim); fixed=Matrix([1]+[0]*(dim-1)); rows=[]
    for n in range(dim):
        e=I[:,n]; P=e*e.T
        fixed_response=(P*fixed).dot(P*fixed)
        moving_response=(P*e).dot(P*e)
        assert moving_response==1 and P*P==P
        rows.append({"coordinate":n+1,"fixed_e1_response_squared":int(fixed_response),"moving_response_squared":1,"operator_norm":1})
    assert all(r["fixed_e1_response_squared"]==0 for r in rows[1:])
    payload={"schema":"marici.kitaev.pointwise_vs_uniform_closure.v1","status":"pass","strong_limit_on_fixed_states":"zero","gram_strong_limit_on_fixed_states":"zero","operator_norm_limit":1,"moving_normalized_witness":"e_N","uniform_closure":False,"records":rows,"checker_sha256":hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
    RESULT.parent.mkdir(parents=True,exist_ok=True)
    RESULT.write_text(json.dumps(payload,indent=2)+"\n",encoding="utf-8")
    print(json.dumps(payload,indent=2))
if __name__=="__main__": main()
