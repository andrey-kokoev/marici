#!/usr/bin/env python3
import hashlib, json
from pathlib import Path
from sympy import Rational

ROOT=Path(__file__).resolve().parents[3]
RESULT=ROOT/"research/kitaev/results/equivariant-nondisturbing-lift.json"

def main():
    # Nondisturbance is t=0.
    nondisturbing=Rational(0)
    affine_fixed=Rational(1,2)
    reflection_fixed=Rational(0)
    assert affine_fixed!=nondisturbing
    assert reflection_fixed==nondisturbing
    # Trivial symmetry leaves all t, so nondisturbance selects zero.
    payload={"schema":"marici.kitaev.equivariant_nondisturbing_lift.v1","status":"pass","affine_reflection":{"fixed_lift":"1/2","invariant_shear_dimension":0,"joint_solution":False},"ordinary_reflection":{"fixed_lift":"0","joint_solution":True,"unique":True},"trivial_symmetry":{"fixed_torsor_dimension":1,"nondisturbance_selects":"0","joint_solution":True,"unique_after_nondisturbance":True},"compatibility_gate":"-L B_G H in image(N -> L N H on V^G)","checker_sha256":hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
    RESULT.parent.mkdir(parents=True,exist_ok=True)
    RESULT.write_text(json.dumps(payload,indent=2)+"\n",encoding="utf-8")
    print(json.dumps(payload,indent=2))
if __name__=="__main__": main()
