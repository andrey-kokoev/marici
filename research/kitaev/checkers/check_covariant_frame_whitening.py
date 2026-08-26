#!/usr/bin/env python3
import hashlib, json
from pathlib import Path
from sympy import Matrix, Rational

ROOT=Path(__file__).resolve().parents[3]
RESULT=ROOT/"research/kitaev/results/covariant-frame-whitening.json"

def ratio_squared(H,R,x):
    return (H*x).dot(H*x)/(R*x).dot(R*x)

def main():
    records=[]
    e2=Matrix([0,1])
    for n in [1,2,4,8,16]:
        eps=Rational(1,n)
        H=Matrix.diag(1,eps); R=Matrix.eye(2); A=Matrix.diag(1,1/eps)
        assert H*A==Matrix.eye(2)
        assert R*A==A
        original=ratio_squared(H,R,e2)
        transported=ratio_squared(H*A,R*A,e2)
        dishonest=ratio_squared(H*A,R,e2)
        assert original==transported==eps**2
        assert dishonest==1
        records.append({"N":n,"true_beta_squared_witness":str(original),"covariant_beta_squared_witness":str(transported),"one_sided_whitened_value":str(dishonest),"preconditioner_norm":str(n)})
    payload={"schema":"marici.kitaev.covariant_frame_whitening.v1","status":"pass","covariant_source_change_preserves_beta":True,"one_sided_whitening_false_repair":True,"fixtures":records,"checker_sha256":hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
    RESULT.parent.mkdir(parents=True,exist_ok=True)
    RESULT.write_text(json.dumps(payload,indent=2)+"\n",encoding="utf-8")
    print(json.dumps(payload,indent=2))
if __name__=="__main__": main()
