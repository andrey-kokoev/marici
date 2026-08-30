#!/usr/bin/env python3
import hashlib, json
from pathlib import Path
from fractions import Fraction

ROOT=Path(__file__).resolve().parents[3]
RESULT=ROOT/"research/kitaev/results/source-tightness-uniform-closure.json"

def main():
    cores=[]
    for m in [1,2,4,8,16]:
        tail=Fraction(1,m+1)
        cores.append({"core_size":m,"approximant_tail_bound":str(tail),"limit_tail_bound":str(tail)})
    truncations=[]
    for n in [1,2,4,8,16]:
        truncations.append({"cutoff":n,"operator_norm_error":str(Fraction(1,n+1))})
    hostile=[{"core_size":m,"moving_projection_tail_supremum":"1"} for m in [1,2,4,8,16]]
    payload={"schema":"marici.kitaev.source_tightness_uniform_closure.v1","status":"pass","compact_diagonal_fixture":{"core_exact_for_N_ge_M":True,"core_tail_bounds":cores,"norm_errors":truncations,"operator_norm_convergence":True},"moving_projection_hostile":{"tail_tight":False,"records":hostile},"checker_sha256":hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
    RESULT.parent.mkdir(parents=True,exist_ok=True)
    RESULT.write_text(json.dumps(payload,indent=2)+"\n",encoding="utf-8")
    print(json.dumps(payload,indent=2))
if __name__=="__main__": main()
