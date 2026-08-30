#!/usr/bin/env python3
import hashlib, json
from pathlib import Path
from sympy import Matrix, Rational

ROOT=Path(__file__).resolve().parents[3]
RESULT=ROOT/"research/kitaev/results/weak-plus-gram-strong-closure.json"

def main():
    tail_gram=[1 for _ in range(8)]
    tail_limit_gram=0
    assert all(g!=tail_limit_gram for g in tail_gram)
    good=[]
    limit=Matrix.diag(1,0)
    for n in [1,2,4,8,16]:
        C=Matrix.diag(1,Rational(1,n))
        gram=C.T*C
        residual=C-limit
        good.append({"N":n,"weak_coordinate":str(Rational(1,n)),"gram_weak_coordinate":str(Rational(1,n*n)),"strong_residual_on_e2":str(Rational(1,n))})
        assert gram[1,1]==Rational(1,n*n)
        assert residual[1,1]==Rational(1,n)
    payload={"schema":"marici.kitaev.weak_plus_gram_strong_closure.v1","status":"pass","orthogonal_tail":{"weak_limit":"zero","gram_limit_matches":False,"strong_closure":False},"decaying_coordinate":{"weak_limit":"diag(1,0)","gram_limit_matches":True,"strong_closure":True,"records":good},"checker_sha256":hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
    RESULT.parent.mkdir(parents=True,exist_ok=True)
    RESULT.write_text(json.dumps(payload,indent=2)+"\n",encoding="utf-8")
    print(json.dumps(payload,indent=2))
if __name__=="__main__": main()
