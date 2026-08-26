#!/usr/bin/env python3
import hashlib, json
from pathlib import Path
from sympy import Matrix, symbols

ROOT=Path(__file__).resolve().parents[3]
RESULT=ROOT/"research/kitaev/results/authorized-actuator-lift.json"

def main():
    I=Matrix.eye(2); H=I; R=I; S=I
    assert S*H==R
    a,b=symbols("a b")
    B_limited=Matrix([[a,b],[0,0]])
    closed=R*(I-B_limited*H)
    e2=Matrix([0,1])
    assert closed*e2==Matrix([-b,1])
    assert closed*e2!=Matrix.zeros(2,1)
    B_full=I
    assert R*(I-B_full*H)==Matrix.zeros(2)
    payload={"schema":"marici.kitaev.authorized_actuator_lift.v1","status":"pass","perfect_observation":True,"decoder_norm":1,"limited_actuator_corrects_all":False,"uncorrected_witness":[0,1],"full_actuator_algebraic_repair":True,"full_actuator_source_authorized":False,"checker_sha256":hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
    RESULT.parent.mkdir(parents=True,exist_ok=True)
    RESULT.write_text(json.dumps(payload,indent=2)+"\n",encoding="utf-8")
    print(json.dumps(payload,indent=2))
if __name__=="__main__": main()
