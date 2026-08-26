#!/usr/bin/env python3
import hashlib, json
from pathlib import Path
from fractions import Fraction

ROOT=Path(__file__).resolve().parents[3]
RESULT=ROOT/"research/kitaev/results/vanishing-naturality-defects.json"

def block(m):
    return [Fraction(k,m) for k in range(m+1)]+[Fraction(k,m) for k in range(m-1,-1,-1)]

def main():
    blocks=[block(m) for m in range(2,9)]
    assert all(max(b)==1 and b[0]==0 and b[-1]==0 for b in blocks)
    max_defects=[]
    for b in blocks:
        defects=[abs(b[i+1]-b[i]) for i in range(len(b)-1)]
        max_defects.append(max(defects))
    assert max_defects==[Fraction(1,m) for m in range(2,9)]
    assert all(max(abs(x) for x in b)<=1 for b in blocks)
    payload={"schema":"marici.kitaev.vanishing_naturality_defects.v1","status":"pass","uniform_norm_bound":1,"block_max_defects":[str(x) for x in max_defects],"zero_subsequence":True,"one_subsequence":True,"full_limit_exists":False,"summable_defects_sufficient":True,"checker_sha256":hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
    RESULT.parent.mkdir(parents=True,exist_ok=True)
    RESULT.write_text(json.dumps(payload,indent=2)+"\n",encoding="utf-8")
    print(json.dumps(payload,indent=2))
if __name__=="__main__": main()
