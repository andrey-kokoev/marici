#!/usr/bin/env python3
import hashlib, json
from pathlib import Path
from sympy import Matrix, Rational

ROOT=Path(__file__).resolve().parents[3]
RESULT=ROOT/"research/kitaev/results/norm-closure-inverse-bound.json"

def main():
    hostile=[]; passing=[]
    singular_limit=Matrix.diag(1,0); identity=Matrix.eye(2)
    for n in [1,2,4,8,16]:
        T=Matrix.diag(1,Rational(1,n))
        assert T.det()!=0
        hostile.append({"N":n,"forward_norm_error":str(Rational(1,n)),"inverse_norm":n,"smallest_singular_value":str(Rational(1,n))})
        S=Matrix.diag(1,1+Rational(1,n))
        assert S.det()!=0
        passing.append({"N":n,"forward_norm_error":str(Rational(1,n)),"inverse_norm_upper_bound":"1"})
    assert singular_limit.det()==0 and identity.det()==1
    payload={"schema":"marici.kitaev.norm_closure_inverse_bound.v1","status":"pass","hostile":{"every_cutoff_invertible":True,"norm_limit_invertible":False,"records":hostile},"passing":{"uniform_inverse_bound":1,"norm_limit_invertible":True,"records":passing},"checker_sha256":hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
    RESULT.parent.mkdir(parents=True,exist_ok=True)
    RESULT.write_text(json.dumps(payload,indent=2)+"\n",encoding="utf-8")
    print(json.dumps(payload,indent=2))
if __name__=="__main__": main()
