#!/usr/bin/env python3
"""Exact hostile: full seam rank with collapsing quotient frame bound."""

import hashlib
import json
from pathlib import Path
from sympy import Matrix, Rational

ROOT=Path(__file__).resolve().parents[3]
RESULT=ROOT/"research/kitaev/results/uniform-seam-transversality.json"

def main():
    e2=Matrix([0,1])
    rows=[]
    for n in [1,2,4,8,16]:
        eps=Rational(1,n)
        H=Matrix([[1,0],[1,eps]])
        assert H.rank()==2
        assert H*e2==Matrix([0,eps])
        gram=H.T*H
        assert gram.det()==eps**2
        Hfull=H.col_join(Matrix([[0,1]]))
        full_gram=Hfull.T*Hfull
        assert full_gram-Matrix.eye(2)==Matrix([[1,eps],[eps,eps**2]])
        assert (full_gram-Matrix.eye(2)).det()==0
        rows.append({"N":n,"epsilon":str(eps),"rank":H.rank(),"witness_ratio":str(eps),"domination_lower_bound":str(n),"gram_determinant":str(gram.det())})
    payload={"schema":"marici.kitaev.uniform_seam_transversality.v1","status":"pass","finite_rank_complete":True,"row_spaces_equal_residual_space":True,"uniform_lower_frame_bound":False,"aligned_third_row_uniform_repair":True,"fixtures":rows,"checker_sha256":hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
    RESULT.parent.mkdir(parents=True,exist_ok=True)
    RESULT.write_text(json.dumps(payload,indent=2)+"\n",encoding="utf-8")
    print(json.dumps(payload,indent=2))
if __name__=="__main__": main()
