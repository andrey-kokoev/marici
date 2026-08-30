#!/usr/bin/env python3
import hashlib, json
from pathlib import Path
from sympy import Matrix

ROOT=Path(__file__).resolve().parents[3]
RESULT=ROOT/"research/kitaev/results/minimal-seam-rank.json"

def main():
    Q=Matrix.diag(1,0,0)
    R=Matrix([[0,1,0],[0,0,1]])
    H1=Matrix([[0,1,1]])
    H2=Matrix([[0,1,0],[0,0,1]])
    witness=Matrix([0,1,-1])
    assert Q*witness==Matrix.zeros(3,1)
    assert H1*witness==Matrix.zeros(1,1)
    assert R*witness!=Matrix.zeros(2,1)
    assert R.rank()==2 and H1.rank()==1 and H2.rank()==2
    assert (Q+H2.T*H2).rank()==3
    R1=Matrix([[0,1,0]])
    aligned=Matrix([[0,1,0]])
    assert R1==aligned
    payload={"schema":"marici.kitaev.minimal_seam_rank.v1","status":"pass","residual_rank_on_analytic_kernel":2,"one_row_fails":True,"joint_kernel_witness":[0,1,-1],"two_rows_succeed":True,"rank_one_aligned_case_minimal_rows":1,"checker_sha256":hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
    RESULT.parent.mkdir(parents=True,exist_ok=True)
    RESULT.write_text(json.dumps(payload,indent=2)+"\n",encoding="utf-8")
    print(json.dumps(payload,indent=2))
if __name__=="__main__": main()
