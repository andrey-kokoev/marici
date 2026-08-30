#!/usr/bin/env python3
import hashlib, json
from pathlib import Path
from sympy import Matrix, symbols

ROOT=Path(__file__).resolve().parents[3]
RESULT=ROOT/"research/kitaev/results/actuator-lift-torsor.json"

def main():
    t=symbols("t")
    R=Matrix([[1,0]]); H=Matrix([[1,0]]); L=Matrix([[0,1]])
    B=Matrix([1,t]); I=Matrix.eye(2); C=I-B*H
    assert R*B==Matrix([[1]])
    assert R*C==Matrix.zeros(1,2)
    assert L*C==Matrix([[-t,1]])
    B0=Matrix([1,0]); B1=Matrix([1,1])
    assert R*(B1-B0)==Matrix.zeros(1,1)
    assert L*(I-B0*H)==L
    assert L*(I-B1*H)!=L
    witness=Matrix([1,0])
    assert R*(I-B0*H)*witness==R*(I-B1*H)*witness==Matrix.zeros(1,1)
    assert L*(I-B0*H)*witness!=L*(I-B1*H)*witness
    payload={"schema":"marici.kitaev.actuator_lift_torsor.v1","status":"pass","all_B_t_cancel_residual":True,"nondisturbing_parameter":"t=0","torsor_direction_in_kernel_R":True,"successor_logical_probe_separates":True,"checker_sha256":hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
    RESULT.parent.mkdir(parents=True,exist_ok=True)
    RESULT.write_text(json.dumps(payload,indent=2)+"\n",encoding="utf-8")
    print(json.dumps(payload,indent=2))
if __name__=="__main__": main()
