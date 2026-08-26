#!/usr/bin/env python3
import hashlib, json
from pathlib import Path

ROOT=Path(__file__).resolve().parents[3]
RESULT=ROOT/"research/kitaev/results/pro-actuator-coherence.json"

def main():
    values=[(-1)**n for n in range(1,9)]
    defects=[abs(values[n]-values[n-1]) for n in range(1,len(values))]
    assert all(abs(v)==1 for v in values)
    assert all(d==2 for d in defects)
    coherent=[1 for _ in values]
    coherent_defects=[abs(coherent[n]-coherent[n-1]) for n in range(1,len(coherent))]
    assert all(d==0 for d in coherent_defects)
    payload={"schema":"marici.kitaev.pro_actuator_coherence.v1","status":"pass","unique_cutoff_values":values,"uniform_norm_bound":1,"adjacent_naturality_defects":defects,"inverse_limit_exists_for_forced_family":False,"coherent_control_fixture":coherent,"checker_sha256":hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
    RESULT.parent.mkdir(parents=True,exist_ok=True)
    RESULT.write_text(json.dumps(payload,indent=2)+"\n",encoding="utf-8")
    print(json.dumps(payload,indent=2))
if __name__=="__main__": main()
