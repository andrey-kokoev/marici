#!/usr/bin/env python3
import hashlib, json
from pathlib import Path
from sympy import Matrix

ROOT=Path(__file__).resolve().parents[3]
RESULT=ROOT/"research/kitaev/results/source-vs-target-coercivity.json"

def main():
    T=Matrix([[1,0],[0,1],[0,0]])
    source=T.T*T; target=T*T.T
    assert source==Matrix.eye(2)
    assert target==Matrix.diag(1,1,0)
    assert T.rank()==2 and T.rows==3
    missing=Matrix([0,0,1])
    assert T.T*missing==Matrix.zeros(2,1)
    square=Matrix.eye(2)
    assert square.T*square==Matrix.eye(2) and square*square.T==Matrix.eye(2)
    payload={"schema":"marici.kitaev.source_vs_target_coercivity.v1","status":"pass","isometric_embedding":{"source_gram_lower_bound":1,"source_injective":True,"closed_range":True,"target_surjective":False,"target_gram_kernel":[0,0,1]},"two_sided_square_control":{"source_coercive":True,"target_coercive":True,"invertible":True},"rh_required_type":"bounded-below source transport","checker_sha256":hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
    RESULT.parent.mkdir(parents=True,exist_ok=True)
    RESULT.write_text(json.dumps(payload,indent=2)+"\n",encoding="utf-8")
    print(json.dumps(payload,indent=2))
if __name__=="__main__": main()
